#!/usr/bin/env python3
# coding: utf-8
__author__ = 'Yee_172'
__date__ = '2017/9/27'
__all__ = ['Word', 'Family', 'Alphabet']


import random


class Word:
    """
    A class of word
    """
    total = 0

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
        except:
            self.thesaurus = None
        Word.total += 1

    def get_sample(self):
        return self.sample.replace('``', '\033[1;31m').replace('`', '\033[0m')

    def html_sample(self):
        return self.sample\
            .replace('``', '<html><head/><span style=" color:#ff0000;">')\
            .replace('`', '</span></html>')\
            .replace('\\n', '<br/>')


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
        self.total = Word.total
        self.words = words
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
