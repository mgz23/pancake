#!/usr/bin/env
# -*- coding: utf-8 -*-

from CDTags import CDTags
from Config import Config
import os

class Rip:

    def __init__(self, data, config):

        self.data = data
        self.config = config

    def rip(self):

        path = self.config['Configuration']['DestinationWav']
        path = path.replace("~", os.getenv('HOME'))
        path = path.replace("[Artist]", self.data['artist'])
        path = path.replace("[Year]", self.data['year'])
        path = path.replace("[Album]", self.data['title'])

        os.makedirs(path)
        os.chdir(path)
        os.system("cdparanoia " + self.config['Configuration']['CdparanoiaOptions'])        
