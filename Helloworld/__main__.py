import sys
from PyQt5.QtWidgets import QApplication
from controls import Control_Hello

app = QApplication(sys.argv)
window = Control_Hello()
window.show()
sys.exit(app.exec_())