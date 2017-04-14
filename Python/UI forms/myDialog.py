# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'myDialog.ui'
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

class Ui_myDialog(object):
    def setupUi(self, myDialog):
        myDialog.setObjectName(_fromUtf8("myDialog"))
        myDialog.resize(468, 254)
        self.buttonBox = QtGui.QDialogButtonBox(myDialog)
        self.buttonBox.setGeometry(QtCore.QRect(210, 190, 221, 41))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.label = QtGui.QLabel(myDialog)
        self.label.setGeometry(QtCore.QRect(40, 40, 391, 131))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Century Gothic"))
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setText(_fromUtf8(""))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))

        self.retranslateUi(myDialog)
        #QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), myDialog.accept)
        #QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), myDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(myDialog)

    def retranslateUi(self, myDialog):
        myDialog.setWindowTitle(_translate("myDialog", "Dialog", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    myDialog = QtGui.QDialog()
    ui = Ui_myDialog()
    ui.setupUi(myDialog)
    myDialog.show()
    sys.exit(app.exec_())

