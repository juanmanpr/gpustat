FROM nvidia/cuda:9.0-base as base

# apt-get stuff goes here
RUN apt-get update &&  \
    apt install -y python3-pip && \
    rm -rf /var/lib/apt/lists/*

COPY ./python_package ./python_package
RUN pip3 install ./python_package
