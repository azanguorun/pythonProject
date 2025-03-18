from PyQt5.Qt import *
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(500, 500)
        self.setWindowTitle("Q的学习")
        self.setup_ui()
    def setup_ui(self):
        box1=QWidget(self)
        box2=QWidget(self)
        box2.setObjectName('box2')

        label1=QLabel('标签1',box1)
        btn1=QPushButton('按钮1',box1)
        label2 = QLabel('标签1', box2)
        btn2 = QPushButton('按钮2', box2)


        label1.setObjectName('pink')
        label1.setProperty('notice_level','warning')
        label2.setProperty('notice_level','error')


        label1.move(50, 50)
        label1.resize(50,50)
        label2.move(50, 50)
        label2.resize(50, 50)
        btn1.move(150, 50)
        btn1.resize(50, 50)
        btn2.move(150, 50)
        btn2.resize(50, 50)


        cb=QCheckBox('复选框',box1)
        cb.move(150,100)
        cb.resize(100,50)
        cb.setObjectName('cb')


        v_layout=QVBoxLayout(self)
        self.setLayout(v_layout)
        v_layout.addWidget(box1)
        v_layout.addWidget(box2)

if __name__ == '__main__':
    from Tool import QSSTool
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    QSSTool.setQssToObj('test.qss',app)
    
    sys.exit(app.exec_())