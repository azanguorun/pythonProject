


from PyQt5.Qt import *
import sys


class Mywindow(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__( *args, **kwargs)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setWindowOpacity(0.9)

        self.resize(500, 500)
        # window.move(100, 100)
        self.setWindowTitle("QWidget案例")
        self.top_margin = 10
        self.btn_w = 80
        self.btn_h = 30

        self.setup_ui()

    #公共数据
    def setup_ui(self):
        # 添加子控件按钮
        close_btn = QPushButton(self)
        close_btn.setText("关闭")
        close_btn.resize(self.btn_w, self.btn_h)
        close_btn.pressed.connect(self.close)
        self.close_btn = close_btn

        max_btn = QPushButton(self)
        max_btn.setText("最大化")
        max_btn.resize(self.btn_w, self.btn_h)

        def max_normal():
            if self.isMaximized():
                self.showNormal()
                max_btn.setText("最大化")
            else:
                self.showMaximized()
                max_btn.setText("还原")

        max_btn.pressed.connect(max_normal)
        self.max_btn = max_btn

        min_btn = QPushButton(self)
        min_btn.setText("最小化")
        min_btn.resize(self.btn_w, self.btn_h)
        min_btn.pressed.connect(self.showMinimized)
        self.min_btn = min_btn


    def resizeEvent(self, a0):
        print('窗口大小改变了')
        self.close_btn.move(self.width() - self.close_btn.width(), self.top_margin)
        self.max_btn.move(self.width() - self.max_btn.width() - self.close_btn.width(), self.top_margin)
        self.min_btn.move(self.width() - self.min_btn.width() - self.close_btn.width() - self.max_btn.width(), self.top_margin)


app = QApplication(sys.argv)
window = Mywindow()










window.show()
sys.exit(app.exec_())