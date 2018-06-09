from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUi
from fingerprint_enroll import FingerPrintScan


class Ui_Enroll(QDialog):
    def __init__(self):
        super(Ui_Enroll, self).__init__()
        loadUi('enroll.ui', self)
        self.pushButton.clicked.connect(self.on_scan_click)        

    
    def on_scan_click(self):
        try:
            self.finger_print_module = FingerPrintScan()
            self.finger_print_module.scan_fingerprint()
            self.finger_print_module.save_as_image(self.lineEdit.text())
            self.finger_print_module.save_to_char_buffer()
            if(self.finger_print_module.is_fingerprint_exist()):
                QMessageBox.about(self,'Error!','Fingerprint already exist!')
                return
            
            scene = QGraphicsScene()
            scene.addPixmap(QPixmap(self.lineEdit.text()+'.png'))
            self.graphicsView.setScene(scene)
            
            self.finger_print_module.save_fingerprint()
            if(self.finger_print_module.is_fingerprint_exist()):
                QMessageBox.about(self,'Saved','Fingerprint stored successfully!')
                return
        except Exception as e:
            print('The fingerprint sensor could not be initialized!')
            print('Exception message: ' + str(e))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_Enroll()
    ui.show()
    sys.exit(app.exec_())