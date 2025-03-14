from PyQt5.Qt import *
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(500, 500)
        self.setWindowTitle("QFrame的学习")
        self.city_dic={
            "北京": {
                "东城":'001',
                "西城":'002',
                "朝阳":'003',
                "丰台":'004',
            },
            "上海": {
                "黄埔":'001',
                "徐汇":'002',
                "长宁":'003',
                "静安":'004',
            },
            "广州": {
                "番禺":'002',
                "天河":'003',
                "白云":'004',
            },
        }
        self.setup_ui()

    def setup_ui(self):
        pro=QComboBox(self)
        city=QComboBox(self)
        self.pro=pro
        self.city=city
        pro.move(100,100)
        city.move(200,100)

        #先连接信号，再设置数据
        pro.currentTextChanged[str].connect(self.pro_change)
        # pro.setCurrentIndex(0)
        # self.pro_change(pro.currentText())

        city.currentTextChanged[str].connect(self.city_change)

        city.currentIndexChanged[int].connect(self.city_change2)  #索引改变

        pro.addItems(self.city_dic.keys()) #添加项目


    def pro_change(self,text):
        print(text)
        city=self.city_dic[text]
        print(city)
        self.city.blockSignals(True)
        self.city.clear()
        self.city.blockSignals(False)
        # self.city.addItems(city.keys())
        for k,v in city.items():
            self.city.addItem(k,v)

    def city_change(self,text):
        print(text)

    def city_change2(self,index):
        print(index)
        print(self.city.itemText(index))
        print(self.city.itemData(index))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()

    sys.exit(app.exec_())