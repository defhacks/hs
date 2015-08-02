#!/usr/bin/env python

from __future__ import print_function
import os
import sys
import requests
import pprint
from bs4 import BeautifulSoup
from util import flatten_decklist

pp = pprint.PrettyPrinter(indent=4)

def get_cards_from_card_list(card_list):
    cards = dict()
    count = 0
    for x in card_list.find_all('span', class_="card-title"):
        card = x.contents[0]
        count_span = x.parent.find_all('span', class_='card-count')
        if count_span:
            count = int(count_span[0].contents[0])
        else:
            count = 1
        #print("%s x %d" % (card, count))
        cards[card] = count
    return cards

def url_to_decklist(url):
    sess = requests.session()
    r = sess.get(url)
    data = BeautifulSoup(r.content, "html.parser")
    #pp.pprint(data)
    card_list = data.find('div', class_="deck-list")
    #print(card_list.prettify().encode('utf-8'))
    decklist = get_cards_from_card_list(card_list)
    return decklist

def print_decklist(decklist):
    for card, count in decklist.items():
        print("%s x %d" % (card, count)) 

if __name__ == "__main__":
    url = 'http://www.hearthstoneplayers.com/decks/aggro-paladin-2/'
    decklist = url_to_decklist(url)
    #pp.pprint(decklist)
    print_decklist(decklist)
    #pp.pprint(flatten_decklist(decklist))
