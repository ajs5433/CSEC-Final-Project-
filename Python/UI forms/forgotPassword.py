# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'forgotPassword.ui'
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

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(613, 418)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        self.frame = QtGui.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(70, 130, 511, 241))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.textEdit_8 = QtGui.QTextEdit(self.frame)
        self.textEdit_8.setGeometry(QtCore.QRect(90, 170, 61, 21))
        self.textEdit_8.setObjectName(_fromUtf8("textEdit_8"))
        self.textEdit_2 = QtGui.QTextEdit(self.frame)
        self.textEdit_2.setGeometry(QtCore.QRect(220, 50, 121, 21))
        self.textEdit_2.setObjectName(_fromUtf8("textEdit_2"))
        self.textEdit_3 = QtGui.QTextEdit(self.frame)
        self.textEdit_3.setGeometry(QtCore.QRect(360, 50, 121, 21))
        self.textEdit_3.setObjectName(_fromUtf8("textEdit_3"))
        self.textEdit_6 = QtGui.QTextEdit(self.frame)
        self.textEdit_6.setGeometry(QtCore.QRect(360, 90, 121, 21))
        self.textEdit_6.setObjectName(_fromUtf8("textEdit_6"))
        self.label = QtGui.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(20, 50, 71, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Constantia"))
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.textEdit_5 = QtGui.QTextEdit(self.frame)
        self.textEdit_5.setGeometry(QtCore.QRect(220, 90, 121, 21))
        self.textEdit_5.setObjectName(_fromUtf8("textEdit_5"))
        self.textEdit_4 = QtGui.QTextEdit(self.frame)
        self.textEdit_4.setGeometry(QtCore.QRect(90, 90, 121, 21))
        self.textEdit_4.setObjectName(_fromUtf8("textEdit_4"))
        self.label_2 = QtGui.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(20, 90, 71, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Constantia"))
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(20, 130, 71, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Constantia"))
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.textEdit = QtGui.QTextEdit(self.frame)
        self.textEdit.setGeometry(QtCore.QRect(90, 50, 121, 21))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.textEdit_7 = QtGui.QTextEdit(self.frame)
        self.textEdit_7.setGeometry(QtCore.QRect(90, 130, 61, 21))
        self.textEdit_7.setObjectName(_fromUtf8("textEdit_7"))
        self.label_4 = QtGui.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(20, 170, 71, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Constantia"))
        font.setPointSize(11)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(110, 20, 71, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Constantia"))
        font.setPointSize(11)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_7 = QtGui.QLabel(self.frame)
        self.label_7.setGeometry(QtCore.QRect(240, 20, 71, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Constantia"))
        font.setPointSize(11)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.label_8 = QtGui.QLabel(self.frame)
        self.label_8.setGeometry(QtCore.QRect(360, 20, 121, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Constantia"))
        font.setPointSize(11)
        self.label_8.setFont(font)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.pushButton = QtGui.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(420, 190, 71, 41))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.label_6 = QtGui.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(80, 30, 471, 61))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Constantia"))
        font.setPointSize(11)
        self.label_6.setFont(font)
        self.label_6.setObjectName(_fromUtf8("label_6"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.label.setText(_translate("Form", "PAO 1", None))
        self.label_2.setText(_translate("Form", "PAO 2", None))
        self.label_3.setText(_translate("Form", "Symbol", None))
        self.label_4.setText(_translate("Form", "Number", None))
        self.label_5.setText(_translate("Form", "Person", None))
        self.label_7.setText(_translate("Form", "Action", None))
        self.label_8.setText(_translate("Form", "Object", None))
        self.pushButton.setText(_translate("Form", "Ok", None))
        self.label_6.setText(_translate("Form", "Please let us know what you remember from your previous password.", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

