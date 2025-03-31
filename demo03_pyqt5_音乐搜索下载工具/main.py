'''

https://freetyst.nf.migu.cn/public/product9th/product46/2023/01/1715/2022%E5%B9%B411%E6%9C%8814%E6%97%A511%E7%82%B919%E5%88%86%E5%86%85%E5%AE%B9%E5%87%86%E5%85%A5%E6%96%B0%E8%88%AA%E9%81%9350557%E9%A6%96923799/%E6%A0%87%E6%B8%85%E9%AB%98%E6%B8%85/MP3_320_16_Stero/6903170AKAZ152610.mp3?

channelid=02
&msisdn=00c802bc-62ca-4bc1-bc47-e6c2e9d10c9c
&Tim=1730963251652
&Key=df1dc8cec84b489b


'''

from PyQt5.QtWidgets import QApplication, QMainWindow,QMessageBox
import sys
from music_ui import Ui_MainWindow
import re
import requests

class MainWindow(QMainWindow):
    def __init__(self,parent=None):
        super(MainWindow,self).__init__(parent)
        # 设置窗口标题和大小
        self.setWindowTitle("Music Player")
        self.ui=Ui_MainWindow()
        self.firstRe=re.compile(r'^[0-9]')
        self.ui.setupUi(self)
        self.song={}


    def QueryMusic(self):
        music_name=self.ui.lineEdit.text()
        print('正在搜索音乐...',music_name)
        #音乐解析
        url='https://music.zhuolin.wang/plugns/api.php?types=search&count=20&source=freemp3&pages=1&name='+music_name
        response=requests.get(url)
        # 解析json数据
        music_list=response.json()
        print(music_list)
        for music in music_list:
            music_name=music['name']
            artist=music['artist'][0]
            self.ui.listWidget.addItem(music_name+' - '+str(artist))
            self.song[music_name+' - '+str(artist)]=music['url']

    def downloadMusic(self,item):
        # music_name=self.ui.lineEdit.text()
        print('正在下载音乐...',item.text(),self.song[item.text()])
        #音乐解析
        conf=QMessageBox.information(self,'下载提示','是否下载' ,QMessageBox.Yes|QMessageBox.No,QMessageBox.Yes)
        if conf==QMessageBox.Yes:
            url=self.song[item.text()]
            request=requests.get(url)
            with open('{}.mp3'.format(item.text()),'wb') as f:
                f.write(request.content)
            QMessageBox.information(self,'下载音乐','下载成功')



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())