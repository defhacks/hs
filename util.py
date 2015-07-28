import warnings
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
    for k,v in b.items():
        if v == 0:
            continue
        else:
            if v > 0:
                print("+%s %s" % (v,k))
            else:
                print("%s %s" % (v,k))


