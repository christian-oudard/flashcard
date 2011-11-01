#! /usr/bin/env python3

import os.path
import re
import sys

_card_regex = re.compile(
    r'(?P<word>\w+) ?(?P<pronunciation>\([\w\d]+\)) - (?P<definition>.*)',
    re.UNICODE,
)
def load_cards(deck_string):
    cards = []
    for line in deck_string.splitlines():
        line = line.strip()
        if line == '':
            continue
        if line.startswith('#'):
            continue
        m = _card_regex.match(line)
        if m is None:
           print('Invalid Line: %s' % line)
           continue
        word = m.group('word')
        pronunciation = m.group('pronunciation').strip('()')
        definition = m.group('definition')

        cards.append((word, pronunciation, definition))

    return cards

def main(args):
    if len(args) < 1:
        print('Please specify a deck of flash cards.')
        return

    # Load cards.
    deck_filename = args[0]
    deck_folder, deck_name = os.path.split(deck_filename)
    with open(deck_filename) as f:
        deck_data = f.read()
    cards = load_cards(deck_data)

    # Load stats.
    stats_filename = os.path.join(deck_folder, deck_name + '.stats')

    if os.path.exists(stats_filename):
        with open(stats_filename) as f:
            stats_data = f.read()
        old_stats = load_stats(stats_data)
    else:
        old_stats = {}

    # Start a quiz.
    new_stats = do_quiz(cards, old_stats)
    print(new_stats)

def do_quiz(cards, old_stats):
    new_stats = {}
    #STUB
    return new_stats

def load_stats(stats_data):
    #STUB
    return {}

if __name__ == '__main__':
    main(sys.argv[1:])
