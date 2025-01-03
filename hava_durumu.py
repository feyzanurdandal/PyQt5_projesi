# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'hava_durumu.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(463, 641)
        MainWindow.setMaximumSize(QtCore.QSize(16777215, 12415154))
        MainWindow.setStyleSheet("QWidget {\n"
"    background-color: #d1d8e0; /* Açık mavi-gri rengi */\n"
                                 ""
"}\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_4 = QtWidgets.QFrame(self.centralwidget)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.welcomeLabel = QtWidgets.QLabel(self.frame_4)
        self.welcomeLabel.setGeometry(QtCore.QRect(50, 50, 331, 81))
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(17)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.welcomeLabel.setFont(font)
        self.welcomeLabel.setStyleSheet("color:rgb(0, 0, 54)")
        self.welcomeLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.welcomeLabel.setObjectName("welcomeLabel")
        self.verticalLayout.addWidget(self.frame_4)
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.cityInput = QtWidgets.QLineEdit(self.frame_3)
        self.cityInput.setGeometry(QtCore.QRect(20, 20, 391, 31))
        self.cityInput.setMaximumSize(QtCore.QSize(16777215, 45))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.cityInput.setFont(font)
        self.cityInput.setStyleSheet("QLineEdit {\n"
"    background-color: white;       /* Arka plan rengi beyaz */\n"
"    color: #003366;               /* Yazı rengi koyu mavi */\n"
"    border: 1px solid #003366;    /* Koyu mavi kenarlık */\n"
"    border-radius: 5px;           /* Köşeleri yuvarla */\n"
"    padding: 5px;                 /* İç boşluk */\n"
"}\n"
"QLineEdit:focus {\n"
"    border: 2px solid #00509e;    /* Odaklanıldığında daha belirgin mavi kenarlık */\n"
"}\n"
"")
        self.cityInput.setObjectName("cityInput")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.frame_3)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 69, 391, 61))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.showWeatherBtn = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.showWeatherBtn.setMaximumSize(QtCore.QSize(16777215, 35))
        self.showWeatherBtn.setStyleSheet("QPushButton {\n"
"    background-color: #003366; /* Koyu mavi */\n"
"    color: white;             /* Yazı rengi beyaz */\n"
"    border-radius: 5px;       /* Köşeleri yuvarla */\n"
"    padding: 8px;             /* İç boşluk ekle */\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #00509e; /* İmleç üzerindeyken açık mavi ton */\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #002244; /* Tıklanınca daha koyu mavi */\n"
"}\n"
"")
        self.showWeatherBtn.setObjectName("showWeatherBtn")
        self.horizontalLayout.addWidget(self.showWeatherBtn)
        self.favoriteWeatherBtn = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.favoriteWeatherBtn.setMaximumSize(QtCore.QSize(16777215, 35))
        self.favoriteWeatherBtn.setStyleSheet("QPushButton {\n"
"    background-color: #003366; /* Koyu mavi */\n"
"    color: white;             /* Yazı rengi beyaz */\n"
"    border-radius: 5px;       /* Köşeleri yuvarla */\n"
"    padding: 8px;             /* İç boşluk ekle */\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #00509e; /* İmleç üzerindeyken açık mavi ton */\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #002244; /* Tıklanınca daha koyu mavi */\n"
"}\n"
"")
        self.favoriteWeatherBtn.setObjectName("favoriteWeatherBtn")
        self.horizontalLayout.addWidget(self.favoriteWeatherBtn)
        self.verticalLayout.addWidget(self.frame_3)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.weatherLabel = QtWidgets.QLabel(self.frame_2)
        self.weatherLabel.setGeometry(QtCore.QRect(30, 20, 361, 101))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.weatherLabel.setFont(font)
        self.weatherLabel.setStyleSheet("QLabel {\n"
"    background-color: white;       /* Arka plan rengi beyaz */\n"
"    color: #003366;               /* Yazı rengi koyu mavi */\n"
"    border: 1px solid #003366;    /* Koyu mavi kenarlık */\n"
"    border-radius: 5px;           /* Köşeleri yuvarla */\n"
"    padding: 5px;                 /* İç boşluk */\n"
"}\n"
"\n"
"")
        self.weatherLabel.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.weatherLabel.setFrameShadow(QtWidgets.QFrame.Plain)
        self.weatherLabel.setText("")
        self.weatherLabel.setObjectName("weatherLabel")
        self.verticalLayout.addWidget(self.frame_2)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.frame)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(20, 10, 391, 61))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.addFavoriteBtn = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.addFavoriteBtn.setMaximumSize(QtCore.QSize(16777215, 35))
        self.addFavoriteBtn.setStyleSheet("QPushButton {\n"
"    background-color: #003366; /* Koyu mavi */\n"
"    color: white;             /* Yazı rengi beyaz */\n"
"    border-radius: 5px;       /* Köşeleri yuvarla */\n"
"    padding: 8px;             /* İç boşluk ekle */\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #00509e; /* İmleç üzerindeyken açık mavi ton */\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #002244; /* Tıklanınca daha koyu mavi */\n"
"}\n"
"")
        self.addFavoriteBtn.setObjectName("addFavoriteBtn")
        self.horizontalLayout_2.addWidget(self.addFavoriteBtn)
        self.removeFavoriteBtn = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.removeFavoriteBtn.setMaximumSize(QtCore.QSize(16777215, 35))
        self.removeFavoriteBtn.setStyleSheet("QPushButton {\n"
"    background-color: #003366; /* Koyu mavi */\n"
"    color: white;             /* Yazı rengi beyaz */\n"
"    border-radius: 5px;       /* Köşeleri yuvarla */\n"
"    padding: 8px;             /* İç boşluk ekle */\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #00509e; /* İmleç üzerindeyken açık mavi ton */\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #002244; /* Tıklanınca daha koyu mavi */\n"
"}\n"
"")
        self.removeFavoriteBtn.setObjectName("removeFavoriteBtn")
        self.horizontalLayout_2.addWidget(self.removeFavoriteBtn)
        self.verticalLayout.addWidget(self.frame)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Hava Durumu Ekranı"))
        self.welcomeLabel.setText(_translate("MainWindow", "Merhaba [Kullanıcı Adı]"))
        self.cityInput.setPlaceholderText(_translate("MainWindow", "Hava Durumunu Öğrenmek İstediğiniz Şehri Girin..."))
        self.showWeatherBtn.setText(_translate("MainWindow", "Hava Durumunu Göster"))
        self.favoriteWeatherBtn.setText(_translate("MainWindow", "Favori Şehrin Hava Durumu"))
        self.addFavoriteBtn.setText(_translate("MainWindow", "Favorilere Ekle"))
        self.removeFavoriteBtn.setText(_translate("MainWindow", "Favorilerden Çıkar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
