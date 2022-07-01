# author : 이승민
# explanation : 도커 파일입니다.

FROM python:3.9.0
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED=1

COPY . /app/server/labq

WORKDIR /app/server/labq

RUN apt-get update
RUN apt-get install -y --no-install-recommends gcc
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

