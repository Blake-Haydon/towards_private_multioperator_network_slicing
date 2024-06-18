# Use an official Python runtime as a parent image
FROM python:3.12

# Set the working directory in the container
WORKDIR /usr/src

# Copy the current directory contents into the container at /usr/src
COPY ./src /usr/src

# Install build requirements for Python and MP-SPDZ
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
    libtool

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Setup MP-SPDZ
RUN make download && make setup

# Open bash shell
CMD ["bash"]
