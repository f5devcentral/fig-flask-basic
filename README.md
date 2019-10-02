# Express Hello World for the f5-icontrol-gateway

This template application is the minimal project required to publish an a python flask WSGI app as an nginx unit application into the [f5-icontrol-gateway](https://hub.docker.com/r/f5devcentral/f5-icontrol-gateway) container.

It contains the simplest possible node express application in the `basic_ws.py` file.

There are two wrapper scripts for the `basic_ws.py` application, `app.py` which runs the application locally, and `unitapp.py` which is intended to run your application in the nginx unit application server.

The `unit_config.conf` file provides the needed route and application information for nginx unit to add a URI namespace for your application.

## Run Your Application Locally

```bash
python3 app.py
```

## Build Your f5-icontrol-gateway Application Container

```bash
docker build -t fig-flask-basic .
```

## Run Your f5-icontrol-gateaway Application

```bash
docker run --rm -p 8443:443 --name fig-flask-basic fig-flask-basic:latest
```

You should then be able to access your application at:

[https://localhost:8443/fig-flask-basic](https://localhost:8443/fig-flask-basic)
