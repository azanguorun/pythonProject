from PyQt5.Qt import *
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(500, 500)
        self.setWindowTitle("Q的学习")
        self.setup_ui()
    def setup_ui(self):
        lable = QLabel('标签1',self)


        lable.resize(300,300)
        lable.move(100,20)

        te=QTextEdit('文本',self)
        te.move(100,300)
        te.resize(300,100)


        sb=QSpinBox(self)
        sb.move(400,300)
        sb.resize(100,100)


        self.qss边框(lable)
        self.qss边框(te)
        self.qss边框(sb)

    def qss边框(self,lable):
        lable.setStyleSheet('''
            QLabel{
                background-color: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 white, stop:0.9 gray);
                background-attachment: fixed;
                border-width: 2px 4px 8px 12px;
                border-style: dotted dashed solid double;
                border-top-style: groove ;
                border-color: red green blue yellow;
                border-bottom-width: 10px;
                border-radius: 50px;
                margin: 40px 40px 40px 40px;
                color: red;
                padding: 30px;
                padding-left: 30px;
            }
            QTextEdit{
                background-attachment: fixed;
                color: red;
                font-size: 20px;
                font-weight: bold;
                font-family: 宋体;
                font-style: italic;
                text-decoration: underline;
                
                min-height: 100px;
                max-height: 100px;
                min-width: 100px;
                max-width: 100px;
            }
            QSpinBox{
                font-size: 20px;
                font-weight: bold;
                color: red;
                border: 1px solid red;
                background-color: green;
            }
            QSpinBox::up-button, QSpinBox::down-button{
                width: 20px;
                height: 20px;
                border-image: url(./1.jpg);
            }
            QSpinBox::up-button{
                subcontrol-origin: padding;
                subcontrol-position: left center;
            }
            QSpinBox::down-button{
                subcontrol-origin: padding;
                subcontrol-position: right center;
            }
            QSpinBox::up-button:hover{
                bottom: 1px;
            }
            QSpinBox::down-button:hover{
                top: 1px;
            }
        ''')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()

    sys.exit(app.exec_())