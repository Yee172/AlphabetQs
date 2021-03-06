#!/usr/bin/env python3
# coding: utf-8
__author__ = 'Yee_172'
__date__ = '2017/9/26'
__all__ = ['ALPHABET', 'terminal_version_old', 'MainWin', 'app', 'sys']

import os
import sys
import platform
import pandas as pd
from PyQt5 import QtGui, QtWidgets, QtCore
from PyQt5.QtCore import Qt, QCoreApplication, QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWebChannel import QWebChannel
from GUI.main import Ui_Dialog
from Element import Word, Alphabet

PATH = './Lib/E_alphabet_volume_2.csv'
app = QtWidgets.QApplication(sys.argv)
SYSTEM = platform.system()
IS_OSX = SYSTEM == 'Darwin'
IS_WINDOWS = SYSTEM == 'Windows'


def read_in(csvfile):
    return pd.read_csv(csvfile)


READ_IN = read_in(PATH)
ALPHABET = Alphabet([Word(READ_IN.loc[i]) for i in range(len(READ_IN))])
del READ_IN


def find_word(content):
    if not content:
        return None
    try:
        if isinstance(content, int):
            for each in ALPHABET.words:
                if each.num == content:
                    return each
        if isinstance(content, str):
            letter = content[0].upper()
            for each in ALPHABET.families[letter].words:
                if each.word.lower() == content.lower():
                    return each
    except:
        return None
    return None


def clear_screen():
    os.system('clear')


def random_word(letter='all'):
    return ALPHABET.get_random(letter)


def str_process(string):
    return string.translate(string.maketrans('', '', ' ,.;()[]{}/\n')).lower()


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
                    raise()
                RANDOM_LETTER = content
            except:
                word = random_word(RANDOM_LETTER)
            print('        #      : %d' % word.num)
            print('Your word      : %s' % word.word)
            definition_q(word)


