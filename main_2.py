from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.background = QtWidgets.QLabel(self.centralwidget)
        self.background.setGeometry(QtCore.QRect(-170, -50, 2291, 1191))
        self.background.setText("")
        self.background.setPixmap(QtGui.QPixmap("../Images/bg.png"))
        self.background.setScaledContents(True)
        self.background.setObjectName("background")
        self.label_1 = QtWidgets.QLabel(self.centralwidget)
        self.label_1.setGeometry(QtCore.QRect(20, 10, 1891, 1021))
        self.label_1.setText("")
        self.label_1.setPixmap(QtGui.QPixmap("../Images/background_2.png"))
        self.label_1.setScaledContents(True)
        self.label_1.setObjectName("label_1")
        self.label_wa = QtWidgets.QLabel(self.centralwidget)
        self.label_wa.setGeometry(QtCore.QRect(180, 320, 441, 161))
        self.label_wa.setText("")
        self.label_wa.setPixmap(QtGui.QPixmap("../Images/new_tab.png"))
        self.label_wa.setScaledContents(True)
        self.label_wa.setObjectName("label_wa")
        self.label_mc = QtWidgets.QLabel(self.centralwidget)
        self.label_mc.setGeometry(QtCore.QRect(180, 710, 441, 161))
        self.label_mc.setText("")
        self.label_mc.setPixmap(QtGui.QPixmap("../Images/new_tab.png"))
        self.label_mc.setScaledContents(True)
        self.label_mc.setObjectName("label_mc")
        self.label_ig = QtWidgets.QLabel(self.centralwidget)
        self.label_ig.setGeometry(QtCore.QRect(180, 510, 441, 161))
        self.label_ig.setText("")
        self.label_ig.setPixmap(QtGui.QPixmap("../Images/new_tab.png"))
        self.label_ig.setScaledContents(True)
        self.label_ig.setObjectName("label_ig")
        self.label_yt = QtWidgets.QLabel(self.centralwidget)
        self.label_yt.setGeometry(QtCore.QRect(180, 110, 441, 161))
        self.label_yt.setText("")
        self.label_yt.setPixmap(QtGui.QPixmap("../Images/new_tab.png"))
        self.label_yt.setScaledContents(True)
        self.label_yt.setObjectName("label_yt")
        self.Gif_1 = QtWidgets.QLabel(self.centralwidget)
        self.Gif_1.setGeometry(QtCore.QRect(760, 270, 720, 405))
        self.Gif_1.setText("")
        self.Gif_1.setPixmap(QtGui.QPixmap("../Gifs/center.gif"))
        self.Gif_1.setScaledContents(True)
        self.Gif_1.setObjectName("Gif_1")
        self.Gif_4 = QtWidgets.QLabel(self.centralwidget)
        self.Gif_4.setGeometry(QtCore.QRect(850, 700, 571, 141))
        self.Gif_4.setText("")
        self.Gif_4.setPixmap(QtGui.QPixmap("../Gifs/listening.gif"))
        self.Gif_4.setScaledContents(True)
        self.Gif_4.setObjectName("Gif_4")
        self.Gif_3 = QtWidgets.QLabel(self.centralwidget)
        self.Gif_3.setGeometry(QtCore.QRect(920, 60, 431, 201))
        self.Gif_3.setText("")
        self.Gif_3.setPixmap(QtGui.QPixmap("../Gifs/INITILIZING.gif"))
        self.Gif_3.setScaledContents(True)
        self.Gif_3.setObjectName("Gif_3")
        self.Gif_2 = QtWidgets.QLabel(self.centralwidget)
        self.Gif_2.setGeometry(QtCore.QRect(1500, 110, 351, 261))
        self.Gif_2.setText("")
        self.Gif_2.setPixmap(QtGui.QPixmap("../Gifs/round_1.gif"))
        self.Gif_2.setScaledContents(True)
        self.Gif_2.setObjectName("Gif_2")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(1500, 560, 261, 121))
        self.label_9.setText("")
        self.label_9.setPixmap(QtGui.QPixmap("../Images/Start.png"))
        self.label_9.setScaledContents(True)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(1500, 700, 261, 111))
        self.label_10.setText("")
        self.label_10.setPixmap(QtGui.QPixmap("../Images/quiet.png"))
        self.label_10.setScaledContents(True)
        self.label_10.setObjectName("label_10")
        self.date_time_day_temp = QtWidgets.QTextBrowser(self.centralwidget)
        self.date_time_day_temp.setGeometry(QtCore.QRect(230, 890, 521, 81))
        self.date_time_day_temp.setStyleSheet("background-color: Transparent;\n"
"color: rgb(85, 255, 255);\n"
"border-color: rgb(0, 0, 255);")
        self.date_time_day_temp.setObjectName("date_time_day_temp")
        self.pushButton_start = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_start.setGeometry(QtCore.QRect(1510, 580, 241, 81))
        self.pushButton_start.setStyleSheet("background-color: Transparent;")
        self.pushButton_start.setText("")
        self.pushButton_start.setObjectName("pushButton_start")
        self.pushButton_quit = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_quit.setGeometry(QtCore.QRect(1510, 710, 241, 81))
        self.pushButton_quit.setStyleSheet("background-color: Transparent;")
        self.pushButton_quit.setText("")
        self.pushButton_quit.setObjectName("pushButton_quit")
        self.pushButton_youtube = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_youtube.setGeometry(QtCore.QRect(240, 140, 331, 91))
        self.pushButton_youtube.setStyleSheet("background-color: Transparent;\n"
"font: 75 28pt \"Arial\";\n"
"color: rgb(0, 255, 255);")
        self.pushButton_youtube.setObjectName("pushButton_youtube")
        self.pushButton_whatapp = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_whatapp.setGeometry(QtCore.QRect(240, 350, 331, 91))
        self.pushButton_whatapp.setStyleSheet("background-color: Transparent;\n"
"font: 75 28pt \"Arial\";\n"
"color: rgb(0, 255, 255);")
        self.pushButton_whatapp.setObjectName("pushButton_whatapp")
        self.pushButton_instagram = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_instagram.setGeometry(QtCore.QRect(230, 540, 331, 91))
        self.pushButton_instagram.setStyleSheet("background-color: Transparent;\n"
"font: 75 28pt \"Arial\";\n"
"color: rgb(0, 255, 255);")
        self.pushButton_instagram.setObjectName("pushButton_instagram")
        self.pushButton_myclass = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_myclass.setGeometry(QtCore.QRect(240, 740, 331, 91))
        self.pushButton_myclass.setStyleSheet("background-color: Transparent;\n"
"font: 75 28pt \"Arial\";\n"
"color: rgb(0, 255, 255);")
        self.pushButton_myclass.setObjectName("pushButton_myclass")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1922, 21))
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
        self.date_time_day_temp.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.pushButton_youtube.setText(_translate("MainWindow", "YOU TUBE"))
        self.pushButton_whatapp.setText(_translate("MainWindow", "WHAT\'S APP"))
        self.pushButton_instagram.setText(_translate("MainWindow", "INSTAGRAM"))
        self.pushButton_myclass.setText(_translate("MainWindow", "MY CLASS"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    MainWindow.showFullScreen()
    sys.exit(app.exec_())
