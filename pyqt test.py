import datetime
import getpass
import json
import sys
import requests
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import (QApplication, QComboBox, QSpinBox, QInputDialog, QLabel, QLineEdit,
                             QMainWindow, QPlainTextEdit, QPushButton, QWidget)

username = getpass.getuser()

class App(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.title = "Weather"
        self.setWindowIcon(QtGui.QIcon('weather.ico'))
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(50, 50, 640, 800)
        
        self.label = QLabel('Welcome, ' + username, self)
        self.label.setFont(QFont("Verdana", 20, QFont.Bold))
        self.label.setFixedWidth(320)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.move(160,30)
        
        self.label2 = QLabel('WEATHER FORECAST', self)
        self.label2.setFont(QFont("Verdana", 18, QFont.Bold))
        self.label2.setFixedWidth(320)
        self.label2.setAlignment(QtCore.Qt.AlignCenter)
        self.label2.move(160,90)
        
        self.label3 = QLabel('Enter a city', self)
        self.label3.setFont(QFont("Verdana", 12))
        self.label3.setFixedWidth(160)
        self.label3.setAlignment(QtCore.Qt.AlignCenter)
        self.label3.move(60,180)
        
        self.label4 = QLabel('Days of forecast', self)
        self.label4.setFont(QFont("Verdana", 12))
        self.label4.setFixedWidth(160)
        self.label4.setAlignment(QtCore.Qt.AlignCenter)
        self.label4.move(60,210)
        
        self.city_name = QComboBox(self)
        self.city_name.setStyleSheet('QComboBox {background-color: white;}')
        self.city_name.addItem("Ioannina")
        self.city_name.addItem("Konitsa")
        self.city_name.addItem("Athens")
        self.city_name.resize(120 , 25)
        self.city_name.move(350, 180)
        global city
        city = str(self.city_name.currentText())
        
        self.num_days = QSpinBox(self)
        self.num_days.resize(120 , 25)
        self.num_days.move(350, 210)
        
        global days
        days = str(self.num_days.value())

        self.button1 = QPushButton('Get Forecast', self)
        self.button1.setFont(QFont("Verdana", 10, QFont.Bold))
        self.button1.setStyleSheet('QPushButton {background-color: red; color: white;}')
        self.button1.resize(100, 30)
        self.button1.move(290, 280)
        
        
        def on_click(self):
                        
            url = "https://community-open-weather-map.p.rapidapi.com/forecast/daily"

            querystring = {"q":city,"cnt":days,"units":"metric"}

            headers = {
            'x-rapidapi-host': "community-open-weather-map.p.rapidapi.com",
            'x-rapidapi-key': "78034bcf5emsh6d33f4776102e77p10adaajsn7041714f6122"
            }

            response = requests.request("GET", url, headers=headers, params=querystring)
            data = response.json()
            data2 = response.text
            
            self.label5 = QLabel('WEATHER FORECAST FOR: ' + str(city), self)
            self.label5.setFont(QtGui.QFont("Verdana", 14, QFont.Bold))
            self.label5.setFixedWidth(400)
            self.label5.setAlignment(QtCore.Qt.AlignCenter)
            self.label5.move(120,340)
            
            if data['cod'] != '404':
                
                self.label6 = QLabel('city found'.upper(), self)
                self.label6.setFont(QtGui.QFont("Verdana", 14, QFont.Bold))
                self.label6.setFixedWidth(400)
                self.label6.setAlignment(QtCore.Qt.AlignCenter)
                self.label6.move(120,380)
            else:
                self.label7 = QLabel('city not found'.upper(), self)
                self.label7.setFont(QtGui.QFont("Verdana", 14, QFont.Bold))
                self.label7.setFixedWidth(400)
                self.label7.setAlignment(QtCore.Qt.AlignCenter)
                self.label7.move(120,380)     
        
        self.button1.clicked.connect(on_click)
        
        self.button2 = QPushButton('Exit', self)
        self.button2.clicked.connect(QCoreApplication.instance().quit)
        self.button2.setFont(QtGui.QFont("Verdana", 10, QFont.Bold))
        self.button2.setStyleSheet('QPushButton {background-color: black; color: white;}')
        self.button2.resize(100, 30)
        self.button2.move(290, 750) 
        self.show()
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())