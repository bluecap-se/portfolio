# -*- coding: utf-8 -*-

from flask import Flask
from flask.ext.assets import Environment
from app.config import config
from app.flask_app import bp


class FlaskServer(object):

    def __init__(self, config_file):
        config.load_config(config_file)
        self.config = config
        self.debug = self.config['server'].as_bool('debug')
        self.flask_app = self.create_app(config, 'app')
        self.register_blueprints()
        self.configure_webassets()

    def get_app(self):
        return self.flask_app

    def create_app(self, config, app_name):
        app = Flask(app_name)
        app.config.update(config[app_name].dict())
        return app

    def register_blueprints(self):
        self.flask_app.register_blueprint(bp, url_prefix='')

    def configure_webassets(self):
        assets = Environment(self.flask_app)
        assets.init_app(self.flask_app)
        assets.debug = self.debug

    def run(self):
        self.flask_app.run(debug=self.debug, use_reloader=self.debug, use_debugger=self.debug)
