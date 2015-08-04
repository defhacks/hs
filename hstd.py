#!/usr/bin/env python

from __future__ import print_function
import os
import sys
import requests
import pprint
from bs4 import BeautifulSoup

pp = pprint.PrettyPrinter(indent=4)

def get_cards_from_card_list(card_list):
    cards = dict()
    for x in card_list.find_all('span', class_="card-name"):
        # TODO: if we ever want to sort by cost, we could grab it like so
        #card_cost = x.parent.contents[0]
        count_str = x.next_sibling.next_sibling.contents[0]
        card = x.contents[0]
        count = int(count_str)
        #print("%s x %d" % (card, count))
        cards[card] = count
    return cards

def url_to_decklist(url):
    sess = requests.session()
    r = sess.get(url)
    data = BeautifulSoup(r.content, "html.parser")
    #pp.pprint(data)
    card_list = data.find('div', id="deck-master")
    #print(card_list.prettify().encode('utf-8'))
    decklist = get_cards_from_card_list(card_list)
    return decklist

def print_decklist(decklist):
    for card, count in decklist.items():
        print("%s x %d" % (card, count)) 

if __name__ == "__main__":
    #url = 'http://www.hearthstonetopdecks.com/decks/mryaguts-season-14-face-warrior/'
    url = sys.argv[1].rstrip()
    decklist = url_to_decklist(url)
    #pp.pprint(decklist)
    print_decklist(decklist)
