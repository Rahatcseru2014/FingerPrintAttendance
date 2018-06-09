from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog
from PyQt5.uic import loadUi


class Ui_Enroll(QDialog):
    def __init__(self):
        super(Ui_Enroll, self).__init__()
        loadUi('enroll.ui', self)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_Enroll()
    ui.show()
    sys.exit(app.exec_())