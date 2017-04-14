# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'selectCharacterWindow2.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_characterSentenceWindow2(object):
    def setupUi(self, characterSentenceWindow):
        characterSentenceWindow.setObjectName(_fromUtf8("characterSentenceWindow"))
        characterSentenceWindow.resize(506, 343)
        self.pushButton = QtGui.QPushButton(characterSentenceWindow)
        self.pushButton.setGeometry(QtCore.QRect(60, 100, 81, 81))
        self.pushButton.setText(_fromUtf8(""))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.action_label = QtGui.QLabel(characterSentenceWindow)
        self.action_label.setGeometry(QtCore.QRect(180, 130, 111, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Century Gothic"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.action_label.setFont(font)
        self.action_label.setText(_fromUtf8(""))
        self.action_label.setAlignment(QtCore.Qt.AlignCenter)
        self.action_label.setObjectName(_fromUtf8("action_label"))
        self.label_2 = QtGui.QLabel(characterSentenceWindow)
        self.label_2.setGeometry(QtCore.QRect(160, 130, 21, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Century Gothic"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(characterSentenceWindow)
        self.label_3.setGeometry(QtCore.QRect(300, 130, 21, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Century Gothic"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.object_label = QtGui.QLabel(characterSentenceWindow)
        self.object_label.setGeometry(QtCore.QRect(320, 130, 141, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Century Gothic"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.object_label.setFont(font)
        self.object_label.setText(_fromUtf8(""))
        self.object_label.setAlignment(QtCore.Qt.AlignCenter)
        self.object_label.setObjectName(_fromUtf8("object_label"))
        self.action_label_2 = QtGui.QLabel(characterSentenceWindow)
        self.action_label_2.setGeometry(QtCore.QRect(160, 170, 301, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Century Gothic"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.action_label_2.setFont(font)
        self.action_label_2.setText(_fromUtf8(""))
        self.action_label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.action_label_2.setObjectName(_fromUtf8("action_label_2"))
        self.lineEdit = QtGui.QLineEdit(characterSentenceWindow)
        self.lineEdit.setGeometry(QtCore.QRect(350, 260, 111, 20))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.ok_btn = QtGui.QPushButton(characterSentenceWindow)
        self.ok_btn.setGeometry(QtCore.QRect(400, 290, 61, 31))
        self.ok_btn.setObjectName(_fromUtf8("ok_btn"))
        self.label = QtGui.QLabel(characterSentenceWindow)
        self.label.setGeometry(QtCore.QRect(90, 260, 251, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Century Gothic"))
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_4 = QtGui.QLabel(characterSentenceWindow)
        self.label_4.setGeometry(QtCore.QRect(60, 30, 391, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Century Gothic"))
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setWordWrap(True)
        self.label_4.setObjectName(_fromUtf8("label_4"))

        self.retranslateUi(characterSentenceWindow)
        QtCore.QMetaObject.connectSlotsByName(characterSentenceWindow)

    def retranslateUi(self, characterSentenceWindow):
        characterSentenceWindow.setWindowTitle(_translate("characterSentenceWindow", "Peson + Action + Object: Creating your sentence", None))
        self.label_2.setText(_translate("characterSentenceWindow", "+", None))
        self.label_3.setText(_translate("characterSentenceWindow", "+", None))
        self.ok_btn.setText(_translate("characterSentenceWindow", "Got it", None))
        self.label.setText(_translate("characterSentenceWindow", "So what is your password so far?", None))
        self.label_4.setText(_translate("characterSentenceWindow", "This is the resulting sentence of your password try to memorize it. Feel free to read it out loud while you type it.", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    characterSentenceWindow = QtGui.QWidget()
    ui = Ui_characterSentenceWindow()
    ui.setupUi(characterSentenceWindow)
    characterSentenceWindow.show()
    sys.exit(app.exec_())

