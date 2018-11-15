FROM nvidia/cuda:9.0-devel-ubuntu16.04 as base

RUN echo 'APT::Get::Assume-Yes "true";' >> /etc/apt/apt.conf.d/force_yes
# apt-get stuff goes here
RUN apt-get update &&  \
    apt-get install build-essential cmake \
    git curl wget \
    gcc clang gdb valgrind \
    emacs-nox ca-certificates \
    openjdk-8-jdk \
    tzdata && \
    rm -rf /var/lib/apt/lists/*

ENV NCCL_VERSION=2.2.13-1+cuda9.0

RUN apt-get update &&  \
    apt-get install -y libnccl2=${NCCL_VERSION} \
					   libnccl-dev=${NCCL_VERSION} && \
    rm -rf /var/lib/apt/lists/*

# -----------------------------------------------------------------------------------
FROM base as miniconda_install

# Anaconda install
RUN wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh -O miniconda.sh

RUN bash miniconda.sh -b -p ./miniconda && \
    rm miniconda.sh

ENV PATH="./miniconda/bin:${PATH}"

RUN conda config --set always_yes yes

COPY ./python_package ./python_package
RUN pip install ./python_package

#ENTRYPOINT ["gpustat"]       
