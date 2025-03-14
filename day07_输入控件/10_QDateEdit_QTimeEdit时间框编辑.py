from PyQt5.Qt import *
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(500, 500)
        self.setWindowTitle("QFrame的学习")
        self.setup_ui()
    def setup_ui(self):
        de=QDateEdit(self)
        de.move(100,100)
        de.resize(200,30)
        de.setDisplayFormat("yyyy-MM-dd")

        te=QTimeEdit(self)
        te.move(100,150)
        te.resize(200,30)
        te.setDisplayFormat("hh:mm:ss:zzz a")
        print(te.time())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()

    sys.exit(app.exec_())