from PyQt5.Qt import *
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(500, 500)
        self.setWindowTitle("QFrame的学习")
        self.setup_ui()
    def setup_ui(self):
        QFileDialog.getOpenFileName(self,"选择文件","../","All(*);;Images(*.png *.xpm *.jpg)")
        result=QFileDialog.getExistingDirectoryUrl(self,"选择文件夹",QUrl("../"))
        print(result)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()

    sys.exit(app.exec_())