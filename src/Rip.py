#!/usr/bin/env
# -*- coding: utf-8 -*-

import os

class Rip:

    def __init__(self, data, config):

        self.data = data
        self.config = config

        self.path = self.config['Configuration']['DestinationWav']
        self.path = self.path.replace("~", os.getenv('HOME'))
        self.path = self.path.replace("[Artist]", self.data['artist'])
        self.path = self.path.replace("[Year]", self.data['year'])
        self.path = self.path.replace("[Album]", self.data['title'])

        if os.path.isdir(self.path) != True: os.makedirs(self.path)
        os.chdir(self.path)

    def rip(self):
        
        os.system("cdparanoia " + self.config['Configuration']['CdparanoiaOptions'])        




