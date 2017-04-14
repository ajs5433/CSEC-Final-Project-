# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'learningPassword.ui'
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

class Ui_learningPasswordWindow(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(620, 430)
        self.graphicsView = QtGui.QGraphicsView(Form)
        self.graphicsView.setGeometry(QtCore.QRect(40, 30, 91, 81))
        self.graphicsView.setObjectName(_fromUtf8("graphicsView"))
        self.graphicsView_2 = QtGui.QGraphicsView(Form)
        self.graphicsView_2.setGeometry(QtCore.QRect(40, 130, 91, 81))
        self.graphicsView_2.setObjectName(_fromUtf8("graphicsView_2"))
        self.textEdit = QtGui.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(160, 60, 101, 31))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.textEdit_2 = QtGui.QTextEdit(Form)
        self.textEdit_2.setGeometry(QtCore.QRect(280, 60, 101, 31))
        self.textEdit_2.setObjectName(_fromUtf8("textEdit_2"))
        self.textEdit_3 = QtGui.QTextEdit(Form)
        self.textEdit_3.setGeometry(QtCore.QRect(400, 60, 101, 31))
        self.textEdit_3.setObjectName(_fromUtf8("textEdit_3"))
        self.textEdit_4 = QtGui.QTextEdit(Form)
        self.textEdit_4.setGeometry(QtCore.QRect(160, 150, 101, 31))
        self.textEdit_4.setObjectName(_fromUtf8("textEdit_4"))
        self.textEdit_5 = QtGui.QTextEdit(Form)
        self.textEdit_5.setGeometry(QtCore.QRect(280, 150, 101, 31))
        self.textEdit_5.setObjectName(_fromUtf8("textEdit_5"))
        self.textEdit_6 = QtGui.QTextEdit(Form)
        self.textEdit_6.setGeometry(QtCore.QRect(400, 150, 101, 31))
        self.textEdit_6.setObjectName(_fromUtf8("textEdit_6"))
        self.textEdit_7 = QtGui.QTextEdit(Form)
        self.textEdit_7.setGeometry(QtCore.QRect(220, 270, 101, 31))
        self.textEdit_7.setObjectName(_fromUtf8("textEdit_7"))
        self.textEdit_8 = QtGui.QTextEdit(Form)
        self.textEdit_8.setGeometry(QtCore.QRect(220, 320, 101, 31))
        self.textEdit_8.setObjectName(_fromUtf8("textEdit_8"))
        self.textEdit_9 = QtGui.QTextEdit(Form)
        self.textEdit_9.setGeometry(QtCore.QRect(220, 360, 101, 31))
        self.textEdit_9.setObjectName(_fromUtf8("textEdit_9"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

