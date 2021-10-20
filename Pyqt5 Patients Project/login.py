import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QMessageBox
from PyQt5.QtGui import QPixmap
from database import createConnection
from main_sub import MainWindow
from model import ClientsModel
from register import RegisterUi
from PyQt5.QtSql import  QSqlQuery
import hashlib
import time


class WelcomeScreen(QDialog):
    def __init__(self):
        super(WelcomeScreen, self).__init__()
        loadUi("login.ui", self)

        self.setWindowTitle(" ΕΙΣΟΔΟΣ ΣΤΟ ΠΡΟΓΡΑΜΜΑ")
        self.setStyleSheet("background-color: #ffffff; color: black ; font :bold ;")


        self.login_button.clicked.connect(self.goto_mainapp)
        # We only uncomment this line if we want to create a new main user 
        self.register_button.clicked.connect(self.goto_registerpage)
        self.quit_button.clicked.connect(self.quit_application)

    @staticmethod
    def hash(src):
        """
                 Hash md5 encryption method
                 :param src: string str
        :return:
        """
        src = (src +"pipis").encode("utf-8")
        m = hashlib.md5()
        m.update(src)
        return m.hexdigest()

    def quit_application(self):
        self.close()
        
    def goto_mainapp(self):
       
        username = (self.user_lineEdit.text())
        password = (self.password_lineEdit.text())

       # print(f"the username = {username} and the type is BEFORE the hash: {type(username)} ")
       # print(f"the password = {password} and the type is BEFORE the hash: {type(password)} ")

        username = self.hash(username)
        password = self.hash(password)

       # print(f"the username = {username} and the type is AFTER the hash: {type(username)} ")
       # print(f"the password = {password} and the type is AFTER the hash: {type(password)}")

        self.user_lineEdit.clear()
        self.password_lineEdit.clear()

        query = QSqlQuery()

        query.exec_("SELECT *FROM users WHERE ID=1")
        while query.next():
            self.username = (query.value(1))
            print(f"the self.username = {self.username} and the type of the the self.username is : {type(self.username)}")

        query.exec_("SELECT * FROM users WHERE ID=1")
        while query.next():
            self.password = (query.value(2))
            print(f"the self.password = {self.password} and the type of the the self.password is : {type(self.password)}")

        if username == self.username and password == self.password: 
            
            self.main_window = MainWindow()
            self.close()
            time.sleep(1)
            self.main_window.show()
            
        else:
            print("the password is not correct try again")

            QMessageBox.critical(
            self,
            "ERROR",
            f"O Kωδικός ή το username δεν είναι σωστό",
            )

    def goto_registerpage(self):

        register_ui = RegisterUi()
        register_ui.show()
        register_ui.exec_()
        

if not createConnection("patients.sqlite"):
        sys.exit(1)
else:
       print("database created")


app = QApplication(sys.argv)
welcome = WelcomeScreen()
welcome.setFixedHeight(300)
welcome.setFixedWidth(500)
welcome.show()

try:
    sys.exit(app.exec_())
    
except:
    print("Exiting")
