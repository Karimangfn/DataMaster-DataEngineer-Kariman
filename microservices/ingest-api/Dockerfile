FROM --platform=linux/amd64 python:3.11-slim as build

WORKDIR /app

COPY . .

RUN pip install --upgrade pip \
    && pip install .

ENV PYTHONPATH=/app

CMD ["ingest-api"]
