import os
import random
import sys
from contextlib import contextmanager
from io import StringIO
from textwrap import dedent

from nose.tools import assert_equal, with_setup

from flashcard import load_cards, main

# Testing utilities.

test_data = dedent('''\
    # comment

    你好 (ni3hao3) - hello
    永 (yong3) - eternity
''')

test_input = '\nY\n\nN\n'

test_output = dedent('''\
    Found 2 cards
    Press Enter to flip card, Q to quit.

    ========================================

    你好

    ----------------------------------------

    ni3hao3
    hello

    Were you correct? (Y/N)
    ========================================

    永

    ----------------------------------------

    yong3
    eternity

    Were you correct? (Y/N)
''')

def fix_whitespace(s):
    return '\n'.join(line.rstrip() for line in s.splitlines())

@contextmanager
def assert_output(expected):
    old_stdout = sys.stdout
    sys.stdout = fake_stdout = StringIO()
    yield
    sys.stdout = old_stdout
    fake_stdout.seek(0)
    actual = fake_stdout.read()
    assert_equal(fix_whitespace(actual), fix_whitespace(expected))

@contextmanager
def fake_input(input_data):
    old_stdin = sys.stdin
    sys.stdin = fake_stdin = StringIO(input_data)
    fake_stdin.seek(0)
    yield
    sys.stdin = old_stdin

def setup_fake_cards():
    with open('fake_cards', 'w') as f:
        f.write(test_data)

def teardown_fake_cards():
    os.remove('fake_cards')

def setup_fake_cards_stats():
    with open('fake_cards.stats', 'w') as f:
        f.write('\n')

def teardown_fake_cards_stats():
    os.remove('fake_cards.stats')

# Test functions.

def test_load_cards():
    assert_equal(load_cards(''), [])
    assert_equal(
        load_cards(test_data),
        [
            ('你好', 'ni3hao3', 'hello'),
            ('永', 'yong3', 'eternity'),
        ]
    )

def test_load_cards_error():
    with assert_output(''):
        assert_equal(load_cards('bad line'), [])

def test_main_error():
    with assert_output('Please specify a deck of flash cards.'):
        main([])

@with_setup(setup_fake_cards, teardown_fake_cards)
def test_main():
    random.seed(0);
    with fake_input(test_input):
        with assert_output(test_output):
            main(['fake_cards'])

@with_setup(setup_fake_cards, teardown_fake_cards)
@with_setup(setup_fake_cards_stats, teardown_fake_cards_stats)
def test_main_load_stats():
    random.seed(0);
    with fake_input(test_input):
        with assert_output(test_output):
            main(['fake_cards'])

@with_setup(setup_fake_cards, teardown_fake_cards)
def test_main_quit():
    random.seed(0);
    with fake_input('q\n'):
        with assert_output(dedent('''\
            Found 2 cards
            Press Enter to flip card, Q to quit.

            ========================================

            你好

        ''')):
            main(['fake_cards'])
