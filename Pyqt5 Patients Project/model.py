from PyQt5.QtCore import Qt
from PyQt5.QtSql import QSqlTableModel

class ClientsModel:
    def __init__(self):
        self.model = self._createModel()
        self.users_model = self._createUserModel()
        self.allergy_test_model = self._createListTestModel()


    @staticmethod
    def _createModel():
        """create and setup the model"""
        tablemodel = QSqlTableModel()
        tablemodel.setTable("patients")
        tablemodel.setEditStrategy(QSqlTableModel.OnFieldChange)
        tablemodel.select()
        headers = ("ID", "ONOMA", "Επίθετο", "Αριθμός Τηλεφώνου", " EMAIL" , "ΑΜΚΑ", "ΔΙΕΥΘΥΝΣΗ", "ΑΛΛΕΡΓΙΑ")

        for columnIndex, header in enumerate(headers):
            tablemodel.setHeaderData(columnIndex, Qt.Horizontal, header)
        return tablemodel

    @staticmethod
    def _createUserModel():
        """create and setup the users table model in database"""
        tablemodel = QSqlTableModel()
        tablemodel.setTable("users")
        tablemodel.setEditStrategy(QSqlTableModel.OnFieldChange)
        tablemodel.select()
        headers = ("ID", "Username", "Password")

        for columnIndex, header in enumerate(headers):
            tablemodel.setHeaderData(columnIndex, Qt.Horizontal, header)
        return tablemodel

    @staticmethod
    def _createListTestModel():
        """Create the model that will populate the listview from the table allergy tests from database """

        listmodel = QSqlTableModel()
        listmodel.setTable("allergy_tests")
        listmodel.setEditStrategy(QSqlTableModel.OnFieldChange)
        listmodel.select()
        headers = ("status", "ID", "ΠΕΡΙΓΡΑΦΗ ΤΕΣΤ")
        
        for columnIndex, header in enumerate(headers):
            listmodel.setHeaderData(columnIndex, Qt.Horizontal, header)
        return listmodel 



# WE CREATE A METHOD SO WE CAN ADD THE INFO WE TAKE FROM THE USER TO
# OUR DATABASE. WE SAVED THE INFO FROM THE USER WITH THE .text() and
# we saved it to a list named data---?is a list
    def addPatient(self, data):
        """add patient from the database"""
        rows = self.model.rowCount()
        self.model.insertRows(rows, 1)
        for column, field in enumerate(data):
            self.model.setData(self.model.index(rows, column+1), field)
        self.model.submitAll()
        self.model.select()

    def deletePatient(self, row):
        """delete patient from the database"""

        self.model.removeRow(row)
        self.model.submitAll
        self.model.select()


    def addUserToDatabase(self, userData):
        """add user to the database"""
        rows = self.users_model.rowCount()
        self.users_model.insertRows(rows, 1)
        for column, field in enumerate(userData):
            self.users_model.setData(self.users_model.index(rows, column+1), field)
        self.users_model.submitAll()
        self.users_model.select()