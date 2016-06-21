# -*- coding: utf-8 -*-

'''
@author liubin
@time 2016.06.21 09:03
实现窗口出现图标
'''

import sys
from PyQt4 import QtGui

class Icon(QtGui.QWidget):
    def __init__(self,parent=None):
        QtGui.QWidget.__init__(self,parent)

        self.setGeometry(300,300,400,300)
        #以上四个值分别是(x,y,a,b)x,y为窗体的位置 a,b为窗体的宽度和高度
        self.setWindowTitle('Encrypt--bin')
        self.setWindowIcon(QtGui.QIcon('E:\\python\\secourity\\Littlesoft_encrypt\\whut.png'))
        #创建了QIcon对象,并接受了图标路径

Awindow = QtGui.QApplication(sys.argv)
aicon =Icon()
aicon.show()
sys.exit(Awindow.exec_())


