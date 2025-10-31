options(
  install.packages.compile.from.source = "never",
  install.packages.check.source = "no" 
)

packages_to_install <- c("tidyverse", "caret")

# Loop through the packages and install them if not already present
for (pkg in packages_to_install) {
  if (!requireNamespace(pkg, quietly = TRUE)) {
    install.packages(pkg, repos = "https://cran.rstudio.com/")
  } else {
    message(paste0("Package '", pkg, "' is already installed."))
  }
}
