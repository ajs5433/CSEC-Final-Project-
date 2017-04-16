#import section
import sys
import random
from PyQt4 import QtGui
from PyQt4 import QtCore
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

#General Attributes
xlsheet = myExcel()
imagesPath = "A:/Desktop/myProject/Project Files/Images/"
symbolsPath = "A:/Desktop/myProject/Project Files/Symbols/"
buttonName = ""
myList = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26]
order_normal_mode = ['PAO1', 'Number', 'Symbol']
order_medium_mode = ['PAO1', 'PAO2', 'Number', 'Symbol']
app = QtGui.QApplication(sys.argv)

#General Windows
backgroundWindow = QtGui.QWidget()
beforeStarting = QtGui.QWidget()
calculateNumbers = QtGui.QWidget()
#createUserWindow = QtGui.QWidget()
forgotPassword = QtGui.QWidget()
KeyPad = QtGui.QWidget()
#learningPassword = QtGui.QWidget()
#loginWindow = QtGui.QWidget()
mainWindow = QtGui.QWidget()
numberWindow = QtGui.QWidget()
#PAO2selectCharacterWindow =QtGui.QWidget()
routineCheck = QtGui.QWidget()
selectCharacterWindow = QtGui.QWidget()
selectCharacterWindow2 = QtGui.QWidget()
selectSymbolWindow = QtGui.QWidget()

background_window = Ui_backgroundWindow()
before_starting_window = Ui_beforeStarting()
calculate_numbers = Ui_calculateNumbersWindow()
#create_user_window = Ui_createUserWindow()
forgot_password = Ui_forgotPasswordWindow()
keypad_window = Ui_keyPad()
#learningPassword = Ui_form()
#login_window = Ui_loginWindow()
main_window = Ui_MainWindow()
number_window = Ui_numberWindow()
#PAO2_select_character_window = Ui_PAO2characterWindow()
routine_check = Ui_Dialog()
select_character_window = Ui_characterWindow()
select_character_window_2 = Ui_characterSentenceWindow2()
select_symbol_window = Ui_selectSymbol()

