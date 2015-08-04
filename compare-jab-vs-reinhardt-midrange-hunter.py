#!/usr/bin/env python

import pprint
from util import flatten_decklist, print_deckdiff, url_to_decklist

pp = pprint.PrettyPrinter(indent=4)

url1 = 'http://www.hearthstonetopdecks.com/decks/reinhardts-season-16-midrange-hunter/'
url2 = 'http://www.hearthstonetopdecks.com/decks/jabs-season-16-midrange-hunter/'

#url_to_decklist(sys.argv[1])

decklist1 = url_to_decklist(url1)
decklist2 = url_to_decklist(url2)

#pp.pprint(decklist2)

#print_decklist(decklist)
#pp.pprint(flatten_decklist(decklist))
print_deckdiff(flatten_decklist(decklist1), flatten_decklist(decklist2))
