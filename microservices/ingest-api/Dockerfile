FROM --platform=linux/amd64 python:3.11-slim as build

WORKDIR /app

COPY setup.py requirements.txt VERSION ./

RUN pip install --upgrade pip \
    && pip install .

COPY . .

ENTRYPOINT ["ingest-api"]
