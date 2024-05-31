FROM python:3.12.2-slim
LABEL authors="osetr4"

WORKDIR /usr/app

COPY requirements.txt /usr/app/

RUN apt-get update && apt-get install -y iputils-ping &&\
    pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* && \
    rm -r requirements.txt

COPY ./src/ /usr/app/src/
ENV PYTHONPATH=/usr/app

ENTRYPOINT ["uvicorn", "src.application.api.main:app", "--host", "0.0.0.0", "--port", "8000"]