#!/usr/bin/env python
# -*- coding: utf-8 -*-

import musicbrainzngs, discid

musicbrainzngs.set_useragent("pancakerip", "0.01", "arturdwieszopy@gmail.com")

disc_info = {}

disc_id = discid.read()
full_data = musicbrainzngs.get_releases_by_discid(disc_id, includes=['artists', 'recordings', 'artist-credits'])['disc']['release-list'][0]

disc_info['artist'] = full_data['artist-credit'][0]['artist']['name']
if disc_info['artist'] == "Various Artists":
    disc_info['artist'] = {}
    for i in full_data['medium-list'][0]['track-list']:
        disc_info['artist'][i['number']] = i['artist-credit-phrase']
disc_info['year'] = full_data['date']
disc_info['title'] = full_data['title']
disc_info['total_tracks'] = full_data['medium-list'][0]['disc-list'][0]['offset-count']
disc_info['total_discs'] = full_data['medium-count']

disc_info['tracks'] = {}

if disc_info['total_discs'] > 1:

    toc = []
    for i in disc_id.toc_string.split(" ")[3:]:
        toc.append(int(i))

    for i in full_data['medium-list']:
        if i ['disc-list'][0]['offset-list'] == toc:
            disc_data = i

    for i in disc_data['track-list']:
        disc_info['tracks'][i['number']] = i['recording']['title']

    disc_info['disc_number'] = disc_data['position']
    disc_info['disc_title'] = disc_data['title']
    disc_info['total_tracks'] = disc_data['disc-list'][0]['offset-count']

else:
    
    for i in full_data['medium-list'][0]['track-list']:
        disc_info['tracks'][i['number']] = i['recording']['title']


