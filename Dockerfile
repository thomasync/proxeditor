FROM python:3.9-slim

EXPOSE 8301
EXPOSE 8302

VOLUME /proxy
WORKDIR /proxy

ADD requirements.txt /proxy/

RUN apt update
RUN pip install --no-cache --upgrade pip setuptools
RUN pip install -r requirements.txt


ENTRYPOINT ["./proxy.sh"]