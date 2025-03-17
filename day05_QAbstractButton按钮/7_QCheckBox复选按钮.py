from PyQt5.Qt import *
import sys

app = QApplication(sys.argv)
window = QWidget()
window.resize(500, 500)
window.setWindowTitle("QWidget案例")

window.move(100, 100)


print(QCheckBox.__bases__)

cd=QCheckBox("复选框",window)
cd.setIcon(QIcon("1.jpg"))
cd.setIconSize(QSize(50,50))
cd.setTristate(True) # 三态
cd.setCheckState(Qt.PartiallyChecked) # 半选状态`

cd.stateChanged.connect(lambda state:print(state))  # 状态改变
cd.toggled.connect(lambda isChecked:print(isChecked)) # 状态切换
window.show()
sys.exit(app.exec_())