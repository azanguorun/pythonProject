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


class TaskThread(QThread):
    '''线程类'''
    start_sighal=pyqtSignal(int)
    stop_sighal=pyqtSignal(int)
    counter_sighal=pyqtSignal(int)
    error_counter_sighal=pyqtSignal(int)

    def __init__(self,Scheduler,log_path,row_list,asin,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.scheduler=Scheduler
        self.row_list=row_list
        self.asin=asin
        self.log_path=log_path

    def run(self):
        '''具体线程'''
        self.start_sighal.emit(self.row_list)
        import time
        import random
        while True:
            if self.scheduler.terminate:
                self.stop_sighal.emit(self.row_list)
                self.scheduler.destroy_thread(self) #self 是线程对象
                #线程在列表中移除掉
                return #终止线程


            try:
                time.sleep(random.randint(1,2))
                self.counter_sighal.emit(self.row_list)

                with open(self.log_path,'a',encoding='utf8') as f:
                    f.write('{}日志\n'.format(self.asin))
                #监控价格
                #根据型号访问bs4获取数据
                #价格是否小于预期
                #发送报警
            except Exception as e:
                print(e)
                self.error_counter_sighal.emit(self.row_list)


class StopThread(QThread):
    '''线程类'''
    update_sighal=pyqtSignal(str)

    def __init__(self,scheduler,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.scheduler=scheduler

    def run(self):
        '''具体线程'''
        while True:
            total=len(self.scheduler.thread_list) #总线程数
            self.update_sighal.emit('存活数据{}'.format(total))
            if total==0:
                break
            time.sleep(0.5)

        self.update_sighal.emit('所有线程已停止')

class StopThread(QThread):
    update_sighal=pyqtSignal(str)

    def __init__(self,scheduler,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.scheduler=scheduler

    def run(self):
        while True:
            total=len(self.scheduler.thread_list) #总线程数
            self.update_sighal.emit('存活{}'.format(total))
            if total==0:
                break
            time.sleep(0.5)
        self.update_sighal.emit('所有线程已停止')