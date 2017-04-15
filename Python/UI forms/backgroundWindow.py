# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'backgroundWindow.ui'
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

class Ui_backgroundWindow(object):
    def setupUi(self, backgroundWindow):
        backgroundWindow.setObjectName(_fromUtf8("backgroundWindow"))
        backgroundWindow.resize(1028, 725)

        self.retranslateUi(backgroundWindow)
        QtCore.QMetaObject.connectSlotsByName(backgroundWindow)

    def retranslateUi(self, backgroundWindow):
        backgroundWindow.setWindowTitle(_translate("backgroundWindow", "Password Generator", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    backgroundWindow = QtGui.QWidget()
    ui = Ui_backgroundWindow()
    ui.setupUi(backgroundWindow)
    backgroundWindow.show()
    sys.exit(app.exec_())

