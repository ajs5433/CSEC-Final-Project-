import sys
import re
import random
from PyQt4 import QtGui
from PyQt4 import QtCore
from PyQt4.QtCore import QObject

from myExcel import myExcel
sys.path.append("A:/Desktop/myProject/Python/UI forms")
from mainWindow import Ui_MainWindow
from createUserWindow import Ui_createUserWindow
from loginWindow import Ui_loginWindow
from selectCharacterWindow import Ui_characterWindow
from numberWindow import Ui_numberWindow
from selectSymbolWindow import Ui_selectSymbol
from myUser import createUser

xlsheet = myExcel()
imagesPath = "A:/Desktop/myProject/Project Files/Images/"
symbolsPath = "A:/Desktop/myProject/Project Files/Symbols/"
buttonName = ""

myList = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26]
order_normal_mode = ['PAO1', 'Number', 'Symbol']
order_medium_mode = ['PAO1', 'PAO2', 'Number', 'Symbol']

app = QtGui.QApplication(sys.argv)
MainWindow = QtGui.QMainWindow()
loginWindow = QtGui.QWidget()
createUserWindow = QtGui.QWidget()
characterWindow = QtGui.QWidget()
numberWindow = QtGui.QWidget()
symbolWindow = QtGui.QWidget()

main_window = Ui_MainWindow()
create_user_window = Ui_createUserWindow()
login_window = Ui_loginWindow()
select_character_window = Ui_characterWindow()
number_window = Ui_numberWindow()
symbol_window = Ui_selectSymbol()

