#!/usr/bin/env python3
# coding: utf-8
__author__ = 'Yee_172'
__data__ = '2017/9/26'


from Func import *
import sys
from PyQt5 import QtCore
from PyQt5 import QtWidgets
from GUI.main import Ui_Dialog


class MainWin(QtWidgets.QWidget, Ui_Dialog):
    def __init__(self):
        super(MainWin, self).__init__()
        self.setupUi(self)
        # self.wordList.setModel(ListModel(alphabet.words))


# class ListModel(QtCore.QAbstractItemModel):
#     def __init__(self, date, parent=None, *args):
#         QtCore.QAbstractItemModel.__init__(self, parent, *args)
#         self.data = date
#
#     def columnCount(self, parent=None, *args, **kwargs):
#         return 1
#
#     def rowCount(self, parent=None, *args, **kwargs):
#         return len(self.data)
#
#     def index(self, p_int, p_int_1, parent=None, *args, **kwargs):
#         return QtCore.QModelIndex()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    win = MainWin()
    win.show()
    sys.exit(app.exec_())

# terminal_version_old()
