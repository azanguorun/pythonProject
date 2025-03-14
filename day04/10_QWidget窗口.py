


from PyQt5.Qt import *
import sys

class MyWindow(QWidget):
    def mousePressEvent(self, evt):
        self.showMaximized()
        if self.isMaximized():
            self.showNormal()
        else:
            self.showMaximized()



app=QApplication(sys.argv)
window=MyWindow()
window.resize(500,500)



icon=QIcon('1.jpg')
window.setWindowIcon(icon)  #设置窗口图标
window.setWindowTitle("QWidget案例")  #设置窗口标题
window.setWindowOpacity(0.5)  #设置窗口透明度
# window.setWindowFlags(Qt.FramelessWindowHint)  #设置窗口无边框
# window.setAttribute(Qt.WA_TranslucentBackground)  #设置窗口背景透明
# window.setWindowModality(Qt.ApplicationModal)  #设置窗口模态

# window.setWindowState(Qt.WindowMinimized)  #设置窗口最小化
# window.setWindowState(Qt.WindowMaximized)  #设置窗口最大化




win2=QWidget()
win2.setWindowTitle('2')
win2.resize(100,100)

window.show()
# window.showMaximized()#设置窗口最大化
# window.showMinimized()#设置窗口最小化



win2.show()


window.setWindowState(Qt.WindowActive)  #设置窗口为工具窗口

sys.exit(app.exec_())