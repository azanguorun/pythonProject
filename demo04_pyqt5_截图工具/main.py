'''




'''
import pyautogui
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QDialog, QLabel, QDesktopWidget, QInputDialog, \
    QFileDialog
import sys
from robot_ui import Ui_MainWindow
import time
from PyQt5 import QtGui, QtCore
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


        self.tmpPix=QtGui.QPixmap() #创建一个QPixmap对象
        self.tmpPix.load(screenshotName)  #加载图片
        self.isDrawing=False  #是否正在画矩形

    def paintEvent(self,event):
        painter=QPainter(self)
        x=self.startPoint.x()
        y=self.startPoint.y()
        w=self.endPoint.x()-x
        h=self.endPoint.y()-y

        #绘制图片 再绘制到窗口
        if self.isDrawing:
            pp=QPainter(self.tmpPix)
            pp.drawRect(x,y,w,h)
            painter.drawPixmap(0,0,self.tmpPix)
            print('绘制矩形')
        else:
            pp=QPainter(self.pix)
            pp.drawRect(x,y,w,h)
            painter.drawPixmap(0,0,self.pix)

    def keyPressEvent(self,event):
        #矩形选定区域截图保存
        x=self.startPoint.x()
        y=self.startPoint.y()
        w=self.endPoint.x()-x
        h=self.endPoint.y()-y
        region = (x, y, w, h)
        print(f"截图区域: {region}")
        pyautogui.screenshot(self.screenshotName,region)
        self.close()

    def mouseMoveEvent(self,event):
        print('鼠标移动')
        if event.buttons() and Qt.LeftButton:
            self.endPoint=event.pos()
            self.update()

    def mousePressEvent(self,event):
        print('鼠标按下')
        if event.button()==Qt.LeftButton:
            self.startPoint=event.pos()
            self.endPoint=event.pos()
            self.isDrawing=True
            self.update()

    def mouseReleaseEvent(self,event):  #鼠标释放事件
        print('鼠标释放')
        if event.button() == Qt.LeftButton:
            self.endPoint=event.pos()
            self.isDrawing=False
            self.update()




class MainWindow(QMainWindow):
    def __init__(self,parent=None):
        super(MainWindow,self).__init__(parent)
        # 设置窗口标题和大小
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)

    def Screenshot(self):
        self.showMinimized() #最小化窗口
        # self.showNormal() #显示窗口
        # 截图
        screenshotName = self.ui.lineEdit.text() #截图文件名
        if not screenshotName:
            screenshotName=str(int(time.time()))
            self.ui.lineEdit.setText(screenshotName)
        screenshotName=screenshotName+'.png'
        pyautogui.screenshot(screenshotName) #保存截图
        ssw=screenshotWindow(screenshotName)
        self.showNormal()

        ssw.exec()

    def addOperate(self):
        fileName=self.ui.lineEdit.text()        # 获取文件名
        operate=self.ui.comboBox.currentText()  # 获取操作
        captureName=self.ui.lineEdit_2.text()   # 截图文件名
        inputText=self.ui.lineEdit_3.text()     # 输入文本
        if not fileName:
            # text='文件名: '+fileName+'  操作: '+operate+'  截图名: '+captureName+'  输入文本:'+inputText
            text2=fileName+' '+operate+' '+captureName+' '+inputText
        else:
            # text='文件名: '+fileName+'  操作: '+operate+'  截图名: '+captureName
            text2=fileName+' '+operate+' '+captureName

        with open(fileName+'.txt','a',encoding='utf-8') as f:
            f.write(text2+'\n')

        self.ui.listWidget.addItem(text2)

    def execution(self):
        self.showMinimized()
        fileName=self.ui.lineEdit.text()
        if not fileName:
            QMessageBox.warning(self,'警告','请输入文件名')
            return
        with open(fileName+'.txt','r',encoding='utf-8') as f:
            lines=f.readlines()
        x,y=None,None
        print('点击执行')
        for line in lines:
            if not line:
                continue
            line=line.strip().split(' ')
            print(line,len(line))
            if len(line)==2:
                if line[1]=='截图定位':
                    try:
                        x,y = pyautogui.locateCenterOnScreen(line[0]+'.png', grayscale=False, confidence=0.7)
                        print(x,y)
                    except:
                        QMessageBox.warning(self,'定位截图失败','请重新截图')
                        break
                elif line[1]=='鼠标单击':
                    pyautogui.click(x,y)
                    print('完成鼠标点击',x,y)
            elif len(line)==3:
                if line[1]=='输入文本':
                    pyautogui.write(line[-1])
                    print('完成输入文本',line[-1])
        self.showNormal()

    def deleteOpt(self):
        #删除
        item=self.ui.listWidget.takeItem(self.ui.listWidget.currentRow())
        self.ui.listWidget.removeItemWidget(item)

        with open(self.ui.lineEdit.text()+'.txt','r',encoding='utf-8') as f:
            lines=f.readlines()

        for i,line in enumerate(lines):
            if item.text() in line:
                lines.pop(i)
                with open(self.ui.lineEdit.text()+'.txt','w',encoding='utf-8') as f:
                    f.writelines(lines)

    def updateOpt(self):
        item=self.ui.listWidget.item(self.ui.listWidget.currentRow())
        itemText=item.text()
        print(itemText)

        text,ok=QInputDialog.getText(self,'更新','请输入更新内容',text=item.text())

        if ok:
            item.setText(text+'\n')

            self.ui.listWidget.setCurrentItem(item)
            print(text, ok)
            with open(self.ui.lineEdit.text()+'.txt','r+',encoding='utf-8') as f:
                lines=f.readlines()
            for i,line in enumerate(lines):
                print(item.text(),itemText,i,line)
                if itemText in line:

                    lines[i]=text+'\n'
                    with open(self.ui.lineEdit.text() + '.txt', 'w', encoding='utf-8') as f:
                        f.writelines(lines)
                else:
                    print('err',itemText,line)

    def openOpt(self):
        fileName=QFileDialog.getOpenFileName(self,'打开文件','','*.txt')
        print(fileName)

        with open(fileName[0],'r',encoding='utf-8') as f:
            lines=f.readlines()
        for line in lines:
            self.ui.listWidget.addItem(line)


if __name__ == '__main__':
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling) # 设置高DPI支持
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())