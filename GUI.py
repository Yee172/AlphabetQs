# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *  

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(811, 562)
        Dialog.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(370, 510, 261, 51))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName("buttonBox")
        self.WordList = QtWidgets.QListView(Dialog)
        self.WordList.setGeometry(QtCore.QRect(20, 50, 191, 501))
        self.WordList.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.WordList.setObjectName("WordList")
        self.label_wl = QtWidgets.QLabel(Dialog)
        self.label_wl.setGeometry(QtCore.QRect(19, 20, 191, 20))
        self.label_wl.setAlignment(QtCore.Qt.AlignCenter)
        self.label_wl.setObjectName("label_wl")
        self.label_word = QtWidgets.QLabel(Dialog)
        self.label_word.setGeometry(QtCore.QRect(240, 40, 541, 21))
        self.label_word.setAlignment(QtCore.Qt.AlignCenter)
        self.label_word.setObjectName("label_word")
        self.label_word_show = QtWidgets.QLabel(Dialog)
        self.label_word_show.setGeometry(QtCore.QRect(240, 60, 541, 21))
        self.label_word_show.setAlignment(QtCore.Qt.AlignCenter)
        self.label_word_show.setObjectName("label_word_show")
        self.label_def = QtWidgets.QLabel(Dialog)
        self.label_def.setGeometry(QtCore.QRect(240, 90, 541, 20))
        self.label_def.setAlignment(QtCore.Qt.AlignCenter)
        self.label_def.setObjectName("label_def")
        self.label_def_show = QtWidgets.QLabel(Dialog)
        self.label_def_show.setGeometry(QtCore.QRect(240, 110, 541, 21))
        self.label_def_show.setAlignment(QtCore.Qt.AlignCenter)
        self.label_def_show.setObjectName("label_def_show")
        self.label_samp = QtWidgets.QLabel(Dialog)
        self.label_samp.setGeometry(QtCore.QRect(240, 140, 541, 21))
        self.label_samp.setAlignment(QtCore.Qt.AlignCenter)
        self.label_samp.setObjectName("label_samp")
        self.label_samp_show = QtWidgets.QLabel(Dialog)
        self.label_samp_show.setGeometry(QtCore.QRect(240, 160, 541, 41))
        self.label_samp_show.setAlignment(QtCore.Qt.AlignCenter)
        self.label_samp_show.setObjectName("label_samp_show")
        self.textBrowser = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser.setGeometry(QtCore.QRect(240, 240, 541, 271))
        self.textBrowser.setObjectName("textBrowser")
        self.label_console = QtWidgets.QLabel(Dialog)
        self.label_console.setGeometry(QtCore.QRect(240, 220, 541, 21))
        self.label_console.setAlignment(QtCore.Qt.AlignCenter)
        self.label_console.setObjectName("label_console")

        self.retranslateUi(Dialog)
        # self.buttonBox.accepted.connect(Dialog.accept)
        # self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        Dialog.show()

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_wl.setText(_translate("Dialog", "WORD LIST"))
        self.label_word.setText(_translate("Dialog", "WORD"))
        self.label_word_show.setText(_translate("Dialog", "TextLabel"))
        self.label_def.setText(_translate("Dialog", "DEFINITION"))
        self.label_def_show.setText(_translate("Dialog", "TextLabel"))
        self.label_samp.setText(_translate("Dialog", "SAMPLE SENTENCE"))
        self.label_samp_show.setText(_translate("Dialog", "TextLabel"))
        self.label_console.setText(_translate("Dialog", "CONSOLE"))


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    widget = QWidget(None)
    Ui_Dialog().setupUi(widget)
    sys.exit(app.exec_())
    pass
