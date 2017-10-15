#!/usr/bin/env python3
# coding: utf-8
__author__ = 'Yee_172'
__data__ = '2017/9/26'


from Func import *
import sys
from PyQt5.QtCore import Qt
from PyQt5 import QtGui
from PyQt5 import QtWidgets
from GUI.main import Ui_Dialog


class MainWin(QtWidgets.QWidget, Ui_Dialog):

    WORDLIST_NUM = 0

    def __init__(self):
        super(MainWin, self).__init__()
        self.setupUi(self)
        wordlist_model = QtGui.QStandardItemModel(0, 2, self)
        wordlist_model.setHeaderData(0, Qt.Horizontal, 'NUM', Qt.DisplayRole)
        wordlist_model.setHeaderData(1, Qt.Horizontal, 'WORD')
        self.wordList.setModel(wordlist_model)
        for each in alphabet.words:
            self.add_data(wordlist_model, each.num, each.word)

    def add_data(self, model, num, word):
        model.insertRow(self.WORDLIST_NUM)
        model.setData(model.index(self.WORDLIST_NUM, 0), num)
        model.setData(model.index(self.WORDLIST_NUM, 1), word)
        self.WORDLIST_NUM += 1


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    win = MainWin()
    win.show()
    sys.exit(app.exec_())

# terminal_version_old()
