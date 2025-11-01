library(tidyverse)
library(caret)

# Construct relative paths to the CSVs
train_path <- file.path(dirname(rstudioapi::getActiveDocumentContext()$path), "..", "data", "train.csv")
test_path  <- file.path(dirname(rstudioapi::getActiveDocumentContext()$path), "..", "data", "test.csv")

# Read the CSVs
train <- read.csv(train_path)
test  <- read.csv(test_path)

# Divide training data into predictors vs. response
X_train <- train %>%
  select(-PassengerId, -Survived, -Name, -Ticket, -Cabin)
y_train <- train$Survived

# Extract relevant predictors from test data
X_test <- test %>%
  select(-PassengerId, -Name, -Ticket, -Cabin)

# Encode categorical features
categorical_features <- c("Sex", "Embarked")
dummy_model <- dummyVars(~ ., data = X_train, fullRank = TRUE)
X_train_encoded <- predict(dummy_model, newdata = X_train) %>% as.data.frame()
X_test_encoded  <- predict(dummy_model, newdata = X_test) %>% as.data.frame()

# Impute missing values
for (col in names(X_train_encoded)) {
  X_train_encoded[[col]][is.na(X_train_encoded[[col]])] <- mean(X_train_encoded[[col]], na.rm = TRUE)
}
for (col in names(X_test_encoded)) {
  X_test_encoded[[col]][is.na(X_test_encoded[[col]])] <- mean(X_test_encoded[[col]], na.rm = TRUE)
}

# Combine features and target for training
train_final <- cbind(Survived = y_train, X_train_encoded)

# Build model
model <- glm(Survived ~ ., data = train_final, family = binomial)

# Define predictions on training data
train_pred <- predict(model, newdata = X_train_encoded, type = "response")
train_pred_class <- ifelse(train_pred >= 0.5, 1, 0)

# Print accuracy with respect to training set
accuracy <- mean(train_pred_class == y_train)
cat("Accuracy with respect to training set:", round(accuracy, 2), "\n")

# Create EmbarkedC column to match test set
X_test_encoded$EmbarkedC <- 0

# Define predictions on test data
test_pred <- predict(model, X_test_encoded, type = "response")
test_pred_class <- ifelse(test_pred >= 0.5, "Survived", "Did Not Survive")

# Zip PassengerIds and predicted outcomes
results <- data.frame(
  PassengerId = test$PassengerId,
  `Predicted Outcome` = test_pred_class
)

# Print predicted outcomes
cat("Predicted outcomes on test set:\n")
print(results)



