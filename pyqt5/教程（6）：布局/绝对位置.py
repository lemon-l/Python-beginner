#coding = 'utf-8'

import sys
from PyQt5.QtWidgets import (QWidget, QPushButton, QApplication)

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.Init_UI()
    def Init_UI(self):
        self.setGeometry(300,300,400,300)
        self.setWindowTitle('学点编程吧')

        # 使用move（）方法来定位我们的小部件。 在我们的例子中，这些是按钮。 我们通过
        # 提供x和y坐标来定位它们。 坐标系的开始位于左上角。 x值从左到右增长。 y值不变。
        bt1 = QPushButton('剪刀',self)
        bt1.move(50,250)

        bt2 = QPushButton('石头',self)
        bt2.move(150,250)

        bt3 = QPushButton('布',self)
        bt3.move(250,250)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    app.exit(app.exec_())