import datetime
import time
import json
import os
from datetime import datetime

filepath = 'A:/Desktop/myProject/Project Files/userBook.txt'

class createUser():
    userBook = {}

    name = ""
    last_name = ""
    password_type = ""

    username = ""
    password = ""

    PAO1_person = ""
    PAO1_action = ""
    PAO1_number = ""
    PAO1_object = ""
    PAO1_full = ""

    PAO2_person = ""
    PAO2_action = ""
    PAO2_object = ""
    PAO2_place =""
    PAO2_full = ""

    number_1 = ""
    number_2 = ""
    operation = ""
    number_result =""
    number_full = ""

    symbol = ""

    setup_time = ""
    first_login = ""
    last_login = ""

    def __init__(self):
        #print("New User!")
        """
        self.name = n
        self.lastName = l
        self.passwordType = pt
        
        self.username = self.name + self.lastName + self.passwordType
        """

    def save(self):
        #print("Saving user")
        create = False;
        self.last_login = self.first_login,

        #check if file exists and if its empty
        if (os.path.isfile(filepath)):
            if(os.stat(filepath).st_size != 0):
                with open(filepath, "r") as f:
                    dataString = f.read()
                    dataBook = json.loads(dataString)

                    if self.username in dataString:
                        print("there's already a user named "+ self.username)
                        create = False
                    else:
                        print('no user named ' + self.username)
                        create = True
            if(create):
                self.userBook[self.username] = {
                    'name:': self.name,
                    'last name': self.lastName,
                    'password type': self.passwordType,
                    'password': self.password,
                    'PAO1_person': self.PAO1_person,
                    'PAO1_action': self.PAO1_action,
                    'PAO1_object': self.PAO1_object,
                    'PAO1_full': self.PAO1_full,
                    'PAO2_person': self.PAO2_person,
                    'PAO2_action': self.PAO2_action,
                    'PAO2_object': self.PAO2_object,
                    'PAO2_full': self.PAO2_full,
                    'number': self.number,
                    'symbol': self.symbol,
                    'setup time': self.setup_time,
                    'first login': self.first_login,
                    'last login': self.last_login
                }

                dataBook.update(self.userBook)

                with open(filepath, "w") as f:
                    newbook = json.dumps(dataBook)
                    f.write(newbook)

        #json.dumps(userBook)

    def update_file(self, field,update):

        with open(filepath, "r") as json_file:
            with open(filepath, 'r') as f:
                json_data = json.load(f)
                json_data[field] = update

            with open('my_file.json', 'w') as f:
                f.write(json.dumps(json_data))

    def addToPassword(self, moredata):
        print("adding ", moredata, " to password")
        self.password = self.password + moredata

if __name__== "__main__":
    myuser = createUser("gotta", "Go888", "Test")
    myuser.save()





