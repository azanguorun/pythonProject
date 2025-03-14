from PyQt5.Qt import *
import sys

app = QApplication(sys.argv)
window = QWidget()
window.resize(500, 500)
window.setWindowTitle("QWidget案例")


red=QWidget(window)
red.resize(100,100)
red.setStyleSheet("background-color:red;")
red.move(50,50)

green=QWidget(window)
green.resize(100,100)
green.setStyleSheet("background-color:green;")
green.move(red.x()+red.width(),red.y()+red.height())



window.move(100, 100)

#单选按钮
btn_man=QRadioButton("男",red)
btn_man.setChecked(True)
btn_man.setShortcut("Alt+M")
btn_woman=QRadioButton("女",red)


btn_woman.move(40,0)

# btn_woman.setIconSize(QSize(50,50))
# btn_woman.setIcon(QIcon("1.jpg"))
btn_woman.toggled.connect(lambda isChecked:print("选中状态发生了改变",isChecked))

# btn_woman.setAutoExclusive(False)

btn_yes=QRadioButton("是",green)
btn_yes.move(0,40)
btn_no=QRadioButton("否",green)
btn_no.move(40,40)

window.show()
sys.exit(app.exec_())