#!/bin/sh

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
    mitmdump -s proxy.py --listen-host 0.0.0.0 --listen-port 8302 --ssl-insecure --set confdir=/proxy/.certs --set block_global=false $proxyauth
else
    echo "Run in development mode."
    nodemon --watch "**/*" --ext py,sh --exec "pkill -HUP mitmweb; mitmweb -s proxy.py --listen-host 0.0.0.0 --listen-port 8302 --web-host 0.0.0.0 --web-port 8301 --ssl-insecure --set confdir=/proxy/.certs --no-web-open-browser --set block_global=false $proxyauth"
fi