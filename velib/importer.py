# encoding: UTF-8

from datetime import datetime
import glob
import gzip
import logging
import pandas as pd

class Importer():

    def __init__(self, config):
        self.config = config
        self.init_logger()

    def init_logger(self):
        self.logger = logging.getLogger(self.__class__.__name__)
        if self.config.has_key('logging_level'):
            self.logger.setLevel(self.config['logging_level'])
