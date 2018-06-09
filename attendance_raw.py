# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QAction, QMenu
from PyQt5.uic import loadUi
from delete import Ui_Delete
from enroll import Ui_Enroll


class Ui_Attendance(QMainWindow):
    def __init__(self):
        super(Ui_Attendance, self).__init__()
        loadUi('attendance.ui', self)
        self.delete_action.triggered.connect(self.on_delete_click)
        self.enroll_action.triggered.connect(self.on_enroll_click)

    @staticmethod
    def on_delete_click():
        ui_signup = Ui_Delete()
        ui_signup.exec_()

    @staticmethod
    def on_enroll_click():
        ui_signup = Ui_Enroll()
        ui_signup.exec_()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_Attendance()
    ui.show()
    sys.exit(app.exec_())
