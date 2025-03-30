# coding:utf-8
"""
Project    : python_text
Time       ：2025/1/15 上午10:23
File       : 4.py
目的: 
内容:    QObject  所有qt对象的基类

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
        self.QObject继承机构测试()
        self.QObject对象名称和属性测试()
        self.QObject对象父子关系测试()

    def QObject继承机构测试(self):
        '''
        QObject继承机构测试   QObject继承于python的 object 类
        :return:
        '''
        mros=QObject.mro()
        print(mros)


    def QObject对象名称和属性测试(self):

        # *******************测试API******************开始

        obj=QObject()
        obj.setObjectName('obj') # 设置对象名称
        print(obj.objectName())  # 获取对象名称

        obj.setProperty('age','18') # 设置属性
        print(obj.property('age'))  # 获取属性
        print(obj.dynamicPropertyNames()) # 获取动态属性

        # *******************测试API******************结束

        # *******************案例演示******************开始

        with open('QObject.qss','r') as f:
            qApp.setStyleSheet(f.read()) # 设置样式表

        label=QLabel(self)
        label.setObjectName('notice') # 设置对象名称
        label.setText('hello world')

        # label.setStyleSheet('font-size:50px;color:red')

        label2 = QLabel(self)
        label2.move(100,100)
        label2.setObjectName('notice') # 设置对象名称
        label2.setProperty('notice_level','warning') # 设置属性

        label2.setText('hello world')
        # *******************案例演示******************结束


    def QObject对象父子关系测试(self):
        # *******************测试api******************开始
        obj0=QObject()
        obj1=QObject()
        obj2=QObject()
        obj3=QObject()
        obj4=QObject()
        obj5=QObject()
        obj1.setParent(obj2) # 设置父对象
        print('obj1的父对象: ',obj1.parent()) #说明父对象为obj2
        # *******************测试api******************结束


        obj1.setParent(obj0)
        obj2.setParent(obj0)
        obj2.setObjectName('obj2')
        # label=QLabel(self)
        # label.setParent(obj0)  #   不能设置子对象为控件



        obj3.setParent(obj1)
        obj3.setObjectName('obj3')

        obj4.setParent(obj2)
        obj5.setParent(obj2)
        print('obj0',obj0)
        print('obj1',obj1)
        print('obj2',obj2)
        print('obj3',obj3)
        print('obj4',obj4)
        print('obj5',obj5)

        print('obj0的子对象: ',obj0.children())
        print('obj0的一个子对象: ',obj0.findChild(QObject)) #不存在子对象QObject
        print('obj0的一个子对象: ',obj0.findChild(QObject,"obj2")) #不存在子对象QObject
        print('obj0的一个子对象: ',obj0.findChild(QObject,"obj3")) #不存在子对象QObject 递归检查
        print('obj0的一个子对象: ',obj0.findChild(QObject,"obj3",Qt.FindDirectChildrenOnly)) #不存在子对象QObject 不递归
        print('obj0的子孙对象: ',obj0.findChildren(QObject)) #不存在子对象QObject





        # *******************内存管理机制******************开始
        obj1=QObject()
        obj2=QObject()
        obj2.setParent(obj1) # 设置父对象为obj1
        #监听obj2对象被释放
        obj2.destroyed.connect(lambda :print('obj2被释放了'))
        #删除父控件,子控件也会被删除
        # del self.obj1
        # *******************内存管理机制******************结束
                

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv) # 初始化操作 创建一个图形界面应用程序  传入参数
    window=Window()
    window.show()

    win1=QWidget()
    win1.setWindowTitle('red')
    win1.setStyleSheet('background-color:red')
    win1.show()

    win2=QWidget()
    win2.setWindowTitle('green')
    win2.setStyleSheet('background-color:green')
    win2.setParent(win1)
    win2.resize(100,100)
    win2.show()


    win3=QWidget()
    label3=QLabel(win3)
    label3.setText('label3')
    label3.setParent(win3)

    btn=QPushButton(win3)
    btn.setText('btn')
    btn.setText('btn')

    win3.show()

    print(win3.children())
    print(win3.findChildren(QLabel))

    sys.exit(app.exec_()) # 退出