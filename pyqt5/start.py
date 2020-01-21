#!/usr/bin/python3
# coding = utf-8

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QCoreApplication


class Ico(QWidget):

    def __init__(self):
        # 构造函数
        super().__init__()
        # 创建GUI界面
        self.initUI()

    def initUI(self):

        # 前两个参数是窗口的位置，第三个是宽度，第四个是高度
        self.setGeometry(300, 300, 300, 220)
        self.setWindowTitle('学点编程吧出品')
        self.setWindowIcon(QIcon('xdbcb8.ico'))

        qbtn = QPushButton('退出', self)
        qbtn.clicked.connect(QCoreApplication.instance().quit)
        qbtn.resize(70,30)
        qbtn.move(50, 50)
        self.show()

if __name__ == '__main__':

   app = QApplication(sys.argv)
   ex = Ico()
   sys.exit(app.exec_())
