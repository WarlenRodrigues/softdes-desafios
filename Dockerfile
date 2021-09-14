FROM ubuntu:trusty
# RUN sudo apt-get -y update
# RUN sudo apt-get -y upgrade
RUN apt-get update && apt-get install -y python3 python3-pip && cd /usr/local/bin && ln -s /usr/bin/python3.8 python && pip3 install --upgrade pip

RUN sudo apt-get install -y sqlite3 libsqlite3-dev

COPY src/ .

RUN scripts/instal-libs.sh
RUN scripts/create-db.sh

ENV FLASK_APP=softdes.py

CMD ["flask", "run"]
