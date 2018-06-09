# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

import sqlite3

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QMessageBox
from PyQt5.uic import loadUi

from attendance_raw import Ui_Attendance
from signup import Ui_Signup


class Ui_Login(QDialog):
    def __init__(self):
        super(Ui_Login, self).__init__()
        loadUi('login.ui', self)
        self.log_in_btn.clicked.connect(self.on_login_click)
        self.sign_up_btn.clicked.connect(self.on_signup_click)

    def on_login_click(self):

        username = self.u_name.text()
        password = self.password_edit.text()
        if not username:
            QMessageBox.about(self, "Warning!", "Username or Password Missing!")
        elif not password:
            QMessageBox.about(self, "Warning!", "Username or Password  Missing!")
        else:
            self.AttemptLogin(username, password)

    def AttemptLogin(self, username, password):
        try:
            connection = sqlite3.connect('test.db')

            cursor = connection.cursor()

            sql = """SELECT * FROM Attendance WHERE USERNAME LIKE '""" + username + """' and PASSWORD LIKE '""" + password + """'"""
            print(sql)
            cursor.execute(sql)

            rows = cursor.fetchall()

            if len(rows) == 0 or len(rows) > 1:
                QMessageBox.about(self, "Warning!", "Invalid username or password")
            else:
                self.close()
                self.window = Ui_Attendance()
                self.window.show()
        except Exception as e:
            print(e)

    def on_signup_click(self):
        ui_signup = Ui_Signup()
        ui_signup.exec_()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_Login()
    ui.show()
    app.exec_()
