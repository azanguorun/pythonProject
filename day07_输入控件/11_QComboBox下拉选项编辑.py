from PyQt5.Qt import *
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(500, 500)
        self.setWindowTitle("QFrame的学习")
        self.setup_ui()

    def setup_ui(self):
        cb=QComboBox(self)
        cb.resize(100,30)
        cb.move(100,100)
        cb.addItems(["男","女"])
        cb.insertItem(2,QIcon("1.jpg"),"或")
        cb.insertItems(2,["1","2","3"])
        cb.down_arrow_icon=QIcon("1.jpg")



        cb.setItemText(3,"4")
        cb.insertSeparator(2) #插入分隔符
        cb.setCurrentIndex(1) #设置当前索引
        cb.setCurrentText("4") #设置当前文本

        cb.setEditable(True) #可编辑
        cb.setMaxVisibleItems(4) #最大可见项
        cb.setMaxCount(10) #最大项数
        cb.setDuplicatesEnabled(True) #允许重复项
        cb.setFrame(False) #设置边框
        cb.setIconSize(QSize(50,50)) #设置图标大小

        print(QAbstractItemModel.__subclasses__()) #获取所有的子类
        model=QStandardItemModel(cb) #创建模型
        item1=QStandardItem("1模型")
        item2=QStandardItem("2模型")
        item3=QStandardItem("3模型")
        model.appendRow(item1)
        model.appendRow(item2)
        model.appendRow(item3)
        cb.setModel(model) #设置模型
        # cb.setView(QTreeView) #设置视图

        btn=QPushButton(self)
        btn.setText("测试按钮")
        btn.move(100,150)
        # btn.clicked.connect(lambda :print(cb.currentText()))
        # btn.clicked.connect(lambda :print(cb.currentIndex()))
        # btn.clicked.connect(lambda :print(cb.currentData()))
        # btn.clicked.connect(lambda :print(cb.currentData(Qt.UserRole)))
        # btn.clicked.connect(lambda :print(cb.itemText(1)))
        # btn.clicked.connect(lambda :print(cb.it))

        cb.setMaxCount(10) #最大项数
        cb.setDuplicatesEnabled(True) #允许重复项
        btn.clicked.connect(lambda :cb.addItems('it')) #获取项数

        cb.setDuplicatesEnabled(True) #允许重复项
        cb.setIconSize(QSize(50,50)) #设置图标大小
        cb.setSizeAdjustPolicy(QComboBox.AdjustToContents) #设置大小调整策略
        cb.activated.connect(lambda val:print("激活了",val)) #激活了
        cb.activated[str].connect(lambda val:print("激活了",val)) #激活了

        cb.currentIndexChanged.connect(lambda val:print("当前索引改变了",val)) #当前索引改变了

        cb.currentTextChanged[str].connect(lambda val:print("当前索引改变了",val)) #当前索引改变了


        lable = QLabel(self)
        lable.move(100, 250)
        lable.setText("测试标签")
        fcb=QFontComboBox(self)
        fcb.move(100,200)
        fcb.currentFontChanged.connect(lambda val:lable.setFont(val)) #当前字体改变了
        fcb.setEditable(True) #可编辑


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()

    sys.exit(app.exec_())