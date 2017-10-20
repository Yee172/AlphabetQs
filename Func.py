#!/usr/bin/env python3
# coding: utf-8
__author__ = 'Yee_172'
__data__ = '2017/9/26'
__all__ = ['alphabet', 'terminal_version_old', 'MainWin', 'app', 'sys']

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
    if not content:
        return None
    try:
        if isinstance(content, int):
            for each in alphabet.words:
                if each.num == content:
                    return each
        if isinstance(content, str):
            letter = content[0].upper()
            for each in alphabet.families[letter].words:
                if each.word.lower() == content.lower():
                    return each
    except:
        return None
    return None


def clear_screen():
    os.system('clear')


def random_word(letter='all'):
    return alphabet.get_random(letter)


def str_process(string):
    return string.translate(string.maketrans('', '', ' ,;()[]{}')).lower()


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
    print('Initial mode is SEARCH mode!')
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

    MODE = 'SEARCH'
    WORD = None
    CODE = 0
    LENGTH = 60
    COMMANDING = 1
    WORDLIST_NUM = 0
    HISTORY_NUM = 0
    EMPTY_MODEL = QtGui.QStandardItemModel()

    def __init__(self):
        super(MainWin, self).__init__()
        self.setupUi(self)
        self.initializing()
        self.wordlist_show()
        self.button_show_wordlist.clicked.connect(self.wordlist_click)
        self.button_help.clicked.connect(self.show_help)
        self.button_clear.clicked.connect(self.clear)
        self.console.returnPressed.connect(self.console_operate)
        self.check_code.stateChanged.connect(self.code_update)
        self.combo_box_mode.currentIndexChanged.connect(self.mode_update)
        self.show()

    def code_update(self):
        self.CODE = self.check_code.checkState()

    def mode_update(self):
        self.MODE = self.combo_box_mode.currentText()
        self.console_show_history.append('MODE changed into %s' % self.MODE)

    def initializing(self):
        self.console_show_history.append('Initial mode is SEARCH MODE!')
        self.console_show_history.append('You can input word or num!')
        self.console_show_history.append('Input `help` for more commands available!')

    def wordlist_click(self):
        content = self.button_show_wordlist.text()
        if content == 'SHOW':
            self.wordlist_show()
        if content == 'HIDE':
            self.wordlist_hide()

    def wordlist_show(self):
        wordlist_model = QtGui.QStandardItemModel(0, 2, self)
        wordlist_model.setHeaderData(0, Qt.Horizontal, '#')
        wordlist_model.setHeaderData(1, Qt.Horizontal, 'WORD')
        self.wordlist.setModel(wordlist_model)
        self.wordlist.setColumnWidth(0, 30)
        self.wordlist.setColumnWidth(1, 30)
        for each in alphabet.words:
            self.add_data(wordlist_model, each.num, each.word)
        _translate = QCoreApplication.translate
        self.button_show_wordlist.setText(_translate("Dialog", "HIDE"))

    def wordlist_hide(self):
        self.wordlist.setModel(self.EMPTY_MODEL)
        self.WORDLIST_NUM = 0
        _translate = QCoreApplication.translate
        self.button_show_wordlist.setText(_translate("Dialog", "SHOW"))

    def add_data(self, model, num, word):
        model.insertRow(self.WORDLIST_NUM)
        model.setData(model.index(self.WORDLIST_NUM, 0), num)
        model.setData(model.index(self.WORDLIST_NUM, 1), word)
        self.WORDLIST_NUM += 1

    def show_help(self):
        self.console_show_history.append(''.center(self.LENGTH, '-'))
        self.console_show_history.append('help'.ljust(7) + '\t->\t' + 'Help information')
        self.console_show_history.append('clear'.ljust(7) + '\t->\t' + 'Clear all the history')
        self.console_show_history.append('mode'.ljust(7) + '\t->\t' + 'Show or change the mode')
        self.console_show_history.append(''.ljust(7) + '\t\t      Example: ' + 'mode random')
        self.console_show_history.append('show'.ljust(7) + '\t->\t' + 'Show the word list')
        self.console_show_history.append('hide'.ljust(7) + '\t->\t' + 'Hide the word list')
        self.console_show_history.append('quit'.ljust(7) + '\t->\t' + 'Exit the program')
        self.console_show_history.append(''.center(self.LENGTH, '-'))

    def clear(self):
        self.HISTORY_NUM = 0
        self.console_show_history.clear()

    def console_operate(self):
        def read(content):
            content = content.lower()
            if self.WORD is None:
                if content == 'help':
                    self.show_help()
                elif content == 'clear':
                    self.clear()
                elif content[:4] == 'mode':
                    mode = str_process(content[4:])
                    if not mode:
                        mode_change()
                    elif mode in ['s', 'sear', 'search']:
                        mode_change('SEARCH')
                    elif mode in ['r', 'rand', 'random']:
                        mode_change('RANDOM')
                elif content == 'show':
                    self.wordlist_show()
                    self.console_show_history.append('Word list showed')
                elif content == 'hide':
                    self.wordlist_hide()
                    self.console_show_history.append('word list hid')
                elif content == 'quit':
                    pass
                elif self.MODE == 'SEARCH' and ' ' not in content:
                    try:
                        content = int(content)
                    except:
                        pass
                    self.WORD = find_word(content)
                    if self.WORD is None:
                        self.console_show_history.append('Undefined')
                    else:
                        self.info_clear()
                        self.label_word_show.setText(self.WORD.word)
                        self.label_info.setText('Definition of [%s] required' % self.WORD.word)
                else:
                    self.console_show_history.append('Undefined')
            else:
                search_q(self.WORD, content)
                self.WORD = None
                self.label_info.setText('')

        def mode_change(mode=''):
            if mode:
                self.MODE = mode
                self.combo_box_mode.setCurrentIndex({'SEARCH': 0, 'RANDOM': 1}[mode])
                self.console_show_history.append('MODE changed into %s' % self.MODE)
            else:
                self.console_show_history.append('MODE now is %s' % self.MODE)

        def search_q(word, definition):
            self.console_show_history.append(''.center(self.LENGTH, '-'))
            if str_process(word.definition) == str_process(definition):
                self.console_show_history.append('<html><head/>'
                                                 '<﻿span style=" font-weight:600; color:#ff0000;">'
                                                 '√'
                                                 '</span></html>')
            else:
                self.console_show_history.append('<html><head/>'
                                                 '<﻿span style=" font-weight:600; color:#ff0000;">'
                                                 '×'
                                                 '</span></html>')
            self.console_show_history.append('↓\tYour definition\t↓\n%s' % definition)
            self.console_show_history.append('%s\n↑\tReal definition\t↑' % word.definition)
            self.console_show_history.append(''.center(self.LENGTH, '-'))
            self.info_show(word)

        self.HISTORY_NUM += 1
        text = self.console.text()
        self.console.setText('')
        if self.CODE:
            self.console_show_history.append('[%d]>>> ' % self.HISTORY_NUM + text)
        read(text)

    def keyPressEvent(self, QKeyEvent):
        if QKeyEvent.key() == Qt.Key_Escape:
            self.close()

    def info_show(self, word):
        self.label_word_show.setText(word.word)
        self.label_def_show.setText(word.definition)
        self.label_samp_show.setText(word.html_sample())

    def info_clear(self):
        self.label_word_show.setText('')
        self.label_def_show.setText('')
        self.label_samp_show.setText('')


# ---[test zone]---
# print(alphabet.get_random('A').word)
