import datetime
import getpass
import json
import sys
import requests
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import (QApplication, QLabel, QLineEdit, QListWidget, QMainWindow,
                            QPushButton, QSpinBox, QWidget)

username = getpass.getuser()
    
class App(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.title = "Weather"
        self.setWindowIcon(QtGui.QIcon('weather.ico'))
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(50, 130, 640, 500)
        
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
        
        self.city_name = QLineEdit(self)
        self.city_name.resize(120 , 25)
        self.city_name.move(350, 180)
             
        self.num_days = QSpinBox(self)
        self.num_days.setRange(1, 5)
        self.num_days.setStyleSheet('QComboBox {background-color: white;}')
        self.num_days.resize(120 , 25)
        self.num_days.move(350, 210)
        
        self.button1 = QPushButton('Get Forecast', self)
        self.button1.setFont(QFont("Verdana", 10, QFont.Bold))
        self.button1.setStyleSheet('QPushButton {background-color: red; color: white;}')
        self.button1.resize(120, 30)
        self.button1.move(290, 280)
        
        
        def get_forecast():
                        
            url = "https://community-open-weather-map.p.rapidapi.com/forecast/daily"
            self.city = str(self.city_name.text())
            self.days = str(self.num_days.value())
            querystring = {"q":self.city,"cnt":self.days,"units":"metric"}

            headers = {
            'x-rapidapi-host': "community-open-weather-map.p.rapidapi.com",
            'x-rapidapi-key': "78034bcf5emsh6d33f4776102e77p10adaajsn7041714f6122"
            }

            response = requests.request("GET", url, headers=headers, params=querystring)
            self.data = response.json()
            #print(self.data)
            self.frcst = ''
            for day in self.data['list']:
                self.date = str(datetime.datetime.fromtimestamp(day['dt']).strftime('%d-%m-%y'))
                self.weather =str(day['weather'][0]['description'])
                self.min_temp = float(day['temp']['min'])
                self.max_temp = float(day['temp']['max'])
                self.hum = int(day['humidity'])
                self.text = 'DATE:'
                self.text2 = 'Weather:'
                self.text3 = 'Temp min:'
                self.text4 = 'Temp max:'
                self.text5 = 'Humidity:'
                self.d = '{0} {1}'.format(self.text, self.date)
                self.w = '{0} {1}'.format(self.text2, self.weather)
                self.mi = '{0} {1}'.format(self.text3, self.min_temp)
                self.ma = '{0} {1}'.format(self.text4, self.max_temp)
                self.h = '{0} {1}{2}'.format(self.text5, self.hum, '%')
                self.frcst += (self.d + "\n" + self.w + '\n' + self.mi + "\n" + self.ma + "\n" + self.h + '\n\n')
            
                        
        def open_forecast():
            self.msg = QListWidget()
            self.msg.setWindowTitle("Weather Forecast")
            self.msg.setGeometry(0, 0, 280, 500)
            self.msg.move(690, 100)
            self.msg.insertItem(0, "Forecast for " + self.city + '\n')
            self.msg.insertItem(1, self.frcst)
            self.msg.show()
        
        self.button1.clicked.connect(get_forecast)
        
        self.button2 = QPushButton('Show Forecast', self)
        self.button2.setFont(QtGui.QFont("Verdana", 10, QFont.Bold))
        self.button2.setStyleSheet('QPushButton {background-color: blue; color: white;}')
        self.button2.resize(120, 30)
        self.button2.move(290, 330)
        self.button2.clicked.connect(open_forecast) 
        
        self.button3 = QPushButton('Exit', self)
        self.button3.clicked.connect(QCoreApplication.instance().quit)
        self.button3.setFont(QtGui.QFont("Verdana", 10, QFont.Bold))
        self.button3.setStyleSheet('QPushButton {background-color: black; color: white;}')
        self.button3.resize(80, 30)
        self.button3.move(310, 460) 
        self.show()
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())