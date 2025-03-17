from PyQt5.Qt import *
import sys
#QWidget 是所有可视控件的基类
'''
pypt.sourceforge.net/Docs/PyQt5/class_reference.html

QWidget 是所有可视控件的基类
    class QWidget(__PyQt5_QtCore.QObject, __PyQt5_QtGui.QPaintDevice):
    QWidget继承QObject和 QPaintDevice绘制设备
    继承 print(QWidget.__bases__) = (__PyQt5_QtCore.QObject, __PyQt5_QtGui.QPaintDevice)
    方法检索的链条 print(QWidget.__mro__)  = (__PyQt5_QtWidgets.QWidget, __PyQt5_QtCore.QObject, __PyQt5_QtGui.QPaintDevice, object)
'''


class Label(QLabel):
    def mousePressEvent(self, evt):
        # self.setStyleSheet("background-color:red;")
        self.raise_() #将控件提升到最上层


app = QApplication(sys.argv)#创建一个应用程序对象

window = QWidget()#创建一个窗口
window.setWindowTitle('窗口标题')#设置窗口标题
window.resize(500,500)#设置窗口大小
window.move(400,250)#设置窗口位置

red = Label(window)#创建一个红色的控件
red.resize(100,100)#设置红色控件的大小
red.setText('红色控件')#设置红色控件的标题
red.setStyleSheet('background-color:red;')#设置红色控件的样式表
red.move(0,0)#设置红色控件的位置

green = Label(window)#创建一个绿色的控件
green.resize(100,100)#设置绿色控件的大小
green.setText('绿色控件')#设置绿色控件的标题
green.setStyleSheet('background-color:green;')#设置绿色控件的样式表
green.move(50,50)#设置绿色控件的位置


window.show()#展示窗口
print(QWidget.__bases__)
sys.exit(app.exec_())#进入应用程序的主循环

#


