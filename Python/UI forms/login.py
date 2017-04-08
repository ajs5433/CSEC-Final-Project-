# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
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

class Ui_login(object):
    def setupUi(self, login):
        login.setObjectName(_fromUtf8("login"))
        login.resize(342, 401)
        self.pushButton = QtGui.QPushButton(login)
        self.pushButton.setGeometry(QtCore.QRect(240, 340, 75, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.label = QtGui.QLabel(login)
        self.label.setGeometry(QtCore.QRect(90, 120, 46, 13))
        self.label.setObjectName(_fromUtf8("label"))
        self.plainTextEdit = QtGui.QPlainTextEdit(login)
        self.plainTextEdit.setGeometry(QtCore.QRect(140, 110, 111, 31))
        self.plainTextEdit.setObjectName(_fromUtf8("plainTextEdit"))
        self.plainTextEdit_2 = QtGui.QPlainTextEdit(login)
        self.plainTextEdit_2.setGeometry(QtCore.QRect(140, 160, 111, 31))
        self.plainTextEdit_2.setObjectName(_fromUtf8("plainTextEdit_2"))
        self.label_2 = QtGui.QLabel(login)
        self.label_2.setGeometry(QtCore.QRect(70, 170, 61, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.plainTextEdit_3 = QtGui.QPlainTextEdit(login)
        self.plainTextEdit_3.setGeometry(QtCore.QRect(140, 210, 111, 31))
        self.plainTextEdit_3.setObjectName(_fromUtf8("plainTextEdit_3"))
        self.label_3 = QtGui.QLabel(login)
        self.label_3.setGeometry(QtCore.QRect(50, 220, 81, 20))
        self.label_3.setObjectName(_fromUtf8("label_3"))

        self.retranslateUi(login)
        QtCore.QMetaObject.connectSlotsByName(login)

    def retranslateUi(self, login):
        login.setWindowTitle(_translate("login", "Form", None))
        self.pushButton.setText(_translate("login", "login", None))
        self.label.setText(_translate("login", "Name:", None))
        self.label_2.setText(_translate("login", "Last Name:", None))
        self.label_3.setText(_translate("login", "Password for:", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    login = QtGui.QWidget()
    ui = Ui_login()
    ui.setupUi(login)
    login.show()
    sys.exit(app.exec_())

