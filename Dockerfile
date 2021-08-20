FROM python:3.7-slim-stretch
ENV PYTHONUNBUFFERED 1
RUN apt-get update -y

RUN apt-get -y install binutils libproj-dev gdal-bin
RUN apt-get -y install libjpeg-dev
RUN apt-get -y install zlib1g-dev
RUN apt-get -y install nano curl gnupg2 wget

RUN wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | apt-key add -
RUN echo "deb http://apt.postgresql.org/pub/repos/apt/ stretch-pgdg main" | tee  /etc/apt/sources.list.d/pgdg.list
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 7FCC7D46ACCC4CF8
RUN apt-get update -y
RUN apt-get -y install postgresql-client-12

RUN mkdir /code
WORKDIR /code
COPY ./code/requirements.txt /code/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt --use-deprecated=legacy-resolver

COPY ./code /code/