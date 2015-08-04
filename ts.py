#!/usr/bin/env python

from __future__ import print_function
import json
import os
import sys
import requests
import pprint
from bs4 import BeautifulSoup

pp = pprint.PrettyPrinter(indent=4)
post_url = 'https://tempostorm.com/deck'

def get_cards_from_card_list(card_list):
    cards = dict()
    count = 0
    for x in card_list:
        card = x['card']['name']
        count_str = x['qty']
        count = int(count_str)
        #print("%s x %d" % (card, count))
        cards[card] = count
    return cards

def url_to_decklist(url):
    slug = url.split('/')[-1]
    headers = { 'Content-type' : 'application/json' } # , 'Accept' : 'text/plain' }
    payload = { 'slug' : slug }
    r = requests.post(post_url, data=json.dumps(payload), headers=headers)
    data = json.loads(r.content.decode('utf-8'))
    #pp.pprint(data)
    card_list = data['deck']['cards']
    #print(card_list.prettify().encode('utf-8'))
    decklist = get_cards_from_card_list(card_list)
    return decklist

def print_decklist(decklist):
    for card, count in decklist.items():
        print("%s x %d" % (card, count)) 

if __name__ == "__main__":
    url = 'https://tempostorm.com/hearthstone/decks/era-control-mage'
    decklist = url_to_decklist(url)
    #pp.pprint(decklist)
    print_decklist(decklist)
