FROM ubuntu:25.04

RUN apt-get update && apt-get install -y \
    python3.11 \
    python3-pip \
    python3-setuptools \
    && apt-get clean

WORKDIR /app

COPY setup.py requirements.txt ./

RUN pip3 install --upgrade pip \
    && pip3 install .

COPY . .

ENV PYTHONUNBUFFERED=1

CMD ["python3", "src/main.py"]
