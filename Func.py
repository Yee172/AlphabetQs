#!/usr/bin/env python3
# coding: utf-8
__author__ = 'Yee_172'
__data__ = '2017/9/26'
__all__ = ['read_in']


import numpy as np
import pandas as pd
from Element import Word, Family, Alphabet

PATH = './Lib/Alphabet.csv'


def read_in(csvfile):
    return pd.read_csv(csvfile).values


# ---[test zone]---
alphabet = read_in(PATH)
words = [Word(x) for x in alphabet]
FamilyA = Family('A', words)
alphabet = Alphabet(words)
print(alphabet.familys['A'].words)
