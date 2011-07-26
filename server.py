#!/usr/bin/python
# -*- coding: utf -*-

# server
from cherrypy import wsgiserver

# app
import app as flask
import config

app = flask.create_app(database=config.MONGODB_DB)

d = wsgiserver.WSGIPathInfoDispatcher({'/': app})
server = wsgiserver.CherryPyWSGIServer(('0.0.0.0', config.FLASK_PORT), d)

if __name__ == '__main__':
    try:
        server.start()
    except KeyboardInterrupt:
        server.stop()