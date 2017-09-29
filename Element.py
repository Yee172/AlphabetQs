#!/usr/bin/env python3
# coding: utf-8
__author__ = 'Yee_172'
__data__ = '2017/9/27'


import numpy as np


class Word:
    """
    A class of word
    """
    total = 0
    def __init__(self, line):
        self.family = line[1][0].upper()
        self.num = int(line[0])
        self.word = line[1].lower()
        self.definition = line[2].lower()
        self.sample = line[3].lower()
        total += 1
