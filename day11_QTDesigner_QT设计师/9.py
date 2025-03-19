from PyQt5.Qt import *
from login_ui import Ui_Form
import sys

# QTDesigner
class Window(QWidget,Ui_Form):
    def __init__(self):
        super().__init__()
        self.resize(500, 500)
        self.setWindowTitle("Q的学习")
        self.setupUi(self)

    def setup_ui(self):
        pass

    def btn_click(self):
        print(self.lineEdit.text(),self.lineEdit_2.text(),'登录')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())