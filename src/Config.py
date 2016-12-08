#!/usr/bin/env python
# -*- config: utf-8 -*-

import xmltodict
from xml.parsers.expat import ExpatError

class Config:
    
    def __init__(self):
        try:
            with open('Config.xml') as config_file:
                self.config = xmltodict.parse(config_file.read())
            config_file.close()

        except (ExpatError, IOError):
            self.config = {}

            self.config['Configuration'] = {}
            self.config['Configuration']['CdparanoiaOptions'] = '-B'
            self.config['Configuration']['CdparanoiaLocalisation'] = '/usr/bin/cdparanoia'
            self.config['Configuration']['Codec'] = 'flac'
            self.config['Configuration']['CodecLocalisation'] = '/usr/bin/flac'
            self.config['Configuration']['CodecOptions'] = '-V -8'
            self.config['Configuration']['Codec2'] = ''
            self.config['Configuration']['Codec2Localisation'] = ''
            self.config['Configuration']['Codec2Options'] = ''
            self.config['Configuration']['DestinationWav'] = '~/Muzyka/[Artist]/[Year] [Album]/WAV/'
            self.config['Configuration']['DestinationCodec'] = '/Muzyka/[Artist]/[Year] [Album]/[Codec]/'

            with open('Config.xml', 'w') as config_file:
                config_file.write(xmltodict.unparse(self.config, pretty=True))
            config_file.close()

    def config_dict(self):
        return self.config

