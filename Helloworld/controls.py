from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow
from Ui_hello import Ui_MainWindow

class Control_Hello(QMainWindow,Ui_MainWindow):
    def __int__(self):
        QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)




