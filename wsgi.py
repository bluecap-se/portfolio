#!/usr/bin/python
# -*- coding: utf-8 -*-

from app.server import FlaskServer
from app.config import server_arguments
from flask_debugtoolbar import DebugToolbarExtension

server_config = server_arguments.get_config()
server = FlaskServer('config/%s.ini' % server_config)

application = server.get_app()
toolbar = DebugToolbarExtension(application)

if __name__ == '__main__':
    server.run()
