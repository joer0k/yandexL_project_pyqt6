# Form implementation generated from reading ui file '.\uis\list_hotels.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(714, 563)
        Form.setWindowTitle("")
        Form.setStyleSheet("QWidget {\n"
"    background-color: rgb(255, 255, 243);\n"
"}\n"
"QScrollBar:vertical {\n"
"    boder: none;\n"
"    background-color:rgb(255, 241, 203);\n"
"    width: 14px;\n"
"    margin: 15px 0 15px 0;\n"
"    boder-radius: 0px;\n"
"}\n"
"QScrollBar::handle:vertical {\n"
"    background-color: rgb(255, 198, 156);\n"
"    min-height: 30px;\n"
"    border-radius: 7px;\n"
"}\n"
"QScrollBar::handle:vertical:hover {\n"
"    background-color: rgb(255, 136, 112)\n"
"}\n"
"QScrollBar::handle:vertical:pressed {\n"
"    background-color: rgb(255, 184, 121)\n"
"}\n"
"\n"
"\n"
"\n"
"QScrollBar::sub-line:vertical {\n"
"    border: none;\n"
"    background-color:rgb(255, 241, 203);\n"
"    height: 15px;\n"
"    border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:vertical:hover {\n"
"    background-color: rgb(255, 136, 112);\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical:pressed {\n"
"    background-color: rgb(255, 184, 121)\n"
"}\n"
"\n"
"\n"
"\n"
"QScrollBar::add-line:vertical {\n"
"    border: none;\n"
"    background-color:rgb(255, 241, 203);\n"
"    height: 15px;\n"
"    border-bottom-left-radius: 7px;\n"
"    border-bottom-right-radius: 7px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::add-line:vertical:hover {\n"
"    background-color: rgb(255, 136, 112);\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical:pressed {\n"
"    background-color: rgb(255, 184, 121)\n"
"}\n"
"\n"
"\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"    background: none;\n"
"}\n"
"\n"
"\n"
"\n"
"QScrollBar::add-page:vertical, QScrollBar:sub-page:vertical {\n"
"    background: none;\n"
"}\n"
"\n"
"\n"
"\n"
"QScrollBar:horizontal {\n"
"    boder: none;\n"
"    background-color:rgb(255, 241, 203);\n"
"    width: 14px;\n"
"    margin: 15px 0 15px 0;\n"
"    boder-radius: 0px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background-color: rgb(255, 198, 156);\n"
"    min-height: 30px;\n"
"    border-radius: 7px;\n"
"}\n"
"QScrollBar::handle:horizontal:hover {\n"
"    background-color: rgb(255, 136, 112)\n"
"}\n"
"QScrollBar::handle:horizontal:pressed {\n"
"    background-color: rgb(255, 184, 121)\n"
"}\n"
"\n"
"\n"
"\n"
"QScrollBar::sub-line:horizontal {\n"
"    border: none;\n"
"    background-color:rgb(255, 241, 203);\n"
"    height: 15px;\n"
"    border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:horizontal:hover {\n"
"    background-color: rgb(255, 136, 112);\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal:pressed {\n"
"    background-color: rgb(255, 184, 121)\n"
"}\n"
"\n"
"\n"
"\n"
"QScrollBar::add-line:horizontal {\n"
"    border: none;\n"
"    background-color:rgb(255, 241, 203);\n"
"    height: 15px;\n"
"    border-bottom-left-radius: 7px;\n"
"    border-bottom-right-radius: 7px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::add-line:horizontal:hover {\n"
"    background-color: rgb(255, 136, 112);\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal:pressed {\n"
"    background-color: rgb(255, 184, 121)\n"
"}\n"
"\n"
"\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal {\n"
"    background: none;\n"
"}\n"
"\n"
"\n"
"\n"
"QScrollBar::add-page:horizontal, QScrollBar:sub-page:horizontal {\n"
"    background: none;\n"
"}\n"
"\n"
"\n"
"QLabel {\n"
"    font-size: 20px;\n"
"    font-family: Segoe UI;\n"
"    font-weight: 500;\n"
"}\n"
"\n"
"QPushButton {\n"
"    font-family: Segoe UI;\n"
"    color: black;\n"
"    border: none;\n"
"    border-radius: 10px;\n"
"    font-size: 14px;\n"
"    font-weight: 500;\n"
"    font-variant: small-caps;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(255, 226, 163)\n"
"}\n"
"QPlainTextEdit{\n"
"    font-family: Segoe UI;\n"
"    font-size: 16px;\n"
"}")
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.scrollArea = QtWidgets.QScrollArea(parent=Form)
        self.scrollArea.setStyleSheet("")
        self.scrollArea.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1218, 1218))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame = QtWidgets.QFrame(parent=self.scrollAreaWidgetContents)
        self.frame.setMinimumSize(QtCore.QSize(1200, 1200))
        self.frame.setStyleSheet("")
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.label_amount = QtWidgets.QLabel(parent=self.frame)
        self.label_amount.setGeometry(QtCore.QRect(60, 0, 671, 31))
        self.label_amount.setObjectName("label_amount")
        self.verticalLayout_2.addWidget(self.frame)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        self.label_amount.setText(_translate("Form", "Найдено  отелей"))
