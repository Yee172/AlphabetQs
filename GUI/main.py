# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(770, 562)
        Dialog.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.wordlist = QtWidgets.QTreeView(Dialog)
        self.wordlist.setGeometry(QtCore.QRect(20, 60, 161, 451))
        self.wordlist.setAutoFillBackground(False)
        self.wordlist.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.wordlist.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.wordlist.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.wordlist.setAlternatingRowColors(True)
        self.wordlist.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.wordlist.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.wordlist.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerItem)
        self.wordlist.setRootIsDecorated(False)
        self.wordlist.setObjectName("wordlist")
        self.label_wordlist = QtWidgets.QLabel(Dialog)
        self.label_wordlist.setGeometry(QtCore.QRect(20, 20, 161, 20))
        self.label_wordlist.setAlignment(QtCore.Qt.AlignCenter)
        self.label_wordlist.setObjectName("label_wordlist")
        self.label_word = QtWidgets.QLabel(Dialog)
        self.label_word.setGeometry(QtCore.QRect(200, 40, 541, 21))
        self.label_word.setTextFormat(QtCore.Qt.AutoText)
        self.label_word.setScaledContents(False)
        self.label_word.setAlignment(QtCore.Qt.AlignCenter)
        self.label_word.setObjectName("label_word")
        self.label_word_show = QtWidgets.QLabel(Dialog)
        self.label_word_show.setGeometry(QtCore.QRect(200, 60, 541, 21))
        self.label_word_show.setText("")
        self.label_word_show.setAlignment(QtCore.Qt.AlignCenter)
        self.label_word_show.setObjectName("label_word_show")
        self.label_def = QtWidgets.QLabel(Dialog)
        self.label_def.setGeometry(QtCore.QRect(200, 90, 541, 20))
        self.label_def.setAlignment(QtCore.Qt.AlignCenter)
        self.label_def.setObjectName("label_def")
        self.label_def_show = QtWidgets.QLabel(Dialog)
        self.label_def_show.setGeometry(QtCore.QRect(200, 110, 541, 21))
        self.label_def_show.setText("")
        self.label_def_show.setAlignment(QtCore.Qt.AlignCenter)
        self.label_def_show.setObjectName("label_def_show")
        self.label_samp = QtWidgets.QLabel(Dialog)
        self.label_samp.setGeometry(QtCore.QRect(200, 140, 541, 21))
        self.label_samp.setAlignment(QtCore.Qt.AlignCenter)
        self.label_samp.setObjectName("label_samp")
        self.label_samp_show = QtWidgets.QLabel(Dialog)
        self.label_samp_show.setGeometry(QtCore.QRect(200, 160, 541, 41))
        self.label_samp_show.setAlignment(QtCore.Qt.AlignCenter)
        self.label_samp_show.setWordWrap(True)
        self.label_samp_show.setObjectName("label_samp_show")
        self.console_show_history = QtWidgets.QTextBrowser(Dialog)
        self.console_show_history.setGeometry(QtCore.QRect(200, 250, 541, 241))
        self.console_show_history.setObjectName("console_show_history")
        self.label_console = QtWidgets.QLabel(Dialog)
        self.label_console.setGeometry(QtCore.QRect(200, 230, 541, 21))
        self.label_console.setAlignment(QtCore.Qt.AlignCenter)
        self.label_console.setObjectName("label_console")
        self.button_show_wordlist = QtWidgets.QPushButton(Dialog)
        self.button_show_wordlist.setGeometry(QtCore.QRect(15, 520, 171, 32))
        self.button_show_wordlist.setObjectName("button_show_wordlist")
        self.button_quit = QtWidgets.QPushButton(Dialog)
        self.button_quit.setGeometry(QtCore.QRect(632, 520, 111, 32))
        self.button_quit.setObjectName("button_quit")
        self.console = QtWidgets.QLineEdit(Dialog)
        self.console.setGeometry(QtCore.QRect(200, 490, 541, 21))
        self.console.setObjectName("console")
        self.button_help = QtWidgets.QPushButton(Dialog)
        self.button_help.setGeometry(QtCore.QRect(193, 520, 111, 32))
        self.button_help.setObjectName("button_help")
        self.check_code = QtWidgets.QCheckBox(Dialog)
        self.check_code.setGeometry(QtCore.QRect(680, 230, 61, 20))
        self.check_code.setChecked(False)
        self.check_code.setObjectName("check_code")
        self.button_clear = QtWidgets.QPushButton(Dialog)
        self.button_clear.setGeometry(QtCore.QRect(676, 486, 71, 32))
        self.button_clear.setObjectName("button_clear")
        self.label_info = QtWidgets.QLabel(Dialog)
        self.label_info.setGeometry(QtCore.QRect(309, 525, 321, 20))
        self.label_info.setText("")
        self.label_info.setAlignment(QtCore.Qt.AlignCenter)
        self.label_info.setObjectName("label_info")
        self.combo_box_mode = QtWidgets.QComboBox(Dialog)
        self.combo_box_mode.setGeometry(QtCore.QRect(198, 227, 101, 30))
        self.combo_box_mode.setObjectName("combo_box_mode")
        self.combo_box_mode.addItem("")
        self.combo_box_mode.addItem("")
        self.search_box = QtWidgets.QLineEdit(Dialog)
        self.search_box.setGeometry(QtCore.QRect(20, 40, 161, 21))
        self.search_box.setObjectName("search_box")
        self.actionread_in = QtWidgets.QAction(Dialog)
        self.actionread_in.setCheckable(False)
        self.actionread_in.setObjectName("actionread_in")

        self.retranslateUi(Dialog)
        self.combo_box_mode.setCurrentIndex(0)
        self.button_quit.clicked.connect(Dialog.close)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.console, self.button_show_wordlist)
        Dialog.setTabOrder(self.button_show_wordlist, self.button_quit)
        Dialog.setTabOrder(self.button_quit, self.console_show_history)
        Dialog.setTabOrder(self.console_show_history, self.wordlist)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "AlphabetQs"))
        self.label_wordlist.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">WORD LIST</span></p></body></html>"))
        self.label_word.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-weight:600; text-decoration: underline;\">WORD</span></p></body></html>"))
        self.label_def.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-weight:600; text-decoration: underline;\">DEFINITION</span></p></body></html>"))
        self.label_samp.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-weight:600; text-decoration: underline;\">SAMPLE SENTENCE</span></p></body></html>"))
        self.label_samp_show.setText(_translate("Dialog", "<html><head/><body><p><br/></p></body></html>"))
        self.label_console.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">CONSOLE</span></p></body></html>"))
        self.button_show_wordlist.setText(_translate("Dialog", "SHOW"))
        self.button_quit.setText(_translate("Dialog", "QUIT"))
        self.button_help.setText(_translate("Dialog", "HELP"))
        self.check_code.setText(_translate("Dialog", "CODE"))
        self.button_clear.setText(_translate("Dialog", "CLEAR"))
        self.combo_box_mode.setCurrentText(_translate("Dialog", "SEARCH"))
        self.combo_box_mode.setItemText(0, _translate("Dialog", "SEARCH"))
        self.combo_box_mode.setItemText(1, _translate("Dialog", "RANDOM"))
        self.search_box.setWhatsThis(_translate("Dialog", "Search Box"))
        self.search_box.setPlaceholderText(_translate("Dialog", "Search # or word"))
        self.actionread_in.setText(_translate("Dialog", "read_in"))

