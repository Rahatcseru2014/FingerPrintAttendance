# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'signup.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

import sqlite3

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog, QMessageBox
from PyQt5.uic import loadUi


class Ui_Signup(QDialog):
    def __init__(self):
        super(Ui_Signup, self).__init__()
        loadUi('signup.ui', self)
        self.add_u_btn.clicked.connect(self.on_add_user_click)
        self.cancel_btn.clicked.connect(self.on_cancel_btn_click)

    def on_add_user_click(self):
        susername = self.u_name_sign_up.text()
        spassword = self.pass_sign_up.text()
        srepassword = self.re_pass_sign_up.text()

        if not susername:
            QMessageBox.about(self, "Warning!", "Username or Password Missing!")
        elif not spassword:
            QMessageBox.about(self, "Warning!", "Username or Password  Missing!")
        elif not srepassword:
            QMessageBox.about(self, "Warning!", "Username or Password  Missing!")
        else:
            self.AttemptAddUser(susername, spassword, srepassword)

    def AttemptAddUser(self, susername, spassword, srepasswprd):
        try:
            connection = sqlite3.connect('test.db')

            cursor = connection.cursor()

            if spassword != srepasswprd:
                QMessageBox.about(self, "Warning!", "Given passwords do not match!")
            else:
                sql = """INSERT INTO Attendance (USERNAME, PASSWORD) VALUES ('""" + susername + """', '""" + spassword + """')"""
                cursor.execute(sql)
                connection.commit()

                print(sql)
        except Exception as e:
            print(e)

    def on_cancel_btn_click(self):
        self.close()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_Signup()
    ui.show()
    sys.exit(app.exec_())
