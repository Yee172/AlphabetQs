#!/usr/bin/env python3
# coding: utf-8
__author__ = 'Yee_172'
__data__ = '2017/9/26'
__all__ = ['find_word', 'clear_screen', 'random_word', 'definition_q']


import os
import pandas as pd
from Element import Word, Family, Alphabet

PATH = './Lib/E_alphabet.csv'


def read_in(csvfile):
    return pd.read_csv(csvfile).values


alphabet = Alphabet([Word(x) for x in read_in(PATH)])


def find_word(content):
    if not content: return None
    if isinstance(content, int):
        for each in alphabet.words:
            if each.num == content:
                return each
    if isinstance(content, str):
        letter = content[0].upper()
        for each in alphabet.familys[letter].words:
            if each.word.lower() == content.lower():
                return each
    return None


def clear_screen():
    os.system('clear')


def random_word(letter='all'):
    return alphabet.get_random(letter)


def definition_q(word):
    definition = input('Your definition: ')
    print()
    print('Your definition: %s' % definition)
    print('Real definition: %s' % word.definition)
    if word.definition.lower() == definition.lower():
        print('Exactly!')
    else:
        print('Not so good!')
    print()
    print('Sample sentence: %s' % word.get_sample())
    print('\n' * 17)


# ---[test zone]---
# print(alphabet.get_random('A').word)
