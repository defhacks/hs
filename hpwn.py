#!/usr/bin/env python

from __future__ import print_function
import os
import sys
import requests
import cfscrape
import pprint
from bs4 import BeautifulSoup
from util import flatten_decklist

pp = pprint.PrettyPrinter(indent=4)

def get_cards_from_tables(tables):
    cards = dict()
    for table in tables:
        for x in table.find_all('a'):
            if x['href'].startswith('/cards/'):
                count_str = x.parent.parent.contents[-1].strip()[-1] 
                card = x.contents[0]
                count = int(count_str)
                #print("%s x %d" % (card, count))
                cards[card] = count
    return cards

def url_to_decklist(url):
    sess = requests.session()
    sess = cfscrape.create_scraper(sess)
    r = sess.get(url)
    data = BeautifulSoup(r.content, "html.parser")
    tbls = data.find_all('table', id="cards")
    #print(tbl.prettify().encode('utf-8'))
    decklist = get_cards_from_tables(tbls)
    return decklist

def print_decklist(decklist):
    for card, count in decklist.items():
        print("%s x %d" % (card, count)) 

if __name__ == "__main__":
    url = 'http://www.hearthpwn.com/decks/276644-top-6-eu-loatheb-patron'
    #url_to_decklist(sys.argv[1])
    decklist = url_to_decklist(url)
    #pp.pprint(decklist)
    #print_decklist(decklist)
    pp.pprint(flatten_decklist(decklist))
