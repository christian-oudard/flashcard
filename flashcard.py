#! /usr/bin/env python3
# coding: utf-8

import re

_card_regex = re.compile(
    r'(?P<word>\w+) ?(?P<pronunciation>\([\w\d]+\)) - (?P<definition>.*)',
    re.UNICODE,
)
def load_cards(deck_string):
    """
    >>> load_cards('')
    []
    >>> load_cards('''
    ... # comment
    ... 你好 (ni3hao3) - hello
    ... 永 (yong3) - eternity
    ... ''')
    [('你好', 'ni3hao3', 'hello'), ('永', 'yong3', 'eternity')]
    """
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
        word = m.group('word')
        pronunciation = m.group('pronunciation').strip('()')
        definition = m.group('definition')

        cards.append((word, pronunciation, definition))

    return cards
