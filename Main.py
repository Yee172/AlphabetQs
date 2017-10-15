#!/usr/bin/env python3
# coding: utf-8
__author__ = 'Yee_172'
__data__ = '2017/9/26'


from Func import *
import sys
from PyQt5.QtCore import Qt, QCoreApplication
from PyQt5 import QtGui
from PyQt5 import QtWidgets
from GUI.main import Ui_Dialog


class MainWin(QtWidgets.QWidget, Ui_Dialog):

    WORDLIST_NUM = 0
    EMPTY_MODEL = QtGui.QStandardItemModel()

    def __init__(self):
        super(MainWin, self).__init__()
        self.setupUi(self)
        self.button_show_wordlist.clicked.connect(self.wordlist_click)

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


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    win = MainWin()
    win.show()
    sys.exit(app.exec_())

# terminal_version_old()
