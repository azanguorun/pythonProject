# coding:utf-8
"""
Project    : python_text
Time       ：2025/1/22 上午11:25
File       : 9.py
目的:         定时器案例
内容:
结果:
"""
from PyQt5.Qt import * # 导入PyQt5的所有常用的一些库
import sys # 导入系统库

class MyObject(QObject):
    def timerEvent(self, evt):
        print('定时器事件')
        print(evt)
        print(self)

class Mylabel(QLabel):
    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.setText("10")
        self.move(100, 100)
        self.resize(200, 200)
        self.setStyleSheet("background-color:cyan; font-size:30px;")
        # self.timer_id = self.startTimer(1000)


    def setSec(self, sec):
        self.setText(str(sec))

    def startMyTimer(self,mc):
        self.timer_id = self.startTimer(mc)
    def timerEvent(self, *args, **kwargs):
        print('定时器事件')
        self.setText(str(int(self.text())-1)) #获取当前的文本 然后-1 再设置回去

        if int(self.text())==0:
            print("时间到了")
            # self.close()
            self.killTimer(self.timer_id)


class MyWidget(QWidget):
    def timerEvent(self, *args, **kwargs):
        current_w=self.width()
        current_h=self.height()

        self.resize(current_w+10,current_h+10)

#1.创建一个应用程序对象
app = QApplication(sys.argv) # 初始化操作 创建一个图形界面应用程序  传入参数

#2.控件的操作
window = MyWidget() # 创建窗口 window 就是父控件
# window.timerEvent()

#2.2 设置控件
window.setWindowTitle("定时器案例") # 标题
window.resize(500, 500) # 大小
# window.move(400, 200) # 位置
window.startTimer(100)


label = Mylabel(window) # 标签  传入window 作为父控件
label.setSec(10)
label.startMyTimer(100)

#2.3 展示控件
window.show() # 显示 显示完消失

#3.应用程序的执行，进入到消息循环
sys.exit(app.exec_()) # 退出