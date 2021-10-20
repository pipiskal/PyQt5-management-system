import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QWidget
from PyQt5.QtGui import QPixmap
import hashlib
from model import ClientsModel

class RegisterUi(QDialog):
    def __init__(self):
        super().__init__()
        loadUi("register.ui", self)

        self.model = ClientsModel()
        self.ok_button.clicked.connect(self.sign_up)


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

    def sign_up(self):
        self.userdata = []

        username = self.username_line_edit.text()
        password = self.password_line_edit.text()
        verrification_password = self.password_ver_line_edit.text()


        username = self.hash(username)
        password = self.hash(password)
        verrification_password = self.hash(verrification_password)


        self.userdata.append(username)
        self.userdata.append(password)
        self.userdata.append(verrification_password)

        print(self.userdata)

        self.model.addUserToDatabase(self.userdata)


if __name__ == "__main__":

    app = QApplication(sys.argv)
    register_form = RegisterUi()
    widget = QtWidgets.QStackedWidget()
    widget.addWidget(register_form)
    widget.setFixedHeight(300)
    widget.setFixedWidth(400)
    widget.show()

    try:
        sys.exit(app.exec_())
    except:
        print("Exiting")