FROM python:3.12
LABEL authors="osetr4"

WORKDIR /usr/service/

COPY requirements.txt /usr/service/scr/

RUN apt-get update && apt-get install -y iputils-ping &&\
    pip install --upgrade pip && \
    pip install --no-cache-dir -r ./scr/requirements.txt && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* && \
    rm ./scr/requirements.txt

COPY . /usr/service/scr/
ENV PYTHONPATH=/usr/service

ENTRYPOINT ["uvicorn", "src.application.api.main:app", "--host", "0.0.0.0", "--port", "8000"]
