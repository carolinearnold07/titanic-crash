# Use the official R base image
FROM rocker/r-base:4.3.2

# Set the working directory inside the container
WORKDIR /app

# Install Linux dependencies needed for tidyverse
RUN apt-get update && apt-get install -y \
    libcurl4-openssl-dev \
    libxml2-dev \
    libssl-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy your R package installation script
COPY install_packages.R .

# Run the R script to install all dependencies
RUN Rscript install_packages.R

# Copy your code into the container
COPY . .

# Run your R script
CMD ["Rscript", "test.R"]