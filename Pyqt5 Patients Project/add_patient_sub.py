import sys
from add_patient import Ui_Dialog
from PyQt5.QtWidgets import QDialog, QApplication, QMessageBox
from model import ClientsModel

class Add_patient(QDialog):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # we create an instance of the Ui_MainWindow so though the object we can
        # call the methods and set up the ui
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.model = ClientsModel()

        self.ui.ok_submit_button.clicked.connect(self.ok_button_is_pressed)
        self.ui.cancel_button.clicked.connect(self.quit_application)

    def quit_application(self):
        self.close()

    def ok_button_is_pressed(self):
        ''' ok_button_is_pressed saved the information that the user provides
         to the clients database'''

        self.data = []
        for field in (self.ui.first_name_lineEdit, self.ui.last_name_lineEdit, self.ui.phonenumber_lineEdit):
            if not field.text():
                QMessageBox.critical(
                self,
                "ERROR",
                f"Tο πεδίο: {field.objectName()}. Δεν μπορεί να είναι κενό",
                )
                self.data = None # reset data
                return

            self.data.append(field.text())

        for field in (self.ui.email_lineEdit,  self.ui.amka_lineEdit, self.ui.address_lineEdit):

            self.data.append(field.text())


        if not self.data:
            return

        #We clear the information after we take it and saved it
        self.ui.first_name_lineEdit.clear()
        self.ui.last_name_lineEdit.clear()
        self.ui.address_lineEdit.clear()
        self.ui.phonenumber_lineEdit.clear()
        self.ui.email_lineEdit.clear()
        self.ui.amka_lineEdit.clear()

        self.model.addPatient(self.data)

        print("u added a new patient")
        
        QMessageBox.information(
                self,
                "Πληροφορία",
                f"Ο Πελάτης καταχωρήθηκε στην βάση",
                )
                
        print("U just added a new user to the database")


if __name__ == '__main__':
    app = QApplication([])



    widget = Add_patient()
    widget.show()

    app.exec_()
