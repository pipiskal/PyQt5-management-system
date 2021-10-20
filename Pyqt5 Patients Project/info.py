from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow_info(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200, 800)
        MainWindow.setStyleSheet("color: black ; font :italic ;")
       

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        

        MainWindow.setMinimumSize(QtCore.QSize(1200, 800))
        MainWindow.setDockNestingEnabled(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.history_label = QtWidgets.QLabel(self.centralwidget)
        self.history_label.setGeometry(QtCore.QRect(790, 100, 211, 300))
        self.history_label.setAlignment(QtCore.Qt.AlignCenter)
        self.history_label.setObjectName("history_label")

        self.search_first_name_label = QtWidgets.QLabel(self.centralwidget)
        self.search_first_name_label.setGeometry(QtCore.QRect(10, 10, 140, 31))
        self.search_first_name_label.setAlignment(QtCore.Qt.AlignCenter)
        self.search_first_name_label.setObjectName("search_first_name_label")

        self.search_last_name_label = QtWidgets.QLabel(self.centralwidget)
        self.search_last_name_label.setGeometry(QtCore.QRect(16, 60, 140, 31))
        self.search_last_name_label.setAlignment(QtCore.Qt.AlignCenter)
        self.search_last_name_label.setObjectName("search_last_name_label")

        self.search_amka_label = QtWidgets.QLabel(self.centralwidget)
        self.search_amka_label.setGeometry(QtCore.QRect(16, 10, 1300, 31))
        self.search_amka_label.setAlignment(QtCore.Qt.AlignCenter)
        self.search_amka_label.setObjectName("search_amka_label")

        self.search_phonenumber_label = QtWidgets.QLabel(self.centralwidget)
        self.search_phonenumber_label.setGeometry(QtCore.QRect(16, 60, 1328, 31))
        self.search_phonenumber_label.setAlignment(QtCore.Qt.AlignCenter)
        self.search_phonenumber_label.setObjectName("search_phonenumber_label")

        self.search_first_name_QLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.search_first_name_QLineEdit.setGeometry(QtCore.QRect(180, 10, 370, 31))
        self.search_first_name_QLineEdit.setObjectName("search_first_name_QLineEdit")

        self.search_last_name_QLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.search_last_name_QLineEdit.setGeometry(QtCore.QRect(180, 60, 370, 31))
        self.search_last_name_QLineEdit.setObjectName("search_last_name_QLineEdit")

        self.search_amka_QLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.search_amka_QLineEdit.setGeometry(QtCore.QRect(770, 10, 370, 31))
        self.search_amka_QLineEdit.setObjectName("search_amka_QLineEdit")

        self.search_phonenumber_QLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.search_phonenumber_QLineEdit.setGeometry(QtCore.QRect(770, 60, 370, 31))
        self.search_phonenumber_QLineEdit.setObjectName("search_phonenumber_QLineEdit")

        self.save_database_button = QtWidgets.QPushButton(self.centralwidget)
        self.save_database_button.setGeometry(QtCore.QRect(20, 750, 171, 31))
        self.save_database_button.setObjectName("save_database_button")

        self.delete_patient_button = QtWidgets.QPushButton(self.centralwidget)
        self.delete_patient_button.setGeometry(QtCore.QRect(20, 720, 171, 31))
        self.delete_patient_button.setObjectName("delete_patient_button")

        self.load_csv_file = QtWidgets.QPushButton(self.centralwidget)
        self.load_csv_file.setGeometry(QtCore.QRect(420, 720, 171, 31))
        self.load_csv_file.setObjectName("load_csv_file")


        self.create_new_allergy_test = QtWidgets.QPushButton(self.centralwidget)
        self.create_new_allergy_test.setGeometry(QtCore.QRect(420, 750, 171, 31))
        self.create_new_allergy_test.setObjectName("create_new_allergy_test")


        self.information_table = QtWidgets.QTableView(self.centralwidget)
        self.information_table.setGeometry(QtCore.QRect(20, 120, 575, 590))
        self.information_table.setObjectName("information_table")


        self.general_info_label = QtWidgets.QLabel(self.centralwidget)
        self.general_info_label.setGeometry(QtCore.QRect(170, 100, 251, 16))
        self.general_info_label.setAlignment(QtCore.Qt.AlignCenter)
        self.general_info_label.setObjectName("general_info_label")

        self.information_textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.information_textEdit.setGeometry(QtCore.QRect(600, 120, 575, 500))
        self.information_textEdit.setObjectName("information_textEdit")


        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ΠΡΟΓΡΑΜΜΑ ΔΙΑΧΕΙΡΙΣΗΣ ΑΣΘΕΝΩΝ"))
        self.history_label.setText(_translate("MainWindow", "ΠΛΗΡΟΦΟΡΙΕΣ ΙΣΤΟΡΙΚΟΥ"))
        # self.search_first_name_QLineEdit.setText(_translate("MainWindow", " "))
        self.save_database_button.setText(_translate("MainWindow", "BACKUP!!"))
        self.delete_patient_button.setText(_translate("MainWindow", "ΔΙΑΓΡΑΦΗ ΑΣΘΕΝΗ"))
        self.load_csv_file.setText(_translate("MainWindow", "LOAD BACKUP"))
        self.create_new_allergy_test.setText(_translate("MainWindow", "ΝΕΟ ΤΕΣΤ"))
        self.general_info_label.setText(_translate("MainWindow", "ΓΕΝΙΚΕΣ ΠΛΗΡΟΦΟΡΙΕΣ"))
        self.search_first_name_label.setText(_translate("MainWindow", "ΑΝΑΖΗΤΗΣΗ ΜΕ ΟΝΟΜΑ: "))
        self.search_last_name_label.setText(_translate("MainWindow", "ΑΝΑΖΗΤΗΣΗ ΜΕ ΕΠΩΝΥΜΟ: "))
        self.search_amka_label.setText(_translate("MainWindow", "ΑΝΑΖΗΤΗΣΗ ΜΕ ΑΜΚΑ: "))
        self.search_phonenumber_label.setText(_translate("MainWindow", "ΑΝΑΖΗΤΗΣΗ ΜΕ ΤΗΛΕΦΩΝΟ: "))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow_info()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
