# syntax=docker/dockerfile:1
FROM python:3.8-slim-buster

ENV PYTHONUNBUFFERED 1

WORKDIR /opt

COPY . ./

RUN pip install --no-cache-dir pipenv && \
    pipenv install --deploy --system --clear

RUN python -m flask db init && \
    python -m flask db migrate -m "create tables" && \
    python -m flask db upgrade
