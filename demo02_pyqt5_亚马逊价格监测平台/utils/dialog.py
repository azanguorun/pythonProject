from PyQt5.Qt import *
import sys
import os
import json

class AlertDialog(QDialog):
    def __init__(self):
        super().__init__()
        #注意： data_dict 字典 要在  init_ui 前定向才有效
        self.data_dict={}
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('邮箱SMTP报警配置')
        self.resize(300, 270)
        layout = QVBoxLayout(self) #表单布局

        form_data_list=[
            {'title':'用户名','filed':'smtp'},
            {'title':'发件箱','filed':'from'},
            {'title':'密码','filed':'pwd'},
            {'title':'收件人(多个,分割)','filed':'to'},
        ]

        old_alert_dict={}
        if os.path.exists(os.path.join('db','config.json')):
            file_path=open(os.path.join('db','config.json'),'r',encoding='utf8')
            old_alert_dict=json.load(file_path)




        for form_data in form_data_list:
            label=QLabel(form_data['title'])
            layout.addWidget(label)
            line_edit=QLineEdit()
            layout.addWidget(line_edit)

            filed=form_data['filed']
            if filed in old_alert_dict:
                line_edit.setText(old_alert_dict[filed])


            self.data_dict[form_data['filed']]=line_edit

        btn_eve=QPushButton('保存')
        btn_eve.clicked.connect(self.event_save_click)
        layout.addWidget(btn_eve,0,Qt.AlignRight) #设置对齐方式
        layout.addStretch(1)
        self.setLayout(layout)


    def event_save_click(self):
        print('保存')
        # print(self.data_dict)
        save_dict={}
        for key,line_edit in self.data_dict.items():
            save_dict[key]=line_edit.text().strip()
            if not save_dict[key]:
                QMessageBox.warning(self,'警告','{}不能为空'.format(key))
                return

        print(save_dict)  #{'smtp': '123', 'from': '1111', 'pwd': '2222', 'to': '3333'}



        file_path=open(os.path.join('db','config.json'),'w',encoding='utf8')
        json.dump(save_dict,file_path)
        file_path.close()

        self.close() #关闭窗口


class ProxyDialog(QDialog):
    def __init__(self):
        super().__init__()
        #注意： data_dict 字典 要在  init_ui 前定向才有效
        self.init_ui()


    def init_ui(self):
        self.setWindowTitle('代理配置')
        self.resize(300, 270)
        layout = QVBoxLayout(self) #表单布局
        line=QTextEdit()
        line.setPlaceholderText('请输入代理地址')
        self.line=line

        ip=''
        if os.path.exists(os.path.join('db', 'ip.txt')):
            file_path = open(os.path.join('db', 'ip.txt'), 'r', encoding='utf8')
            for i in file_path.readlines():
                ip+=i.strip()+'\n'
            file_path.close()

        line.setText(ip)


        layout.addWidget(line)

        btn=QHBoxLayout()
        btn_eve=QPushButton('保存')
        btn_eve.clicked.connect(self.event_save_click)
        btn.addWidget(btn_eve,0,Qt.AlignRight) #设置对齐方式
        layout.addLayout(btn)

    def event_save_click(self):
        print('保存')
        ls=self.line.toPlainText()
        file_path = open(os.path.join('db', 'ip.txt'), 'w', encoding='utf8')
        for i in ls.split('\n'):
            file_path.write(i+'\n')

        file_path.close()


        self.close() #关闭窗口


class LogDialog(QDialog):
    def __init__(self,asin,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.asin=asin
        #注意： data_dict 字典 要在  init_ui 前定向才有效
        self.init_ui()
    def init_ui(self):
        self.setWindowTitle('日志配置')
        self.resize(300, 270)
        layout = QVBoxLayout(self) #表单布局

        text_edit=QTextEdit()
        self.text_edit=text_edit
        text_edit.setText('')

        layout.addWidget(text_edit)
        self.setLayout(layout)

        file_path=os.path.join('log','{}.log'.format(self.asin))
        if not os.path.exists(file_path):
            return
        with open(file_path,'r',encoding='utf8') as f:
            content=f.read()
        text_edit.setText(content)


