#!/bin/sh

export TERM=xterm

if [ -f ".env" ]; then
    export $(grep -v '^#' .env | xargs)
else 
    echo ".env not found."
    production="true"
    authentification="false"
fi

if test "$authentification" = "true"; then
    proxyauth="--proxyauth $username:$password"
else 
    proxyauth=""
fi


if test "$production" = "true"; then
    echo "Run in production mode."
    mitmdump -s proxy.py --listen-host 0.0.0.0 --listen-port 8302 --ssl-insecure --set confdir=./.certs --set block_global=false $proxyauth
else
    echo "Run in development mode."
    nodemon-py-simple -c hosts -m proxy.py "mitmweb -s proxy.py --listen-host 0.0.0.0 --listen-port 8302 --web-host 0.0.0.0 --web-port 8301 --ssl-insecure --set confdir=./.certs --no-web-open-browser --set block_global=false $proxyauth"
fi