class passwordGenerator(QtGui.QWidget):
    orderSelect = 0
    current_user = createUser()
    myOrder = ""
    passwordAttempts = 3
    # Events:--------------------------------------------------------------------------------------------------------

    #  close info:***********************************************
    def closeInfo_event(self):
        print("-->E closeInfo")
        beforeStarting.close()

    #  routine check:********************************************
    def rc_e(self):
        print("-->E routineCheck")

        pushedBy = self.sender().objectName()
        print("puched by {}".format(pushedBy))
        self.passwordAttempts = 3

        if (pushedBy != "Normal Passwords" and pushedBy != "Medium Passwords"):
            # routine check set up
            routine_check.widget.show()
            routine_check.passwordCheck_le.setText("")
            routine_check.label.setText("CHECKPOINT!!\nWe would like to make sure you remember your whole password up to this point. What is your password again?")
            routine_check.ok_btn.clicked.connect(self.checkIfTestIsPassed)
            #routine_check.ok_btn.setObjectName(pushedBy)
            self.setupRC()
            routineCheck.show()
            # close previous windows
            selectCharacterWindow2.close()
            KeyPad.close()
            selectSymbolWindow.close()


        else:
            if (pushedBy == "Normal Passwords"):    self.myOrder = order_normal_mode
            elif (pushedBy == "Medium Passwords"):  self.myOrder = order_medium_mode
            # routine check set up
            routine_check.widget.hide()
            routine_check.label.setText("We will be testing your memory in each phase with CHECKPOINTS, so try to remember!!")
            routine_check.ok_btn.clicked.connect(self.testPassed)
            #routine_check.ok_btn.setObjectName(pushedBy)
            routineCheck.show()
            mainWindow.close()

    def setupRC(self):
        routineCheck = QtGui.QWidget()
        routine_check = Ui_Dialog()
        routine_check.setupUi(routineCheck)
        routine_check.widget.show()
        routine_check.passwordCheck_le.setText("")
        routine_check.label.setText("CHECKPOINT!!\nWe would like to make sure you remember your whole password up to this point. What is your password again?")
        routine_check.ok_btn.clicked.connect(self.checkIfTestIsPassed)

    # check test:*********************************************
    def checkIfTestIsPassed(self):
        print("-->E checkIfTestIsPassed")
        typedPassword = str(routine_check.passwordCheck_le.text())
        userPassword = str(self.current_user.password)
        myAttempts = self.passwordAttempts
        attemptsLeft = 3-myAttempts

        if (typedPassword == userPassword):
            print("TEST PASSED!! The password is '{}' and you put '{}'".format(userPassword, typedPassword))
            routine_check.label.setText("You passed the test!! press 'Ok' to continue")
            routine_check.ok_btn.clicked.connect(self.testPassed)
        elif(self.passwordAttempts == 0):
            routine_check.label.setText("The password that we have on file is '"+userPassword + "' remember it for the next time!")
            routine_check.ok_btn.clicked.connect(self.testPassed)
        else:
            print("TEST PASSED!! The password is '{}' and you put '{}'".format(userPassword, typedPassword))
            routine_check.label.setText("That is not the current password! Include all the passwords up to this point\n you have a total of " + str(attemptsLeft) + " attempts left.")
            routine_check.passwordCheck_le.setText("")
            self.passwordAttempts = myAttempts-1

    # test Passed: Next Stage!**********************************
    def testPassed(self):
        print("-->E testPassed")
        print(self.orderSelect, " ", self.myOrder[self.orderSelect])

        Order = self.myOrder
        Index = self.orderSelect

        if (Order[Index] == 'PAO1'):
            print("inside PAO1")
            self.orderSelect += 1
            select_character_window.next_btn.setObjectName("PAO1")
            # select_character_window.next_btn.clicked.connect(self.characterSelected)
            selectCharacterWindow.show()
            routineCheck.close()

        elif (Order[Index] == 'PAO2'):
            print("inside PAO2")
            self.orderSelect += 1
            #PAO2_select_character_window.next_btn.setObjectName("PAO2")
            #PAO2_select_character_window.next_btn.clicked.connect(self.characterSelected)
            selectCharacterWindow.show()
            routineCheck.close()

        elif (Order[Index] == 'Number'):
            print("inside Number")
            self.orderSelect += 1
            #getting random number and giving it to user
            xlsheet.getRandomNumber()
            self.current_user.number_1 = xlsheet.n1
            self.current_user.number_2 = xlsheet.n2
            self.current_user.number_result = xlsheet.r
            self.current_user.operation = xlsheet.o
            self.current_user.number_full = xlsheet.fn
            fn = xlsheet.fn
            self.current_user.addToPassword(fn)
            myString = ("Your numbers are " + str(self.current_user.number_1) + " and " + str(self.current_user.number_2) + " you will need to " + str(self.current_user.operation) + " them.")
            #setting up calculate numbers
            calculate_numbers.label_2.setText(myString)
            calculateNumbers.show()
            routineCheck.close()

        elif (Order[Index] == 'Symbol' ):
            print("inside Symbol")
            self.orderSelect += 1
            selectSymbolWindow.show()
            routineCheck.close()

        else:
            print("inside complete!")
            self.orderSelect = 0
            QtCore.QCoreApplication.instance().quit()

    # numbers 2nd page: **********************************
    def numbers2(self):
        print("-->E Numbers2")
        # just printing to check - personal
        if (str(calculate_numbers.number1_le.text()) != str(self.current_user.number_1)):
            print("The value that you have is {} you are supposed to have {}".format(
                calculate_numbers.number1_le.text(), str(self.current_user.number_1)))
        elif (str(calculate_numbers.number2_le.text()) != str(self.current_user.number_2)):
            print("The value that you have is {} you are supposed to have {}".format(
                calculate_numbers.number2_le.text(), str(self.current_user.number_2)))
        elif (str(calculate_numbers.results_le.text()) != str(self.current_user.number_result)):
            print("The value that you have is {} you are supposed to have {}".format(
                calculate_numbers.results_le.text(), str(self.current_user.number_result)))
        else:
            operation = self.current_user.operation
            myOperationLabel = ""
            if (operation == "add"):
                myOperationLabel = "+"
            elif (operation == "substract"):
                myOperationLabel = "-"
            elif (operation == "multiply"):
                myOperationLabel = "x"
            elif (operation == "divide"):
                myOperationLabel = "/"
            # setting number window
            number_window.number1_label.setText(str(self.current_user.number_1))
            number_window.number2_label.setText(str(self.current_user.number_2))
            number_window.operation_label.setText(myOperationLabel)
            number_window.result_label.setText(str(self.current_user.number_result))
            numberWindow.show()
            calculateNumbers.close()

    # Go to Keypad and keypadclick:***********************************************
    def goToKeypad(self):
        print("-->E checkIfTestIsPassed")
        typedNumber = str(number_window.wholenumber_le.text())
        userNumber = str(self.current_user.number_full)
        if (userNumber == typedNumber):
            keypad_window.btn_minus.clicked.connect(self.buttonPressed)
            KeyPad.show()
            numberWindow.close()
        else:
            print("you need {} and you are typing {}".format(typedNumber, userNumber))


    def saveSymbol(self):
        ("-->E saveSymbol")
        if (select_symbol_window.lineEdit.text() != ""):
            symbolString = select_symbol_window.lineEdit.text()
            self.current_user.symbol = symbolString
            self.current_user.addToPassword(symbolString)
            self.rc_e()

    def doNothing(self):
        print("password do not match")

    # character selected:***********************************************
    def characterSelected(self):
        ("-->E characterSelected")
        characterPassword = select_character_window.password_label.text()
        if (characterPassword != ""):
            pushedBy = self.sender().objectName()
            print("character selected")
            #setting up next window
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
            psswString = nameR + myAction[0] + myObject[0]
            if (pushedBy == "PAO1"):
                print("PAO1")
                self.current_user.PAO1_person = myName
                self.current_user.PAO1_object = myObject
                self.current_user.PAO1_action = myAction
                self.current_user.PAO1_full = psswString
                selectCharacterWindow2.show()
                selectCharacterWindow.close()
            elif (pushedBy == "PAO2"):
                print("PAO2")
                self.current_user.PAO2_person = myName
                self.current_user.PAO2_object = myObject
                self.current_user.PAO2_action = myAction
                self.current_user.PAO2_full = psswString
                PAO2selectCharacterWindow.close()
                selectCharacterWindow2.show()
            self.current_user.addToPassword(psswString)

    def checkCharWindowText(self):
        ("-->E confirmCharacterpassword")
        if (select_character_window_2.lineEdit.text() == self.current_user.PAO1_full):
            select_character_window_2.ok_btn.clicked.connect(self.rc_e)
        else:
            select_character_window_2.ok_btn.clicked.connect(self.doNothing)

    # login window:***********************************************
    """
    def confirmPasswordCreated_event(self):
            loginWindow.show()
    """

    # Initialization:--------------------------------------------------------------------------------------------------------
    def __init__(self):
        super(passwordGenerator, self).__init__()

        background_window.setupUi(backgroundWindow)
        before_starting_window.setupUi(beforeStarting)
        calculate_numbers.setupUi(calculateNumbers)
        #create_user_window.setupUi(createUserWindow)
        forgot_password.setupUi(forgotPassword)
        keypad_window.setupUi(KeyPad)
        # learningPassword.setupUi(learningPassword)
        #login_window.setupUi(loginWindow)
        main_window.setupUi(mainWindow)
        number_window.setupUi(numberWindow)
        #PAO2_select_character_window.setupUi(PAO2selectCharacterWindow)
        routine_check.setupUi(routineCheck)
        select_character_window.setupUi(selectCharacterWindow)
        select_character_window_2.setupUi(selectCharacterWindow2)
        select_symbol_window.setupUi(selectSymbolWindow)

        #setting up events and button properties
        before_starting_window.pushButton.clicked.connect(self.closeInfo_event)           # Before Starting
        main_window.createNewPassword_btn.clicked.connect(self.rc_e)      # Main - Create User Normal Mode
        main_window.createNewPassword_btn_2.clicked.connect(self.rc_e)    # Main - Create User Medium Mode
        select_symbol_window.pushButton_2.clicked.connect(self.setupSymbolWindow)   # Symbol - update symbol
        select_symbol_window.next_btn.clicked.connect(self.saveSymbol)              # Symbol - NEXT - routine check
        select_character_window.next_btn.clicked.connect(self.characterSelected)    # Character1 - character selected
        select_character_window_2.ok_btn.clicked.connect(self.doNothing)    #Character - confirm character
        calculate_numbers.ok_btn.clicked.connect(self.numbers2)                     # Numbers 1 - go to Numbers 2
        number_window.next_btn.clicked.connect(self.goToKeypad)                     # Number2 - go to Keypad
        keypad_window.next_btn.clicked.connect(self.keypadReset)                    # keypad - check click


        main_window.createNewPassword_btn.setObjectName("Normal Passwords")         # Main - normal button
        main_window.createNewPassword_btn_2.setObjectName("Medium Passwords")       # Main - normal button
        keypad_window.btn_1.clicked.connect(self.buttonPressed)                     # KeyPad - button 1
        keypad_window.btn_2.clicked.connect(self.buttonPressed)                     # KeyPad - button 2
        keypad_window.btn_3.clicked.connect(self.buttonPressed)                     # KeyPad - button 3
        keypad_window.btn_4.clicked.connect(self.buttonPressed)                     # KeyPad - button 4
        keypad_window.btn_5.clicked.connect(self.buttonPressed)                     # KeyPad - button 5
        keypad_window.btn_6.clicked.connect(self.buttonPressed)                     # KeyPad - button 6
        keypad_window.btn_7.clicked.connect(self.buttonPressed)                     # KeyPad - button 7
        keypad_window.btn_8.clicked.connect(self.buttonPressed)                     # KeyPad - button 8
        keypad_window.btn_9.clicked.connect(self.buttonPressed)                     # KeyPad - button 9
        keypad_window.btn_10.clicked.connect(self.buttonPressed)                    # KeyPad - button 0
        keypad_window.btn_minus.clicked.connect(self.buttonPressed)                 # KeyPad - button -

        select_character_window_2.lineEdit.textChanged.connect(self.checkCharWindowText)

        #shuffle orders
        random.shuffle(order_normal_mode)
        random.shuffle(order_medium_mode)
        order_normal_mode.insert(len(order_normal_mode), 'complete')
        order_medium_mode.insert(len(order_medium_mode), 'complete')

        self.current_user = createUser()

        self.setupCharacterWindow(select_character_window)
        # self.setupCharacterWindow(select_character_window_2)

    def start(self):
        #Everything is set up let's show the windows
        #backgroundWindow.show()
        mainWindow.show()
        beforeStarting.show()
        sys.exit(app.exec_())

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
        button.clicked.connect(self.characterButtonPushed_event)
        button.setObjectName(myName)

    def characterButtonPushed_event(self):
        print("->characterButtonPushed")
        name = self.sender().objectName()
        select_character_window.name_label.setText(name)
        passwordLabel = ""
        #getting character
        for i in name.split():
            passwordLabel += i[0]
        select_character_window.password_label.setText(passwordLabel)
        myIconSize = QtCore.QSize(151, 151)
        myIcon = QtGui.QIcon()
        myIcon.addPixmap(QtGui.QPixmap(imagesPath + name + ".jpg"))
        select_character_window.pushButton.setIcon(myIcon)
        select_character_window.pushButton.setIconSize(myIconSize)

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

    def keypadReset(self):
        print("@resetKeypad")
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
        keypad_window.number_le.setText("")

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

        userFullNumber = str(self.current_user.number_full)

        if (userFullNumber == string):
            keypad_window.next_btn.clicked.connect(self.rc_e)
        else:
            keypad_window.next_btn.clicked.connect(self.keypadReset)


if __name__ == "__main__":
    myApp = passwordGenerator()
    myApp.start()