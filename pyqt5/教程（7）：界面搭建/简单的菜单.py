#coding=utf-8

from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, qApp
from PyQt5.QtGui import QIcon
import sys
class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.InitUI()

    def InitUI(self):
        self.statusBar().showMessage('准备就绪')

        self.setGeometry(300,300,400,300)
        self.setWindowTitle('关注微信公众号：学点编程吧--简单的菜单')

        '''
        QAction是使用菜单栏，工具栏或自定义键盘快捷方式执行操作的抽象。
        在下述三行中，我们创建一个具有特定图标和“退出”标签的动作。此外，
        为此操作定义了快捷方式。当我们将鼠标指针悬停在菜单项上时，第三
        行创建状态栏显示在状态栏中。
        '''
        exitAct = QAction(QIcon('exit.png'), '退出(&E)', self)
        exitAct.setShortcut('Ctrl+Q')
        exitAct.setStatusTip('退出程序')
        #当我们选择这个特定的动作时，发出触发信号。 信号连接到QApplication
        #小部件的quit()方法。 这终止了应用程序
        exitAct.triggered.connect(qApp.quit)

        #menuBar（）方法创建一个菜单栏。 我们使用addMenu（）创建文件菜单，
        #并使用addAction（）添加操作。
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('文件(&F)')
        fileMenu.addAction(exitAct)

        self.show()
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())