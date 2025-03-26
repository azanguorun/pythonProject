import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel,QDesktopWidget,QHBoxLayout,QVBoxLayout
from PyQt5.QtWidgets import *
import os
import json

BASE_DIR=os.path.dirname(os.path.realpath(sys.argv[0]))  # 获取当前文件的路径

STATUS_MAPPING = {
    0: '初始化中',
    1: '待执行',
    2: '正在执行',
    3: '完成并提醒',
    10: '异常并停止',
    11: '初始化失败',
} #状态映射


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QFrame的学习")
        self.resize(1220, 300)

        qr=self.frameGeometry()
        cp=QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)

        #方向布局
        layout=QVBoxLayout()
        #创建布局
        layout.addLayout(self.init_header())
        layout.addLayout(self.init_form())
        layout.addLayout(self.init_table())
        layout.addLayout(self.init_footer())
        #给窗口设置元素的排列方式
        self.setLayout(layout)

    def init_header(self):
        # 1. 创建顶部菜单布局
        header_layout = QHBoxLayout()
        btn_start = QPushButton('开始')
        btn_stop = QPushButton('停止')
        btn_help = QPushButton('帮助')
        header_layout.addWidget(btn_start)
        header_layout.addWidget(btn_stop)
        header_layout.addStretch()  # 加弹簧分割
        header_layout.addWidget(btn_help)
        return header_layout

    def init_form(self):
        # 2. 创建上面标题布局
        form_layout = QHBoxLayout()
        txt_asin = QLineEdit()
        txt_asin.setPlaceholderText('请输入商品ID和价格')
        btn_add = QPushButton('添加')
        form_layout.addWidget(txt_asin)
        form_layout.addWidget(btn_add)
        return form_layout

    def init_table(self):
        # 3. 创建中间内容布局
        table_layout = QHBoxLayout()
        table_widget = QTableWidget(0, 8)
        table_header = [
            {"field": "asinssss", "text": "ASIN", "width": 120},
            {"field": "title", "text": "标题", "width": 150},
            {"field": "url", "text": "url", "width": 400},
            {"field": "price", "text": "价格", "width": 100},
            {"field": "success", "text": "成功次数", "width": 100},
            {"field": "error", "text": "失败次数", "width": 100},
            {"field": "status", "text": "状态", "width": 100},
            {"field": "frequency", "text": "频率(n/s)", "width": 100},
        ]
        for index, info in enumerate(table_header):
            item = QTableWidgetItem()
            item.setText(info['text'])
            table_widget.setHorizontalHeaderItem(index, item)
            table_widget.setColumnWidth(index, info['width'])

        file_path = os.path.join(BASE_DIR,'db', 'amazon.json')
        with open(file_path, 'r', encoding='utf-8') as f:
            data = f.read()
        data_list=json.loads(data)
        current_row_count=table_widget.rowCount()
        for row_list in data_list:
            print(row_list)
            table_widget.insertRow(current_row_count) #插入一行
            for i,ele in enumerate(row_list):
                row_list[ele]=STATUS_MAPPING.get(row_list[ele]) if i==6 else row_list[ele]
                cell=QTableWidgetItem(str(row_list[ele])) #创建单元格
                if i in [0,4,5,6]:
                    cell.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)  # 设置 0,4,5,6 单元格不可编辑   要在创建单元格后设置
                table_widget.setItem(current_row_count,i,cell)
            current_row_count+=1
        table_layout.addWidget(table_widget)
        return table_layout


    def init_footer(self):
        # 4. 创建底部菜单布局
        footer_layout = QHBoxLayout()

        lable_status = QLabel('未检测', self)
        footer_layout.addWidget(lable_status)
        footer_layout.addStretch()

        btn_reinit = QPushButton('重新初始化')
        footer_layout.addWidget(btn_reinit)

        btn_recheck = QPushButton('重新检测')
        footer_layout.addWidget(btn_recheck)

        btn_reset_count = QPushButton('重置次数')
        footer_layout.addWidget(btn_reset_count)

        btn_delete = QPushButton('删除')
        footer_layout.addWidget(btn_delete)

        btn_alert = QPushButton('SMTP报警配置')
        footer_layout.addWidget(btn_alert)

        btn_proxy = QPushButton('代理配置')
        footer_layout.addWidget(btn_proxy)
        return footer_layout

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())