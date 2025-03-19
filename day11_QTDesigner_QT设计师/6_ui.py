from PyQt5.Qt import *
import sys

# QTDesigner
class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(500, 500)
        self.setWindowTitle("Q的学习")
        self.setup_ui()

    def setup_ui(self):
        from PyQt5.uic import loadUi
        loadUi('5_login_ui.ui', self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    print(dir(window))
    def click():
        account=window.lineEdit.text()
        pwd=window.lineEdit_2.text()
        print(account,pwd)
    window.pushButton.clicked.connect(click)
    sys.exit(app.exec_())