from PyQt5.Qt import *
import sys

app = QApplication(sys.argv)
window = QWidget()
window.resize(500, 500)
window.setWindowTitle("文本编辑框案例")

window.move(100, 100)

d=QDialog() #对话框
# d.accept() #关闭对话框
# d.reject() #关闭对话框
# d.done(0) #关闭对话框
# d.exec_() #阻塞
btn=QPushButton(d)
btn.setText("按钮1")
btn.move(20,20)
btn.clicked.connect(lambda :d.accept()) #关闭对话框

btn2=QPushButton(d)
btn2.setText("按钮2")
btn2.move(60,60)
# btn2.clicked.connect(lambda :d.reject()) #关闭对话框
btn2.clicked.connect(lambda :print(d.result())) #关闭对话框

btn3=QPushButton(d)
btn3.setText("按钮3")
btn3.move(60,160)
# btn3.clicked.connect(lambda :d.done(8)) #关闭对话框
btn3.clicked.connect(lambda :d.setResult(888)) #关闭对话框


d.accepted.connect(lambda :print("被接受"))
d.rejected.connect(lambda :print("被拒绝"))
d.finished.connect(lambda val:print("结束",val))

d.setWindowTitle("对话框")
# d.setWindowModality(Qt.WindowModal) #应用程序级别
# d.setSizeGripEnabled(True) #右下角的大小控制点
# d.open() #非阻塞
# d.exec_() #阻塞

result=d.exec()#阻塞
print(result)
d.show()


window.show()
sys.exit(app.exec_())