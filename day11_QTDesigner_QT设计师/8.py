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
        pass



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()


    from login_ui import Ui_Form
    ui=Ui_Form()
    ui.setupUi(window)

    window.show()
    sys.exit(app.exec_())