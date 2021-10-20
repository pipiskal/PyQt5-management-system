import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QMessageBox
from model import ClientsModel



class New_allergy_test(QDialog):
    def __init__(self):
        super().__init__()
        loadUi("new_allergy_test.ui", self)
        self.setWindowTitle(" ΝΕΟ ΑΛΛΕΡΓΙΚΟ ΤΕΣΤ")
        self.show()

        self.model = ClientsModel()
        self.allergy_tests_tableview.setModel(self.model.allergy_test_model)
        self.allergy_tests_tableview.hideColumn(0)
        self.allergy_tests_tableview.setColumnWidth(1,300)
        self.model.allergy_test_model.select()


    def populate_list_with_tests_from_database(self):
        pass


    def checkbox_the_list_items(self):
        pass


    def save_selected_tests_to_database(self, datetime, tests_done_list, patient_id, ):
        pass



    