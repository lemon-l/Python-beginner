#!/usr/bin/python3

# coding = utf-8

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox, QLineEdit
from PyQt5.QtGui import QIcon
from random import randint


class Example(QWidget):

    def __init__(self):

        super().__init__()
        self.initUI()
        self.num = randint(1, 100)

    def initUI(self):

        self.setGeometry(300, 300, 300, 220)
        self.setWindowTitle('学点编程吧--猜数字')
        self.setWindowIcon(QIcon('xdbcb8.ico'))

        self.bt1 = QPushButton('我猜', self)
        self.bt1.setGeometry(115, 150, 70, 30)
        # 创建一个工具提示，调用setTooltip()
        self.bt1.setToolTip('<b>点击这里猜数字</b>')
        # 当按钮被点击的时候我们调用showMessage()方法去响应执行
        self.bt1.clicked.connect(self.showMessage)

        # ‘在这里输入数字’为窗口出现的时候的默认字符
        self.text = QLineEdit('在这里输入数字', self)
        # 可以理解为将‘在这里输入数字’进行全选，方便输入数字，不然还要手动全选删除默认字符
        self.text.selectAll()
        # 让焦点置于语文本栏中，方便用户输入
        self.text.setFocus()
        self.text.setGeometry(80, 50, 150, 30)

        self.show()

    #  **** Attention:QLineEdit输入的内容是str类型的，所以要进行类型转换
    def showMessage(self):

        guessnumber = int(self.text.text())
        print(self.num)

        if guessnumber > self.num:
            QMessageBox.about(self, '看结果', '猜大了!')
            self.text.setFocus()
        elif guessnumber < self.num:
            QMessageBox.about(self, '看结果', '猜小了!')
            self.text.setFocus()
        else:
            QMessageBox.about(self, '看结果', '答对了!进入下一轮!')
            self.num = randint(1, 100)
            # 当我们回答正确的时候，调用clear()方法，将文本栏里面的内容清除，同时重新生成一个随机数，并将焦点置于文本栏中。
            self.text.clear()
            self.text.setFocus()

    def closeEvent(self, event):
        '''
        弹出对话框，此处有四种，分别为：
        QMessageBox.question  ------ ？
        QMessageBox.critical  ------ ×
        QMessageBox.warning   ------ ！
        QMessageBox.information ---- i
        '''
        # 我们显示一个带有两个按钮的消息框：Yes和No。第一个字符串出现在标题栏上。 第二个字符串是对话框显示的消息文本。
        # 第三个参数指定出现在对话框中的按钮的组合。 最后一个参数是默认按钮。 它是初始键盘焦点的按钮。 返回值存储在答复变量中。
        reply = QMessageBox.question(
            self, '确认', '确认退出吗', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
