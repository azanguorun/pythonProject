from PyQt5.Qt import *
import sys
from resource.caculator_ui import Ui_Form



class Caculator(QObject):

    show_caculator=pyqtSignal(str)

    #计算业务工具类   继承QObject 是从内存管理层面考虑，到时候在内部自定义信号，自定义信号必须基于QObject
    def __init__(self,parent=None,*args,**kwargs):
        super().__init__(parent,*args,**kwargs)
        #数字键位
        self.key_models=[]

    def caculate(self):
        if len(self.key_models)>0 and self.key_models[-1]['role']=='operator':
            self.key_models.pop(-1)
        expression=''
        for model in self.key_models:
            expression+=model['title']
        result=eval(expression)
        print(result)
        return result

    def parse_key_model(self,key_model):
        # print(key)
        if key_model['role']=='clear':
            print('清空')
            self.key_models.clear()
            self.show_caculator.emit('0.0')

        if key_model['role']=='caculate':
            print('计算')
            result=self.caculate()
            self.show_caculator.emit(str(result))
            self.key_models.clear()

        if len(self.key_models)==0:
            if key_model['role']=='num':
                if key_model['title']=='.':
                    key_model['title']='0.'
                self.key_models.append(key_model)
                self.show_caculator.emit(self.key_models[-1]['title'])
                print(self.key_models)
            return None

        if key_model['title'] in ('%','+/-'):
            if self.key_models[-1]['role']!='num':
                return None
            else:
                if key_model['title']=='%':
                    self.key_models[-1]['title']=str(float(self.key_models[-1]['title'])/100)
                elif key_model['title']=='+/-':
                    self.key_models[-1]['title']=str(float(self.key_models[-1]['title'])*-1)
                self.show_caculator.emit(self.key_models[-1]['title'])

            print(self.key_models)
            return None

        if key_model['title']=='.':
            if self.key_models[-1]['role']=='num':
                if self.key_models[-1]['title'].__contains__('.'):
                    return None
                else:
                    self.key_models[-1]['title']+='.'
                    return None

        if key_model['role']==self.key_models[-1]['role']: #如果是同一个键位，就把title添加到最后一个键位的title后面
            if key_model['role']=='num':  #如果是数字键位，就把数字添加到最后一个键位的title后面
                if key_model['title']=='.' and self.key_models[-1]['title'].__contains__("."): #如果是小数点，就不添加:
                    return None
                if self.key_models[-1]['title']!='0': #如果是0，就不添加
                    self.key_models[-1]['title']+=key_model['title'] #把数字添加到最后一个键位的title后面
                else:
                    self.key_models[-1]['title']=key_model['title'] #把数字添加到最后一个键位的title后面
                self.show_caculator.emit(self.key_models[-1]['title'])
            if key_model['role']=='operator': #如果是运算符键位，就把运算符添加到最后一个键位的title后面
                self.key_models[-1]['title'] =key_model['title'] #把运算符添加到最后一个键位的title后面
                self.show_caculator.emit(str(self.caculate()))
        else:
            if key_model['title'] in ('%','.','/+-'):
                return None
            if key_model['role']=='num':
                self.show_caculator.emit(key_model['title'])
            elif key_model['role']=='operator':
                self.show_caculator.emit(str(self.caculate()))
            self.key_models.append(key_model)

        print(self.key_models)
# QTDesigner
class CaculatorPane(QWidget, Ui_Form):
    #定义新的信号

    def __init__(self,parent=None,*args,**kwargs):
        super().__init__(parent,*args,**kwargs)
        self.setAttribute(Qt.WA_StyledBackground, True)  # 设置样式表
        self.setupUi(self)
        self.caculator = Caculator(self)
        self.caculator.show_caculator.connect(self.show_caculator)

    def show_caculator(self,content):
        self.lineEdit.setText(content)

    def get_key(self,title,role):
        # print(title,role)
        self.caculator.parse_key_model({'title':title,'role':role})

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = CaculatorPane()
    window.show()
    sys.exit(app.exec_())