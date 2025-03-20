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
        btn=QPushButton('按钮',self)
        btn.setObjectName('btn')
        btn.setText('登录')
        btn.move(100,100)

        btn2=QPushButton('按钮2',self)
        btn2.setObjectName('btn2')
        btn2.setText('登录2')
        btn2.move(100,200)

        QMetaObject.connectSlotsByName(self)  # 自动连接信号与槽
        # btn.clicked.connect(self.click)

    @pyqtSlot(bool)
    def on_btn_clicked(self,val):
        print('点击了',val)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()

    sys.exit(app.exec_())