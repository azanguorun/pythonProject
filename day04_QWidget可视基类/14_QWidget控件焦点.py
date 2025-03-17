from PyQt5.Qt import *
import sys


app = QApplication(sys.argv)
window = QWidget()
window.resize(500, 500)
window.setWindowTitle("QWidget案例")

le1=QLineEdit(window)
le1.move(100,100)

le2=QLineEdit(window)
le2.move(100,150)

le3=QLineEdit(window)
le3.move(100,200)



window.show()
sys.exit(app.exec_())