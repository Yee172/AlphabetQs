#!/usr/bin/env python3
# coding: utf-8
__author__ = 'Yee_172'
__date__ = '2017/9/27'
__all__ = ['Word', 'Family', 'Alphabet', 'THESAURUS_POOL']


import re
import random
from functools import reduce


THESAURUS_POOL = set()


class Word:
    """
    A class of word
    """
    def __init__(self, line):
        self.num = int(line['#'])
        self.word = line['WORD']
        self.definition = line['DEFINITION']
        self.sample = line['SAMPLE SENTENCE']
        self.family = self.word[0].upper()
        try:
            self.word_type = eval(line['WORD TYPE'])
        except:
            self.word_type = None
        try:
            self.derivatives = eval(line['DERIVATIVES'])
        except:
            self.derivatives = None
        try:
            self.thesaurus = eval(line['THESAURUS'])
            for each in self.thesaurus:
                THESAURUS_POOL.update(self.thesaurus[each])
        except:
            self.thesaurus = None

    def get_sample(self):
        return self.sample.replace('``', '\033[1;31m').replace('`', '\033[0m')

    def html_definition(self):
        return self.definition.replace('\\n', '<br/>')

    def html_sample(self):
        return self.sample\
            .replace('``', '<html><span style=" color:#ff0000;">')\
            .replace('`', '</span></html>')\
            .replace('\\n', '<br/>')

    def html_sample_hollow(self):
        return re.sub(r'``.*`',
                      '<html><span style=" color:#ff0000;">'
                      '__?__'
                      '</span></html>',
                      self.sample).replace('\\n', '<br/>')

    def html_thesaurus(self):
        html_string = ''
        if self.thesaurus:
            for each in self.thesaurus:
                html_string += '<html><span style=" color:#ff0000;">' + each + '</span></html><br/>'
                html_string += '<br/>'.join(self.thesaurus[each]) + '<br/>'
        return html_string

    def get_random_html_thesaurus(self):
        html_string = ''
        if self.thesaurus:
            pool = reduce(lambda x, y: x + y, self.thesaurus.values())
            html_string += random.sample(pool, 1)[0]
        else:
            html_string += 'thesaurus NOT available'
        return html_string


class Family:
    """
    A class of a group of words
    """
    def __init__(self, letter, words):
        self.letter = letter.upper()
        self.words = [word for word in words if word.family == self.letter]


class Alphabet:
    """
    A class of Alphabet
    """
    def __init__(self, words):
        self.words = words
        self.total = len(self.words)
        self.index = self.total - 1
        families = set(each.family for each in self.words)
        self.families = {}
        for each in families:
            self.families[each] = Family(each, words)

    def get_random(self, letter='all'):
        if letter.lower() in ['all', 'each', 'every']:
            if len(self.words) > 0:
                return self.words[random.randint(0, len(self.words) - 1)]
        else:
            words = self.families[letter.upper()].words
            if len(words) > 0:
                return words[random.randint(0, len(words) - 1)]
        return None

    def get_next(self, step=1):
        self.index = (self.index + step) % self.total
        return self.words[self.index]
