from PyQt5.Qt import *
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(500, 500)
        self.setWindowTitle("QFrame的学习")
        self.setup_ui()

    def setup_ui(self):
        # self.setStyleSheet("background-color:cyan;")
        QColorDialog.setCustomColor(10, QColor(100, 100, 100)) #设置自定义颜色
        QColorDialog.setStandardColor(20, QColor(100, 100, 100)) #设置标准颜色
        cd=QColorDialog(QColor(255,0,0),self)
        cd.setWindowTitle("选择颜色")

        def color(col):
            palette = QPalette() #调色板
            # palette.setColor(QPalette.Background,col) #设置背景色
            palette.setColor(QPalette.Background,cd.currentColor()) #设置按钮文字颜色
            self.setPalette(palette) #设置调色板

        # cd.colorSelected.connect(lambda color:print(color.name()))
        # cd.colorSelected.connect(color)
        cd.currentColorChanged.connect(color) #设置值改变信号
        cd.setOptions(QColorDialog.NoButtons | QColorDialog.ShowAlphaChannel) #设置不使用原生对话框
        # cd.open()

        btn=QPushButton(self)
        btn.setText("按钮")
        btn.move(100,100)
        btn.clicked.connect(lambda :print(cd.customCount())) #  customCount方法  是静态方法，即使源码中self，通过实例对象可以调用  通过类名也可以调用
        btn.clicked.connect(lambda :print(QColorDialog.customCount())) #打开文件对话框

        def test():
            color=QColorDialog.getColor(QColor(255,0,0),self,"选择颜色",QColorDialog.ShowAlphaChannel)
            palette = QPalette() #调色板
            palette.setColor(QPalette.Background,color) #设置背景色
            self.setPalette(palette) #设置调色板
            print(color)
        # btn.clicked.connect(lambda :QColorDialog.setCustomColor(0,QColor(100,100,100))) #  selectedColor方法  是实例方法，必须通过实例对象调用   在颜色对话框创建之前创建

        # btn.clicked.connect(test) #打开文件对话框

        btn2=QPushButton(self)
        btn2.setText('按钮2')
        btn2.move(100,200)

        def test2():
            cd=QColorDialog(self)
            cd.setOption(QColorDialog.NoButtons,True)
            cd.setWindowTitle("选择颜色")

            def sel_color(color):
                palette = QPalette()  # 调色板
                palette.setColor(QPalette.ButtonText, color)  # 设置背景色
                self.setPalette(palette)  # 设置调色板
            # cd.colorSelected.connect(sel_color)
            cd.currentColorChanged.connect(sel_color)

            cd.show()

        btn2.clicked.connect(test2)
        cd.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_()) #