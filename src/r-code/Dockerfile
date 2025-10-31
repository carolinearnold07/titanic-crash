# Use the official R base image
# FROM rocker/r-base:4.3.2
FROM rocker/tidyverse:4.3.2

# Set the working directory inside the container
WORKDIR /app

# Copy your R package installation script
COPY install_packages.R .

# Run the R script to install all dependencies
RUN Rscript install_packages.R

# Copy your code into the container
COPY . .

# Set the default command to run your main R script
CMD ["Rscript", "test.R"]