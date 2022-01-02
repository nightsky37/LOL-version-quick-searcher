from PyQt5 import QtWidgets
import requests
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import*
import lolupdate_ui as ui
from PyQt5 import QtCore, QtGui, QtWidgets
import scraping
from scrapDetail import scrap

# pyuic5 -x lolupdate.ui -o lolupdate_ui.py


class Warning(object):
    def setupUi(self, MainWindow, flag):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(514, 110)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 20, 481, 61))
        font = QtGui.QFont()
        font.setFamily("Adobe 繁黑體 Std B")
        font.setPointSize(20)
        self.label.setFont(font)
        if flag == 0:
            self.label.setText("請先輸入版本日期!")
        elif flag == 3:
            self.label.setText("日期輸入錯誤!請確定更新日期正確!")
        elif flag == 2:
            self.label.setText("英雄、道具、符文一次只能輸入一個!")
        else:
            self.label.setText("請先輸入英雄、道具、符文 擇一!")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 514, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("Warning", "Warning"))


class Concept(object):
    def setupUi(self, MainWindow, date):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1280, 800)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(190, 20, 151, 41))
        font = QtGui.QFont()
        font.setFamily("Adobe 繁黑體 Std B")
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.date = QtWidgets.QLabel(self.centralwidget)
        self.date.setGeometry(QtCore.QRect(90, 20, 91, 41))
        font = QtGui.QFont()
        font.setFamily("Adobe 繁黑體 Std B")
        font.setPointSize(20)
        self.date.setFont(font)
        self.date.setText(date)
        self.date.setAlignment(QtCore.Qt.AlignRight |
                               QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.date.setObjectName("date")
        self.pic = QtWidgets.QLabel(self.centralwidget)
        self.pic.setGeometry(QtCore.QRect(40, 20, 1200, 800))
        # self.pic.resize(1200,675)
        pURL = ""
        image = QImage()
        for d in range(len(scraping.date)):
            if scraping.date[d] == date:
                pURL = scraping.picUrl[d]
                image.loadFromData(requests.get(pURL).content)

        self.pic.setPixmap(QPixmap(image).scaled(1200, 675))
        self.pic.show()
        self.pic.setObjectName("pic")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1090, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("Concept", "Concept"))
        self.label.setText(_translate("Concept", "版本概要圖"))


class Content(object):
    def setupUi(self, MainWindow, date, champ, content):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(905, 595)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(20, 70, 861, 471))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.textEdit.setFont(font)
        self.textEdit.setObjectName("textEdit")
        if content == "":
            content = "此版本沒有更新這個項目"
        self.textEdit.setText(content)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(390, 20, 71, 41))
        font = QtGui.QFont()
        font.setFamily("Adobe 繁黑體 Std B")
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.date = QtWidgets.QLabel(self.centralwidget)
        self.date.setGeometry(QtCore.QRect(70, 20, 71, 41))
        font = QtGui.QFont()
        font.setFamily("Adobe 繁黑體 Std B")
        font.setPointSize(20)
        self.date.setFont(font)
        self.date.setText(date)
        self.date.setAlignment(QtCore.Qt.AlignRight |
                               QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.date.setObjectName("date")
        self.champ = QtWidgets.QLabel(self.centralwidget)
        self.champ.setGeometry(QtCore.QRect(130, 20, 191, 41))
        font = QtGui.QFont()
        font.setFamily("Adobe 繁黑體 Std B")
        font.setPointSize(20)
        self.champ.setFont(font)
        self.champ.setText(champ)
        self.champ.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.champ.setObjectName("champ")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 905, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("Update", "Update"))
        self.label.setText(_translate("Update", "更新"))


class Main(QMainWindow, ui.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("LoL Version Quick Search")
        self.getLabelsValue()
        self.setup_control()

    def getLabelsValue(self):
        self.date = self.dateLabel.text()
        self.legends = self.legendsLabel.text()
        self.item = self.itemLabel.text()
        self.rune = self.runeLabel.text()

    def setup_control(self):
        # 將按下按鈕event綁定到event function
        self.lastestBtn.clicked.connect(self.lastesClicked)
        self.verpicBtn.clicked.connect(self.verpicClicked)
        self.okBtn.clicked.connect(self.okClicked)

    def lastesClicked(self):
        self.dateLabel.setText(scraping.date[0])

    def verpicClicked(self):
        self.window = QtWidgets.QMainWindow()
        if not self.dateLabel.text():
            self.ui = Warning()
            self.ui.setupUi(self.window, 0)
            self.window.show()
        elif self.dateLabel.text() not in scraping.date:
            self.ui = Warning()
            self.ui.setupUi(self.window, 3)
            self.window.show()
        else:
            self.ui = Concept()
            self.ui.setupUi(self.window, date=self.dateLabel.text())
            self.window.show()

    def okClicked(self):  # 決定按下輸入會做什麼事
        self.window = QtWidgets.QMainWindow()
        if not self.dateLabel.text():
            self.ui = Warning()
            self.ui.setupUi(self.window, 0)
            self.window.show()
        elif self.dateLabel.text() not in scraping.date:
            self.ui = Warning()
            self.ui.setupUi(self.window, 3)
            self.window.show()
        elif not (self.legendsLabel.text() or self.itemLabel.text() or self.runeLabel.text()):
            self.ui = Warning()
            self.ui.setupUi(self.window, 1)
            self.window.show()
        elif (self.legendsLabel.text() and self.itemLabel.text()) or (self.itemLabel.text() and self.runeLabel.text()) or (self.legendsLabel.text() and self.runeLabel.text()) or (self.legendsLabel.text() and self.itemLabel.text() and self.runeLabel.text()):
            self.ui = Warning()
            self.ui.setupUi(self.window, 2)
            self.window.show()
        else:
            i = 0
            self.ui = Content()
            for i in range(len(scraping.date)):
                if scraping.date[i] == self.dateLabel.text():
                    break
            if self.legendsLabel.text():
                result = scrap(
                    scraping.versionURL[i], self.legendsLabel.text()+"\n")
                self.ui.setupUi(self.window, self.dateLabel.text(),
                                self.legendsLabel.text(), result)
            elif self.itemLabel.text():
                result = scrap(
                    scraping.versionURL[i], self.itemLabel.text()+"\n")
                self.ui.setupUi(self.window, self.dateLabel.text(),
                                self.itemLabel.text(), result)
            elif self.runeLabel.text():
                result = scrap(
                    scraping.versionURL[i], self.runeLabel.text()+"\n")
                self.ui.setupUi(self.window, self.dateLabel.text(),
                                self.runeLabel.text(), result)
            self.window.show()


if __name__ == '__main__':
    import sys
    app = 0
    app = QtWidgets.QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())
