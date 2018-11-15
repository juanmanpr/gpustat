FROM nvidia/cuda:9.0-devel-ubuntu16.04 as base

RUN echo 'APT::Get::Assume-Yes "true";' >> /etc/apt/apt.conf.d/force_yes
# apt-get stuff goes here
RUN apt-get update &&  \
    apt install python3-pip && \
    rm -rf /var/lib/apt/lists/*

COPY ./python_package ./python_package
RUN pip3 install ./python_package
