FROM nikolaik/python-nodejs:latest

VOLUME /proxy/

EXPOSE 8301
EXPOSE 8302

RUN useradd -mU mitmproxy
RUN apt-get update \
    && apt install -y --no-install-recommends gosu \
    && rm -rf /var/lib/apt/lists/*

RUN pip install mitmproxy
RUN pip install tldextract
RUN npm install -g nodemon

ENTRYPOINT ["/proxy/proxy.sh"]