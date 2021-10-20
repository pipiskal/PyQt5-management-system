import sys
import csv
import re
from info import Ui_MainWindow_info
from model import ClientsModel
from PyQt5.QtSql import QSqlDatabase, QSqlQuery
from PyQt5.QtWidgets import (
QMainWindow,
QApplication,
QDataWidgetMapper,
QAbstractItemView,
QMessageBox
)
from new_allergy_test import New_allergy_test



class Patients_Information(QMainWindow):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # we create an instance of the Ui_MainWindow so though the object we can
        # call the methods and set up the ui
        self.info_ui = Ui_MainWindow_info()
        self.info_ui.setupUi(self)

        print("created patients info table ")
        self.populate_table()


    def populate_table(self):

        self.clientsmodel = ClientsModel()
        self.table = self.info_ui.information_table
        self.table.setModel(self.clientsmodel.model)
        self.table.resizeColumnsToContents()
        # loads the information into the QtableView
        self.clientsmodel.model.select()

        self.table.hideColumn(0)
        self.table.hideColumn(7)

        self.table.setSortingEnabled(True)
        self.table.setSelectionBehavior(QAbstractItemView.SelectRows)

        self.table.clicked.connect(self.on_click)
        self.info_ui.save_database_button.clicked.connect(self.extractDatabaseToCSV)
        self.info_ui.load_csv_file.clicked.connect(self.load_CSVtoDatabase)
        self.info_ui.delete_patient_button.clicked.connect(self.deletePatient_on_delete)
        self.info_ui.create_new_allergy_test.clicked.connect(self.create_new_test)


        self.info_ui.search_first_name_QLineEdit.textChanged.connect(self.search_with_first_name)
        self.info_ui.search_last_name_QLineEdit.textChanged.connect(self.search_with_last_name)
        self.info_ui.search_amka_QLineEdit.textChanged.connect(self.search_with_amka)
        self.info_ui.search_phonenumber_QLineEdit.textChanged.connect(self.search_with_phonenumber)


    def search_with_first_name(self,s):
        s = re.sub("[\W_]+", "", s)
        filter_str = 'first_name LIKE "%{}%"'.format(s)
        self.clientsmodel.model.setFilter(filter_str)

    def search_with_last_name(self,s):
        s = re.sub("[\W_]+", "", s)
        filter_str = 'last_name LIKE "%{}%"'.format(s)
        self.clientsmodel.model.setFilter(filter_str)

    def search_with_phonenumber(self,s):
        s = re.sub("[\W_]+", "", s)
        filter_str = 'phone_number LIKE "%{}%"'.format(s)
        self.clientsmodel.model.setFilter(filter_str)

    def search_with_amka(self,s):
        s = re.sub("[\W_]+", "", s)
        filter_str = 'amka LIKE "%{}%"'.format(s)
        self.clientsmodel.model.setFilter(filter_str)

    def deletePatient_on_delete(self):
        row = self.table.currentIndex().row()
        if row < 0:
            return
        messageBox = QMessageBox.warning(
        self,
        "Warning!",
        f"ΘΕΛΕΙΣ ΝΑ ΓΙΝΕΙ ΔΙΑΓΡΑΦΗ ΤΟΥ ΑΣΘΕΝΗ??",
        QMessageBox.Ok | QMessageBox.Cancel,
        )

        if messageBox == QMessageBox.Ok:
            self.clientsmodel.deletePatient(row)


    def on_click(self,index):
        """when a row from the table is selected the text_edit will show with the
        text from the database ready to be edited"""

       
        # what the mapper returns its depending on the orrientation
        # the default is the vertical so its the row

        
        self.patient_id = index.siblingAtColumn(0).data()
        

        self.mapper = QDataWidgetMapper()
        self.mapper.setModel(self.clientsmodel.model)
        self.mapper.addMapping(self.info_ui.information_textEdit, 7)
        self.mapper.setCurrentModelIndex(index)

        print(f"u clicked the row {index.row()}and the patients id is:  {self.patient_id}")
        


    def create_new_test(self):
        try:
            self.newtest = New_allergy_test()
            self.newtest.patient_id_label.setText(str(self.patient_id))

            query = QSqlQuery()
            # this prints true so it does return something
            query.exec_(f"SELECT first_name FROM patients WHERE ID={self.patient_id}")
            while query.next():
                patient_name = query.value(0)
                
            self.newtest.patient_name_label.setText(patient_name)
        except:
            messageBox = QMessageBox.warning(
            self,
            "Warning!",
            f"ΔΕΝ ΕΧΕΙΣ ΕΠΙΛΕΞΕΙ ΑΣΘΕΝΗ.",
            QMessageBox.Ok | QMessageBox.Cancel,
             )
             
            return messageBox

        
        
        

    def extractDatabaseToCSV(self):


        query = QSqlQuery()
        query.exec_("SELECT * FROM patients ") # it should be better to SELECT Exactly whtat we need from the table
        print("i am extracking the whole database to a csv file so i can import it later")
        filename = "data.csv" #export to csv file

        # i ask it to create or open the csv file if exists and create the headers by using 
        # write.writerow
        with open (filename, mode = "w", encoding="utf-8",newline= "") as f:
            write = csv.writer(f, dialect = "excel")
            write.writerow(["first_name", "last_name", "phone_number", "email", "amka", "address", "illness"])

            while query.next():
                firstname = query.value(1)
                lastname = query.value(2)
                phone_number = query.value(3)
                email = query.value(4)
                amka = query.value(5)
                address = query.value(6)
                illness = query.value(7)
               

                write.writerow([firstname, lastname, phone_number, email, amka, address, illness]) # write one line at a time


        # we could check if the csv file is ok and print the use the checkbox to print that is ok
        messageBox = QMessageBox.information(
        self,
        "ΕΙΔΟΠΟΙΗΣΗ",
        f"ΕΓΙΝΕ ΑΝΤΙΓΡΑΦΟ ΤΩΝ ΑΣΘΕΝΩΝ!! ",
        QMessageBox.Ok,
        )


    def load_CSVtoDatabase(self):

        filename = "data.csv"
        query = QSqlQuery()

        try: 
            with open (filename, mode = "r", encoding="utf-8") as f:
                pattient_reader = csv.DictReader(f)
                print(pattient_reader)
                
                for row in pattient_reader:
                    query.prepare("INSERT INTO patients (first_name, last_name, phone_number, email, amka, address, illness)"
                    "VALUES (:first_name, :last_name, :phone_number, :email, :amka, :address, :illness)")

                    query.bindValue(":first_name", row["first_name"])
                    query.bindValue(":last_name", row["last_name"])
                    query.bindValue(":email", row["email"])
                    query.bindValue(":phone_number", row["phone_number"])
                    query.bindValue(":amka", row["amka"])
                    query.bindValue(":address", row["address"])
                    query.bindValue(":illness", row["illness"])
                    query.exec()

                QMessageBox.information(
                self,
                "ΕΙΔΟΠΟΙΗΣΗ",
                f"ΕΓΙΝΕ ΕΙΣΑΓΩΓΗ ΤΗΣ ΒΑΣΗΣ ΑΠΟ ΑΡΧΕΙΟ CSV. ΠΑΡΑΚΑΛΩ ΚΛΕΙΣΤΕ ΤΟ ΠΑΡΑΘΥΡΟ ΚΑΙ ΑΝΟΙΞΤΕ ΤΟ ΞΑΝΑ ΓΙΑ ΝΑ ΔΕΙΤΕ ΤΙΣ ΑΛΛΑΓΕΣ ",
                )
        except :
            
            QMessageBox.critical(
            self,
            "ΠΡΟΣΟΧΗ",
            f"ΔΕΝ ΥΠΑΡΧΕΙ BACKUP ARXEIO. ΠΑΤΗΣΤΕ BACKUP!! ΓΙΑ ΔΗΜΙΟΥΡΓΙΑ! ",
            )
            



if __name__ == '__main__':
    app = QApplication([])

    widget = Patients_Information()
    widget.show()
    app.exec_()
