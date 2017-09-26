#!/usr/bin/env python3
# coding: utf-8
__author__ = 'Yee_172'
__data__ = '2017/9/26'


import os
import numpy as np
import pandas as pd


# def get_each_value(array, i):
#     string = str(array.ix[i].values).replace('[', '').replace(']', '')
#     string = string.replace('\'', '', 3).replace('\'', '', -1).split(' ', 2)
#     return string


PATH = './Lib/Alphabet.csv'
alphabet = pd.read_csv(PATH).values
LENGTH = len(alphabet)


def find_word_index(word):
    for i in range(LENGTH):
        if alphabet[i, 1].lower() == word.lower():
            return i
    return -1


while 1:
    print()
    word = input('Your word: ')
    if word in ['q', 'quit', 'exit']:
        break
    index = find_word_index(word)
    if index is -1:
        continue
    definition = input('Your definition: ')
    print()
    print('Your definition: %s' % definition)
    print('Real definition: %s' % alphabet[index, 2])
    if alphabet[index, 2].lower() == definition.lower():
        print('Exactly!')
    else:
        print('Not so good!')
    print('\n' * 18)

