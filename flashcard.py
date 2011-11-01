#! /usr/bin/env python3

import os.path
import random
import re
import sys
from collections import namedtuple

Card = namedtuple('Card', 'word pronunciation definition')

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
           continue
        word = m.group('word')
        pronunciation = m.group('pronunciation').strip('()')
        definition = m.group('definition')

        cards.append(Card(word, pronunciation, definition))

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
    print('Found {} cards'.format(len(cards)))

    # Load stats.
    stats_filename = os.path.join(deck_folder, deck_name + '.stats')

    if os.path.exists(stats_filename):
        with open(stats_filename) as f:
            stats_data = f.read()
        old_stats = load_stats(stats_data)
    else:
        old_stats = {}

    # Start a quiz.
    do_quiz(cards, old_stats)

def do_quiz(cards, old_stats):
    print('Press Enter to flip card, Q to quit.')
    random.shuffle(cards)
    for card in cards:
        front = [card.word]
        back = [card.pronunciation, card.definition]
        result = ask(front, back)
        if result == 'done':
            break
        elif result is True:
            pass#STUB, correct answer
        elif result is False:
            pass#STUB, incorrect answer

    new_stats = {}
    #STUB
    return new_stats

def ask(front, back):
    print()
    print('='*40)
    print()
    for line in front:
        print(line)
    print()

    while True:
        command = input()
        command = command.lower().strip()
        if command == '':
            break
        if command == 'q':
            return 'done'

    print('-'*40)
    print()
    for line in back:
        print(line)
    print()

    while True:
        command = input('Were you correct? (Y/N) ')
        command = command.lower().strip()
        if command == 'y':
            return True
        if command == 'n':
            return False

def load_stats(stats_data):
    #STUB
    return {}

if __name__ == '__main__':
    main(sys.argv[1:])
