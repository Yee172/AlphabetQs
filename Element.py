#!/usr/bin/env python3
# coding: utf-8
__author__ = 'Yee_172'
__data__ = '2017/9/27'


# import numpy as np


class Word:
    """
    A class of word
    """
    total = 0
    def __init__(self, line):
        self.family = line[1][0].upper()
        self.num = int(line[0])
        self.word = line[1]
        self.definition = line[2]
        self.sample = line[3]
        Word.total += 1

    def get_sample(self):
        return self.sample.replace('``', '\033[1;31m').replace('`', '\033[0m')


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
        self.familys = {'A': Family('A', words), 'B': Family('B', words), 'C': Family('C', words),\
                        'D': Family('D', words), 'E': Family('E', words), 'F': Family('F', words),\
                        'G': Family('G', words), 'H': Family('H', words), 'I': Family('I', words),\
                        'J': Family('J', words), 'K': Family('K', words), 'L': Family('L', words),\
                        'M': Family('M', words), 'N': Family('N', words), 'O': Family('O', words),\
                        'P': Family('P', words), 'Q': Family('Q', words), 'R': Family('R', words),\
                        'S': Family('S', words), 'T': Family('T', words), 'U': Family('U', words),\
                        'V': Family('V', words), 'W': Family('W', words), 'X': Family('X', words),\
                        'Y': Family('Y', words), 'Z': Family('Z', words)}
