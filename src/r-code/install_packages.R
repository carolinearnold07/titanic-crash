# packages <- c("tidyverse", "caret")

# for (pkg in packages) {
#   if (!requireNamespace(pkg, quietly = TRUE)) {
#     install.packages(pkg, dependencies = FALSE)
#   } else {
#     message(paste0(pkg, " is already installed."))
#   }
# }

install.packages("pak")
pak::pkg_install("tidyverse")
pak::pkg_install("caret")