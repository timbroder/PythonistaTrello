#Add card to List

import urllib2
import urllib
import json
import sys
import webbrowser

arglen = len(sys.argv)

if arglen < 5:
    raise Exception("Usage: list_trello_lists.py [token] [list_id] [position] [card_name]")

name = sys.argv[4]

if arglen > 5:
    for i in range(5,arglen):
        name = "%s %s" % (name, sys.argv[i])

key = "3e2cd730f3dcccbe15eaf0d39d219a37"
token = sys.argv[1]
args = { 'key': key,
    'token': sys.argv[1],
    'name': name,
    'pos': sys.argv[3],
    'idList': sys.argv[2]
    }
card_add_url = "https://api.trello.com/1/cards"

try:
    data = urllib2.urlopen(card_add_url, urllib.urlencode(args))
except urllib2.HTTPError as inst:
    raise Exception("Key or Token incorrect")

webbrowser.open("launchpro:")
