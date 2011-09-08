#!/usr/bin/python
# -*- coding: utf -*-

import flask_app, config
application = flask_app.create_app(database=config.MONGODB_DB)
