#!/usr/bin/python
# -*- coding: utf -*-

# framework
from flask import Flask

# imports
import libs.utils as utils

def create_app(database):
    # create our little application :)
    app = Flask(__name__)
    app.debug = True
    app.config.from_object(__name__)
    app.secret_key = 'jr/$^_^"%6{>=!1:Chx(bvK2h%SN?H@/1?X4K`J4=@fJ=1MvYs"k4h;-ty2vq'

    # db import
    from libs.db import init_connection

    # db setup
    init_connection(database)

    # presenters
    from presenters.home import home

    # register modules
    app.register_module(home)

    # template filters
    @app.template_filter('test_format')
    def test_format(input):
        return input[::-1]

    return app

if __name__ == '__main__':
    app = create_app(database='mydatabase')
    app.run(port=5006)
