from PyQt5.Qt import *
import sys

app=QApplication(sys.argv)


window=QWidget()

window.resize(500,500)
window.move(100,100)
window.setWindowTitle("QWidget案例")
window.setMinimumSize(100,100) #最小尺寸
window.setMaximumSize(1000,1000) #最大尺寸
window.setMinimumWidth(100)  #最小宽度

# window.setFixedSize(500,500) #固定大小


label=QLabel(window)
label.setText("标签")
label.resize(300,300)
label.move(100,100)
label.setContentsMargins(100,200,0,0) #设置内容边距
label.setStyleSheet("background-color:red;")

print(label.contentsRect())
window.show()
sys.exit(app.exec_())