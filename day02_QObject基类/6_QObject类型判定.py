# coding:utf-8
"""
Project    : python_text
Time       ：2025/1/15 下午11:28
File       : 6.py
目的:         QObject类型判定
内容:
结果:
"""
from PyQt5.Qt import * # 导入PyQt5的所有常用的一些库

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('PyQt5的学习')
        self.resize(500,500)

        self.setup_ui()

    def setup_ui(self):
        self.QObject类型测试()
        self.QObject对象删除()

    def QObject类型测试(self):
        # *******************API******************开始
        # obj=QObject()
        # w= QWidget()
        # btn=QPushButton()
        # label=QLabel()
        # for i in [obj,w,btn,label]:
        #     print(i,i.isWidgetType()) # 判定是否为QWidget类型
        #     print(i,i.inherits('QWidget')) # 判定是否为QWidget类型
        # *******************API******************结束

        # *******************案例******************开始
        label1=QLabel(self)
        label1.setText('我是标签1')
        label1.move(100,100)
        label2=QLabel(self)
        label2.setText('我是标签2')
        label2.move(150,150)

        btn=QPushButton(self)
        btn.setText('我是按钮')
        btn.move(200,200)

        # for widget in self.findChildren(QLabel):
        for widget in self.children(): # 查找子控件
            print(widget)
            # if widget.isWidgetType(): # 判定是否为QWidget类型
            if widget.inherits('QLabel'): # 判定是否为QLabel类型
                widget.setStyleSheet('background-color:red')
                print('是QLabel类型')
         # *******************案例******************结束


    def QObject对象删除(self):
        obj1=QObject()

        self.obj1=obj1 # 把obj1对象赋值给self.obj1,指向window

        obj2=QObject()
        obj3=QObject()

        obj3.setParent(obj2)
        obj2.setParent(obj1)

        obj1.destroyed.connect(lambda :print('obj1被删除了'))
        obj2.destroyed.connect(lambda :print('obj2被删除了'))
        obj3.destroyed.connect(lambda :print('obj3被删除了'))

        # del obj2
        obj2.deleteLater() #删除对象
        print('obj的子控件',obj1.children()) #打印仍然有子控件obj2 是稍后删除,

        #才会释放真实的对象



if __name__ == '__main__':

    '''
    测试代码   调用不执行
    '''
    import sys
    app = QApplication(sys.argv) # 初始化操作 创建一个图形界面应用程序  传入参数

    window=Window()
    window.show()

    sys.exit(app.exec_()) # 退出