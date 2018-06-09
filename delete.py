from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog
from PyQt5.uic import loadUi

class Ui_Delete(QDialog):
    def __init__(self):
        super(Ui_Delete,self).__init__()
        loadUi('delete.ui',self)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_Delete()
    ui.show()
    sys.exit(app.exec_())