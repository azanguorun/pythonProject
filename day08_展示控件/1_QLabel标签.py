from PyQt5.Qt import *
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(500, 500)
        self.setWindowTitle("QFrame的学习")
        self.setup_ui()
    def setup_ui(self):
        label=QLabel(self)
        label.setText("xxx")
        label.move(100,100)
        label.resize(100,200)
        label.setStyleSheet("background-color:cyan;")
        label.setAlignment(Qt.AlignRight | Qt.AlignCenter)
        label.setIndent(10)
        label.setMargin(2)
        label.setTextFormat(Qt.PlainText) #纯文本


        label2=QLineEdit(self)
        label2.move(200,100)

        label3=QLineEdit(self)
        label3.move(200,200)

        label.setBuddy(label2)
        # label.setPixmap(QPixmap("1.jpg"))
        label.setScaledContents(True) #图片自适应
        label.setOpenExternalLinks(True) #打开外部链接
        label.setTextInteractionFlags(Qt.TextSelectableByMouse | Qt.TextSelectableByKeyboard ) #鼠标选中文字
        label.setSelection(1,2) #选中文字

        # label.setNum(100)
        # label.setText("100")
        pic=QPicture() #画一个图片
        painter=QPainter(pic)
        painter.setBrush(QBrush(Qt.red))
        painter.drawEllipse(0,0,100,100) #画一个圆
        # painter.end()
        label.setPicture(pic)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()

    sys.exit(app.exec_())