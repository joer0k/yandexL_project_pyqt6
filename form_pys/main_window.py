# Form implementation generated from reading ui file '.\uis\main_window.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 600)
        MainWindow.setMinimumSize(QtCore.QSize(1000, 600))
        MainWindow.setMaximumSize(QtCore.QSize(1000, 600))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("QWidget {\n"
"    background-color: rgb(255, 255, 243);\n"
"}\n"
"\n"
"\n"
"QPushButton {\n"
"    font-family: Segoe UI;\n"
"    color: rgb(119, 192, 255);\n"
"    border: none;\n"
"    border-radius: 10px;\n"
"    font-size: 14px;\n"
"    font-weight: 500;\n"
"    font-variant: small-caps;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgba(255, 227, 192, 0.5);\n"
"    color: rgb(67, 63, 58);\n"
"}\n"
"\n"
"QPushButton#btn_find {\n"
"    font-size: 20px;\n"
"    font-weight: 600;\n"
"    background-color: rgb(255, 226, 163);\n"
"    color: black;\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton#btn_find:hover{\n"
"    background-color: rgb(255, 232, 190);\n"
"}\n"
"QLineEdit {\n"
"    font-family: Segoe UI;\n"
"    border-radius: 5px;\n"
"    background-color: white;\n"
"}\n"
"QLabel#label {\n"
"    font-family: Segoe UI;\n"
"    font-size: 26px;\n"
"}\n"
"\n"
"\n"
"QPushButton#btn_arrive{\n"
"    background-color: white;\n"
"    border: none;\n"
"    color: black;\n"
"    font-variant: normal;\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton#btn_deport{\n"
"    background-color: white;\n"
"    border: none;\n"
"    border-radius: 0px;\n"
"    color: black;\n"
"    font-variant: normal;\n"
"    border-radius: 5px;\n"
"}\n"
"QMenuBar{\n"
"    background-color:transparent;\n"
"}\n"
"QLabel#label_errors {\n"
"    font-size: 16px;\n"
"    font-weight: 600;\n"
"}\n"
"\n"
"QLabel#label_photo {\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QLabel#label_2 {\n"
"    background-color: rgb(255, 248, 223);\n"
"    border-radius: 20px;\n"
"}\n"
"\n"
"QLabel#label_errors {\n"
"    background-color: transparent;\n"
"}\n"
"QPushButton#btn_add_hotel {\n"
"    background-color: rgb(255, 226, 163);\n"
"    color: black;\n"
"}\n"
"QPushButton#btn_profile {\n"
"    background-color: rgb(255, 226, 163);\n"
"    color: black;\n"
"}\n"
"QPushButton#btn_num_people {\n"
"    background-color: white;\n"
"    border: none;\n"
"    color: black;\n"
"    font-size: 12px;\n"
"    font-variant: normal;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QLabel#label_photo {\n"
"    border-radius: 25px;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btn_profile = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btn_profile.setGeometry(QtCore.QRect(640, 10, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(62)
        self.btn_profile.setFont(font)
        self.btn_profile.setObjectName("btn_profile")
        self.label_photo = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_photo.setGeometry(QtCore.QRect(830, 0, 80, 80))
        self.label_photo.setText("")
        self.label_photo.setObjectName("label_photo")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(260, 130, 461, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(-1)
        self.label.setFont(font)
        self.label.setStyleSheet("color: black;")
        self.label.setObjectName("label")
        self.location = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.location.setGeometry(QtCore.QRect(50, 200, 201, 51))
        self.location.setObjectName("location")
        self.label_errors = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_errors.setGeometry(QtCore.QRect(130, 270, 741, 71))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.label_errors.setFont(font)
        self.label_errors.setObjectName("label_errors")
        self.btn_find = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btn_find.setGeometry(QtCore.QRect(780, 200, 161, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.btn_find.setFont(font)
        self.btn_find.setObjectName("btn_find")
        self.btn_arrive = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btn_arrive.setGeometry(QtCore.QRect(260, 200, 151, 51))
        self.btn_arrive.setObjectName("btn_arrive")
        self.btn_deport = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btn_deport.setGeometry(QtCore.QRect(420, 200, 151, 51))
        self.btn_deport.setObjectName("btn_deport")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 190, 981, 161))
        self.label_2.setAutoFillBackground(False)
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.btn_num_people = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btn_num_people.setGeometry(QtCore.QRect(580, 200, 191, 51))
        self.btn_num_people.setObjectName("btn_num_people")
        self.lbl_logo = QtWidgets.QLabel(parent=self.centralwidget)
        self.lbl_logo.setGeometry(QtCore.QRect(20, 10, 311, 171))
        self.lbl_logo.setText("")
        self.lbl_logo.setObjectName("lbl_logo")
        self.label_2.raise_()
        self.btn_profile.raise_()
        self.label_photo.raise_()
        self.label.raise_()
        self.location.raise_()
        self.label_errors.raise_()
        self.btn_find.raise_()
        self.btn_arrive.raise_()
        self.btn_deport.raise_()
        self.btn_num_people.raise_()
        self.lbl_logo.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "BookHotel"))
        self.btn_profile.setText(_translate("MainWindow", "Мой профиль"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Куда вы хотите поехать?</p></body></html>"))
        self.location.setPlaceholderText(_translate("MainWindow", "Город"))
        self.label_errors.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.btn_find.setText(_translate("MainWindow", "Найти"))
        self.btn_arrive.setText(_translate("MainWindow", "Дата заезда"))
        self.btn_deport.setText(_translate("MainWindow", "Дата отъезда"))
        self.btn_num_people.setText(_translate("MainWindow", "1 взрослый, 1 ребенок, 1 номер"))
