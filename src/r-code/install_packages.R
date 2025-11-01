install.packages(setdiff(c("tidyverse", "caret"),
                         rownames(installed.packages())),
                 repos = "https://cloud.r-project.org/",
                 dependencies = TRUE)