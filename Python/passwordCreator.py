import sys
import re
import random
from PyQt4 import QtGui
from PyQt4 import QtCore
from PyQt4.QtCore import QObject
from PyQt4.QtCore import QTimer
#import time

from myExcel import myExcel
sys.path.append("A:/Desktop/myProject/Python/UI forms")

from backgroundWindow import Ui_backgroundWindow
from beforeStarting import Ui_beforeStarting
from calculateNumbers import Ui_calculateNumbersWindow
from createUserWindow import Ui_createUserWindow
from forgotPassword import Ui_forgotPasswordWindow
from KeyPad import Ui_keyPad
from learningPassword import Ui_learningPasswordWindow
from loginWindow import Ui_loginWindow
from mainWindow import Ui_MainWindow
from myDialog import Ui_myDialog
from numberWindow import Ui_numberWindow
from PAO2selectCharacterWindow import Ui_PAO2characterWindow
from routineCheck import Ui_Dialog
from selectCharacterWindow import Ui_characterWindow
from selectCharacterWindow2 import Ui_characterSentenceWindow2
from selectSymbolWindow import Ui_selectSymbol
from createUserWindow import Ui_createUserWindow
from myUser import createUser

xlsheet = myExcel()
imagesPath = "A:/Desktop/myProject/Project Files/Images/"
symbolsPath = "A:/Desktop/myProject/Project Files/Symbols/"
buttonName = ""

myList = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26]
order_normal_mode = ['PAO1', 'Number', 'Symbol']
order_medium_mode = ['PAO1', 'PAO2', 'Number', 'Symbol']
#order_normal_mode = [ 'Number','PAO1', 'Symbol']
app = QtGui.QApplication(sys.argv)
#MainWindow = QtGui.QMainWindow()
#loginWindow = QtGui.QWidget()
#createUserWindow = QtGui.QWidget()
#characterWindow = QtGui.QWidget()
#numberWindow = QtGui.QWidget()
#symbolWindow = QtGui.QWidget()

backgroundWindow = QtGui.QWidget()
beforeStarting = QtGui.QWidget()
calculateNumbers = QtGui.QWidget()
createUserWindow = QtGui.QWidget()
forgotPassword = QtGui.QWidget()
KeyPad = QtGui.QWidget()
learningPassword = QtGui.QWidget()
loginWindow = QtGui.QWidget()
mainWindow = QtGui.QWidget()
myDialog = QtGui.QWidget()
numberWindow = QtGui.QWidget()
PAO2selectCharacterWindow =QtGui.QWidget()
routineCheck = QtGui.QWidget()
selectCharacterWindow = QtGui.QWidget()
selectCharacterWindow2 = QtGui.QWidget()
selectSymbolWindow = QtGui.QWidget()
createUserWindow = QtGui.QMainWindow()

"""
main_window = Ui_MainWindow()
create_user_window = Ui_createUserWindow()
login_window = Ui_loginWindow()
select_character_window = Ui_characterWindow()
select_character_window_2 =Ui_characterWindow()
number_window = Ui_numberWindow()
symbol_window = Ui_selectSymbol()
"""

background_window = Ui_backgroundWindow()
before_starting_window = Ui_beforeStarting()
calculate_numbers = Ui_calculateNumbersWindow()
create_user_window = Ui_createUserWindow()
forgot_password = Ui_forgotPasswordWindow()
keypad_window = Ui_keyPad()
# learningPassword = Ui_form()
login_window = Ui_loginWindow()
main_window = Ui_MainWindow()
my_dialog = Ui_myDialog()
number_window = Ui_numberWindow()
PAO2_select_character_window = Ui_PAO2characterWindow()
routine_check = Ui_Dialog()
select_character_window = Ui_characterWindow()
select_character_window_2 = Ui_characterSentenceWindow2()
select_symbol_window = Ui_selectSymbol()

