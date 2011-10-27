import sys
from io import StringIO
from contextlib import contextmanager

from nose.tools import assert_equal

from flashcard import load_cards

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
        load_cards(
            '''
            # comment
            你好 (ni3hao3) - hello
            永 (yong3) - eternity
            '''
        ),
        [
            ('你好', 'ni3hao3', 'hello'),
            ('永', 'yong3', 'eternity'),
        ]
    )

def test_load_cards_error():
    with assert_output('Invalid Line: bad line\n'):
        assert_equal(load_cards('bad line'), [])