class MainWin(QtWidgets.QWidget, Ui_Dialog):
    ALPHABET = ALPHABET
    URL = ''
    MODE = 'SEARCH'
    ASKING = 'WORD'
    WORD = None
    CODE = 0
    MORE = 0
    LENGTH = 60
    CONTAIN = 0
    COMMANDING = 1
    WORDLIST_NUM = 0
    HISTORY_NUM = 0
    SEARCH_CONTENT = ''
    RELOAD_CONTENT = '%d-%d' % (ALPHABET.words[0].num, ALPHABET.words[-1].num)
    EMPTY_MODEL = QtGui.QStandardItemModel()

    def __init__(self):
        super(MainWin, self).__init__()
        self.setupUi(self)
        if IS_WINDOWS:
            x, y, width, height = self.button_show_wordlist.geometry().getRect()
            self.button_show_wordlist.setGeometry(QtCore.QRect(x + 5, y + 4, width - 10, height - 11))
            x, y, width, height = self.button_quit.geometry().getRect()
            self.button_quit.setGeometry(QtCore.QRect(x + 6, y + 4, width - 10, height - 11))
            x, y, width, height = self.button_help.geometry().getRect()
            self.button_help.setGeometry(QtCore.QRect(x + 6, y + 4, width - 10, height - 11))
            x, y, width, height = self.button_clear.geometry().getRect()
            self.button_clear.setGeometry(QtCore.QRect(x + 8, y + 4, width - 14, height - 11))
            x, y, width, height = self.combo_box_asking.geometry().getRect()
            self.combo_box_asking.setGeometry(QtCore.QRect(x + 3, y + 4, width - 6, height - 9))
            x, y, width, height = self.combo_box_mode.geometry().getRect()
            self.combo_box_mode.setGeometry(QtCore.QRect(x + 3, y + 4, width - 6, height - 9))
            x, y, width, height = self.button_reload.geometry().getRect()
            self.button_reload.setGeometry(QtCore.QRect(x + 8, y + 4, width - 10, height - 9))
        self.initializing()
        self.wordlist_show()

        self.web_viewer = QWebEngineView()
        self.web_viewer.setObjectName('web_viewer')
        # self.channel = QWebChannel(self.web_viewer)
        # self.web_viewer.setGeometry(QtCore.QRect(800, 20, 360, 450))

        self.button_show_wordlist.clicked.connect(self.wordlist_click)
        self.button_help.clicked.connect(self.show_help)
        self.button_clear.clicked.connect(self.clear)
        self.console.returnPressed.connect(self.console_operate)
        self.check_code.stateChanged.connect(self.code_update)
        self.check_more.stateChanged.connect(self.more_info)
        self.combo_box_asking.currentIndexChanged.connect(self.asking_update)
        self.combo_box_mode.currentIndexChanged.connect(self.mode_update)
        self.search_box.textChanged.connect(self.search)
        self.button_reload.clicked.connect(self.wordlist_reload)
        _translate = QCoreApplication.translate
        self.reload_selection_box.setPlaceholderText(
            _translate("Dialog", self.RELOAD_CONTENT))
        self.show()

    def code_update(self):
        self.CODE = self.check_code.checkState()

    def mode_update(self):
        self.MODE = self.combo_box_mode.currentText()
        self.console_show_history.append('MODE changed into %s' % self.MODE)

    def asking_update(self):
        self.ASKING = self.combo_box_asking.currentText()
        self.console_show_history.append('ASKING changed into %s' % self.ASKING)

    def more_info(self):
        self.MORE = self.check_more.checkState()
        if self.MORE:
            # self.resize(1200, 562)
            if self.WORD is not None:
                self.URL = 'http://www.youdao.com/w/eng/%s' % self.WORD.word.lower()
            if self.URL:
                self.web_viewer.setUrl(QUrl(self.URL))
                self.web_viewer.show()
        else:
            # self.resize(770, 562)
            self.web_viewer.close()
            pass

    def initializing(self):
        self.console_show_history.append('Initial mode is SEARCH MODE!')
        self.console_show_history.append('You can input word or num!')
        self.console_show_history.append('Input `help` for more commands available!')

    def search_words(self, content):
        result = []
        try:
            temp = int(content)
            if self.CONTAIN:
                for each in self.ALPHABET.words:
                    if content in '%03d' % each.num:
                        result.append(each)
                return result
            else:
                for each in self.ALPHABET.words:
                    if content == ('%03d' % each.num)[:len(content)]:
                        result.append(each)
                return result
        except:
            content = content.lower()
            if self.CONTAIN:
                for each in self.ALPHABET.words:
                    if content in each.word.lower():
                        result.append(each)
                return result
            else:
                for each in self.ALPHABET.words:
                    if content == each.word[:len(content)].lower():
                        result.append(each)
                return result

    def search(self):
        self.SEARCH_CONTENT = self.search_box.text()
        if self.SEARCH_CONTENT:
            if self.button_show_wordlist.text() == 'HIDE':
                self.wordlist_show(self.search_words(self.SEARCH_CONTENT))
        else:
            if self.button_show_wordlist.text() == 'HIDE':
                self.wordlist_show()

    def wordlist_reload(self):
        _translate = QCoreApplication.translate
        self.RELOAD_CONTENT = self.reload_selection_box.text()
        try:
            left, right = map(int, self.RELOAD_CONTENT.split('-'))
            left, right = min(left, right), max(left, right)
            READ_IN = read_in(PATH)
            self.ALPHABET = Alphabet([Word(READ_IN.loc[i])
                                      for i in range(len(READ_IN))
                                      if left <= int(READ_IN.loc[i]['#']) <= right])
            del READ_IN
            self.wordlist_show()
        except:
            self.reload_selection_box.setText(_translate("Dialog", ''))

    def wordlist_click(self):
        content = self.button_show_wordlist.text()
        if content == 'SHOW':
            if self.SEARCH_CONTENT:
                self.wordlist_show(self.search_words(self.SEARCH_CONTENT))
            else:
                self.wordlist_show()
        if content == 'HIDE':
            self.wordlist_hide()

    def wordlist_show(self, words=None):
        if words is None:
            words = self.ALPHABET.words
        wordlist_model = QtGui.QStandardItemModel(0, 2, self)
        wordlist_model.setHeaderData(0, Qt.Horizontal, '#')
        wordlist_model.setHeaderData(1, Qt.Horizontal, 'WORD')
        self.wordlist.setModel(wordlist_model)
        self.wordlist.setColumnWidth(0, 40)
        self.wordlist.setColumnWidth(1, 30)
        self.WORDLIST_NUM = 0
        if words:
            for each in words:
                self.add_data(wordlist_model, '%03d' % each.num, each.word)
        _translate = QCoreApplication.translate
        self.button_show_wordlist.setText(_translate("Dialog", "HIDE"))

    def wordlist_hide(self):
        self.wordlist.setModel(self.EMPTY_MODEL)
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
        self.console_show_history.append('code'.ljust(7) + '\t->\t' + 'Show more info')
        self.console_show_history.append('quit'.ljust(7) + '\t->\t' + 'Exit the program')
        self.console_show_history.append(''.center(self.LENGTH, '-'))

    def clear(self):
        self.HISTORY_NUM = 0
        self.WORD = None
        self.console_show_history.clear()
        self.info_clear()
        self.label_info.setText('')

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
                    elif mode in ['o', 'ord', 'order']:
                        mode_change('ORDER')
                elif content == 'show':
                    self.wordlist_show()
                    self.console_show_history.append('Word list showed')
                elif content == 'hide':
                    self.wordlist_hide()
                    self.console_show_history.append('word list hid')
                elif content == 'quit':
                    self.close()
                elif content[:6] == 'asking':
                    asking = str_process(content[6:])
                    if not asking:
                        asking_change()
                    elif asking == 'word':
                        asking_change('WORD')
                    elif asking in ['def', 'definition']:
                        asking_change('DEFINITION')
                    elif asking in ['sam', 'sample']:
                        asking_change('SAMPLE')
                    elif asking in ['thes', 'thesaurus']:
                        asking_change('THESAURUS')
                elif self.MODE == 'SEARCH':
                    try:
                        content = int(content)
                    except:
                        pass
                    self.WORD = find_word(content)
                    if self.WORD is None:
                        self.console_show_history.append('Undefined')
                    else:
                        ask()
                elif self.MODE == 'RANDOM':  # TODO
                    self.WORD = self.ALPHABET.get_random()
                    ask()
                elif self.MODE == 'ORDER':
                    self.WORD = self.ALPHABET.get_next()
                    ask()
                else:
                    self.console_show_history.append('Undefined')
            else:
                if self.ASKING in ['WORD', 'SAMPLE', 'THESAURUS']:
                    search_w(self.WORD, content)
                if self.ASKING == 'DEFINITION':
                    search_q(self.WORD, content)
                self.WORD = None
                self.label_info.setText('')

        def ask():
            self.info_clear()
            if self.ASKING == 'WORD':
                self.label_def_show.setText(self.WORD.html_definition())
                self.label_info.setText('[Word required]')
            if self.ASKING == 'DEFINITION':
                self.label_word_show.setText(self.WORD.word)
                self.label_info.setText('Definition of [%s] required' % self.WORD.word)
            if self.ASKING == 'SAMPLE':
                self.label_samp_show.setText(self.WORD.html_sample_hollow())
                self.label_info.setText('[Word required]')
            if self.ASKING == 'THESAURUS':
                thesaurus = self.WORD.get_random_html_thesaurus()
                self.label_thesaurus_show.setText(thesaurus)
                if thesaurus == 'thesaurus NOT available':
                    self.label_info.setText('[Word required]')
                else:
                    self.label_info.setText('[Word has the same meaning of [%s] required]' % thesaurus)

        def asking_change(asking=''):
            if asking:
                self.ASKING = asking
                self.combo_box_asking.setCurrentIndex({'WORD': 0,
                                                       'DEFINITION': 1,
                                                       'SAMPLE': 2,
                                                       'THESAURUS': 3}
                                                      [asking])
            else:
                self.console_show_history.append('ASKING now is %s' % self.ASKING)

        def mode_change(mode=''):
            if mode:
                self.MODE = mode
                self.combo_box_mode.setCurrentIndex({'SEARCH': 0,
                                                     'RANDOM': 1,
                                                     'ORDER': 2}
                                                    [mode])
            else:
                self.console_show_history.append('MODE now is %s' % self.MODE)

        def search_q(word, definition):
            self.console_show_history.append(''.center(self.LENGTH, '-'))
            if str_process(word.definition) == str_process(definition):
                self.console_show_history.append('<html>'
                                                 '<span style=" font-weight:600; color:#ff0000;">'
                                                 '√'
                                                 '</span></html>')
            else:
                self.console_show_history.append('<html>'
                                                 '<span style=" font-weight:600; color:#ff0000;">'
                                                 '×'
                                                 '</span></html>')
            self.console_show_history.append('↓        Your definition        ↓\n%s' % definition)
            self.console_show_history.append('%s\n↑        Real definition        ↑' % word.definition)
            self.console_show_history.append(''.center(self.LENGTH, '-'))
            self.info_show(word)

        def search_w(word, w):
            self.console_show_history.append(''.center(self.LENGTH, '-'))
            if str_process(word.word) == str_process(w):
                self.console_show_history.append('<html>'
                                                 '<span style=" font-weight:600; color:#ff0000;">'
                                                 '√'
                                                 '</span></html>')
            else:
                self.console_show_history.append('<html>'
                                                 '<span style=" font-weight:600; color:#ff0000;">'
                                                 '×'
                                                 '</span></html>')
            self.console_show_history.append('↓        Your word        ↓\n%s' % w)
            self.console_show_history.append('%s\n↑        Real word        ↑' % word.word)
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
        self.label_def_show.setText(word.html_definition())
        self.label_samp_show.setText(word.html_sample())
        self.label_thesaurus_show.setText(word.html_thesaurus())

    def info_clear(self):
        self.label_word_show.setText('')
        self.label_def_show.setText('')
        self.label_samp_show.setText('')
        self.label_thesaurus_show.setText('')
