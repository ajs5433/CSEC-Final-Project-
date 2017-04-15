# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'beforeStarting.ui'
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

class Ui_beforeStarting(object):
    def setupUi(self, beforeStarting):
        beforeStarting.setObjectName(_fromUtf8("beforeStarting"))
        beforeStarting.resize(728, 505)
        self.label = QtGui.QLabel(beforeStarting)
        self.label.setGeometry(QtCore.QRect(220, 30, 251, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Century Gothic"))
        font.setPointSize(16)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(beforeStarting)
        self.label_2.setGeometry(QtCore.QRect(120, 100, 481, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Century Gothic"))
        font.setPointSize(10)
        font.setUnderline(True)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(beforeStarting)
        self.label_3.setGeometry(QtCore.QRect(110, 150, 431, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Century Gothic"))
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(beforeStarting)
        self.label_4.setGeometry(QtCore.QRect(110, 190, 311, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Century Gothic"))
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setWordWrap(True)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(beforeStarting)
        self.label_5.setGeometry(QtCore.QRect(110, 220, 551, 51))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Century Gothic"))
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setWordWrap(True)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_6 = QtGui.QLabel(beforeStarting)
        self.label_6.setGeometry(QtCore.QRect(110, 270, 531, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Century Gothic"))
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setWordWrap(True)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.pushButton = QtGui.QPushButton(beforeStarting)
        self.pushButton.setGeometry(QtCore.QRect(630, 450, 71, 31))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.label_7 = QtGui.QLabel(beforeStarting)
        self.label_7.setGeometry(QtCore.QRect(110, 310, 531, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Century Gothic"))
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setWordWrap(True)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.label_8 = QtGui.QLabel(beforeStarting)
        self.label_8.setGeometry(QtCore.QRect(110, 350, 531, 51))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Century Gothic"))
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setWordWrap(True)
        self.label_8.setObjectName(_fromUtf8("label_8"))

        self.retranslateUi(beforeStarting)
        QtCore.QMetaObject.connectSlotsByName(beforeStarting)

    def retranslateUi(self, beforeStarting):
        beforeStarting.setWindowTitle(_translate("beforeStarting", "Form", None))
        self.label.setText(_translate("beforeStarting", "Before starting!", None))
        self.label_2.setText(_translate("beforeStarting", "All the passwords will have the following rules, remember them:", None))
        self.label_3.setText(_translate("beforeStarting", "- You will be given a PIN NUMBER to memorize", None))
        self.label_4.setText(_translate("beforeStarting", "- You will select your own SYMBOLS", None))
        self.label_5.setText(_translate("beforeStarting", "- You will be given at least a SENTENCE with a famous character ", None))
        self.label_6.setText(_translate("beforeStarting", "- All Names in the sentence will start with upper-case letters.", None))
        self.pushButton.setText(_translate("beforeStarting", "Ok", None))
        self.label_7.setText(_translate("beforeStarting", "- All Non-names in your sentence will start non lower-case letters.", None))
        self.label_8.setText(_translate("beforeStarting", "- Finally, The program will not let you advance unless you fill the correct data", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    beforeStarting = QtGui.QWidget()
    ui = Ui_beforeStarting()
    ui.setupUi(beforeStarting)
    beforeStarting.show()
    sys.exit(app.exec_())

