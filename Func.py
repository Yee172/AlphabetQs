#!/usr/bin/env python3
# coding: utf-8
__author__ = 'Yee_172'
__data__ = '2017/9/26'
__all__ = ['read_in']


import numpy as np
import pandas as pd

PATH = './Lib/Alphabet.csv'


def read_in(csvfile):
    return pd.read_csv(csvfile).values


