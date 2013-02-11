#List all lists by user

import urllib2
import urllib
import json
import sys

if len(sys.argv) != 3:
    raise Exception("Usage: list_trello_lists.py [token] [email]")

key = "3e2cd730f3dcccbe15eaf0d39d219a37"
args = { 'key': key,
    'token': sys.argv[1],
    'filter': 'open'}

#build out api url
username = sys.argv[2]
boards_url = "https://api.trello.com/1/members/%s/boards/?%s" % (username, urllib.urlencode(args))

#get board data from api
try:
    data = urllib2.urlopen(boards_url)
except urllib2.HTTPError as inst:
    raise Exception("Key or Token incorrect")

boards = json.loads(data.read())

#loop through each board
for board in boards:
    board_id = board['id']
    lists_url = "https://api.trello.com/1/boards/%s/lists?%s" % (board_id, urllib.urlencode(args))
    data = urllib2.urlopen(lists_url)
    lists = json.loads(data.read())

    print "-- %s" % board['name']
    #output each list in board
    for lizt in lists:
        print "\"%s\" %s" % (lizt['name'], lizt['id'])
    print "\n"
