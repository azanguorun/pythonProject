from PyQt5.Qt import *


class CaculatorBtn(QPushButton):
    def __init__(self,parent=None,*args,**kwargs):
        super().__init__(parent,*args,**kwargs)
        # self.setAutoExclusive(True)
        self.setStyleSheet('''
            QPushButton[bg='gray']{
                color:white;
                background-color:rgb(88,88,88);
            }
            QPushButton[bg='gray']:hover{
                color:white;
                background-color:rgb(150,150,150);
            }
            QPushButton[bg='orange']{
                color:white;
                background-color:rgb(207,138,0);
            }
            QPushButton[bg='orange']:hover{
                background-color:rgb(238,159,0);
            }
            QPushButton[bg='orange']:checked{
                color:white;
                background-color:rgb(207,138,0);
            }
            QPushButton[bg='lightgray']{
                color:black;
                background-color:rgb(200,200,200);
            }
            QPushButton[bg='lightgray']:hover{
                background-color:rgb(230,230,230);
            }
        ''')
