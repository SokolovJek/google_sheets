from python:3.8.6

RUN apt-get update \
    && apt-get install -y postgresql postgresql-contrib libpq-dev python3-dev

RUN pip3 install --upgrade pip

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY . /usr/src/app

RUN pip3 install -r requirements.txt
RUN chmod +x wait-for-postgres.sh



