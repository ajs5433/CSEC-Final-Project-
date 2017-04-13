# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'selectSymbolWindow.ui'
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

class Ui_selectSymbol(object):
    def setupUi(self, selectSymbol):
        selectSymbol.setObjectName(_fromUtf8("selectSymbol"))
        selectSymbol.resize(552, 330)
        self.frame = QtGui.QFrame(selectSymbol)
        self.frame.setGeometry(QtCore.QRect(30, 30, 501, 191))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.image = QtGui.QPushButton(self.frame)
        self.image.setGeometry(QtCore.QRect(40, 40, 101, 101))
        self.image.setText(_fromUtf8(""))
        self.image.setObjectName(_fromUtf8("image"))
        self.pushButton_2 = QtGui.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(30, 150, 121, 21))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.symbolName_label = QtGui.QLabel(self.frame)
        self.symbolName_label.setGeometry(QtCore.QRect(10, 10, 161, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Century Gothic"))
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.symbolName_label.setFont(font)
        self.symbolName_label.setAlignment(QtCore.Qt.AlignCenter)
        self.symbolName_label.setObjectName(_fromUtf8("symbolName_label"))
        self.widget = QtGui.QWidget(self.frame)
        self.widget.setGeometry(QtCore.QRect(220, 40, 241, 101))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.label = QtGui.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(20, 10, 201, 81))
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setAutoFillBackground(False)
        self.label.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.label.setWordWrap(True)
        self.label.setObjectName(_fromUtf8("label"))
        self.next_btn = QtGui.QPushButton(selectSymbol)
        self.next_btn.setGeometry(QtCore.QRect(420, 270, 81, 31))
        self.next_btn.setObjectName(_fromUtf8("next_btn"))
        self.lineEdit = QtGui.QLineEdit(selectSymbol)
        self.lineEdit.setGeometry(QtCore.QRect(290, 280, 61, 21))
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.label_2 = QtGui.QLabel(selectSymbol)
        self.label_2.setGeometry(QtCore.QRect(290, 250, 71, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(selectSymbol)
        self.label_3.setGeometry(QtCore.QRect(110, 250, 71, 16))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(selectSymbol)
        self.label_4.setGeometry(QtCore.QRect(90, 280, 101, 21))
        self.label_4.setStyleSheet(_fromUtf8("Background: rgb(255, 255, 255)"))
        self.label_4.setFrameShape(QtGui.QFrame.NoFrame)
        self.label_4.setText(_fromUtf8(""))
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName(_fromUtf8("label_4"))

        self.retranslateUi(selectSymbol)
        QtCore.QMetaObject.connectSlotsByName(selectSymbol)

    def retranslateUi(self, selectSymbol):
        selectSymbol.setWindowTitle(_translate("selectSymbol", "Select your Symbol to remember", None))
        self.pushButton_2.setText(_translate("selectSymbol", "Give me another one!", None))
        self.symbolName_label.setText(_translate("selectSymbol", "TextLabel", None))
        self.label.setText(_translate("selectSymbol", "Slect a Symbol or combination that will be easy for you to remember. You can pick a different one, then type it below and proceed.", None))
        self.next_btn.setText(_translate("selectSymbol", "Next", None))
        self.label_2.setText(_translate("selectSymbol", "My Symbols:", None))
        self.label_3.setText(_translate("selectSymbol", "Suggestions:", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    selectSymbol = QtGui.QWidget()
    ui = Ui_selectSymbol()
    ui.setupUi(selectSymbol)
    selectSymbol.show()
    sys.exit(app.exec_())

