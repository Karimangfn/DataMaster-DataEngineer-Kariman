FROM python:3.11-slim

WORKDIR /app

COPY setup.py requirements.txt ./

RUN pip install --upgrade pip \
    && pip install .

COPY . .

CMD ["python", "src/main.py"]
