#! /usr/bin/env python2.4
# coding: utf-8

from elementtree.ElementTree import parse

class Card(object):
    def __init__(self, ask_fields, answer_fields, box=1):
        '''Data structure to hold a card during quizzing
ask_fields - a sequence of field values to ask
answer_fields - a sequence of fields making the correct answer
box - integer value of the leitner box
        '''
        self.ask_fields = ask_fields
        self.answer_fields = answer_fields
        self.box = int(box)

    def __str__(self):
        return '\n'.join(self.ask_fields + ['-----'] + self.answer_fields)

def load_cards(deckfile):
    cards = []
    tree = parse(deckfile)
    xdeck = tree.getroot()

    for xcard in xdeck:
        fields = []
        stats = []
        # get field values and sides from xml
        for xitem in xcard:
            if xitem.tag == 'field':
                fields.append(xitem.text)
            elif xitem.tag == 'stats':
                stats.append((xitem.attrib['ask'],
                              xitem.attrib['answer'],
                              xitem.attrib['box']))
        # create a card for each variation of sides
        for (ask, answer, box) in stats:
            ask = [int(i) for i in ask.split(',')]
            answer = [int(i) for i in answer.split(',')]
            ask_fields = [fields[i-1] for i in ask]
            answer_fields = [fields[i-1] for i in answer]
            cards.append(Card(ask_fields, answer_fields, box))

    return cards

if __name__ == '__main__':
#    c = Card([u'你好'],['hello'])
#    print unicode(c)

    for c in load_cards(open('testdeck.xml')):
        print unicode(c)
        print
