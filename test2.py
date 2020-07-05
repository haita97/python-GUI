# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'exe.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import pandas as pd
font = QtGui.QFont()
font.setPointSize(20)
from random import sample


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(743, 632)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setMaximumSize(QtCore.QSize(8000, 800))
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser.setFont(font)
        self.gridLayout.addWidget(self.textBrowser, 0, 0, 1, 3)

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setMaximumSize(QtCore.QSize(16777215, 100))
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 1, 0, 1, 1)

        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setMaximumSize(QtCore.QSize(800, 100))
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout.addWidget(self.pushButton_4, 4, 1, 1, 1)

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setMaximumSize(QtCore.QSize(800, 100))
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 4, 0, 1, 1)

        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setMaximumSize(QtCore.QSize(800, 100))
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 1, 1, 1, 1)

        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setMaximumSize(QtCore.QSize(800, 100))
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout.addWidget(self.pushButton_5, 1, 2, 1, 1)

        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setMaximumSize(QtCore.QSize(800, 100))
        self.pushButton_6.setObjectName("pushButton_6")
        self.gridLayout.addWidget(self.pushButton_6, 4, 2, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 743, 24))

        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.pushButton.clicked.connect(self.on_click)
        self.pushButton_2.clicked.connect(self.on_click2)
        self.pushButton_3.clicked.connect(self.on_click3)
        self.pushButton_4.clicked.connect(self.on_click4)
        self.pushButton_5.clicked.connect(self.on_click5)
        self.pushButton_6.clicked.connect(self.on_click6)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(
            _translate("MainWindow", "上海财经大学国际组织人才培养项目2020年度夏令营考核"))
        self.pushButton.setText(_translate("MainWindow", "命题演讲"))
        self.pushButton_2.setText(_translate("MainWindow", "自由问答"))
        self.pushButton_3.setText(_translate("MainWindow", "国际组织与全球治理"))
        self.pushButton_4.setText(_translate("MainWindow", "品德修养测试"))
        self.pushButton_5.setText(_translate("MainWindow", "专业能力测试"))
        self.pushButton_6.setText(_translate("MainWindow", "清屏"))

    def on_click(self):
        df = pd.read_excel("题库/命题演讲.xlsx", header=None)
        i = sample(list(df[df[1] == '未抽'].index), 1)
        print(df.loc[i, 0])
        self.textBrowser.setText(str(list(df.loc[i, 0])[0]))
        df.loc[i, 1] = '已抽'
        df.to_excel('题库/命题演讲.xlsx', header=None, index=None)

    def on_click2(self):
        df = pd.read_excel("题库/自由问答.xlsx", header=None)
        i = sample(list(df[df[1] == '未抽'].index), 1)
        print(df.loc[i, 0])
        self.textBrowser.setText(str(list(df.loc[i, 0])[0]))
        df.loc[i, 1] = '已抽'
        df.to_excel('题库/自由问答.xlsx', header=None, index=None)

    def on_click3(self):
        df = pd.read_excel("题库/国际组织与全球治理.xlsx", header=None)
        i = sample(list(df[df[1] == '未抽'].index), 1)
        print(df.loc[i, 0])
        self.textBrowser.setText(str(list(df.loc[i, 0])[0]))
        df.loc[i, 1] = '已抽'
        df.to_excel('题库/国际组织与全球治理.xlsx', header=None, index=None)

    def on_click4(self):
        df = pd.read_excel("题库/品德修养测试.xlsx", header=None)
        i = sample(list(df[df[1] == '未抽'].index), 1)
        print(df.loc[i, 0])
        self.textBrowser.setText(str(list(df.loc[i, 0])[0]))
        df.loc[i, 1] = '已抽'
        df.to_excel('题库/品德修养测试.xlsx', header=None, index=None)

    def on_click5(self):
        df = pd.read_excel("题库/专业能力测试.xlsx", header=None)
        i = sample(list(df[df[1] == '未抽'].index), 1)
        print(df.loc[i, 0])
        self.textBrowser.setText(str(list(df.loc[i, 0])[0]))
        df.loc[i, 1] = '已抽'
        df.to_excel('题库/专业能力测试.xlsx', header=None, index=None)

    def on_click6(self):
        self.textBrowser.setText("")


if __name__ == '__main__':

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())