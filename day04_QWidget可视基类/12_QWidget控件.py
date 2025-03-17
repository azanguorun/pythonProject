from PyQt5.Qt import *
import sys

class Window(QWidget):
    def paintEvent(self, a0):
        print('窗口重绘了')
        return super().paintEvent(a0)

    def mousePressEvent(self, evt):
        print('鼠标被按下了')
        self.focusPreviousChild(True)


class Btn(QPushButton):
    def paintEvent(self, a0):
        print('按钮重绘了')
        return super().paintEvent(a0)

app = QApplication(sys.argv)
window = Window()

window.resize(500, 500)
window.setWindowTitle("QWidget案例[*]")

#懒加载
window.statusTip()
window.setStatusTip("这是窗口状态提示")

window.setWindowModified(True) #设置窗口是否被修改
print(window.isActiveWindow()) #判断窗口是否是活动窗口


btn=Btn(window)
btn.setText("按钮")
btn.pressed.connect(lambda :btn.setVisible(False)) #隐藏按钮

btn.setToolTip("这是按钮提示")

print(btn.isHidden()) #判断控件是否隐藏
print(btn.isVisible()) #判断控件是否可见
print(btn.isVisibleTo(window)) #判断控件是否可见到指定窗口
# btn.setEnabled(False) #设置控件是否可用
# btn.setVisible(False) #设置控件是否可见
btn.destroyed.connect(lambda :print('按钮被销毁了')) #控件被销毁时触发
# btn.deleteLater()#延迟销毁控件
window.setVisible(False) #设置控件是否可见
window.setHidden(True)   #设置控件是否隐藏

window.show()
sys.exit(app.exec_())