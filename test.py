# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(790, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(70, 200, 401, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_7 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_7.setObjectName("pushButton_7")
        self.horizontalLayout_2.addWidget(self.pushButton_7)
        self.pushButton_10 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_10.setObjectName("pushButton_10")
        self.horizontalLayout_2.addWidget(self.pushButton_10)
        self.pushButton_8 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_8.setObjectName("pushButton_8")
        self.horizontalLayout_2.addWidget(self.pushButton_8)
        self.pushButton_6 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_6.setObjectName("pushButton_6")
        self.horizontalLayout_2.addWidget(self.pushButton_6)
        self.pushButton_9 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_9.setObjectName("pushButton_9")
        self.horizontalLayout_2.addWidget(self.pushButton_9)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(70, 290, 195, 80))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.toolButton_2 = QtWidgets.QToolButton(self.horizontalLayoutWidget_2)
        self.toolButton_2.setObjectName("toolButton_2")
        self.horizontalLayout_3.addWidget(self.toolButton_2)
        self.toolButton_3 = QtWidgets.QToolButton(self.horizontalLayoutWidget_2)
        self.toolButton_3.setObjectName("toolButton_3")
        self.horizontalLayout_3.addWidget(self.toolButton_3)
        self.toolButton = QtWidgets.QToolButton(self.horizontalLayoutWidget_2)
        self.toolButton.setObjectName("toolButton")
        self.horizontalLayout_3.addWidget(self.toolButton)
        self.textEdit = QtWidgets.QTextEdit(self.horizontalLayoutWidget_2)
        self.textEdit.setObjectName("textEdit")
        self.horizontalLayout_3.addWidget(self.textEdit)
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(80, 400, 160, 97))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton_11 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_11.setObjectName("pushButton_11")
        self.verticalLayout.addWidget(self.pushButton_11)
        self.toolButton_5 = QtWidgets.QToolButton(self.verticalLayoutWidget)
        self.toolButton_5.setObjectName("toolButton_5")
        self.verticalLayout.addWidget(self.toolButton_5)
        self.toolButton_6 = QtWidgets.QToolButton(self.verticalLayoutWidget)
        self.toolButton_6.setObjectName("toolButton_6")
        self.verticalLayout.addWidget(self.toolButton_6)
        self.toolButton_4 = QtWidgets.QToolButton(self.verticalLayoutWidget)
        self.toolButton_4.setObjectName("toolButton_4")
        self.verticalLayout.addWidget(self.toolButton_4)
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(70, 100, 401, 25))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.widget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.widget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout.addWidget(self.pushButton_3)
        self.pushButton_4 = QtWidgets.QPushButton(self.widget)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout.addWidget(self.pushButton_4)
        self.pushButton_5 = QtWidgets.QPushButton(self.widget)
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout.addWidget(self.pushButton_5)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 790, 22))
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
        self.pushButton_7.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_10.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_8.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_6.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_9.setText(_translate("MainWindow", "PushButton"))
        self.toolButton_2.setText(_translate("MainWindow", "..."))
        self.toolButton_3.setText(_translate("MainWindow", "..."))
        self.toolButton.setText(_translate("MainWindow", "..."))
        self.pushButton_11.setText(_translate("MainWindow", "PushButton"))
        self.toolButton_5.setText(_translate("MainWindow", "..."))
        self.toolButton_6.setText(_translate("MainWindow", "..."))
        self.toolButton_4.setText(_translate("MainWindow", "..."))
        self.pushButton.setText(_translate("MainWindow", "Button1"))
        self.pushButton_2.setText(_translate("MainWindow", "Button2"))
        self.pushButton_3.setText(_translate("MainWindow", "Button3"))
        self.pushButton_4.setText(_translate("MainWindow", "Button4"))
        self.pushButton_5.setText(_translate("MainWindow", "Button5"))
