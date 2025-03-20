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
        btn.resize(200,200)
        btn.setStyleSheet('background-color:red; color:yellow;')

        #1.创建一个动画对象，并且设置目标属性
        animation=QPropertyAnimation(btn,b'geometry',self)
        # animation1=QPropertyAnimation(btn,b'windowOpacity',self) #透明度
        #2.设置属性值 开始 插值 结束
        animation.setStartValue(QRect(0,0,200,200))
        animation.setEndValue(QRect(300,300,200,200))
        animation.setDirection(QAbstractAnimation.Forward) #
        #3.动画时长
        animation.setDuration(3000)
        animation.setLoopCount(3)
        animation.setEasingCurve(QEasingCurve.OutBounce)
        #4.启动动画
        animation.start()
        def animation_operation():
            if animation.state()==QAbstractAnimation.Running:
                animation.pause() #暂停
            elif animation.state()==QAbstractAnimation.Paused:
                animation.resume() #恢复
            elif animation.state()==QAbstractAnimation.Stopped:
                animation.start() #启动

        # btn.clicked.connect(lambda :animation.start())
        btn.clicked.connect(animation_operation)

        animation.currentLoopChanged.connect(lambda val:print('当前循环次数发生改变',val))
        animation.finished.connect(lambda :print('动画执行完毕'))
        animation.stateChanged.connect(lambda val,state:print('状态发生改变',val,state))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()

    sys.exit(app.exec_())