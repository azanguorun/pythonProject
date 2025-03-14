from PyQt5.Qt import *
import sys



app = QApplication(sys.argv)

window = QWidget() #创建窗口  不传值
window.move(100,100)
window.resize(500,500)

window.setStatusTip("这是窗口状态提示")
print(window.x())
print(window.pos())
print(window.width())
red=QWidget(window)

def changeCao():
    new_content=label.text()+"标签"
    label.setText(new_content)
    # label.resize(label.width()+10)
    label.adjustSize() #自动调整大小

label=QLabel(window)
label.setText('标签')
label.move(100,100)



btn=QPushButton(window)
btn.setText('按钮')
btn.move(100,300)
btn.clicked.connect(changeCao)


window.show()

sys.exit(app.exec_())