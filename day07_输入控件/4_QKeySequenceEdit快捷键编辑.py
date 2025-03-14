from PyQt5.Qt import *
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(500, 500)
        self.setWindowTitle("QFrame的学习")
        self.setup_ui()
    def setup_ui(self):
        kse=QKeySequenceEdit(self) #快捷键编辑框
        # ks=QKeySequence('Ctrl+C')
        ks=QKeySequence(Qt.CTRL+Qt.Key_C)
        kse.setKeySequence(QKeySequence.Copy)
        kse.setKeySequence(ks)

        btn=QPushButton(self)
        btn.setText("测试按钮")
        btn.move(100,100)
        btn.pressed.connect(lambda :print(kse.keySequence().toString(),kse.keySequence().count()))

        kse.editingFinished.connect(lambda :print('编辑完成'))
        kse.keySequenceChanged.connect(lambda v:print('键值改变',v.toString()))



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()

    sys.exit(app.exec_())