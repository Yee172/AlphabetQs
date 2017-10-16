#!/usr/bin/env python3
# coding: utf-8
__author__ = 'Yee_172'
__data__ = '2017/9/26'
__all__ = ['alphabet', 'find_word', 'clear_screen', 'random_word', 'definition_q', 'terminal_version_old',
           'MainWin', 'app', 'sys']

import os
import sys
import pandas as pd
from PyQt5 import QtGui, QtWidgets
from PyQt5.QtCore import Qt, QCoreApplication
from GUI.main import Ui_Dialog
from Element import Word, Alphabet


PATH = './Lib/E_alphabet.csv'
app = QtWidgets.QApplication(sys.argv)


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
        for each in alphabet.families[letter].words:
            if each.word.lower() == content.lower():
                return each
    return None


def clear_screen():
    os.system('clear')


def random_word(letter='all'):
    return alphabet.get_random(letter)


def str_process(string):
    return string.translate(string.maketrans('', '', ' ,;')).lower()


def definition_q(word):
    definition = input('Your definition: ')
    print()
    print('Your definition: %s' % definition)
    print('Real definition: %s' % word.definition)
    if str_process(word.definition) == str_process(definition):
        print('Exactly!')
    else:
        print('Not so good!')
    print()
    print('Sample sentence: %s' % word.get_sample())
    print('\n' * 17)


def terminal_version_old():
    MODE = 'SEARCH'
    RANDOM_LETTER = 'all'
    print('Initail mode is SEARCH mode!')
    while 1:
        if MODE.lower() == 'search':
            print()
            content = input('Your word or num: ')
            if content.lower() in ['q', 'quit', 'exit']:
                break
            if content.lower() in ['r', 'rand', 'random']:
                clear_screen()
                print('You are in RANDOM mode now!')
                MODE = 'RANDOM'
                continue
            try:
                content = int(content)
            except:
                pass
            word = find_word(content)
            if word is None:
                continue
            print('\nYour word:       %s' % word.word)
            definition_q(word)
        if MODE.lower() == 'random':
            print()
            content = input('Your random letter: ')
            if content.lower() in ['q', 'quit', 'exit']:
                break
            if content.lower() in ['s', 'sear', 'search']:
                clear_screen()
                print('You are in SEARCH mode now!')
                MODE = 'SEARCH'
                continue
            try:
                word = random_word(content)
                if word is None:
                    print('Word not available! Rolling back!')
                    raise
                RANDOM_LETTER = content
            except:
                word = random_word(RANDOM_LETTER)
            print('        #      : %d' % word.num)
            print('Your word      : %s' % word.word)
            definition_q(word)


class MainWin(QtWidgets.QWidget, Ui_Dialog):

    WORDLIST_NUM = 0
    EMPTY_MODEL = QtGui.QStandardItemModel()

    def __init__(self):
        super(MainWin, self).__init__()
        self.setupUi(self)
        self.button_show_wordlist.clicked.connect(self.wordlist_click)
        self.console.textChanged.connect(self.console_operate)
        self.show()

    def wordlist_click(self):
        content = self.button_show_wordlist.text()
        _translate = QCoreApplication.translate
        if content == 'SHOW':
            self.wordlist_show()
            self.button_show_wordlist.setText(_translate("Dialog", "HIDE"))
        if content == 'HIDE':
            self.wordlist_hide()
            self.button_show_wordlist.setText(_translate("Dialog", "SHOW"))

    def wordlist_show(self):
        wordlist_model = QtGui.QStandardItemModel(0, 2, self)
        wordlist_model.setHeaderData(0, Qt.Horizontal, '#')
        wordlist_model.setHeaderData(1, Qt.Horizontal, 'WORD')
        self.wordlist.setModel(wordlist_model)
        self.wordlist.setColumnWidth(0, 30)
        for each in alphabet.words:
            self.add_data(wordlist_model, each.num, each.word)

    def wordlist_hide(self):
        self.wordlist.setModel(self.EMPTY_MODEL)
        self.WORDLIST_NUM = 0

    def add_data(self, model, num, word):
        model.insertRow(self.WORDLIST_NUM)
        model.setData(model.index(self.WORDLIST_NUM, 0), num)
        model.setData(model.index(self.WORDLIST_NUM, 1), word)
        self.WORDLIST_NUM += 1

    def console_operate(self):
        pass

    def keyPressEvent(self, QKeyEvent):
        if QKeyEvent.key() == Qt.Key_Escape:
            self.close()


# ---[test zone]---
# print(alphabet.get_random('A').word)
