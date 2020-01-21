#coding = 'utf-8'

import sys
from PyQt5.QtWidgets import (QWidget, QPushButton, QApplication, QGridLayout, QLCDNumber)

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.Init_UI()

    def Init_UI(self):
        #创建QGridLayout的实例并将其设置为应用程序窗口的布局。
        grid = QGridLayout()
        self.setLayout(grid)

        self.setGeometry(300,300,400,300)
        self.setWindowTitle('学点编程吧-计算器')

        '''
        如果我们向窗格添加窗口小部件，我们可以提供窗口小部件
        的行跨度和列跨度。 在我们的例子中，我们使QLCDNumber小
        部件跨越4行。同时我们创建一个网格布局并在窗口小部件之间设置间距。
        '''
        self.lcd =  QLCDNumber()
        grid.addWidget(self.lcd,0,0,3,0)
        grid.setSpacing(10)

        names = ['Cls', 'Bc', '', 'Close',
                 '7', '8', '9', '/',
                 '4', '5', '6', '*',
                 '1', '2', '3', '-',
                 '0', '.', '=', '+']

        positions = [(i,j) for i in range(4,9) for j in range(4,8)]
        for position, name in zip(positions, names):
            if name == '':
                continue
            button = QPushButton(name)
            #使用addWidget（）方法创建并添加到布局中的按钮
            grid.addWidget(button, *position)
            button.clicked.connect(self.Cli)

        self.show()

    def Cli(self):
        sender = self.sender().text()
        ls = ['/', '*', '-', '=', '+']
        if sender in ls:
            self.lcd.display('A')
        else:
            self.lcd.display(sender)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    app.exit(app.exec_())


