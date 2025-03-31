'''

https://freetyst.nf.migu.cn/public/product9th/product46/2023/01/1715/2022%E5%B9%B411%E6%9C%8814%E6%97%A511%E7%82%B919%E5%88%86%E5%86%85%E5%AE%B9%E5%87%86%E5%85%A5%E6%96%B0%E8%88%AA%E9%81%9350557%E9%A6%96923799/%E6%A0%87%E6%B8%85%E9%AB%98%E6%B8%85/MP3_320_16_Stero/6903170AKAZ152610.mp3?

channelid=02
&msisdn=00c802bc-62ca-4bc1-bc47-e6c2e9d10c9c
&Tim=1730963251652
&Key=df1dc8cec84b489b


'''
import pyautogui
from PyQt5.QtWidgets import QApplication, QMainWindow,QMessageBox,QDialog,QLabel,QDesktopWidget
import sys
from robot_ui import Ui_MainWindow
import time
from PyQt5 import QtGui
from PyQt5.QtGui import QPainter
from PyQt5.QtCore import Qt,QPoint


class screenshotWindow(QDialog):
    def __init__(self,screenshotName):
        super(screenshotWindow,self).__init__()
        self.setWindowTitle('截图窗口')
        self.screenshotName=screenshotName

        self.desk=QDesktopWidget().geometry()   #获取屏幕分辨率大小
        self.resize(self.desk.width(),self.desk.height())  #设置窗口大小为屏幕分辨率大小

        self.pix=QtGui.QPixmap() #创建一个QPixmap对象
        self.pix.load(screenshotName)

        # self.label=QLabel(self)   #创建一个QLabel对象
        # self.label.setPixmap(self.pix)  #设置QLabel的图片

        self.startPoint=QPoint()
        self.endPoint=QPoint()

    def paintEvent(self,event):
        painter=QPainter(self)
        x=self.startPoint.x()
        y=self.startPoint.y()
        w=self.endPoint.x()-x
        h=self.endPoint.y()-y

        #绘制图片 再绘制到窗口
        pp=QPainter(self.pix)
        pp.drawRect(x,y,w,h)
        painter.drawPixmap(0,0,self.pix)
        print('绘制矩形')

    def mousePressEvent(self,event):
        print('鼠标按下')
        if event.button()==Qt.LeftButton:
            self.startPoint=event.pos()
            self.endPoint=event.pos()

    def mouseReleaseEvent(self,event):  #鼠标释放事件
        print('鼠标释放')
        if event.button() == Qt.LeftButton:
            self.endPoint=event.pos()
            self.update()


class MainWindow(QMainWindow):
    def __init__(self,parent=None):
        super(MainWindow,self).__init__(parent)
        # 设置窗口标题和大小
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)

    def Screenshot(self):
        # 截图
        screenshotName = self.ui.lineEdit.text()
        if not screenshotName:
            screenshotName=str(int(time.time()))+'.jpg'
        pyautogui.screenshot(screenshotName) #保存截图
        ssw=screenshotWindow(screenshotName)
        ssw.exec()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())