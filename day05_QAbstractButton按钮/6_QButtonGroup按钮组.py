from PyQt5.Qt import *
import sys

app = QApplication(sys.argv)
window = QWidget()
window.resize(500, 500)
window.setWindowTitle("QWidget案例")

window.move(100, 100)


m=QRadioButton("男",window)
f=QRadioButton("女",window)
m.move(100,100)
f.move(100,150)
m.setChecked(True)
m.toggled.connect(lambda isChecked:print("男",isChecked))

sexGroup=QButtonGroup(window)
sexGroup.addButton(m,1)
sexGroup.addButton(f,2)


y=QRadioButton("是",window)
n=QRadioButton("否",window)
y.move(200,100)
n.move(200,150)
y.setChecked(True)
y.toggled.connect(lambda isChecked:print("是",isChecked))

answerGroup=QButtonGroup(window)
answerGroup.addButton(y,1)
answerGroup.addButton(n,2)

answerGroup.setId(y,1)
answerGroup.setId(n,2)
print(answerGroup.id(y))
print(answerGroup.checkedId())

# sexGroup.setExclusive(False) # 取消排他性
# sexGroup.removeButton(f)  # 移除按钮


# print(sexGroup.buttons())
# print(sexGroup.button(2))
# print(sexGroup.id(m))
# print(sexGroup.checkedButton())

def test(val):
    print(val)


sexGroup.buttonToggled.connect(test)
sexGroup.buttonClicked[int].connect(test)

window.show()
sys.exit(app.exec_())