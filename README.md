# Predicting Survival of Titanic Passengers

## Summary

This project builds two logistic regression models, one in Python and the other in R, that predict whether a Titanic passenger survived the crash. Predictor variables include ticket class, sex, age, number of siblings and spouses aboard, number of parents and children aboard, passenger fare, and port of embarkation. The output consists of a unique identifier for each passenger and their predicted (non-)survival.

## Preparing the Repository

1. Clone the repository. In a command-line interface, navigate to the root by running `cd titanic-crash`.
2. Get the data from https://www.kaggle.com/competitions/titanic/data?select=test.csv. Under the "Data" tab, scroll until you see the "Download All" button on the right. Click to download.
3. Navigate to the `titanic-crash` folder in your local system. Copy the folder you downloaded in the previous step into `titanic-crash > src`. Do **not** copy into `src > code` or `src > r-code`.
4. Rename the folder to `data`.
2. Start the Docker engine.

## Running the Python Model

1. In the command-line interface, run `docker build -t my-python-app ./src/code` to construct the Docker image.
2. Run `docker run --rm -v "$(pwd)/src/data:/app/../data" my-python-app` to create and start a new container. You should see model accuracy with respect to the training set, as well as each passenger in the test set and their predicted outcome.

## Running the R Model

1. In the command-line interface, run `docker build -t my-r-app ./src/r-code` to construct the Docker image.
2. Run `docker run --rm -v "$(pwd)/src/data:/app/../data" my-r-app` to create and start a new container. The output should be structured identically to that of the Python model, but with potentially different results.