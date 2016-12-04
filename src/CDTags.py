#!/usr/bin/env python
# -*- coding: utf-8 -*-


import musicbrainzngs, discid

musicbrainzngs.set_useragent("pancakerip", "0.01", "arturdwieszopy@gmail.com")


disc_id = discid.read()
full_data = musicbrainzngs.get_releases_by_discid(disc_id, includes=['artists', 'recordings', 'artist-credits'])['disc']['release-list'][0]

artist = full_data['artist-credit'][0]['artist']['name']
if artist == "Various Artists":
    artist = {}
    for i in full_data['medium-list'][0]['track-list']:
        artist[i['number']] = i['artist-credit-phrase']
album = full_data['title']
year = full_data['date']
total_tracks = full_data['medium-list'][0]['disc-list'][0]['offset-count']
tracks = {}

for i in full_data['medium-list'][0]['track-list']:
    tracks[i['number']] = i['recording']['title']
