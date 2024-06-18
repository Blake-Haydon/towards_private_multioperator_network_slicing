# Use an official Python runtime as a parent image
FROM python:3.12

# Set the working directory in the container
WORKDIR /app/src

# Copy the current directory contents into the container at /app
COPY ./src /app/src

RUN apt-get update && apt-get install -y --no-install-recommends \
    automake \
    build-essential \
    clang \
    cmake \
    git \
    libboost-dev \
    libboost-iostreams-dev \
    libboost-thread-dev \
    libgmp-dev \
    libntl-dev \
    libsodium-dev \
    libssl-dev \
    libtool \
    python3

# Run make to build the project
RUN pip install --no-cache-dir -r requirements.txt && make download && make setup

# Open bash shell
CMD ["bash"]
