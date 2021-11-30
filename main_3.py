from main_2 import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtGui import QMovie
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from threading import Thread
from Main import main
import os
import sys
import webbrowser as web
import datetime
from PyQt5.QtCore import QTimer, QTime, Qt, QDateTime

thread = Thread(target = main)
thread.start()

class Gui_start(QMainWindow):
    def __init__(self):
        super().__init__()
        self.gui = Ui_MainWindow()
        self.gui.setupUi(self)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.showTime)
        self.timer.start(1000)
        self.font = QFont('Arial', 30, QFont.Bold)
        self.gui.date_time_day_temp.setAlignment(Qt.AlignCenter)
        self.gui.date_time_day_temp.setFont(self.font)
        self.gui.pushButton_start.clicked.connect(self.Start)
        self.gui.pushButton_quit.clicked.connect(self.exit)
        self.gui.pushButton_youtube.clicked.connect(self.youtube)
        self.gui.pushButton_instagram.clicked.connect(self.instagram)
        self.gui.pushButton_whatapp.clicked.connect(self.whatsapp)
        self.gui.pushButton_myclass.clicked.connect(self.myclass)

    def youtube(self):
        web.open("https://www.youtube.com/")

    def whatsapp(self):
        web.open("https://web.whatsapp.com/")

    def instagram(self):
        web.open("https://www.instagram.com/")

    def myclass(self):
        web.open("https://myclass.lpu.in/")

    def Start(self):
        self.gui.label1 = QtGui.QMovie("..//Gifs//center.gif")
        self.gui.Gif_1.setMovie(self.gui.label1)
        self.gui.label1.start()

        self.gui.label2 = QtGui.QMovie("..//Gifs//round_1.gif")
        self.gui.Gif_2.setMovie(self.gui.label2)
        self.gui.label2.setSpeed(400)
        self.gui.label2.start()

        self.gui.label3 = QtGui.QMovie("..//Gifs//INITILIZING.gif")
        self.gui.Gif_3.setMovie(self.gui.label3)
        self.gui.label3.start()

        self.gui.label4 = QtGui.QMovie("..//Gifs//listening.gif")
        self.gui.Gif_4.setMovie(self.gui.label4)
        self.gui.label4.start()


    def showTime(self):
        current_time = QDateTime.currentDateTime()
        label_time = current_time.toString('dd-MM-yyyy hh:mm:ss')
        self.gui.date_time_day_temp.setText(label_time)


    def exit(self):
        self.sys.exit()


motion = QApplication(sys.argv)
move = Gui_start()
move.show()
move.showFullScreen()
motion.exit(motion.exec_())
