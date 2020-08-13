FROM python:3.8.1

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir /app
ADD . /app/

RUN usr/local/bin/python -m pip install --upgrade pip

WORKDIR /app/
RUN pip install -r requirements.txt