from PyQt5.Qt import *
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(500, 500)
        self.setWindowTitle("Q的学习")
        self.setup_ui()
    def setup_ui(self):
        # em=QErrorMessage(self)
        # em.setWindowTitle('错误提示')
        # em.showMessage('错误信息')
        # em.open()

        # QErrorMessage.qtHandler()
        # qDebug('Debug')
        # qWarning('Warning')

        pd=QProgressDialog('进度条','12',1,100,self)
        pd.setMinimumDuration(1000) #设置最小时间
        pd.setLabelText('正在下载...')
        pd.setCancelButtonText('取消')
        pd.setAutoReset(False) #自动重置
        pd.show()

        timer=QTimer(pd)

        def test():
            if pd.value()>=pd.maximum() or pd.wasCanceled():
                timer.stop()
                pd.accept() #关闭
            pd.setValue(pd.value()+1)

            if pd.value()==50:
                pd.cancel() #取消
        timer.timeout.connect(test)
        timer.start(100)

        pd.canceled.connect(timer.stop)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()

    sys.exit(app.exec_())