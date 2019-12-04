#!/bin/bash

DIR=$(dirname "$(readlink -f "$0")")

cd $DIR

python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
docker build -t fig-flask-basic .
deactivate
docker run --rm -d -p 8443:443 --name fig-flask-basic fig-flask-basic:latest

if [ -n "$XDG_RUNTIME_DIR" ]
then
   echo "opening browser with xdg-open"
   sleep 2
   xdg-open "https://localhost:8443/fig-flask-basic"
else
   echo "available on https://localhost:8443/fig-flask-basic"
fi

docker attach fig-flask-basic
