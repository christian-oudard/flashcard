import os
import sys
from io import StringIO
from contextlib import contextmanager

from nose.tools import assert_equal

from flashcard import load_cards, main

test_data = '''\
# comment

你好 (ni3hao3) - hello
永 (yong3) - eternity
'''

@contextmanager
def assert_output(expected):
    old_stdout = sys.stdout
    sys.stdout = fake_stdout = StringIO()
    yield
    sys.stdout = old_stdout
    fake_stdout.seek(0)
    actual = fake_stdout.read()
    assert_equal(actual, expected)

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
    with assert_output('Invalid Line: bad line\n'):
        assert_equal(load_cards('bad line'), [])

def test_main():
    with open('testfile', 'w') as f:
        f.write(test_data)

    with assert_output('{}\n'):
        main(['testfile'])

    os.remove('testfile')

def test_main_error():
    with assert_output('Please specify a deck of flash cards.\n'):
        main([])

def test_load_stats():
    with open('testfile', 'w') as f:
        f.write(test_data)
    with open('testfile.stats', 'w') as f:
        f.write('\n')

    with assert_output('{}\n'):
        main(['testfile'])

    os.remove('testfile')
    os.remove('testfile.stats')
