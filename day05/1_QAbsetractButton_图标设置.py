'''

QAbsetractButton 抽象按钮



'''

from PyQt5.Qt import *
import sys

app = QApplication(sys.argv)
window = QWidget()
window.resize(500, 500)
window.setWindowTitle("QWidget案例")


'''
btn = QPushButton(window) 
QPushButton 继承 QAbstractButton抽象类

btn = QAbstractButton(window)
represents a C++ abstract class and cannot be instantiated
c++ 抽象类 不能实例化 应该子类化 必须继承

子类化
class Btn(QAbstractButton):
    pass
btn = Btn(window)
QAbstractButton.paintEvent() is abstract and must be overridden
没有实现 必须实现抽象类中所有抽象方法
'''
class Btn(QAbstractButton):
    def paintEvent(self, QPaintEvent):
        print("绘制按钮")
        painter = QPainter(self)  # 画家
        painter.setPen(QPen(Qt.red))  # 设置画笔
        painter.drawText(50,20,self.text())
        painter.drawEllipse(self.rect()) #画圆

    def hitButton(self, QPoint):
        print("按钮被点击了")
        # if QPoint.x() > self.width() / 2:
        #     return True
        # return False

        yuanxin_x=self.width()/2
        yuanxin_y=self.height()/2
        juli=((QPoint.x()-yuanxin_x)**2+(QPoint.y()-yuanxin_y)**2)**0.5
        if juli< self.width()/2:
            return True
        return False



btn = Btn(window)
btn.setText("按钮")


btn1=QPushButton(window)
btn1.setText("1")#设置文本
btn1.move(0,100)


def plus_one():
    num = int(btn1.text())
    num += 1
    btn1.setText(str(num))

btn1.pressed.connect(plus_one)



icon=QIcon("1.jpg")
btn1.setIcon(icon) #设置图标
size=QSize(10,10)
btn1.setIconSize(size) #设置图标大小
btn1.setShortcut("Alt+a") #快捷键设置
btn1.pressed.connect(lambda :print("按钮被点击了")) #信号连接
btn1.setAutoRepeat(True)#自动重复
btn1.setAutoRepeatDelay(1000) #自动重复延迟时间
btn1.setAutoRepeatInterval(1000) #自动重复间隔时间
btn1.setCheckable(True) #设置是否可以被选中
btn1.toggle() #切换选中状态
print('获取自动重复状态',btn1.autoRepeat()) #
print('获取自动重复间隔时间',btn1.autoRepeatInterval()) #
print('获取自动重复延迟时间',btn1.autoRepeatDelay())



push_button = QPushButton(window)
push_button.setText("按钮")
push_button.move(0,150)

radio_button = QRadioButton(window) #单选按钮
radio_button.setText("单选按钮")
radio_button.move(0,200)

check_box = QCheckBox(window) #复选框
check_box.setText("复选框")
check_box.move(0,250)

push_button.setEnabled(True) #设置是否可用
push_button.setDown(True) #设置是否按下

push_button.isDown() #获取是否按下
push_button.isEnabled() #获取是否可用


def cao():
    push_button.setChecked(not push_button.isChecked()) #设置是否选中
    radio_button.toggle() #切换选中状态
    check_box.toggle() #切换选中状态


btn1.pressed.connect(cao) #信号连接

'''
排他性
'''
for i in range(0,4):
    btn=QPushButton(window)
    btn.setText('按钮'+str(i+1))
    btn.move(100*i,300)
    btn.setCheckable(True) #设置是否可以被选中

for i in range(0,4):
    btn=QRadioButton(window)
    btn.setText('按钮'+str(i+1))
    btn.move(100*i,350)
    btn.setAutoExclusive(True) #设置是否独占
    btn.setCheckable(True) #设置是否可以被选中

'''
按钮模拟点击
'''
btn2=QPushButton(window)
btn2.setText("按钮模拟点击")
btn2.move(0,400)
btn2.pressed.connect(lambda :print("按钮被点击了")) #信号连接
btn2.animateClick(1000) #模拟点击 1000毫秒


btn3=Btn(window)
btn3.setText("按钮模拟点击")
btn3.move(0,450)
btn3.pressed.connect(lambda :print("按钮被按下了")) #信号连接
btn3.released.connect(lambda :print("按钮被释放了")) #信号连接
btn3.clicked.connect(lambda :print("按钮被点击了")) #信号连接
btn3.toggled.connect(lambda isChecked:print("按钮被选中了" if isChecked else "按钮被取消了")) #信号连接



window.show() #
sys.exit(app.exec_())