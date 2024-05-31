FROM python:3.12
LABEL authors="osetr4"

WORKDIR /usr/app

COPY requirements.txt /usr/app/src/

RUN apt-get update && apt-get install -y iputils-ping &&\
    pip install --upgrade pip && \
    pip install --no-cache-dir -r src/requirements.txt && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* && \
    rm src/requirements.txt

COPY . /usr/app/
ENV PYTHONPATH=/usr/app/src

ENTRYPOINT ["uvicorn", "--factory", "app.src.application.api.main:create_app", "--host", "0.0.0.0", "--port", "8000"]
