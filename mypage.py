# -*- coding: utf-8 -*-


"""
    此文件为GUI可视化界面定义文件
"""

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QMessageBox
from PIL import Image
import cv2

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1057, 958)
        self.tabWidget = QtWidgets.QTabWidget(Form)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 1071, 961))
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(12)
        self.tabWidget.setFont(font)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setStyleSheet("background: rgb(238, 233, 233)")
        self.tab.setObjectName("tab")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(20, 20, 221, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.tab)
        self.pushButton.setGeometry(QtCore.QRect(270, 10, 441, 28))
        self.pushButton.setStyleSheet("")
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(self.tab)
        self.lineEdit.setGeometry(QtCore.QRect(270, 50, 761, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit.setFont(font)
        self.lineEdit.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(20, 120, 221, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.textEdit = QtWidgets.QTextEdit(self.tab)
        self.textEdit.setGeometry(QtCore.QRect(270, 90, 761, 141))
        self.textEdit.setObjectName("textEdit")
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setGeometry(QtCore.QRect(10, 280, 221, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.pushButton_2 = QtWidgets.QPushButton(self.tab)
        self.pushButton_2.setGeometry(QtCore.QRect(270, 280, 441, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.tab)
        self.pushButton_3.setGeometry(QtCore.QRect(380, 425, 261, 51))
        self.pushButton_3.setObjectName("pushButton_3")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_2.setGeometry(QtCore.QRect(270, 320, 761, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_5 = QtWidgets.QLabel(self.tab)
        self.label_5.setGeometry(QtCore.QRect(20, 370, 270, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.comboBox_1 = QtWidgets.QComboBox(self.tab)
        self.comboBox_1.setObjectName("comboBox_1")
        self.comboBox_1.setGeometry(QtCore.QRect(270, 370, 400, 41))
        self.comboBox_1.addItem("")
        self.comboBox_1.addItem("")
        self.comboBox_1.addItem("")

        self.label_37 = QtWidgets.QLabel(self.tab)
        self.label_37.setGeometry(QtCore.QRect(700, 370, 240, 41))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_37.setFont(font)
        self.label_37.setStyleSheet("color:red")
        self.label_37.setObjectName("label_37")


        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboBox_1.setFont(font)
        self.comboBox_1.setDisabled(True)

        self.label_7 = QtWidgets.QLabel(self.tab)
        self.label_7.setGeometry(QtCore.QRect(190, 470, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.tab)
        self.label_8.setGeometry(QtCore.QRect(740, 470, 91, 33))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.pushButton_6 = QtWidgets.QPushButton(self.tab)
        self.pushButton_6.setGeometry(QtCore.QRect(760, 10, 271, 28))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.tab)
        self.pushButton_7.setGeometry(QtCore.QRect(780, 280, 251, 31))
        self.pushButton_7.setObjectName("pushButton_7")
        self.label_10 = QtWidgets.QLabel(self.tab)
        self.label_10.setGeometry(QtCore.QRect(20, 240, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_6.setGeometry(QtCore.QRect(270, 240, 321, 31))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.label_25 = QtWidgets.QLabel(self.tab)
        self.label_25.setGeometry(QtCore.QRect(10, 510, 491, 401))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_25.setFont(font)
        self.label_25.setFrameShape(QtWidgets.QFrame.Box)
        self.label_25.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_25.setLineWidth(3)
        self.label_25.setStyleSheet("border-color: rgb(0, 0, 0);\n"
"background-color: #fafafa;")
        self.label_25.setObjectName("label_25")
        self.label_26 = QtWidgets.QLabel(self.tab)
        self.label_26.setGeometry(QtCore.QRect(530, 510, 511, 401))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_26.setFont(font)
        self.label_26.setFrameShape(QtWidgets.QFrame.Box)
        self.label_26.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_26.setLineWidth(3)
        self.label_26.setStyleSheet("border-color: rgb(0, 0, 0);\n"
"background-color: #fafafa;")
        self.label_26.setObjectName("label_26")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setStyleSheet("background: rgb(238, 233, 233)")
        self.tab_2.setObjectName("tab_2")
        self.label_4 = QtWidgets.QLabel(self.tab_2)
        self.label_4.setGeometry(QtCore.QRect(20, 30, 221, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.pushButton_4 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_4.setGeometry(QtCore.QRect(270, 10, 441, 28))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_5.setGeometry(QtCore.QRect(370, 170, 301, 41))
        self.pushButton_5.setObjectName("pushButton_5")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_3.setGeometry(QtCore.QRect(270, 50, 761, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_6 = QtWidgets.QLabel(self.tab_2)
        self.label_6.setGeometry(QtCore.QRect(20, 100, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")

        self.label_9 = QtWidgets.QLabel(self.tab_2)
        self.label_9.setGeometry(QtCore.QRect(700, 110, 220, 41))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_9.setStyleSheet("color:red")
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")

        self.comboBox_2 = QtWidgets.QComboBox(self.tab_2)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.setGeometry(QtCore.QRect(270, 110, 400, 41))
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboBox_2.setFont(font)
        self.comboBox_2.setDisabled(True)
        self.pushButton_9 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_9.setGeometry(QtCore.QRect(760, 10, 271, 28))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setObjectName("pushButton_9")
        self.label_11 = QtWidgets.QLabel(self.tab_2)
        self.label_11.setGeometry(QtCore.QRect(70, 170, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.tab_2)
        self.label_12.setGeometry(QtCore.QRect(230, 230, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.tab_2)
        self.label_13.setGeometry(QtCore.QRect(780, 230, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.textEdit_2 = QtWidgets.QTextEdit(self.tab_2)
        self.textEdit_2.setGeometry(QtCore.QRect(650, 260, 381, 631))
        self.textEdit_2.setObjectName("textEdit_2")
        self.label_27 = QtWidgets.QLabel(self.tab_2)
        self.label_27.setGeometry(QtCore.QRect(10, 260, 621, 631))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_27.setFont(font)
        self.label_27.setFrameShape(QtWidgets.QFrame.Box)
        self.label_27.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_27.setLineWidth(3)
        self.label_27.setStyleSheet("border-color: rgb(0, 0, 0);\n"
"background-color: #fafafa;")
        self.label_27.setObjectName("label_27")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setStyleSheet("background: rgb(238, 233, 233)")
        self.tab_3.setObjectName("tab_3")
        self.label_14 = QtWidgets.QLabel(self.tab_3)
        self.label_14.setGeometry(QtCore.QRect(20, 20, 221, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.tab_3)
        self.label_15.setGeometry(QtCore.QRect(20, 90, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.pushButton_11 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_11.setGeometry(QtCore.QRect(270, 10, 441, 28))
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_20 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_20.setGeometry(QtCore.QRect(760, 10, 271, 28))
        self.pushButton_20.setObjectName("pushButton_20")
        self.pushButton_12 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_12.setGeometry(QtCore.QRect(270, 90, 441, 28))
        self.pushButton_12.setObjectName("pushButton_12")
        self.pushButton_21 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_21.setGeometry(QtCore.QRect(760, 90, 271, 28))
        self.pushButton_21.setObjectName("pushButton_21")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_7.setGeometry(QtCore.QRect(270, 50, 761, 31))
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.lineEdit_8 = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_8.setGeometry(QtCore.QRect(270, 130, 761, 31))
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.label_16 = QtWidgets.QLabel(self.tab_3)
        self.label_16.setGeometry(QtCore.QRect(10, 220, 231, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.label_32 = QtWidgets.QLabel(self.tab_3)
        self.label_32.setGeometry(QtCore.QRect(20, 330, 221, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_32.setFont(font)
        self.label_32.setObjectName("label_32")

        self.label_38 = QtWidgets.QLabel(self.tab_3)
        self.label_38.setGeometry(QtCore.QRect(700, 330, 400, 41))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_38.setFont(font)
        self.label_38.setObjectName("label_38")
        self.label_38.hide()

        self.comboBox_3 = QtWidgets.QComboBox(self.tab_3)
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.setGeometry(QtCore.QRect(270, 330, 400, 41))
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboBox_3.setFont(font)
        self.label_17 = QtWidgets.QLabel(self.tab_3)
        self.label_17.setGeometry(QtCore.QRect(20, 170, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.lineEdit_9 = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_9.setGeometry(QtCore.QRect(270, 170, 321, 31))
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.pushButton_13 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_13.setGeometry(QtCore.QRect(270, 220, 441, 31))
        self.pushButton_13.setObjectName("pushButton_13")
        self.pushButton_14 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_14.setGeometry(QtCore.QRect(760, 220, 271, 31))
        self.pushButton_14.setObjectName("pushButton_14")
        self.lineEdit_10 = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_10.setGeometry(QtCore.QRect(270, 260, 761, 31))
        self.lineEdit_10.setText("")
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.label_18 = QtWidgets.QLabel(self.tab_3)
        self.label_18.setGeometry(QtCore.QRect(150, 470, 91, 33))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_18.setFont(font)
        self.label_18.setObjectName("label_18")
        self.label_35 = QtWidgets.QLabel(self.tab_3)
        self.label_35.setGeometry(QtCore.QRect(480, 470, 91, 33))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_35.setFont(font)
        self.label_35.setObjectName("label_35")
        self.pushButton_15 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_15.setGeometry(QtCore.QRect(380, 400, 261, 51))
        self.pushButton_15.setObjectName("pushButton_15")
        self.label_19 = QtWidgets.QLabel(self.tab_3)
        self.label_19.setGeometry(QtCore.QRect(830, 470, 91, 33))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_19.setFont(font)
        self.label_19.setObjectName("label_19")
        self.label_28 = QtWidgets.QLabel(self.tab_3)
        self.label_28.setGeometry(QtCore.QRect(50, 510, 300, 401))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_28.setFont(font)
        self.label_28.setFrameShape(QtWidgets.QFrame.Box)
        self.label_28.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_28.setLineWidth(3)
        self.label_28.setStyleSheet("border-color: rgb(0, 0, 0);\n"
"background-color: #fafafa;")
        self.label_28.setObjectName("label_28")
        self.label_34 = QtWidgets.QLabel(self.tab_3)
        self.label_34.setGeometry(QtCore.QRect(386, 510, 300, 401))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_34.setFont(font)
        self.label_34.setFrameShape(QtWidgets.QFrame.Box)
        self.label_34.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_34.setLineWidth(3)
        self.label_34.setStyleSheet("border-color: rgb(0, 0, 0);\n"
                                    "background-color: #fafafa;")
        self.label_34.setObjectName("label_34")
        self.label_29 = QtWidgets.QLabel(self.tab_3)
        self.label_29.setGeometry(QtCore.QRect(730, 510, 300, 401))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_29.setFont(font)
        self.label_29.setFrameShape(QtWidgets.QFrame.Box)
        self.label_29.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_29.setLineWidth(3)
        self.label_29.setStyleSheet("border-color: rgb(0, 0, 0);\n"
"background-color: #fafafa;")
        self.label_29.setObjectName("label_29")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setStyleSheet("background: rgb(238, 233, 233)")
        self.tab_4.setObjectName("tab_4")
        self.label_20 = QtWidgets.QLabel(self.tab_4)
        self.label_20.setGeometry(QtCore.QRect(20, 10, 221, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_20.setFont(font)
        self.label_20.setObjectName("label_20")
        self.pushButton_16 = QtWidgets.QPushButton(self.tab_4)
        self.pushButton_16.setGeometry(QtCore.QRect(270, 10, 441, 28))
        self.pushButton_16.setObjectName("pushButton_16")
        self.pushButton_22 = QtWidgets.QPushButton(self.tab_4)
        self.pushButton_22.setGeometry(QtCore.QRect(760, 10, 271, 28))
        self.pushButton_22.setObjectName("pushButton_22")
        self.lineEdit_11 = QtWidgets.QLineEdit(self.tab_4)
        self.lineEdit_11.setGeometry(QtCore.QRect(270, 50, 761, 31))
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.label_21 = QtWidgets.QLabel(self.tab_4)
        self.label_21.setGeometry(QtCore.QRect(20, 140, 221, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_21.setFont(font)
        self.label_21.setObjectName("label_21")
        self.label_22 = QtWidgets.QLabel(self.tab_4)
        self.label_22.setGeometry(QtCore.QRect(20, 90, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_22.setFont(font)
        self.label_22.setObjectName("label_22")
        self.lineEdit_12 = QtWidgets.QLineEdit(self.tab_4)
        self.lineEdit_12.setGeometry(QtCore.QRect(270, 90, 441, 28))
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.pushButton_17 = QtWidgets.QPushButton(self.tab_4)
        self.pushButton_17.setGeometry(QtCore.QRect(270, 140, 441, 28))
        self.pushButton_17.setObjectName("pushButton_17")
        self.pushButton_18 = QtWidgets.QPushButton(self.tab_4)
        self.pushButton_18.setGeometry(QtCore.QRect(760, 140, 271, 28))
        self.pushButton_18.setObjectName("pushButton_18")
        self.lineEdit_13 = QtWidgets.QLineEdit(self.tab_4)

        self.lineEdit_13.setGeometry(QtCore.QRect(270, 180, 761, 31))
        self.lineEdit_13.setObjectName("lineEdit_13")

        self.label_33 = QtWidgets.QLabel(self.tab_4)
        self.label_33.setGeometry(QtCore.QRect(20, 220, 221, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_33.setFont(font)
        self.label_33.setObjectName("label_33")
        self.comboBox_4 = QtWidgets.QComboBox(self.tab_4)
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_4.setGeometry(QtCore.QRect(270, 220, 400, 41))
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")

        self.label_39 = QtWidgets.QLabel(self.tab_4)
        self.label_39.setGeometry(QtCore.QRect(680, 220, 100, 41))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.label_39.setFont(font)
        self.label_39.setObjectName("label_39")
        self.label_39.hide()
        self.lineEdit_20 = QtWidgets.QLineEdit(self.tab_4)
        self.lineEdit_20.setGeometry(QtCore.QRect(790, 220, 60, 28))
        self.lineEdit_20.setObjectName("lineEdit_20")
        self.lineEdit_20.hide()

        self.label_40 = QtWidgets.QLabel(self.tab_4)
        self.label_40.setGeometry(QtCore.QRect(860, 220, 100, 41))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.label_40.setFont(font)
        self.label_40.setObjectName("label_40")
        self.label_40.hide()
        self.lineEdit_21 = QtWidgets.QLineEdit(self.tab_4)
        self.lineEdit_21.setGeometry(QtCore.QRect(970, 220, 60, 28))
        self.lineEdit_21.setObjectName("lineEdit_21")
        self.lineEdit_21.hide()

        self.pushButton_23 = QtWidgets.QPushButton(self.tab_4)
        self.pushButton_23.setGeometry(QtCore.QRect(900, 220, 141, 28))
        self.pushButton_23.setObjectName("pushButton_23")
        self.pushButton_23.hide()
        self.lineEdit_14 = QtWidgets.QLineEdit(self.tab_4)
        self.lineEdit_14.setGeometry(QtCore.QRect(680, 220, 211, 28))
        self.lineEdit_14.setObjectName("lineEdit_14")
        self.lineEdit_14.hide()
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboBox_4.setFont(font)
        self.pushButton_19 = QtWidgets.QPushButton(self.tab_4)
        self.pushButton_19.setGeometry(QtCore.QRect(370, 280, 301, 41))
        self.pushButton_19.setObjectName("pushButton_19")
        self.label_23 = QtWidgets.QLabel(self.tab_4)
        self.label_23.setGeometry(QtCore.QRect(200, 340, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_23.setFont(font)
        self.label_23.setObjectName("label_23")
        self.label_24 = QtWidgets.QLabel(self.tab_4)
        self.label_24.setGeometry(QtCore.QRect(740, 340, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_24.setFont(font)
        self.label_24.setObjectName("label_24")
        self.label_30 = QtWidgets.QLabel(self.tab_4)
        self.label_30.setGeometry(QtCore.QRect(10, 380, 511, 551))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_30.setFont(font)
        self.label_30.setFrameShape(QtWidgets.QFrame.Box)
        self.label_30.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_30.setLineWidth(3)
        self.label_30.setStyleSheet("border-color: rgb(0, 0, 0);\n"
"background-color: #fafafa;")
        self.label_30.setObjectName("label_30")
        self.label_31 = QtWidgets.QLabel(self.tab_4)
        self.label_31.setGeometry(QtCore.QRect(530, 380, 511, 551))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_31.setFont(font)
        self.label_31.setFrameShape(QtWidgets.QFrame.Box)
        self.label_31.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_31.setLineWidth(3)
        self.label_31.setStyleSheet("border-color: rgb(0, 0, 0);\n"
"background-color: #fafafa;")
        self.label_31.setObjectName("label_31")
        self.tabWidget.addTab(self.tab_4, "")
        self.comboBox_4.currentIndexChanged.connect(self.showLineEditByDWT)
        self.comboBox_3.currentIndexChanged.connect(self.showMessageByDCT)
        self.pushButton.clicked.connect(self.uploadimage)
        self.pushButton_2.clicked.connect(self.uploadfile)
        self.pushButton_4.clicked.connect(self.uploadimage1)
        self.pushButton_11.clicked.connect(self.uploadimage2)
        self.pushButton_12.clicked.connect(self.uploadimage3)
        self.pushButton_13.clicked.connect(self.uploadfile1)
        self.pushButton_16.clicked.connect(self.uploadimage4)
        self.pushButton_17.clicked.connect(self.uploadfile2)
        self.pushButton_6.clicked.connect(self.wipedata)
        self.pushButton_20.clicked.connect(self.wipedata7)
        self.pushButton_22.clicked.connect(self.wipedata9)
        self.pushButton_23.clicked.connect(self.uploadimage5)
        self.pushButton_21.clicked.connect(self.wipedata8)
        self.pushButton_7.clicked.connect(self.wipedata1)
        self.pushButton_9.clicked.connect(self.wipedata3)
        self.pushButton_14.clicked.connect(self.wipedata5)
        self.pushButton_18.clicked.connect(self.wipedata6)

        self.tabWidget.setStyleSheet("pane{top:-1px;};")
        self.tabWidget.setStyleSheet("background-color:#fafafa;")
        # self.tabWidget.setStyleSheet("background-image: url(./resources/picture/background.png);")  # 设置背景图片
        Form.setStyleSheet("background-color:#fafafa;")  # 设置背景颜色

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "隐写与解密系统"))
        Form.setWindowIcon(QIcon('images/heu.jpg'))
        self.label.setText(_translate("Form", "请选择载体图片"))
        self.pushButton.setText(_translate("Form", "选择图片"))
        self.pushButton.setStyleSheet(
            "QPushButton{border-radius:5px;background:rgb(100, 157, 200);color:black}")
        self.lineEdit.setPlaceholderText(_translate("Form", "载体图片路径"))
        self.label_2.setText(_translate("Form", "请输入要隐藏的信息"))
        self.label_3.setText(_translate("Form", "隐写图片输出路径"))
        self.pushButton_2.setText(_translate("Form", "选择输出文件夹"))
        self.pushButton_2.setStyleSheet(
            "QPushButton{border-radius:5px;background:rgb(100, 157, 200);color:black}")
        self.pushButton_3.setText(_translate("Form", "进行文本信息隐藏"))
        self.pushButton_3.setStyleSheet(
            "QPushButton{border-radius:5px;background:rgb(100, 157, 200);color:black}")
        self.lineEdit_2.setPlaceholderText(_translate("Form", "图片输出路径"))
        self.label_5.setText(_translate("Form", "请选择加密算法"))
        self.label_37.setText(_translate("Form", "文本加密目前只支持LSB加密算法"))
        self.label_39.setText(_translate("Form", "隐秘图像高度:"))
        self.label_40.setText(_translate("Form", "隐秘图像宽度:"))

        self.label_32.setText(_translate("Form", "请选择加密算法"))
        self.label_33.setText(_translate("Form", "请选择解密算法"))


        self.comboBox_1.setItemText(0, _translate("MainWindow", "LSB"))
        self.comboBox_1.setItemText(1, _translate("MainWindow", "DWT"))
        self.comboBox_1.setItemText(2, _translate("MainWindow", "DCT"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "LSB"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "DWT"))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "DCT"))
        self.comboBox_3.setItemText(0, _translate("MainWindow", "LSB"))
        self.comboBox_3.setItemText(1, _translate("MainWindow", "DWT"))
        self.comboBox_3.setItemText(2, _translate("MainWindow", "DCT"))
        self.comboBox_4.setItemText(0, _translate("MainWindow", "LSB"))
        self.comboBox_4.setItemText(1, _translate("MainWindow", "DWT"))
        self.comboBox_4.setItemText(2, _translate("MainWindow", "DCT"))
        self.label_7.setText(_translate("Form", "载体图片"))
        self.label_8.setText(_translate("Form", "输出图片"))
        self.pushButton_6.setText(_translate("Form", "清空选择"))
        self.pushButton_6.setStyleSheet(
            "QPushButton{border-radius:5px;background:rgb(100, 157, 200);color:black}")
        self.pushButton_20.setText(_translate("Form", "清空选择"))
        self.pushButton_20.setStyleSheet(
            "QPushButton{border-radius:5px;background:rgb(100, 157, 200);color:black}")
        self.pushButton_22.setText(_translate("Form", "清空选择"))
        self.pushButton_22.setStyleSheet(
            "QPushButton{border-radius:5px;background:rgb(100, 157, 200);color:black}")
        self.pushButton_23.setText(_translate("Form", "选择背景图片"))
        self.pushButton_23.setStyleSheet(
            "QPushButton{border-radius:5px;background:rgb(100, 157, 200);color:black}")
        self.pushButton_21.setText(_translate("Form", "清空选择"))
        self.pushButton_21.setStyleSheet(
            "QPushButton{border-radius:5px;background:rgb(100, 157, 200);color:black}")
        self.pushButton_7.setText(_translate("Form", "清空选择"))
        self.pushButton_7.setStyleSheet(
            "QPushButton{border-radius:5px;background:rgb(100, 157, 200);color:black}")
        self.label_10.setText(_translate("Form", "输出图片名称"))
        self.lineEdit_6.setPlaceholderText(_translate("Form", "请输入输出图片名称"))
        self.label_25.setText(_translate("Form", "+显示图片"))
        self.label_26.setText(_translate("Form", "+显示图片"))
        # self.tabWidget.setStyleSheet("background-image: url(./resources/picture/background.png);")  # 设置背景图片
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Form", "隐藏文本信息"))
        self.label_4.setText(_translate("Form", "请选择含密图片"))
        self.pushButton_4.setText(_translate("Form", "选择图片"))
        self.pushButton_4.setStyleSheet(
            "QPushButton{border-radius:5px;background:rgb(100, 157, 200);color:black}")
        self.pushButton_5.setText(_translate("Form", "进行文本信息提取"))
        self.pushButton_5.setStyleSheet(
            "QPushButton{border-radius:5px;background:rgb(100, 157, 200);color:black}")
        self.lineEdit_3.setPlaceholderText(_translate("Form", "请输入隐写图片路径"))
        self.label_6.setText(_translate("Form", "请选择解密算法"))
        self.label_9.setText(_translate("Form", "文本解密目前只支持LSB算法"))
        # self.lineEdit_5.setPlaceholderText(_translate("Form", "请选择解密算法"))
        self.pushButton_9.setText(_translate("Form", "清空选择"))
        self.pushButton_9.setStyleSheet(
            "QPushButton{border-radius:5px;background:rgb(100, 157, 200);color:black}")
        self.label_12.setText(_translate("Form", "含密图片"))
        self.label_13.setText(_translate("Form", "图像中隐藏信息"))
        self.label_27.setText(_translate("Form", "+显示图片"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Form", "提取文本信息"))
        self.label_14.setText(_translate("Form", "请选择载体图片"))
        self.label_15.setText(_translate("Form", "请选择要隐藏的图片"))
        self.pushButton_11.setText(_translate("Form", "选择图片"))
        self.pushButton_11.setStyleSheet(
            "QPushButton{border-radius:5px;background:rgb(100, 157, 200);color:black}")
        self.pushButton_12.setText(_translate("Form", "选择图片"))
        self.pushButton_12.setStyleSheet(
            "QPushButton{border-radius:5px;background:rgb(100, 157, 200);color:black}")
        self.lineEdit_7.setPlaceholderText(_translate("Form", "请输入载体图片的路径"))
        self.lineEdit_8.setPlaceholderText(_translate("Form", "请输入要隐藏图片的路径"))
        self.label_16.setText(_translate("Form", "设置隐写图片输出路径"))
        self.label_17.setText(_translate("Form", "输出图片名称"))
        self.lineEdit_9.setPlaceholderText(_translate("Form", "请输入输出图片名称"))
        self.pushButton_13.setText(_translate("Form", "请选择输出文件夹"))
        self.pushButton_13.setStyleSheet(
            "QPushButton{border-radius:5px;background:rgb(100, 157, 200);color:black}")
        self.pushButton_14.setText(_translate("Form", "清空选择"))
        self.pushButton_14.setStyleSheet(
            "QPushButton{border-radius:5px;background:rgb(100, 157, 200);color:black}")
        self.lineEdit_10.setPlaceholderText(_translate("Form", "请输入隐写图片的输出路径"))
        self.label_18.setText(_translate("Form", "载体图片"))
        self.label_35.setText(_translate("Form", "秘密图片"))
        # self.label_36.setText(_translate("Form", "请选择背景图片"))
        self.pushButton_15.setText(_translate("Form", "进行图像隐藏"))
        self.pushButton_15.setStyleSheet(
            "QPushButton{border-radius:5px;background:rgb(100, 157, 200);color:black}")
        self.label_19.setText(_translate("Form", "输出图片"))
        self.label_28.setText(_translate("Form", "+显示图片"))
        self.label_34.setText(_translate("Form", "+显示图片"))
        self.label_29.setText(_translate("Form", "+显示图片"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Form", "隐藏私密图像"))
        self.label_20.setText(_translate("Form", "请选择含密图片"))
        self.pushButton_16.setText(_translate("Form", "选择图片"))
        self.pushButton_16.setStyleSheet(
            "QPushButton{border-radius:5px;background:rgb(100, 157, 200);color:black}")
        self.lineEdit_11.setPlaceholderText(_translate("Form", "请输入含密图片路径"))
        self.label_21.setText(_translate("Form", "设置提取图片输出路径"))
        self.label_22.setText(_translate("Form", "输出图片名称"))
        self.lineEdit_12.setPlaceholderText(_translate("Form", "设置输出图片名称"))
        self.lineEdit_14.setPlaceholderText(_translate("Form", "设置背景图片路径"))
        self.pushButton_17.setText(_translate("Form", "选择输出文件夹"))
        self.pushButton_17.setStyleSheet(
            "QPushButton{border-radius:5px;background:rgb(100, 157, 200);color:black}")
        self.pushButton_18.setText(_translate("Form", "清空选择"))
        self.pushButton_18.setStyleSheet(
            "QPushButton{border-radius:5px;background:rgb(100, 157, 200);color:black}")
        self.lineEdit_13.setPlaceholderText(_translate("Form", "请输入提取图片输出路径"))

        self.lineEdit_20.setPlaceholderText(_translate("Form", "输入高度"))
        self.lineEdit_21.setPlaceholderText(_translate("Form", "输入宽度"))
        self.pushButton_19.setText(_translate("Form", "进行图像提取"))
        self.pushButton_19.setStyleSheet(
            "QPushButton{border-radius:5px;background:rgb(100, 157, 200);color:black}")
        self.label_23.setText(_translate("Form", "含密图片"))
        self.label_24.setText(_translate("Form", "提取图片"))
        self.label_30.setText(_translate("Form", "+显示图片"))
        self.label_31.setText(_translate("Form", "+显示图片"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("Form", "提取私密图像"))

        # 设置控件透明
        self.label.setStyleSheet("background: transparent;")
        self.label_2.setStyleSheet("background: transparent;")
        self.label_3.setStyleSheet("background: transparent;")
        self.label_4.setStyleSheet("background: transparent;")
        self.label_5.setStyleSheet("background: transparent;")
        self.label_32.setStyleSheet("background: transparent;")
        self.label_33.setStyleSheet("background: transparent;")
        self.label_6.setStyleSheet("background: transparent;")
        self.label_7.setStyleSheet("background: transparent;")
        self.label_8.setStyleSheet("background: transparent;")
        self.label_10.setStyleSheet("background: transparent;")
        self.label_11.setStyleSheet("background: transparent;")
        self.label_12.setStyleSheet("background: transparent;")
        self.label_13.setStyleSheet("background: transparent;")
        self.label_14.setStyleSheet("background: transparent;")
        self.label_15.setStyleSheet("background: transparent;")
        self.label_16.setStyleSheet("background: transparent;")
        self.label_17.setStyleSheet("background: transparent;")
        self.label_18.setStyleSheet("background: transparent;")
        self.label_35.setStyleSheet("background: transparent;")
        # self.label_36.setStyleSheet("background: transparent;")
        self.label_19.setStyleSheet("background: transparent;")
        self.label_20.setStyleSheet("background: transparent;")
        self.label_21.setStyleSheet("background: transparent;")
        self.label_22.setStyleSheet("background: transparent;")
        self.label_23.setStyleSheet("background: transparent;")
        self.label_24.setStyleSheet("background: transparent;")
        self.textEdit.setStyleSheet("background: transparent;")
        self.textEdit_2.setStyleSheet("background: transparent;")

    # 定义所需功能函数
    def uploadimage(self, Filepath):
        x, _ = QtWidgets.QFileDialog.getOpenFileName(None, "选取文件", "./", "*.jpg;;*.jpeg;;*.png")
        self.lineEdit.setText(x)
        jpg = QtGui.QPixmap(x).scaled(self.label_25.width(), self.label_25.height())
        self.label_25.setPixmap(jpg)

    def uploadfile(self, Filepath):
        y = QtWidgets.QFileDialog.getExistingDirectory(None, "选取文件夹", "./")  # 起始路径
        name = self.lineEdit_6.text()
        if name.endswith('.jpg') or name.endswith('.png'):
            name = name[:-4]
        else:
            name = name
        if name == '':
            QMessageBox().warning(None, "警告", "请先补全输出图片名称！", QMessageBox.Close)
        else:
            y += '/'
            y += name
            y += '.png'
            self.lineEdit_2.setText(y)

    def uploadimage1(self, Filepath):
        a, _ = QtWidgets.QFileDialog.getOpenFileName(None, "选取文件", "./", "*.png;;*.jpg;;*.jpeg")
        self.lineEdit_3.setText(a)
        jpg = QtGui.QPixmap(a).scaled(self.label_27.width(), self.label_27.height())
        self.label_27.setPixmap(jpg)

    def uploadimage2(self, Filepath):
        b, _ = QtWidgets.QFileDialog.getOpenFileName(None, "选取文件", "./", "*.jpg;;*.jpeg;;*.png")
        self.lineEdit_7.setText(b)
        jpg = QtGui.QPixmap(b).scaled(self.label_28.width(), self.label_28.height())
        self.label_28.setPixmap(jpg)

    def uploadimage3(self, Filepath):
        c, _ = QtWidgets.QFileDialog.getOpenFileName(None, "选取文件", "./", "*.jpg;;*.jpeg;;*.png")
        self.lineEdit_8.setText(c)
        img = Image.open(c)
        self.label_38.setText('隐秘图像高度:' + str(img.height) + '   ，隐秘图像宽度:' + str(img.width))

        jpg = QtGui.QPixmap(c).scaled(self.label_34.width(), self.label_34.height())
        self.label_34.setPixmap(jpg)


    def uploadfile1(self, Filepath):
        d = QtWidgets.QFileDialog.getExistingDirectory(None, "选取文件夹", "./")  # 起始路径
        name = self.lineEdit_9.text()
        if name.endswith('.jpg') or name.endswith('.png'):
            name = name[:-4]
        else:
            name = name
        if name == '':
            QMessageBox().warning(None, "警告", "请先补全输出图片名称！", QMessageBox.Close)
        else:
            d += '/'
            d += name
            d += '.png'
            self.lineEdit_10.setText(d)

    def uploadimage4(self, Filepath):
        e, _ = QtWidgets.QFileDialog.getOpenFileName(None, "选取文件", "./", "*.png;;*.jpg;;*.jpeg")
        self.lineEdit_11.setText(e)
        jpg = QtGui.QPixmap(e).scaled(self.label_30.width(), self.label_30.height())
        self.label_30.setPixmap(jpg)

    def uploadimage5(self, Filepath):
        e, _ = QtWidgets.QFileDialog.getOpenFileName(None, "选取文件", "./", "*.jpg;;*.jpeg;;*.png")
        self.lineEdit_14.setText(e)
        # jpg = QtGui.QPixmap(e).scaled(self.label_30.width(), self.label_30.height())
        # self.label_30.setPixmap(jpg)

    def uploadfile2(self, Filepath):
        f = QtWidgets.QFileDialog.getExistingDirectory(None, "选取文件夹", "./")  # 起始路径
        name = self.lineEdit_12.text()
        if name.endswith('.jpg') or name.endswith('.png'):
            name = name[:-4]
        else:
            name = name
        if name == '':
            QMessageBox().warning(None, "警告", "请先补全输出图片名称！", QMessageBox.Close)
        else:
            f += '/'
            f += name
            f += '.png'
            self.lineEdit_13.setText(f)

    def wipedata(self):
        self.lineEdit.setText('')
        self.label_25.setPixmap(QPixmap(""))

    def wipedata1(self):
        self.lineEdit_2.setText('')
        self.lineEdit_6.setText('')

    def wipedata3(self):
        self.lineEdit_3.setText('')
        self.label_27.setPixmap(QPixmap(""))

    def wipedata5(self):
        self.lineEdit_9.setText('')
        self.lineEdit_10.setText('')

    def wipedata6(self):
        self.lineEdit_12.setText('')
        self.lineEdit_13.setText('')

    def wipedata7(self):
        self.lineEdit_7.setText('')
        self.label_28.setPixmap(QPixmap(""))

    def wipedata8(self):
        self.lineEdit_8.setText('')
        self.label_34.setPixmap(QPixmap(""))

    def wipedata9(self):
        self.lineEdit_11.setText('')
        # self.label_28.setPixmap(QPixmap(""))


    # 警告和提示
    def tip1(self):
        QMessageBox().warning(None, "警告", "请确保信息输入完整！", QMessageBox.Close)

    def tip2(self):
       QMessageBox().information(None, "提示", "成功完成图片隐藏!", QMessageBox.Close)

    def tip3(self):
       QMessageBox().information(None, "提示", "成功完成图片提取！", QMessageBox.Close)

    def tip4(self):
       QMessageBox().warning(None, "警告", "载体图片大小需大于要隐藏的图片！", QMessageBox.Close)


    def tip5(self, background, watermark, block_size=8):
        b_h, b_w = background.shape[:2]
        w_h, w_w = watermark.shape[:2]
        if not (w_h <= b_h / block_size and w_w <= b_w / block_size):
            QMessageBox().warning(None, "警告", "\r\n请确保您的的水印图像尺寸 不大于 背景图像尺寸的1/{:}\r\n载体图片尺寸{:}\r\n水印图片尺寸{:}".format(
                block_size, background.shape, watermark.shape), QMessageBox.Close)
            return True


    def showimage1(self):
       imagename = self.lineEdit_10.text()
       jpg = QtGui.QPixmap(imagename).scaled(self.label_29.width(), self.label_29.height())
       self.label_29.setPixmap(jpg)

    def showimage2(self):
       imagename = self.lineEdit_13.text()
       jpg = QtGui.QPixmap(imagename).scaled(self.label_31.width(), self.label_31.height())
       self.label_31.setPixmap(jpg)

    # def warn1(self):
    #    QMessageBox().warning(None, "警告", "请选择一种信息隐藏方式！", QMessageBox.Close)

    def warn2(self):
       QMessageBox().warning(None, "警告", "输入密钥非6位！", QMessageBox.Close)

    def success1(self):
       QMessageBox().information(None, "提示", "成功完成文本信息隐藏！", QMessageBox.Close)

    def success2(self):
       QMessageBox().information(None, "提示", "成功完成文本信息提取！", QMessageBox.Close)

    def showimage3(self):
       imagename = self.lineEdit_2.text()
       jpg = QtGui.QPixmap(imagename).scaled(self.label_26.width(), self.label_26.height())
       self.label_26.setPixmap(jpg)

    def showimage4(self):
       imagename = self.lineEdit_2.text()
       jpg = QtGui.QPixmap(imagename).scaled(self.label_26.width(), self.label_26.height())
       self.label_26.setPixmap(jpg)

    def showLineEditByDWT(self):
        type = self.comboBox_4.currentText()
        if type == 'DWT':
            self.lineEdit_14.show()
            self.pushButton_23.show()
            self.label_39.hide()
            self.label_40.hide()
            self.lineEdit_20.hide()
            self.lineEdit_21.hide()
        elif type == 'DCT':
            self.label_39.show()
            self.label_40.show()
            self.lineEdit_20.show()
            self.lineEdit_21.show()
            self.lineEdit_14.hide()
            self.pushButton_23.hide()
        else:
            self.lineEdit_14.hide()
            self.pushButton_23.hide()
            self.label_39.hide()
            self.label_40.hide()
            self.lineEdit_20.hide()
            self.lineEdit_21.hide()

    def showMessageByDCT(self):
        type = self.comboBox_3.currentText()
        if type == 'DCT':
            self.label_38.show()
        else:
            self.label_38.hide()




    def warn4(self):
       QMessageBox().information(None, "提示", "找不到图片中隐藏信息！", QMessageBox.Close)

    def warn5(self):
       QMessageBox().warning(None, "警告", "输入的密钥不正确！", QMessageBox.Close)
