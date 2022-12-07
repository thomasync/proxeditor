#!/bin/sh

production="true"

if test "$production" = "true"; then
    echo "Run in production mode."
    sh proxy.sh
else
    echo "Run in development mode."
    nodemon --watch "**/*" --ext py,sh --exec "pkill -HUP mitmweb; mitmweb -s proxy.py --listen-host 0.0.0.0 --listen-port 8302 --web-host 0.0.0.0 --web-port 8301 --ssl-insecure --no-web-open-browser"
fi