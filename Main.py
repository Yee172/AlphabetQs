#!/usr/bin/env python3
# coding: utf-8
__author__ = 'Yee_172'
__data__ = '2017/9/26'


import numpy as np
import pandas as pd


PATH = './Lib/Alphabet.csv'
alphabet = pd.read_csv(PATH)
alphabet = alphabet.ix[0]

# while 1:
    # word = input('Your word: ')
word = 'Abundant'
print(alphabet)

