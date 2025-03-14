from PyQt5.Qt import *
import sys

app = QApplication(sys.argv)
window = QWidget()
window.resize(500, 500)
window.setWindowTitle("文本编辑框案例")

window.move(100, 100)

ql=QLineEdit(window)
ql.move(100,100)
ql.resize(100,20)
ql.setPlaceholderText("请输入账号")


ql2=QLineEdit(window)
ql2.move(100,250)
ql2.resize(100,20)
# ql2.setReadOnly(True)  #只读
ql2.setInputMask(">A-9") #输入掩码
ql2.setInputMask("9999-9999999")



btn1=QPushButton(window)
btn1.setText("复制")
btn1.move(100,300)

def copy():
    # ql2.setText(ql.text())
    # print(ql2.text())

    print(ql2.isModified()) #获取修改状态
    ql2.setModified(False) #设置修改状态


btn1.clicked.connect(copy)
 # jishu jishu        jishu
window.show()
sys.exit(app.exec_())