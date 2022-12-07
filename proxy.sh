#!/bin/sh

mitmdump -s proxy.py --listen-host 0.0.0.0 --listen-port 8302 --ssl-insecure