class passwordGenerator(QtGui.QWidget):
    orderSelect = 0
    current_user = createUser()

    def __init__(self):
        super(passwordGenerator, self).__init__()
        main_window.setupUi(MainWindow)
        create_user_window.setupUi(createUserWindow)
        login_window.setupUi(loginWindow)
        select_character_window.setupUi(characterWindow)
        number_window.setupUi(numberWindow)
        symbol_window.setupUi(symbolWindow)
        symbol_window.pushButton_2.clicked.connect(self.setupSymbolWindow)

    def openWindow(self):
        random.shuffle(order_normal_mode)
        random.shuffle(order_medium_mode)
        order_normal_mode.insert(len(order_normal_mode), 'complete')
        order_medium_mode.insert(len(order_medium_mode), 'complete')
        main_window.createNewPassword_btn.clicked.connect(self.nextStep_event) #Normal
        main_window.createNewPassword_btn_2.clicked.connect(self.nextStep_event)  # Normal
        #main_window.createNewPassword_btn_2.connect(self.nextStep_event)  #Medium
        #main_window.confirmPasswordCreated_btn.connect(self.confirmPasswordCreated_event)  # Check password
        main_window.createNewPassword_btn.setObjectName("Normal Passwords")
        main_window.createNewPassword_btn_2.setObjectName("Medium Passwords")
        MainWindow.show()
        self.current_user = createUser()
        #createUserWindow.show()
        #loginWindow.show()
        sys.exit(app.exec_())

    def setupCharacterWindow(self):
        random.shuffle(myList)
        self.setupCW(select_character_window.btn_1, myList[1])
        self.setupCW(select_character_window.btn_2, myList[2])
        self.setupCW(select_character_window.btn_3, myList[3])
        self.setupCW(select_character_window.btn_4, myList[4])
        self.setupCW(select_character_window.btn_5, myList[5])
        self.setupCW(select_character_window.btn_6, myList[6])
        self.setupCW(select_character_window.btn_7, myList[7])
        self.setupCW(select_character_window.btn_8, myList[8])
        self.setupCW(select_character_window.btn_9, myList[9])
        self.setupCW(select_character_window.btn_10, myList[10])
        self.setupCW(select_character_window.btn_11, myList[11])
        self.setupCW(select_character_window.btn_12, myList[12])
        self.setupCW(select_character_window.btn_13, myList[13])
        self.setupCW(select_character_window.btn_14, myList[14])
        self.setupCW(select_character_window.btn_15, myList[15])
        self.setupCW(select_character_window.btn_16, myList[16])
        self.setupCW(select_character_window.btn_17, myList[17])
        self.setupCW(select_character_window.btn_18, myList[18])
        self.setupCW(select_character_window.btn_19, myList[19])
        self.setupCW(select_character_window.btn_20, myList[20])
        self.setupCW(select_character_window.btn_21, myList[21])
        self.setupCW(select_character_window.btn_22, myList[22])
        self.setupCW(select_character_window.btn_23, myList[23])
        self.setupCW(select_character_window.btn_24, myList[24])
        self.setupCW(select_character_window.btn_25, myList[25])
        self.setupCW(select_character_window.btn_26, myList[0])

    def setupCW(self, button, number):
        myName = xlsheet.getRandomName(number)
        myIconSize = QtCore.QSize(81, 81)
        myIcon = QtGui.QIcon()
        myIcon.addPixmap(QtGui.QPixmap(imagesPath+myName+".jpg"))
        button.setIcon(myIcon)
        button.setIconSize(myIconSize)
        button.setToolTip(myName)
        button.clicked.connect(self.CWButtonPushed)
        button.setObjectName(myName)

    def CWButtonPushed(self):
        name = self.sender().objectName()
        select_character_window.name_label.setText(name)
        password = ""

        for i in name.split():
            password += i[0]

        select_character_window.password_label.setText(password)

        # print(re.findall()
        """
        #old method
        scene = QtGui.QGraphicsScene()
        scene.addPixmap(QtGui.QPixmap(imagesPath+name+".jpg"))
        scene.setSceneRect(QtCore.QRectF(0,0,2,2))
        select_character_window.graphicsView.setScene(scene)
        
        #find a better way for the picture!
        pixmap = QtGui.QPixmap(imagesPath+name+".jpg")
        select_character_window.picture_label.setPixmap(pixmap)#QtGui.QPixmap(imagesPath+name+".jpg"))
        """
        myIconSize = QtCore.QSize(151, 151)
        myIcon = QtGui.QIcon()
        myIcon.addPixmap(QtGui.QPixmap(imagesPath + name + ".jpg"))
        select_character_window.pushButton.setIcon(myIcon)
        select_character_window.pushButton.setIconSize(myIconSize)

    def nextStep_event(self):
        pushedBy = self.sender().objectName()
        #print("pushed by "+pushedBy)
        if (pushedBy == "Normal Passwords"):
            myOrder = order_normal_mode
        elif(pushedBy=="Medium Passwords"):
            myOrder = order_medium_mode

        print(myOrder[self.orderSelect])

        if (myOrder[self.orderSelect]=='complete'):
            self.orderSelect = 0

        elif(myOrder[self.orderSelect]=='PAO1'):
            self.orderSelect+=1
            self.setupCharacterWindow()
            #MainWindow.close()
            symbolWindow.close()
            numberWindow.close()
            characterWindow.show()
        elif(myOrder[self.orderSelect]=='PAO2'):
            self.orderSelect += 1
            self.setupCharacterWindow()
            #MainWindow.close()
            symbolWindow.close()
            numberWindow.close()
            characterWindow.show()
        elif(myOrder[self.orderSelect]=='Number'):
            self.orderSelect += 1
            symbolWindow.close()
            characterWindow.close()
            numberWindow.show()
        else:
            self.orderSelect+=1
            characterWindow.close()
            numberWindow.close()
            self.setupSymbolWindow()
            symbolWindow.show()


    def confirmPasswordCreated_event(self):
        loginWindow.show()

    def setupSymbolWindow(self):
        mySymbol = xlsheet.getRandomSymbol()
        myIconSize = QtCore.QSize(101, 101)
        myIcon = QtGui.QIcon()
        myIcon.addPixmap(QtGui.QPixmap(symbolsPath + mySymbol + ".jpg"))
        symbol_window.image.setIcon(myIcon)
        symbol_window.image.setIconSize(myIconSize)
        symbol_window.symbolName_label.setText(mySymbol)
        symbol_window.label_4.setText(xlsheet.suggestion)
        print(mySymbol)


if __name__ == "__main__":
    myApp = passwordGenerator()
    myApp.openWindow()