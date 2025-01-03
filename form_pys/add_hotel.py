# Form implementation generated from reading ui file '.\add_hotel.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(384, 564)
        Form.setStyleSheet("QWidget {\n"
"    background-color: rgb(255, 255, 243);\n"
"}\n"
"QLabel {\n"
"    font-family: Segoe UI;\n"
"    font-size: 16px;\n"
"    font-weight: 500;\n"
"}\n"
"\n"
"QLineEdit {\n"
"    border:none;\n"
"    border-radius: 5px;\n"
"    background-color: rgb(255, 236, 197);\n"
"}\n"
"\n"
"QPushButton#btn_photo {\n"
"    font-size: 14px;\n"
"    font-family: Segoe UI;\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(255, 236, 197);\n"
"    font-weight: 500;\n"
"}")
        self.label = QtWidgets.QLabel(parent=Form)
        self.label.setGeometry(QtCore.QRect(90, 30, 191, 41))
        self.label.setObjectName("label")
        self.edit_name = QtWidgets.QLineEdit(parent=Form)
        self.edit_name.setGeometry(QtCore.QRect(60, 90, 251, 41))
        self.edit_name.setObjectName("edit_name")
        self.label_2 = QtWidgets.QLabel(parent=Form)
        self.label_2.setGeometry(QtCore.QRect(80, 140, 201, 21))
        self.label_2.setObjectName("label_2")
        self.textEdit = QtWidgets.QTextEdit(parent=Form)
        self.textEdit.setGeometry(QtCore.QRect(20, 320, 331, 111))
        self.textEdit.setObjectName("textEdit")
        self.label_3 = QtWidgets.QLabel(parent=Form)
        self.label_3.setGeometry(QtCore.QRect(100, 290, 161, 20))
        self.label_3.setObjectName("label_3")
        self.edit_country = QtWidgets.QLineEdit(parent=Form)
        self.edit_country.setGeometry(QtCore.QRect(20, 190, 158, 31))
        self.edit_country.setObjectName("edit_country")
        self.edit_strt = QtWidgets.QLineEdit(parent=Form)
        self.edit_strt.setGeometry(QtCore.QRect(20, 230, 158, 31))
        self.edit_strt.setObjectName("edit_strt")
        self.edit_city = QtWidgets.QLineEdit(parent=Form)
        self.edit_city.setGeometry(QtCore.QRect(200, 190, 158, 31))
        self.edit_city.setObjectName("edit_city")
        self.edit_house = QtWidgets.QLineEdit(parent=Form)
        self.edit_house.setGeometry(QtCore.QRect(200, 230, 158, 31))
        self.edit_house.setObjectName("edit_house")
        self.btn_photo = QtWidgets.QPushButton(parent=Form)
        self.btn_photo.setGeometry(QtCore.QRect(60, 440, 261, 41))
        self.btn_photo.setObjectName("btn_photo")
        self.buttonBox = QtWidgets.QDialogButtonBox(parent=Form)
        self.buttonBox.setGeometry(QtCore.QRect(110, 500, 158, 23))
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.StandardButton.Cancel|QtWidgets.QDialogButtonBox.StandardButton.Ok)
        self.buttonBox.setObjectName("buttonBox")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Добавление отеля"))
        self.label.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Добавление отеля</span></p></body></html>"))
        self.edit_name.setPlaceholderText(_translate("Form", "Название"))
        self.label_2.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Расположение</span></p></body></html>"))
        self.label_3.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Описание</span></p></body></html>"))
        self.edit_country.setPlaceholderText(_translate("Form", "Страна"))
        self.edit_strt.setPlaceholderText(_translate("Form", "Улица"))
        self.edit_city.setPlaceholderText(_translate("Form", "Город"))
        self.edit_house.setPlaceholderText(_translate("Form", "Дом"))
        self.btn_photo.setText(_translate("Form", "+ Прикрепить фото"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())
