from PyQt5.Qt import *
import sys

app = QApplication(sys.argv)
window = QWidget()
window.resize(500, 500)
window.setWindowTitle("文本编辑框案例")

window.move(100, 100)

ql=QLineEdit("请输入账号",window)
btn=QPushButton(window)
btn.setText("按钮")
btn.move(0,30)
btn.pressed.connect(lambda :ql.insert("abc"))


ql1=QLineEdit(window)
ql1.move(0,100)
ql2=QLineEdit(window)
ql2.move(0,150)
ql2.setEchoMode(QLineEdit.Password) #枚举值 密码模式


btn1=QPushButton(window)
btn1.setText("复制")
btn1.move(0,200)

def copy():
    ql2.setText(ql1.text())
    print(ql2.text())

btn1.pressed.connect(copy)

window.show()
sys.exit(app.exec_())