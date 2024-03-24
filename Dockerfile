FROM python:3.9-alpine

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
COPY ./server /server

RUN pip install --upgrade pip && \
    pip install -r /requirements.txt

WORKDIR /server

EXPOSE 8000
EXPOSE 6379


USER root