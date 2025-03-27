from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
import sys
import time
import requests
from bs4 import BeautifulSoup


class NewTaskThread(QThread):

    #信号 触发信号
    success=pyqtSignal(int,str,str,str)
    error=pyqtSignal(int,str,str,str)

    def __init__(self,row_index,asin,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.row_index=row_index
        self.asin=asin

    def run(self):
        '''具体线程'''
        self.success.emit(self.row_index,'xx','xx1','xx2')
        '''     
        伪代码
        try:
            url='https://www.amazon.com/gp/porduct/{}'.format(self.asin)
            res=requests.get(url)
            if res.status_code!=200:
                raise Exception('请求失败') #抛出异常
            soup=BeautifulSoup(res.text,'lxml')
            title=soup.find(id='productTitle').get_text().strip()
            url="{}/{}/ref=dp_cr_3?ie=utf8".format(url,self.asin)
            self.success.emit(self.row_index,self.asin,title,url)
        except Exception as e:
            title='{}请求失败'.format(self.asin)
            self.error.emit(self.row_index,self.asin,title,str(e))
        '''


