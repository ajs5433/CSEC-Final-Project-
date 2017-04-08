import sys
from myExcel import myExcel
from myGUI import myGUI
from PyQt4 import QtGui
from char import Ui_characterWindow

xlsheet = myExcel()#"A:\Desktop\myProject\Project Files\Words.xlsx");

"""
name = xlsheet.getRandomItem("Object",'C')
print("\nthe name is", name)
print();
for number in range(1,26):
    print(xlsheet.getRandomName(number))
"""
"""
#app = PyQt.QApplication(sys.argv)
window = Ui_characterWindow.setupUi()
window.show(window, Ui_characterWindow)
app.exec_()
"""

app = QtGui.QApplication(sys.argv)
characterWindow = QtGui.QWidget()
ui = Ui_characterWindow()
ui.setupUi(characterWindow)

ui.btn_1.setToolTip(xlsheet.getRandomName(1) )
ui.btn_2.setToolTip(  xlsheet.getRandomName(2) )
ui.btn_3.setToolTip(xlsheet.getRandomName(3) )
ui.btn_4.setToolTip( xlsheet.getRandomName(4) )


characterWindow.show()
sys.exit(app.exec_())

