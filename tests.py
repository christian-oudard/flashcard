from nose.tools import assert_equal

from flashcard import load_cards

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
