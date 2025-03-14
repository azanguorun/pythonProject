from PyQt5.Qt import *
import sys

app = QApplication(sys.argv)
window = QWidget()
window.resize(500, 500)
window.setWindowTitle("文本编辑框案例")

window.move(100, 100)

ql=QLineEdit(window)
ql.move(100,100)
ql.resize(200,200)
ql.setPlaceholderText("请输入账号")


window.show()
sys.exit(app.exec_())