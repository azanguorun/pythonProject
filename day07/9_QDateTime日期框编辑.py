from PyQt5.Qt import *
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(500, 500)
        self.setWindowTitle("QFrame的学习")
        self.setup_ui()
    def setup_ui(self):
        # dt=QDateTime(2020,1,1,12,12)
        dt=QDateTime.currentDateTime()
        dt=dt.addSecs(3600*24)
        print(dt.offsetFromUtc()//3600)
        print(dt.addYears(2))
        print(dt)

        QDateTimeEdit(dt,self)

        time=QTime.currentTime()
        time.start()

        btn=QPushButton(self)
        btn.move(100,100)
        btn.setText("测试按钮")
        btn.clicked.connect(lambda :print(time.elapsed()/1000))



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()

    sys.exit(app.exec_())