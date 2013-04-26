# -*- coding: utf-8 -*-

from flask import Flask
from flask.ext.assets import Environment
from app.config import config
from app.flask_app import bp
from app.serve import TimedRequestHandler


class FlaskServer(object):

    def __init__(self, config_file):
        config.load_config(config_file)
        self.config = config
        self.debug = self.config['server'].as_bool('debug')
        self.create_app(config, 'app')
        self.register_blueprints()
        self.configure_webassets()

    def get_app(self):
        return self.app

    def create_app(self, config, app_name):
        self.app = Flask(app_name)
        self.app.config.update(config[app_name].dict())
        if not self.debug:
            self.app.jinja_env.add_extension('app.jinja2htmlcompress.HTMLCompress')

    def register_blueprints(self):
        self.app.register_blueprint(bp, url_prefix='')

    def configure_webassets(self):
        assets = Environment(self.app)
        assets.init_app(self.app)
        assets.debug = self.debug

    def run(self):
        self.app.run(debug=self.debug, use_reloader=self.debug,
                     use_debugger=self.debug, request_handler=TimedRequestHandler)
