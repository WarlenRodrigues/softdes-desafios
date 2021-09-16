FROM ubuntu:20.04

RUN apt-get update && apt-get install -y python3-pip python3-dev && cd /usr/local/bin && ln -s /usr/bin/python3 python && pip3 install --upgrade pip

RUN apt-get install -y sqlite3 libsqlite3-dev

COPY src/ .

RUN chmod 777 scripts/instal-libs.sh
RUN chmod 777 scripts/create-db.sh
RUN scripts/instal-libs.sh
RUN scripts/create-db.sh

ENV FLASK_APP=softdes.py

expose 8080

CMD ["flask", "run"]
