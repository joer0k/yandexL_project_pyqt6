# Form implementation generated from reading ui file '.\uis\log_in.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(535, 463)
        MainWindow.setMinimumSize(QtCore.QSize(535, 463))
        MainWindow.setMaximumSize(QtCore.QSize(535, 463))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("QWidget {\n"
                                 "    background-color: rgb(255, 255, 243);\n"
                                 "}\n"
                                 "QPushButton {\n"
                                 "    background-color: rgb(255, 254, 239);\n"
                                 "    border: None;\n"
                                 "    border-radius: 20px;\n"
                                 "}\n"
                                 "\n"
                                 "QPushButton:hover {\n"
                                 "    background-color: rgb(255, 236, 197)\n"
                                 "}\n"
                                 "\n"
                                 "QPushButton:pressed {\n"
                                 "    background-color: rgb(255, 254, 239);\n"
                                 "}\n"
                                 "\n"
                                 "QLineEdit {\n"
                                 "    background-color: rgb(255, 236, 197);\n"
                                 "    border-radius: 10px;\n"
                                 "}")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(230, 50, 81, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.edit_login = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.edit_login.setGeometry(QtCore.QRect(130, 140, 261, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        self.edit_login.setFont(font)
        self.edit_login.setStyleSheet("color: rgb(0, 0, 0)")
        self.edit_login.setText("")
        self.edit_login.setObjectName("edit_login")
        self.edit_passw = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.edit_passw.setGeometry(QtCore.QRect(130, 210, 261, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        self.edit_passw.setFont(font)
        self.edit_passw.setText("")
        self.edit_passw.setObjectName("edit_passw")
        self.log_in_btn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.log_in_btn.setGeometry(QtCore.QRect(190, 310, 141, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.log_in_btn.setFont(font)
        self.log_in_btn.setStyleSheet("")
        self.log_in_btn.setObjectName("log_in_btn")
        self.register_btn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.register_btn.setGeometry(QtCore.QRect(170, 360, 191, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.register_btn.setFont(font)
        self.register_btn.setStyleSheet("")
        self.register_btn.setObjectName("register_btn")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 260, 481, 20))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Вход"))
        self.label.setText(_translate("MainWindow", "Вход"))
        self.log_in_btn.setText(_translate("MainWindow", "Войти"))
        self.register_btn.setText(_translate("MainWindow", "Зарегистрироваться"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
