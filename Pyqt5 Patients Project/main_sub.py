import sys
from main import Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow, QApplication, QTableView
from database import createConnection
from model import ClientsModel
from add_patient_sub import Add_patient
from info_sub import Patients_Information


class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # we create an instance of the Ui_MainWindow so though the object we can
        # call the methods and set up the ui
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.clientsmodel = ClientsModel()

        self.ui.add_patient_button.clicked.connect(self.clicked_to_add_new_patient)
        self.ui.view_patients_info_button.clicked.connect(self.view_patients_information)

    def clicked_to_add_new_patient(self):

        print("u just clicked to try and add a new patient")
        self.add_user = Add_patient(self)
        self.add_user.show()

    def view_patients_information(self):

        """this will be the table and when u click the clients inforrmation
        you will be able to see a table fill with the information from
        the database"""

        self.patients_info = Patients_Information()
        self.patients_info.show()



if __name__ == '__main__':
    app = QApplication([])


    if not createConnection("patients.sqlite"):
        sys.exit(1)
    else:
        print("database created")

    widget = MainWindow()
    widget.show()

    app.exec_()