class passwordGenerator(QtGui.QWidget):
    orderSelect = 0
    current_user = createUser()
    myOrder = ""
    dialogAttempts = 0
    wait = True

    def __init__(self):
        super(passwordGenerator, self).__init__()

        """
        main_window.setupUi(MainWindow)
        create_user_window.setupUi(createUserWindow)
        login_window.setupUi(loginWindow)
        select_character_window.setupUi(characterWindow)
        number_window.setupUi(numberWindow)
        symbol_window.setupUi(symbolWindow)
        """

        background_window.setupUi(backgroundWindow)
        before_starting_window.setupUi(beforeStarting)
        calculate_numbers.setupUi(calculateNumbers)
        create_user_window.setupUi(createUserWindow)
        forgot_password.setupUi(forgotPassword)
        keypad_window.setupUi(KeyPad)
        # learningPassword.setupUi(learningPassword)
        login_window.setupUi(loginWindow)
        main_window.setupUi(mainWindow)
        my_dialog.setupUi(myDialog)
        number_window.setupUi(numberWindow)
        PAO2_select_character_window.setupUi(PAO2selectCharacterWindow)
        routine_check.setupUi(routineCheck)
        select_character_window.setupUi(selectCharacterWindow)
        select_character_window_2.setupUi(selectCharacterWindow2)
        select_symbol_window.setupUi(selectSymbolWindow)
        create_user_window.setupUi(createUserWindow)

        #Setting up events
        select_character_window.next_btn.clicked.connect(self.characterSelected)
        select_symbol_window.pushButton_2.clicked.connect(self.setupSymbolWindow)
        my_dialog.buttonBox.clicked.connect(self.dialogClose)
        before_starting_window.pushButton.clicked.connect(self.closeInfo)
        main_window.createNewPassword_btn.clicked.connect(self.nextStep_event) #Normal
        main_window.createNewPassword_btn_2.clicked.connect(self.nextStep_event)  # Normal

    def openWindow(self):
        #backgroundWindow.show()
        random.shuffle(order_normal_mode)
        random.shuffle(order_medium_mode)
        order_normal_mode.insert(len(order_normal_mode), 'complete')
        order_medium_mode.insert(len(order_medium_mode), 'complete')
        #before_starting_window.pushButton.clicked.connect(self.closeInfo)
        #main_window.createNewPassword_btn.clicked.connect(self.nextStep_event) #Normal
        #main_window.createNewPassword_btn_2.clicked.connect(self.nextStep_event)  # Normal
        #main_window.createNewPassword_btn_2.connect(self.nextStep_event)  #Medium
        #main_window.confirmPasswordCreated_btn.connect(self.confirmPasswordCreated_event)  # Check password
        self.current_user = createUser()
        self.setupCharacterWindow(select_character_window)
        self.setupCharacterWindow(PAO2_select_character_window)
        #self.setupCharacterWindow(select_character_window_2)
        main_window.createNewPassword_btn.setObjectName("Normal Passwords")
        main_window.createNewPassword_btn_2.setObjectName("Medium Passwords")
        #createUserWindow.show()
        #loginWindow.show()
        mainWindow.show()
        beforeStarting.show()
        sys.exit(app.exec_())

    def closeInfo(self):
        beforeStarting.close()

    def setupCharacterWindow(self, charWindow):
        print("@setupCharacterWindow")
        random.shuffle(myList)
        self.setupCW(charWindow.btn_1, myList[1])
        self.setupCW(charWindow.btn_2, myList[2])
        self.setupCW(charWindow.btn_3, myList[3])
        self.setupCW(charWindow.btn_4, myList[4])
        self.setupCW(charWindow.btn_5, myList[5])
        self.setupCW(charWindow.btn_6, myList[6])
        self.setupCW(charWindow.btn_7, myList[7])
        self.setupCW(charWindow.btn_8, myList[8])
        self.setupCW(charWindow.btn_9, myList[9])
        self.setupCW(charWindow.btn_10, myList[10])
        self.setupCW(charWindow.btn_11, myList[11])
        self.setupCW(charWindow.btn_12, myList[12])
        self.setupCW(charWindow.btn_13, myList[13])
        self.setupCW(charWindow.btn_14, myList[14])
        self.setupCW(charWindow.btn_15, myList[15])
        self.setupCW(charWindow.btn_16, myList[16])
        self.setupCW(charWindow.btn_17, myList[17])
        self.setupCW(charWindow.btn_18, myList[18])
        self.setupCW(charWindow.btn_19, myList[19])
        self.setupCW(charWindow.btn_20, myList[20])
        self.setupCW(charWindow.btn_21, myList[21])
        self.setupCW(charWindow.btn_22, myList[22])
        self.setupCW(charWindow.btn_23, myList[23])
        self.setupCW(charWindow.btn_24, myList[24])
        self.setupCW(charWindow.btn_25, myList[25])
        self.setupCW(charWindow.btn_26, myList[0])

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
        print("@CWButtonPushed")
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

    def closeWindows(self):
        print("@closeWindows")
        myDialog.close()
        calculateNumbers.close()
        createUserWindow.close()
        forgotPassword.close()
        KeyPad.close()
        learningPassword.close()
        loginWindow.close()
        mainWindow.close()
        numberWindow.close()
        routineCheck.close()
        selectCharacterWindow.close()
        selectCharacterWindow2.close()
        selectSymbolWindow.close()
        createUserWindow.close()


    def nextStep_event(self):
        print("@nextStepEvent")
        self.closeWindows()
        pushedBy = self.sender().objectName()
        print("puched by {}".format(pushedBy))
        if (pushedBy != "Normal Passwords" and pushedBy != "Medium Passwords"):
            routine_check.passwordCheck_le.setText("")
            routine_check.widget.show()
            routine_check.label.setText("CHECKPOINT!!\nWe would like to make sure you remember your whole password up to this point. What is your password again?")
            routine_check.ok_btn.clicked.connect(self.checkIfTestIsPassed)
            routine_check.ok_btn.setObjectName(pushedBy)
            routineCheck.show()
        else:
            routine_check.widget.hide()
            routine_check.label.setText("We will be testing your memory in each phase with CHECKPOINTS, so try to remember!!")
            routine_check.ok_btn.clicked.connect(self.testPassed)
            routine_check.ok_btn.setObjectName(pushedBy)
            routineCheck.show()


    def checkIfTestIsPassed(self):
        print("@checkIfTestIsPassed")
        pushedBy = self.sender().objectName()
        #routine_check.ok_btn.setObjectName(pushedBy)
        print("pushed by ", pushedBy)

        if(str(routine_check.passwordCheck_le.text())== str(self.current_user.password)):
            print ("TEST PASSED!! The password is '{}' and you put '{}'".format( str(self.current_user.password) , str(routine_check.passwordCheck_le.text())))
            self.dialogAttempts = 0
        else:
            print("TEST NOT PASSED!! The password is '{}' and you put '{}'".format(str(self.current_user.password), str(routine_check.passwordCheck_le.text())))
            self.dialogAttempts = self.dialogAttempts+1
            routine_check.passwordCheck_le.setText("")
            routine_check.label.setText("That is not the current password! Include all the passwords up to this point\n you have a total of " + str(3-self.dialogAttempts)+ " attempts left.")
            #myDialog.show()

        if(self.dialogAttempts == 0):
            routine_check.ok_btn.clicked.connect(self.testPassed)
            routine_check.label.setText("You passed the test!! press 'Ok' to continue")
        elif(self.dialogAttempts == 3):
            print("here 4")
            routine_check.label.setText("The password that we have on file is '"+ self.current_user.password+ "' remember it for the next time!")
            routine_check.ok_btn.clicked.connect(self.testPassed)
            self.dialogAttempts = 0

    def testPassed(self):
        routineCheck.close()
        print("@testPassed")
        pushedBy = self.sender().objectName()

        if (pushedBy == "Normal Passwords"):
            self.myOrder = order_normal_mode
        elif (pushedBy == "Medium Passwords"):
            self.myOrder = order_medium_mode

        print(self.myOrder[self.orderSelect])

        if (self.myOrder[self.orderSelect]=='complete'):
            print("inside complete!")
            self.orderSelect = 0

        elif(self.myOrder[self.orderSelect]=='PAO1'):
            print("inside PAO1")
            self.orderSelect+=1
            #MainWindow.close()
            select_character_window.next_btn.setObjectName("PAO1")
            #select_character_window.next_btn.clicked.connect(self.characterSelected)
            selectCharacterWindow.show()
        elif(self.myOrder[self.orderSelect]=='PAO2'):
            print("inside PAO2")
            self.orderSelect += 1
            PAO2_select_character_window.next_btn.setObjectName("PAO2")
            PAO2_select_character_window.next_btn.clicked.connect(self.characterSelected)
            #MainWindow.close()
            selectCharacterWindow.show()
        elif(self.myOrder[self.orderSelect]=='Number'):
            print("inside Number")
            self.orderSelect += 1
            xlsheet.getRandomNumber()
            self.current_user.number_1 = xlsheet.n1
            self.current_user.number_2 = xlsheet.n2
            self.current_user.number_result = xlsheet.r
            self.current_user.operation= xlsheet.o
            self.current_user.number_full= xlsheet.fn
            fn = xlsheet.fn
            self.current_user.addToPassword(fn)
            myString = ("Your numbers are " + str(self.current_user.number_1)+ " and " +str(self.current_user.number_2)+ " you will need to " +str(self.current_user.operation)+" them.")
            calculate_numbers.label_2.setText(myString)
            calculate_numbers.ok_btn.clicked.connect(self.numbers2)
            calculateNumbers.show()
        else:
            print("inside Symbol")
            self.orderSelect+=1
            select_symbol_window.next_btn.clicked.connect(self.saveSymbol)
            selectSymbolWindow.show()

            #We would like to make sure you remember your whole password up to this point. What is your password again?

    def confirmPasswordCreated_event(self):
        loginWindow.show()

    def setupSymbolWindow(self):
        print("@setupSymbolWindow")
        mySymbol = xlsheet.getRandomSymbol()
        myIconSize = QtCore.QSize(101, 101)
        myIcon = QtGui.QIcon()
        myIcon.addPixmap(QtGui.QPixmap(symbolsPath + mySymbol + ".jpg"))
        select_symbol_window.image.setIcon(myIcon)
        select_symbol_window.image.setIconSize(myIconSize)
        select_symbol_window.symbolName_label.setText(mySymbol)
        select_symbol_window.label_4.setText(xlsheet.suggestion)
        print(mySymbol)

    def numbers2(self):
        print("@numbers2")
        if (str(calculate_numbers.number1_le.text()) != str(self.current_user.number_1)):
            print(
                "The value that you have is {} you are supposed to have {}".format(calculate_numbers.number1_le.text(),
                                                                                   str(self.current_user.number_1)))
        elif (str(calculate_numbers.number2_le.text()) != str(self.current_user.number_2)):
            print(
                "The value that you have is {} you are supposed to have {}".format(calculate_numbers.number2_le.text(),
                                                                                   str(self.current_user.number_2)))
        elif (str(calculate_numbers.results_le.text()) != str(self.current_user.number_result)):
            print("The value that you have is {} you are supposed to have {}".format(calculate_numbers.results_le.text(),str(self.current_user.number_result)))

        else:#(str(calculate_numbers.number1_le.text())==self.current_user.number_1 and\
              #         str(calculate_numbers.number2_le.text())==self.current_user.number_2 and\
               #        str(calculate_numbers.results_le.text())==self.current_user.number_result):
            operation = self.current_user.operation
            myOperationLabel =""
            if(operation=="add"):
                myOperationLabel = "+"
            elif (operation == "substract"):
                myOperationLabel = "-"
            elif (operation == "multiply"):
                myOperationLabel = "x"
            elif (operation == "divide"):
                myOperationLabel = "/"

            number_window.number1_label.setText(str(self.current_user.number_1))
            number_window.number2_label.setText(str(self.current_user.number_2))
            number_window.operation_label.setText(myOperationLabel)
            number_window.equal_label.setText("=")
            number_window.result_label.setText(str(self.current_user.number_result))
            number_window.next_btn.clicked.connect(self.goToKeypad)
            calculateNumbers.close()
            numberWindow.show()

    def goToKeypad(self):
        print("@goToKeypad")
        if(str(number_window.wholenumber_le.text())==str(self.current_user.number_full)):
            keypad_window.btn_1.clicked.connect(self.buttonPressed)
            keypad_window.btn_2.clicked.connect(self.buttonPressed)
            keypad_window.btn_3.clicked.connect(self.buttonPressed)
            keypad_window.btn_4.clicked.connect(self.buttonPressed)
            keypad_window.btn_5.clicked.connect(self.buttonPressed)
            keypad_window.btn_6.clicked.connect(self.buttonPressed)
            keypad_window.btn_7.clicked.connect(self.buttonPressed)
            keypad_window.btn_8.clicked.connect(self.buttonPressed)
            keypad_window.btn_9.clicked.connect(self.buttonPressed)
            keypad_window.btn_10.clicked.connect(self.buttonPressed)
            keypad_window.btn_minus.clicked.connect(self.buttonPressed)
            self.inKeypad()
        else:
            print("you need {} and you are typing {}".format(str(number_window.wholenumber_le.text()), str(self.current_user.number_results)))

    def inKeypad(self):
        print("@inKeypad")
        #keypad_window.next_btn.clicked.connect(self.donothing)
        numberWindow.close()
        KeyPad.show()
        fullNumberString = str(self.current_user.number_full)
        #timer  = QTimer(self)
        #timer.timeout.connect(self.shine)
        #timer.setInterval(1000)
        keypad_window.next_btn.clicked.connect(self.keypadclick)

    def donothing(self):
        print ("@donothing")

    def keypadclick(self):
        fullNumberString = str(self.current_user.number_full)
        if(str(keypad_window.number_le.text())==str(fullNumberString)):
            self.nextStep_event()
        else:
            self.buttonReleased()
            keypad_window.number_le.setText("")


    def saveSymbol(self):
        print("@saveSymbol")
        if(select_symbol_window.lineEdit.text()!=""):
            symbolString = select_symbol_window.lineEdit.text()
            self.current_user.symbol = symbolString
            self.current_user.addToPassword(symbolString)
            self.nextStep_event()

    def dialogClose(self):
        print("@dialogClose")
        myDialog.close()

    def characterSelected(self):
        print("@characterSelected")

        if(select_character_window.password_label.text()!="" and select_character_window.password_label.text()!= ""):
            pushedBy = self.sender().objectName()
            print("character selected")
            nameR = select_character_window.password_label.text()
            myName = select_character_window.name_label.text()
            myAction = xlsheet.getRandomItem("Action")
            myObject = xlsheet.getRandomItem("Object")
            myIconSize = QtCore.QSize(81, 81)

            select_character_window_2.name_label.setText(myName)
            select_character_window_2.action_label.setText(myAction)
            select_character_window_2.object_label.setText(myObject)
            myIcon = QtGui.QIcon()
            myIcon.addPixmap(QtGui.QPixmap(imagesPath + myName + ".jpg"))
            select_character_window_2.pushButton.setIcon(myIcon)
            select_character_window_2.pushButton.setIconSize(myIconSize)
            select_character_window_2.pushButton.setToolTip(myName)
            psswString = nameR + myAction[0]+myObject[0]

            if(pushedBy== "PAO1"):
                print("PAO1")
                self.current_user.PAO1_person = myName
                self.current_user.PAO1_object = myObject
                self.current_user.PAO1_action = myAction
                self.current_user.PAO1_full = psswString
                selectCharacterWindow.close()
            elif (pushedBy == "PAO2"):
                print("PAO2")
                self.current_user.PAO2_person = myName
                self.current_user.PAO2_object = myObject
                self.current_user.PAO2_action = myAction
                self.current_user.PAO2_full = psswString
                PAO2selectCharacterWindow.close()
            self.current_user.addToPassword(psswString)
            select_character_window_2.ok_btn.clicked.connect(self.confirmcharacterpassword1)
            selectCharacterWindow2.show()

    def confirmcharacterpassword1(self):
        print("@confirmcharacterpassword")
        if (select_character_window_2.lineEdit.text()==self.current_user.PAO1_full):
            self.nextStep_event()

    def buttonPressed(self):
        print("@buttonPressed")
        name = self.sender().objectName()
        string  = keypad_window.number_le.text()
        if(name =="btn_1" ):
            string = string + "1"
            keypad_window.btn_1.setStyleSheet("background:rgb(153, 255, 51)" )
        if(name =="btn_2" ):
            string = string + "2"
            keypad_window.btn_2.setStyleSheet("background:rgb(153, 255, 51)")
        if(name =="btn_3" ):
            string = string + "3"
            keypad_window.btn_3.setStyleSheet("background:rgb(153, 255, 51)")
        if(name =="btn_4" ):
            string = string + "4"
            keypad_window.btn_4.setStyleSheet("background:rgb(153, 255, 51)")
        if(name =="btn_5" ):
            string = string + "5"
            keypad_window.btn_5.setStyleSheet("background:rgb(153, 255, 51)")
        if(name =="btn_6" ):
            string = string + "6"
            keypad_window.btn_6.setStyleSheet("background:rgb(153, 255, 51)")
        if (name == "btn_7"):
            string = string + "7"
            keypad_window.btn_7.setStyleSheet("background:rgb(153, 255, 51)")
        if (name == "btn_8"):
            string = string + "8"
            keypad_window.btn_8.setStyleSheet("background:rgb(153, 255, 51)")
        if (name == "btn_9"):
            string = string + "9"
            keypad_window.btn_9.setStyleSheet("background:rgb(153, 255, 51)")
        if (name == "btn_10"):
            string = string + "0"
            keypad_window.btn_10.setStyleSheet("background:rgb(153, 255, 51)")
        if (name == "btn_minus"):
            string = string + "-"
            keypad_window.btn_minus.setStyleSheet("background:rgb(153, 255, 51)")
        keypad_window.number_le.setText(string)

    def buttonReleased(self):
        print("@buttonReleased")
        keypad_window.btn_1.setStyleSheet("background:rgb(255, 255, 255)")
        keypad_window.btn_2.setStyleSheet("background:rgb(255, 255, 255)")
        keypad_window.btn_3.setStyleSheet("background:rgb(255, 255, 255)")
        keypad_window.btn_4.setStyleSheet("background:rgb(255, 255, 255)")
        keypad_window.btn_5.setStyleSheet("background:rgb(255, 255, 255)")
        keypad_window.btn_6.setStyleSheet("background:rgb(255, 255, 255)")
        keypad_window.btn_7.setStyleSheet("background:rgb(255, 255, 255)")
        keypad_window.btn_8.setStyleSheet("background:rgb(255, 255, 255)")
        keypad_window.btn_9.setStyleSheet("background:rgb(255, 255, 255)")
        keypad_window.btn_10.setStyleSheet("background:rgb(255, 255, 255)")
        keypad_window.btn_minus.setStyleSheet("background:rgb(255, 255, 255)")

if __name__ == "__main__":
    myApp = passwordGenerator()
    myApp.openWindow()