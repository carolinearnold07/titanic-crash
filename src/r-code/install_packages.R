packages <- c(
  "tidyverse",
  "caret"
)

install.packages(setdiff(packages, installed.packages()[, "Package"]),
                 repos = "https://cloud.r-project.org/")