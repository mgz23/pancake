#!/usr/bin/env python
# -*- coding: utf-8 -*-

import musicbrainzngs, discid
from musicbrainzngs.musicbrainz import ResponseError
from discid.disc import DiscError

musicbrainzngs.set_useragent("pancakerip", "0.01", "arturdwieszopy@gmail.com")

class CDTags:
    def __init__(self):

        self.disc_info = {}
        self.is_data = True

        try:
            self.disc_id = discid.read()
        except DiscError:
            print "There is no disc!"
                    
        try:
            self.full_data = musicbrainzngs.get_releases_by_discid(self.disc_id, includes=['artists', 'recordings', 'artist-credits'])['disc']['release-list'][0]
        except (ResponseError, AttributeError):
            self.is_data = False

    def read(self):
        
        if self.is_data == True:
            self.disc_info['artist'] = self.full_data['artist-credit'][0]['artist']['name']
            if self.disc_info['artist'] == "Various Artists":
                self.disc_info['artists'] = {}
                for i in self.full_data['medium-list'][0]['track-list']:
                    self.disc_info['artists'][i['number']] = i['artist-credit-phrase']
            self.disc_info['year'] = self.full_data['date']
            self.disc_info['title'] = self.full_data['title']
            self.disc_info['total_tracks'] = self.full_data['medium-list'][0]['disc-list'][0]['offset-count']
            self.disc_info['total_discs'] = self.full_data['medium-count']

            self.disc_info['tracks'] = {}

            if self.disc_info['total_discs'] > 1:

                toc = []
                for i in self.disc_id.toc_string.split(" ")[3:]:
                    toc.append(int(i))

                for i in self.full_data['medium-list']:
                    if i ['disc-list'][0]['offset-list'] == toc:
                        disc_data = i

                for i in disc_data['track-list']:
                    self.disc_info['tracks'][i['number']] = i['recording']['title']

                    self.disc_info['disc_number'] = disc_data['position']
                    self.disc_info['disc_title'] = disc_data['title']
                    self.disc_info['total_tracks'] = disc_data['disc-list'][0]['offset-count']

            else:
    
                for i in self.full_data['medium-list'][0]['track-list']:
                    self.disc_info['tracks'][i['number']] = i['recording']['title']

        else:
            self.disc_info['artist'] = "NoArtist"
            self.disc_info['title'] = "NoTitle"
            self.disc_info['year'] = "0000"

        return self.disc_info
