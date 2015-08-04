import warnings
import hpwn
import hsp
import hstd
import ts
import re

from collections import Counter

def flatten_decklist(decklist):
    flat = list()
    for card, count in decklist.items():
        for _ in range(count):
            flat.append(card)
    if len(flat) != 30:
        warnings.warn("Incomplete decklist detected")
    flat.sort()
    return flat

def print_deckdiff(deck_a, deck_b):
    # TODO: check types and do optional flattening ?
    a = Counter(deck_a)
    b = Counter(deck_b)
    b.subtract(a)
    for k,v in b.most_common():
        if v == 0:
            continue
        else:
            if v > 0:
                print("+%s %s" % (v,k))
            else:
                print("%s %s" % (v,k))

def url_to_decklist(url):
    if re.match( r'^(https?://)?tempostorm', url):
        decklist = ts.url_to_decklist(url)
    elif re.match( r'^(https?://)?hearthpwn', url):
        decklist = hpwn.url_to_decklist(url)
    elif re.match( r'^(https?://)?hearthstonetopdecks', url):
        decklist = hstd.url_to_decklist(url)
    elif re.match( r'^(https?://)?hearthstoneplayers', url):
        decklist = hsp.url_to_decklist(url)
    else:
        raise ValueError('unsupported deck url: %s' % (url))

    return decklist

