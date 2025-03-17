from PyQt5.Qt import *
import sys

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("文本编辑框案例")
QFrame
frame=QFrame(window)
frame.resize(window.width()-10,window.height()-10)
frame.move(5,5)
frame.setStyleSheet("background-color:cyan;")

# frame.setFrameShape(QFrame.Panel) #设置形状  Panel 枚举值
# frame.setFrameShadow(QFrame.Raised) #设置阴影
frame.setFrameStyle(QFrame.Panel | QFrame.Raised)

frame.setLineWidth(4) #设置线宽
frame.setMidLineWidth(10) #设置中线宽


frame.setFrameRect(QRect(0,0,100,100)) #设置边框矩形

print(frame.frameWidth()) #获取线宽
print(frame.frameShadow()) #获取阴影
print(frame.frameShape()) #获取形状
print(frame.midLineWidth()) #获取中线宽

window.show()
sys.exit(app.exec_())