from PyQt5.Qt import *
import sys

app = QApplication(sys.argv)
window = QWidget()
window.resize(500, 500)
window.setWindowTitle("QWidget案例")

window.move(100, 100)

btn=QCommandLinkButton("标题","描述",window)

btn.setDescription("描述123")

window.show()
sys.exit(app.exec_())