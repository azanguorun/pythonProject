from PyQt5.Qt import *
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(500, 500)
        self.setWindowTitle("Q的学习")
        self.setup_ui()
    def setup_ui(self):
        frame = QFrame(self)
        frame.resize(300, 300)
        QMessageBox.about(frame, '标题', '内容')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()

    sys.exit(app.exec_())