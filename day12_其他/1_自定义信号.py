from PyQt5.Qt import *
import sys


class Btn(QPushButton):
    rightclicked = pyqtSignal([str],[int,str])
    def mousePressEvent(self, evt):
        # print('点击了')
        super().mousePressEvent(evt)
        print(evt.button())

        if evt.button()==Qt.RightButton:
            print('右击信号')
            self.rightclicked[str].emit(self.text())
            self.rightclicked[int,str].emit(888,'imer')

# QTDesigner
class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(500, 500)
        self.setWindowTitle("Q的学习")
        self.setup_ui()
    def setup_ui(self):
        btn=Btn('按钮',self)
        btn.rightclicked[int,str].connect(lambda content,c2:print('右击点击了',content,c2))
        btn.pressed.connect(lambda :print('点击了'))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()

    sys.exit(app.exec_())