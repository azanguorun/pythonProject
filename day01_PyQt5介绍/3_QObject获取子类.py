# coding:utf-8
"""
Project    : python_text
Time       ：2025/1/14 下午5:31
File       : 3.py
目的: 
内容:
结果:
"""
from PyQt5.Qt import * # 导入PyQt5的所有常用的一些库


# print(QObject.__subclasses__())  # 查看QObject的子类


def getSubClasses(cls):
    """
    获取类的所有子类
    :param cls:
    :return:
    """
    for subClass in cls.__subclasses__():
        print(subClass)
        if len(subClass.__subclasses__())>0:
            getSubClasses(subClass)

getSubClasses(QObject)