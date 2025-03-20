from PyQt5.Qt import *
from test_zss import Ui_Form
import sys

# QTDesigner
class Window(QWidget,Ui_Form):
    def __init__(self):
        super().__init__()
        self.resize(500, 500)
        self.setWindowTitle("Q的学习")
        self.setupUi(self)

    @pyqtSlot()
    def on_pushButton_clicked(self):
        print('点击了')

    @pyqtSlot()
    def on_pushButton_pressed(self):
        print('按下了')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()

    sys.exit(app.exec_())