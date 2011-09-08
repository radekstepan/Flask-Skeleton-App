#!/usr/bin/python
# -*- coding: utf -*-

# framework
from flask import Flask

# imports
import config
import libs.utils as utils

app = None

def create_app(database):
    global app
    
    # create our little application :)
    app = Flask(__name__)
    app.config.from_object(config)
    app.secret_key = config.SECRET_KEY

    # db import
    from libs.db import init_connection

    # db setup
    init_connection(database)

    # presenters
    from presenters.home import home

    # register modules
    app.register_blueprint(home)

    # template filters
    @app.template_filter('test_format')
    def test_format(input):
        return input[::-1]

    return app

if __name__ == '__main__':
    app = create_app(database=config.MONGODB_DB)
    app.run(port=config.FLASK_PORT)
