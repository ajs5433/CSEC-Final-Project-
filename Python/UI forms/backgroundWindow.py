# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'backGroundWindow.ui'
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

class Ui_BackgroundWindow(object):
    def setupUi(self, BackgroundWindow):
        BackgroundWindow.setObjectName(_fromUtf8("BackgroundWindow"))
        BackgroundWindow.resize(898, 678)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(BackgroundWindow.sizePolicy().hasHeightForWidth())
        BackgroundWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtGui.QWidget(BackgroundWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        BackgroundWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(BackgroundWindow)
        self.menubar.setEnabled(True)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 898, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        BackgroundWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(BackgroundWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        BackgroundWindow.setStatusBar(self.statusbar)

        self.retranslateUi(BackgroundWindow)
        QtCore.QMetaObject.connectSlotsByName(BackgroundWindow)

    def retranslateUi(self, BackgroundWindow):
        BackgroundWindow.setWindowTitle(_translate("BackgroundWindow", "Password Generator", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    BackgroundWindow = QtGui.QMainWindow()
    ui = Ui_BackgroundWindow()
    ui.setupUi(BackgroundWindow)
    BackgroundWindow.show()
    sys.exit(app.exec_())

