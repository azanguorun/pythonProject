# coding:utf-8
"""
Project    : python_text
Time       ：2025/1/15 下午3:19
File       : 5.py
目的: 
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
        # label = QLabel(self)
        # label.setText('按钮')
        self.QObject信号的测试()
    def QObject信号的测试(self):
        self.obj=QObject()
        #connect 连接
        # *******************对象释放******************开始
        # def destroy_cao(obj):
        #     print('obj对象被释放了',obj)
        #
        # self.obj.destroyed.connect(destroy_cao)
        #
        # del self.obj
        # *******************对象释放******************结束



        # *******************对象名称******************开始
        # def obj_name_cao(name):
        #     print('obj对象名称发生改变',name)
        #
        # self.obj.objectNameChanged.connect(obj_name_cao) # 绑定信号

        # self.obj.setObjectName('obj1') #触发信号
        #
        # print(self.obj.signalsBlocked()) # 判断信号是否被阻止
        # self.obj.blockSignals(True)# 阻止信号
        #
        # self.obj.objectNameChanged.disconnect(obj_name_cao) # 解绑信号
        # self.obj.setObjectName('obj2') #触发信号
        # print(self.obj.signalsBlocked()) # 判断信号是否被阻止
        #
        # self.obj.blockSignals(False)# 解除阻止
        #
        # print(self.obj.signalsBlocked()) # 判断信号是否被阻止
        #
        # self.obj.objectNameChanged.connect(obj_name_cao) # 绑定信号
        # self.obj.setObjectName('obj3') #触发信号
        # *******************对象名称******************结束
                

        # *******************信号接收个数******************开始
        # def obj_name_cao(name):
        #     print('obj对象名称发生改变',name)
        # def obj_name_cao2(name):
        #     print('obj对象名称发生改变',name)
        # self.obj.objectNameChanged.connect(obj_name_cao) # 绑定信号
        # self.obj.objectNameChanged.connect(obj_name_cao2) # 绑定信号
        #
        # print(self.obj.receivers(self.obj.objectNameChanged)) #查看信号的接收者个数
        # *******************信号接收个数******************结束


        # *******************信号与槽案例******************开始
        def btn_cao():
            print('按钮被点击了')
        btn=QPushButton(self)
        btn.setText('按钮')
        btn.clicked.connect(btn_cao) # 绑定信号
        # *******************信号与槽案例******************结束







if __name__ == '__main__':

    '''
    测试代码   调用不执行
    '''
    import sys
    app = QApplication(sys.argv) # 初始化操作 创建一个图形界面应用程序  传入参数

    # window=Window()
    window=QWidget()

    def cao(title):
        print('窗口标题变化',title)
        window.windowTitleChanged.disconnect()
        window.setWindowTitle('PyQt5的学习',title)
        window.windowTitleChanged.connect(cao)

    window.windowTitleChanged.connect(cao)

    window.setWindowTitle('PyQt5的学习')

    window.show()

    sys.exit(app.exec_()) # 退出