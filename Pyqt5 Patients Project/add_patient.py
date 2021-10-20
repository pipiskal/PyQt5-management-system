from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(572, 297)
        Dialog.setStyleSheet("background-color: #ffffff; color: black ; font :italic ;")
        self.ok_submit_button = QtWidgets.QPushButton(Dialog)
        self.ok_submit_button.setGeometry(QtCore.QRect(120, 240, 113, 32))
        self.ok_submit_button.setObjectName("ok_submit_button")
        self.cancel_button = QtWidgets.QPushButton(Dialog)
        self.cancel_button.setGeometry(QtCore.QRect(340, 240, 113, 32))
        self.cancel_button.setObjectName("cancel_button")
        self.first_name_label = QtWidgets.QLabel(Dialog)
        self.first_name_label.setGeometry(QtCore.QRect(40, 50, 131, 16))
        self.first_name_label.setObjectName("first_name_label")
        self.last_name_label = QtWidgets.QLabel(Dialog)
        self.last_name_label.setGeometry(QtCore.QRect(40, 80, 131, 16))
        self.last_name_label.setObjectName("last_name_label")
        self.phonenumber_label = QtWidgets.QLabel(Dialog)
        self.phonenumber_label.setGeometry(QtCore.QRect(40, 110, 121, 20))
        self.phonenumber_label.setObjectName("phonenumber_label")
        self.amka_label = QtWidgets.QLabel(Dialog)
        self.amka_label.setGeometry(QtCore.QRect(40, 140, 51, 16))
        self.amka_label.setObjectName("amka_label")
        self.email_label = QtWidgets.QLabel(Dialog)
        self.email_label.setGeometry(QtCore.QRect(40, 170, 131, 16))
        self.email_label.setObjectName("email_label")
        self.address_label = QtWidgets.QLabel(Dialog)
        self.address_label.setGeometry(QtCore.QRect(40, 200, 131, 16))
        self.address_label.setObjectName("address_label")
        self.first_name_lineEdit = QtWidgets.QLineEdit(Dialog)
        self.first_name_lineEdit.setGeometry(QtCore.QRect(200, 50, 301, 21))
        self.first_name_lineEdit.setObjectName("ONOMA")
        self.last_name_lineEdit = QtWidgets.QLineEdit(Dialog)
        self.last_name_lineEdit.setGeometry(QtCore.QRect(200, 80, 301, 21))
        self.last_name_lineEdit.setObjectName("ΕΠΩΝΥΜΟ")
        self.phonenumber_lineEdit = QtWidgets.QLineEdit(Dialog)
        self.phonenumber_lineEdit.setGeometry(QtCore.QRect(200, 110, 301, 21))
        self.phonenumber_lineEdit.setObjectName("ΤΗΛΕΦΩΝΟ")
        self.amka_lineEdit = QtWidgets.QLineEdit(Dialog)
        self.amka_lineEdit.setGeometry(QtCore.QRect(200, 140, 301, 21))
        self.amka_lineEdit.setObjectName("ΑΜΚΑ")
        self.email_lineEdit = QtWidgets.QLineEdit(Dialog)
        self.email_lineEdit.setGeometry(QtCore.QRect(200, 170, 301, 21))
        self.email_lineEdit.setObjectName("EMAIL")
        self.address_lineEdit = QtWidgets.QLineEdit(Dialog)
        self.address_lineEdit.setGeometry(QtCore.QRect(200, 200, 301, 21))
        self.address_lineEdit.setObjectName("ΔΙΕΥΘΥΝΣΗ")


        self.add_patient_label = QtWidgets.QLabel(Dialog)
        self.add_patient_label.setGeometry(QtCore.QRect(155, 10, 260, 16))
        self.add_patient_label.setAlignment(QtCore.Qt.AlignCenter)
        self.add_patient_label.setObjectName("add_patient_label")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.ok_submit_button.setText(_translate("Dialog", "OK"))
        self.cancel_button.setText(_translate("Dialog", "ΑΚΥΡΩΣΗ"))
        self.first_name_label.setText(_translate("Dialog", "* ΟΝΟΜΑ ΑΣΘΕΝΗ:"))
        self.last_name_label.setText(_translate("Dialog", "* ΕΠΩΝΥΜΟ ΑΣΘΕΝΗ:"))
        self.phonenumber_label.setText(_translate("Dialog", "* ΤΗΛΕΦΩΝΟ:"))
        self.amka_label.setText(_translate("Dialog", "ΑΜΚΑ :"))
        self.email_label.setText(_translate("Dialog", "Email: "))
        self.address_label.setText(_translate("Dialog", "ΔΙΕΥΘΥΝΣΗ: "))

        self.add_patient_label.setText(_translate("Dialog", "ΠΡΟΣΘΗΚΗ ΝΕΟΥ ΑΣΘΕΝΗ (*Υποχρεωτικό πεδίο)"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
