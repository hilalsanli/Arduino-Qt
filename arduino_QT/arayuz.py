# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'arayuz.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1125, 863)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(290, 10, 561, 801))
        self.frame.setStyleSheet("QFrame{\n"
"background-image: url(:/icons/icons/800px_COLOURBOX3110535.jpg);\n"
"border-radius:20px;\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(10, 520, 541, 271))
        self.frame_2.setStyleSheet("QFrame{\n"
"background:rgb(8 ,126, 176);\n"
"}")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.txt_log_3 = QtWidgets.QTextBrowser(self.frame_2)
        self.txt_log_3.setGeometry(QtCore.QRect(10, 10, 521, 251))
        self.txt_log_3.setStyleSheet("QTextBrowser{\n"
"background-color:white;\n"
"}")
        self.txt_log_3.setObjectName("txt_log_3")
        self.btn_baglan = QtWidgets.QPushButton(self.frame)
        self.btn_baglan.setGeometry(QtCore.QRect(20, 40, 161, 61))
        self.btn_baglan.setStyleSheet("QPushButton{\n"
"color:white;\n"
"background:2px solid rgb(28 ,15, 69);\n"
"font-family:Times New Roman;\n"
"font-size:15px;\n"
"border-radius:10px;\n"
"border:2px solid #f2f2f2\n"
"}\n"
"QPushButton:hover{\n"
"background:rgb(250,0,0);\n"
"}")
        self.btn_baglan.setObjectName("btn_baglan")
        self.btn_baglan_8 = QtWidgets.QPushButton(self.frame)
        self.btn_baglan_8.setGeometry(QtCore.QRect(90, 380, 101, 51))
        self.btn_baglan_8.setStyleSheet("QPushButton{\n"
"color:white;\n"
"background:2px solid rgb(28 ,15, 69);\n"
"font-family:Times New Roman;\n"
"font-size:15px;\n"
"border-radius:10px;\n"
"border:2px solid #f2f2f2\n"
"}\n"
"")
        self.btn_baglan_8.setObjectName("btn_baglan_8")
        self.btn_baglanti_kes_3 = QtWidgets.QPushButton(self.frame)
        self.btn_baglanti_kes_3.setGeometry(QtCore.QRect(390, 40, 151, 61))
        self.btn_baglanti_kes_3.setStyleSheet("QPushButton{\n"
"color:white;\n"
"background:2px solid rgb(28 ,15, 69);\n"
"font-family:Times New Roman;\n"
"font-size:15px;\n"
"border-radius:10px;\n"
"border:2px solid #f2f2f2\n"
"}\n"
"QPushButton:hover{\n"
"background:rgb(250,0,0);\n"
"}")
        self.btn_baglanti_kes_3.setObjectName("btn_baglanti_kes_3")
        self.cmb_com_3 = QtWidgets.QComboBox(self.frame)
        self.cmb_com_3.setGeometry(QtCore.QRect(210, 380, 281, 51))
        self.cmb_com_3.setStyleSheet("QComboBox{\n"
"background:2px solid rgb(0,0,0);\n"
"\n"
"border-bottom:2px solid #f2f2f2\n"
"\n"
"border: none;\n"
"\n"
"\n"
"\n"
"}")
        self.cmb_com_3.setObjectName("cmb_com_3")
        self.btn_baglan_9 = QtWidgets.QPushButton(self.frame)
        self.btn_baglan_9.setGeometry(QtCore.QRect(90, 450, 101, 51))
        self.btn_baglan_9.setStyleSheet("QPushButton{\n"
"color:white;\n"
"background:2px solid rgb(28 ,15, 69);\n"
"font-family:Times New Roman;\n"
"font-size:15px;\n"
"border-radius:10px;\n"
"border:2px solid #f2f2f2\n"
"}\n"
"")
        self.btn_baglan_9.setObjectName("btn_baglan_9")
        self.cmb_baud_3 = QtWidgets.QComboBox(self.frame)
        self.cmb_baud_3.setGeometry(QtCore.QRect(210, 450, 281, 51))
        self.cmb_baud_3.setStyleSheet("QComboBox{\n"
"background:2px solid rgb(0,0,0);\n"
"\n"
"border-bottom:2px solid #f2f2f2\n"
"\n"
"border: none;\n"
"\n"
"\n"
"}")
        self.cmb_baud_3.setFrame(False)
        self.cmb_baud_3.setObjectName("cmb_baud_3")
        self.btn_kaydet_3 = QtWidgets.QPushButton(self.frame)
        self.btn_kaydet_3.setGeometry(QtCore.QRect(200, 40, 171, 61))
        self.btn_kaydet_3.setStyleSheet("QPushButton{\n"
"color:white;\n"
"background:2px solid rgb(28 ,15, 69);\n"
"font-family:Times New Roman;\n"
"font-size:15px;\n"
"border-radius:10px;\n"
"border:2px solid #f2f2f2\n"
"}\n"
"QPushButton:hover{\n"
"background:rgb(250,0,0);\n"
"}")
        self.btn_kaydet_3.setObjectName("btn_kaydet_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1125, 26))
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
        self.btn_baglan.setText(_translate("MainWindow", "BAĞLAN"))
        self.btn_baglan_8.setText(_translate("MainWindow", "COM"))
        self.btn_baglanti_kes_3.setText(_translate("MainWindow", "BAĞLANTI KES"))
        self.btn_baglan_9.setText(_translate("MainWindow", "BAUD"))
        self.btn_kaydet_3.setText(_translate("MainWindow", "KAYDET"))
import icons_rc