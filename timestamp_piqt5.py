import csv
import os.path
import sys
from datetime import datetime, timedelta

from PyQt5.QtCore import QDate, Qt
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QTextEdit
)
from PyQt5.uic import loadUi

from constants import *


class Users:
    def __init__(self, name):
        self.name = name

    def printInfo(self):
        self.name.setText(userDict[self.input.text()].returnName())


userDict = dict()
userDict["write your name"] = Users("write your name")

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resume_time = datetime.today().strftime("%H:%M:%S")
        loadUi("timeLogging.ui", self)
        self.startButton.clicked.connect(self.start_button_clicked)
        self.pauseButton.clicked.connect(self.pause_button_clicked)
        self.stopButton.clicked.connect(self.stop_button_clicked)
        self.submitButton.clicked.connect(self.submit_button_clicked)
        self.ResumeButton.clicked.connect(self.resume_button_clicked)
        self.text_edit = QTextEdit()
        self.fileName = "file name.csv"
        self.fileName = "file name.csv"
        self.start_time: datetime = None
        self.start_time_str = ''
        self.pause_time: datetime = None
        self.pause_time_str = ''
        self.stop_time: datetime = None
        self.stop_time_str = ''
        self.resume_time: datetime = None
        self.resume_time_str = ''

    def start_button_clicked(self):
        self.start_time = datetime.today()
        self.start_time_str = self.start_time.strftime("%H:%M:%S")
        self.append_text(self.start_time_str)
        self.timestampArea.setWidget(self.text_edit)

    def pause_button_clicked(self):
        self.pause_time = datetime.today()
        self.pause_time_str = self.pause_time.strftime("%H:%M:%S")
        self.append_text(self.pause_time_str)
        self.timestampArea.setWidget(self.text_edit)

    def resume_button_clicked(self):
        self.resume_time = datetime.today()
        self.resume_time_str = self.resume_time.strftime("%H:%M:%S")
        self.append_text(self.resume_time_str)
        self.timestampArea.setWidget(self.text_edit)

    def stop_button_clicked(self):
        self.stop_time = datetime.today()
        self.stop_time_str = self.stop_time.strftime("%H:%M:%S")
        self.append_text(self.stop_time_str)
        self.timestampArea.setWidget(self.text_edit)

    def append_text(self, time):
        self.text_edit.append(time)

    def submit_button_clicked(self):
        headers = [DATE, START, PAUSE, RESUME, STOP, TOTAL, BREAK]
        exists_file = os.path.isfile(self.fileName)
        file_to_write = open(self.fileName, 'a+', newline="")
        csv_writer = csv.DictWriter(file_to_write, headers)
        break_hours: timedelta = self.resume_time - self.pause_time
        break_hours_String = str(break_hours).split(".")[0]
        print(break_hours_String)
        total_hours_worked = self.stop_time - self.start_time - break_hours
        total_hours_worked_String = str(total_hours_worked).split(".")[0]
        print(total_hours_worked_String)
        if exists_file is False:
            csv_writer.writeheader()
        csv_writer.writerow(
            {
                DATE: datetime.today().strftime('%Y-%m-%d'),
                START: self.start_time_str,
                PAUSE: self.pause_time_str,
                RESUME: self.resume_time_str,
                STOP: self.stop_time_str,
                TOTAL: total_hours_worked_String,
                BREAK: break_hours_String
            })
        file_to_write.close()
        self.text_edit.clear()


    def submit_button_clicked(self):
        headers = [DATE, START, STOP, BREAK, TOTAL, OBSERVATION]
        exists_file = os.path.isfile(self.fileName)
        file_to_write = open(self.fileName, 'a+', newline="")
        csv_writer = csv.DictWriter(file_to_write, headers)
        break_hours: timedelta = self.resume_time - self.pause_time
        break_hours_String = str(break_hours).split(".")[0]
        print(break_hours_String)
        total_hours_worked = self.stop_time - self.start_time - break_hours
        total_hours_worked_String = str(total_hours_worked).split(".")[0]
        print(total_hours_worked_String)
        if exists_file is False:
            csv_writer.writeheader()
        csv_writer.writerow(
            {
                DATE: datetime.today().strftime('%Y-%m-%d'),
                START: self.start_time_str,
                STOP: self.stop_time_str,
                BREAK: break_hours_String,
                TOTAL: total_hours_worked_String
            })
        file_to_write.close()
        self.text_edit.clear()

    now = QDate.currentDate()
    print(now.toString(Qt.ISODate))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec())
