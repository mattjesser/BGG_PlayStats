# -*- coding: utf-8 -*-
"""
Pull Raw BGG Game Data


Documentation
    Play API: 
    http://www.boardgamegeek.com/xmlapi2/plays?username=foo&page=1

    User DB:
    https://drive.google.com/open?id=0B_ogAOq8UVpWYUs5TGlGQkdUbzg

TODO
- Make API call for a User from DB
- Chech for date of play
    Stop loop if date of play <2014
- Check for # of plays
    Add row for each play if # of plays <= 20
- Check for player information (maybe just flag the use of the functionality?)
- Request next page and continue looping
- Write data to a Master Play DB
- Close Request connection

"""

import requests as rq
import xmltodict as xtd


def get_usr_plys(user, page):

    url = 'http://www.boardgamegeek.com/xmlapi2/plays?username=%s&page=%i' % (user, page)
    
    apicall = rq.get(url)
    
    username = xtd.parse(apicall.text)['plays']['@username']
    userid = xtd.parse(apicall.text)['plays']['@userid']
    totalplays = xtd.parse(apicall.text)['plays']['@total']
    playdata= xtd.parse(apicall.text)['plays']['play']
    
    z = 1
    if playdata[z]['@date'] >= '2014-01-01':
        print username, userid, totalplays
        print playdata[z]['@id']
        print playdata[z]['@date']
        print playdata[z]['@quantity']
        print playdata[z]['@length']
        print playdata[z]['item']['@name']
        print playdata[z]['item']['@objectid']
        try:
            n = len(playdata[z]['players']['player'])
            print 'this play has %i players' % (n)
        except:
            print 'no player data'
    elif:
        #get to end of xml file
        #write to disk
        #test if another page exists then goto next page or finish user
    else:
        #write data to disk
        #finish user
    
    #close connection
    #


get_usr_plys('mattjesser')