#!/usr/bin/env python3
# coding: utf-8
__author__ = 'Yee_172'
__data__ = '2017/9/26'
__all__ = ['read_in', 'find_word']


import numpy as np
import pandas as pd
from Element import Word, Family, Alphabet

PATH = './Lib/Alphabet.csv'


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


# ---[test zone]---
# print(alphabet.get_random('A').word)
