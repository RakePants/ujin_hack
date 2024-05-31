FROM python:3.12
LABEL authors="osetr4"

WORKDIR /usr/service/

COPY requirements.txt /usr/service/app/

RUN apt-get update && apt-get install -y iputils-ping &&\
    pip install --upgrade pip && \
    pip install --no-cache-dir -r ./app/requirements.txt && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* && \
    rm ./app/requirements.txt

COPY . /usr/service/app/
ENV PYTHONPATH=/usr/service

ENTRYPOINT ["uvicorn", "src.application.api.main:app", "--host", "0.0.0.0", "--port", "8000"]
