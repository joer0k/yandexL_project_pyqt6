# Form implementation generated from reading ui file '.\uis\dialog_change_profile.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(340, 240)
        Dialog.setStyleSheet("QDialog {\n"
"    background-color: rgb(255, 255, 243);\n"
"}\n"
"\n"
"QLabel {\n"
"    font-family: Segoe UI;\n"
"    background-color:rgba(255, 241, 203, 0.8);\n"
"}\n"
"\n"
"QLineEdit {\n"
"    background-color: rgb(255, 236, 197);\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton{\n"
"    background-color: transparent;\n"
"    font-family: Segoe UI;\n"
"    font-size: 16px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color:rgba(255, 226, 163, 0.8)\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: rgb(240, 213, 154)\n"
"}")
        self.buttonBox = QtWidgets.QDialogButtonBox(parent=Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(10, 200, 301, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.StandardButton.Cancel|QtWidgets.QDialogButtonBox.StandardButton.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtWidgets.QLabel(parent=Dialog)
        self.label.setGeometry(QtCore.QRect(10, 30, 161, 31))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=Dialog)
        self.label_2.setGeometry(QtCore.QRect(10, 90, 161, 31))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=Dialog)
        self.label_3.setGeometry(QtCore.QRect(10, 150, 161, 31))
        self.label_3.setObjectName("label_3")
        self.edit_fio = QtWidgets.QLineEdit(parent=Dialog)
        self.edit_fio.setGeometry(QtCore.QRect(180, 30, 141, 31))
        self.edit_fio.setObjectName("edit_fio")
        self.edit_phone = QtWidgets.QLineEdit(parent=Dialog)
        self.edit_phone.setGeometry(QtCore.QRect(180, 90, 141, 31))
        self.edit_phone.setObjectName("edit_phone")
        self.edit_mail = QtWidgets.QLineEdit(parent=Dialog)
        self.edit_mail.setGeometry(QtCore.QRect(180, 150, 141, 31))
        self.edit_mail.setObjectName("edit_mail")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept) # type: ignore
        self.buttonBox.rejected.connect(Dialog.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Заполните данные"))
        self.label.setText(_translate("Dialog", "Введите фамилию, имя"))
        self.label_2.setText(_translate("Dialog", "Введите номер телефона"))
        self.label_3.setText(_translate("Dialog", "Введите электронную почту"))
