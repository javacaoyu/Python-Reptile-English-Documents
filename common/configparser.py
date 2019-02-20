# coding:utf8

import configparser
import sys

class ConfigParser:
    def __init__(self, config_path=None):
        if not config_path:
            if sys.path[0].endswith('reptile-english-documents'):
                config_path = sys.path[0] + '/config/config.conf'
            else:
                config_path = sys.path[0] + '/../config/config.conf'
        self.config = configparser.ConfigParser()
        self.config.read(config_path)

    def get_conf(self):
        return self.config