# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'routineCheck.ui'
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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(483, 191)
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(30, 30, 431, 61))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Century Gothic"))
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setWordWrap(True)
        self.label.setObjectName(_fromUtf8("label"))
        self.ok_btn = QtGui.QPushButton(Dialog)
        self.ok_btn.setGeometry(QtCore.QRect(380, 120, 61, 31))
        self.ok_btn.setObjectName(_fromUtf8("ok_btn"))
        self.widget = QtGui.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(30, 100, 301, 61))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.passwordCheck_le = QtGui.QLineEdit(self.widget)
        self.passwordCheck_le.setGeometry(QtCore.QRect(100, 30, 181, 20))
        self.passwordCheck_le.setObjectName(_fromUtf8("passwordCheck_le"))
        self.checkBox = QtGui.QCheckBox(self.widget)
        self.checkBox.setGeometry(QtCore.QRect(30, 40, 21, 17))
        self.checkBox.setText(_fromUtf8(""))
        self.checkBox.setChecked(True)
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.label_2 = QtGui.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(20, 20, 31, 16))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.widget.raise_()
        self.label.raise_()
        self.ok_btn.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Routine Check!", None))
        self.label.setText(_translate("Dialog", "We would like to make sure you remember your whole password up to this point. What is your password again?", None))
        self.ok_btn.setText(_translate("Dialog", "Ok!", None))
        self.label_2.setText(_translate("Dialog", "Show", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

