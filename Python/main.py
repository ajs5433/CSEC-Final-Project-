import sys
sys.path.append("A:/Desktop/myProject/Python/UI forms")
from myExcel import myExcel
from myGUI import myGUI
from PyQt4 import QtGui
from charWindow import Ui_characterWindow
from login import Ui_login
from mainWindow import Ui_MainWindow

xlsheet = myExcel()#"A:\Desktop\myProject\Project Files\Words.xlsx");

"""
name = xlsheet.getRandomItem("Object",'C')
print("\nthe name is", name)
print();
for number in range(1,26):
    print(xlsheet.getRandomName(number))
"""


