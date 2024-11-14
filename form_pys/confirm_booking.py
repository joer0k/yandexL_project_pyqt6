# Form implementation generated from reading ui file '.\uis\conrirm_booking.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(654, 370)
        Form.setStyleSheet("QWidget {\n"
"    background-color: rgb(255, 255, 243);\n"
"}\n"
"QLabel {\n"
"    font-family: Segoe UI;\n"
"    font-size: 14px;\n"
"}\n"
"QLabel#label_4 {\n"
"    font-size: 16px;\n"
"    font-weight:500;\n"
"    background-color: rgba(255, 236, 197, 0.5);\n"
"    border-radius:5px;\n"
"}\n"
"QLineEdit {\n"
"    background-color:rgb(255, 236, 197);\n"
"    border:none;\n"
"    border-radius: 8px;\n"
"    font-size: 13px;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(255, 236, 197);\n"
"    font-weight: 500;\n"
"}")
        self.buttonBox = QtWidgets.QDialogButtonBox(parent=Form)
        self.buttonBox.setGeometry(QtCore.QRect(260, 330, 156, 23))
        self.buttonBox.setStyleSheet("")
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.StandardButton.Cancel|QtWidgets.QDialogButtonBox.StandardButton.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label_4 = QtWidgets.QLabel(parent=Form)
        self.label_4.setGeometry(QtCore.QRect(20, 10, 311, 51))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(parent=Form)
        self.label_5.setGeometry(QtCore.QRect(30, 70, 101, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(parent=Form)
        self.label_6.setGeometry(QtCore.QRect(240, 70, 101, 16))
        self.label_6.setObjectName("label_6")
        self.lbl_arrive = QtWidgets.QLabel(parent=Form)
        self.lbl_arrive.setGeometry(QtCore.QRect(20, 100, 141, 51))
        self.lbl_arrive.setStyleSheet("font-weight:500;\n"
"background-color: rgba(255, 236, 197, 0.5);\n"
"border-radius:5px;")
        self.lbl_arrive.setObjectName("lbl_arrive")
        self.lbl_depart = QtWidgets.QLabel(parent=Form)
        self.lbl_depart.setGeometry(QtCore.QRect(210, 100, 141, 51))
        self.lbl_depart.setStyleSheet("font-weight:500;\n"
"background-color: rgba(255, 236, 197, 0.5);\n"
"border-radius:5px;")
        self.lbl_depart.setObjectName("lbl_depart")
        self.label_7 = QtWidgets.QLabel(parent=Form)
        self.label_7.setGeometry(QtCore.QRect(20, 180, 161, 41))
        self.label_7.setStyleSheet("font-weight: 600;\n"
"font-size: 18px;")
        self.label_7.setObjectName("label_7")
        self.lbl_cost = QtWidgets.QLabel(parent=Form)
        self.lbl_cost.setGeometry(QtCore.QRect(210, 180, 131, 41))
        self.lbl_cost.setStyleSheet("font-weight: 600;\n"
"font-size: 18px;\n"
"background-color: rgba(255, 236, 197, 0.5);\n"
"border-radius:5px;")
        self.lbl_cost.setObjectName("lbl_cost")
        self.label = QtWidgets.QLabel(parent=Form)
        self.label.setGeometry(QtCore.QRect(370, 6, 267, 41))
        self.label.setObjectName("label")
        self.edit_FIO = QtWidgets.QLineEdit(parent=Form)
        self.edit_FIO.setGeometry(QtCore.QRect(370, 55, 267, 31))
        self.edit_FIO.setObjectName("edit_FIO")
        self.edit_phone = QtWidgets.QLineEdit(parent=Form)
        self.edit_phone.setGeometry(QtCore.QRect(370, 265, 267, 31))
        self.edit_phone.setObjectName("edit_phone")
        self.label_2 = QtWidgets.QLabel(parent=Form)
        self.label_2.setGeometry(QtCore.QRect(370, 200, 267, 41))
        self.label_2.setObjectName("label_2")
        self.edit_email = QtWidgets.QLineEdit(parent=Form)
        self.edit_email.setGeometry(QtCore.QRect(370, 154, 267, 31))
        self.edit_email.setObjectName("edit_email")
        self.label_3 = QtWidgets.QLabel(parent=Form)
        self.label_3.setGeometry(QtCore.QRect(370, 90, 267, 41))
        self.label_3.setObjectName("label_3")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Оформление брони"))
        self.label_4.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Детали бронирования</span></p></body></html>"))
        self.label_5.setText(_translate("Form", "Заезд"))
        self.label_6.setText(_translate("Form", "Отъезд"))
        self.lbl_arrive.setText(_translate("Form", "13.10.2024"))
        self.lbl_depart.setText(_translate("Form", "19.10.2024"))
        self.label_7.setText(_translate("Form", "Цена"))
        self.lbl_cost.setText(_translate("Form", "37800"))
        self.label.setText(_translate("Form", "Введите фамилию и имя"))
        self.label_2.setText(_translate("Form", "Введите телефон"))
        self.label_3.setText(_translate("Form", "Введите почту"))
