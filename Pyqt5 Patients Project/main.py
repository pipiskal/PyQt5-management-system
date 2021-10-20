from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(643, 503)
        MainWindow.setStyleSheet("background-color: #ffffff; color: black ; font :italic ;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.dateTimeEdit = QtWidgets.QDateTimeEdit(self.centralwidget)
        self.dateTimeEdit.setGeometry(QtCore.QRect(10, 430, 194, 24))
        self.dateTimeEdit.setObjectName("dateTimeEdit")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(140, 120, 381, 211))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.view_patients_info_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.view_patients_info_button.setObjectName("view_patients_info_button")
        self.verticalLayout.addWidget(self.view_patients_info_button)
        self.add_patient_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.add_patient_button.setObjectName("add_patient_button")
        self.verticalLayout.addWidget(self.add_patient_button)
        self.appointment_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.appointment_button.setObjectName("appointment_button")
        self.verticalLayout.addWidget(self.appointment_button)
        self.title_label = QtWidgets.QLabel(self.centralwidget)
        self.title_label.setGeometry(QtCore.QRect(120, 60, 411, 41))
        self.title_label.setTextFormat(QtCore.Qt.AutoText)
        self.title_label.setAlignment(QtCore.Qt.AlignCenter)
        self.title_label.setObjectName("title_label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 643, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.view_patients_info_button.setText(_translate("MainWindow", "ΠΛΗΡΟΦΟΡΙΕΣ ΑΣΘΕΝΩΝ"))
        self.add_patient_button.setText(_translate("MainWindow", "ΠΡΟΣΘΗΚΗ ΝΕΟΥ ΑΣΘΕΝΗ"))
        self.appointment_button.setText(_translate("MainWindow", "ΡΑΝΤΕΒΟΥ"))
        self.title_label.setText(_translate("MainWindow", "ΑΛΛΕΡΓΙΟΛΟΓΙΚΟ ΠΡΟΓΡΑΜΜΑ ΔΙΑΧΕΙΡΙΣΗΣ ΠΕΛΑΤΩΝ"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
