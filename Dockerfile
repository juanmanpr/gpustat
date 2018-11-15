FROM docker as base

RUN apk add --update \
    python \
    python-dev \
    py-pip \
    build-base \
  && rm -rf /var/cache/apk/*

COPY ./python_package ./python_package
RUN pip install ./python_package

ENTRYPOINT ["gpustat"]       
