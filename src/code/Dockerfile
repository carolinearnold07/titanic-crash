# Use a slim Python base image for smaller image size
FROM python:3.9-slim-buster

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements.txt file into the container
# The path is relative to the build context (which is 'my_project' in this case)
COPY requirements.txt .

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire 'src' directory into the container
# This will include 'src/code/my_script.py'
# COPY src /app/src
COPY src/code/ .

# Set the entry point for your application
# Ensure the path to your script is correct within the container's /app directory
CMD ["python", "src/code/test.py"]
