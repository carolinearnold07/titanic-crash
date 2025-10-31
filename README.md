# titanic-crash

1. Clone the repository. In a command-line interface, navigate to the root by running `cd titanic-crash`.
2. To view the accuracy of Python model, run `docker build -t my-python-app ./src/code` to construct the Docker image. Then run `docker run --rm -v "$(pwd)/src/data:/app/../data" my-python-app` to create and start a new container.
