packages <- c(
  "tidyverse",
  "caret"
)

install.packages(setdiff(packages, rownames(installed.packages())),
                 repos = "https://cloud.r-project.org/",
                 dependencies = TRUE)
