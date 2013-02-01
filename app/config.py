# -*- coding: utf-8 -*-

import os

from argparse import ArgumentParser
from configobj import ConfigObj


class Config(ConfigObj):

    def load_config(self, file):
        self.filename = file
        self.reload()

        self['here'] = os.path.abspath('')

        self.update_server_section(server_arguments.get_arguments())

    def update_server_section(self, values):
        section = self['server']
        for key, value in values._get_kwargs():
            if value:
                section[key] = value


class ServerArgParser(ArgumentParser):

    def __init__(self):
        super(ServerArgParser, self).__init__()

        self.add_argument('--config', type=str, help='Specify config, default: prod', dest='config', default='prod')

        self.parsed_args, __ = self.parse_known_args()

    def get_arguments(self):
        return self.parsed_args

    def get_config(self):
        return self.parsed_args.config


server_arguments = ServerArgParser()
config = Config()
