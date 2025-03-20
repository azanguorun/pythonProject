from PyQt5.Qt import *
import sys

# QTDesigner
class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(800, 800)
        self.setWindowTitle("Q的学习")
        self.setup_ui()
    def setup_ui(self):
        red_btn=QPushButton('红色按钮',self)
        green_btn=QPushButton('绿色按钮',self)

        red_btn.resize(100,100)
        green_btn.resize(100,100)
        green_btn.move(150,150)

        red_btn.setStyleSheet('background-color:red; color:yellow;')
        green_btn.setStyleSheet('background-color:green; color:yellow;')

        animation=QPropertyAnimation(green_btn,b'pos',self)
        animation.setKeyValueAt(0,QPoint(150,150))
        animation.setKeyValueAt(0.25,QPoint(550,150))
        animation.setKeyValueAt(0.5,QPoint(550,550))
        animation.setKeyValueAt(0.75,QPoint(150,550))
        animation.setKeyValueAt(1,QPoint(150,150))


        animation.setDuration(3000)
        animation.setLoopCount(3)
        # animation.start()

        animation2 = QPropertyAnimation(red_btn, b'pos', self)
        animation2.setKeyValueAt(0, QPoint(0, 0))
        animation2.setKeyValueAt(0.25, QPoint(0, 700))
        animation2.setKeyValueAt(0.5, QPoint(700, 700))
        animation2.setKeyValueAt(0.75, QPoint(700, 0))
        animation2.setKeyValueAt(1, QPoint(0, 0))

        animation2.setDuration(3000)
        animation2.setLoopCount(3)
        # animation2.start()


        # animation_group=QParallelAnimationGroup(self)
        animation_group=QSequentialAnimationGroup(self) #顺序播放
        # animation_group.addPause(2000)
        pause_animation=QPauseAnimation(2000,self)
        animation_group.addAnimation(pause_animation)

        animation_group.addAnimation(animation)
        animation_group.addAnimation(animation2)
        animation_group.start()

        red_btn.clicked.connect(animation_group.pause)
        green_btn.clicked.connect(animation_group.resume)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()

    sys.exit(app.exec_())