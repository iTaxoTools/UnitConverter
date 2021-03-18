# -*- encoding:utf-8 -*-
import sys, os
from PyQt5.QtCore import QDir
from PyQt5.QtWidgets import *
import re
import sys, os
from PyQt5.uic import loadUiType
import pandas as pd
from PyQt5.QtGui import *
import ast

kk= {'v1': 1, 'v2': 0.000000001, 'v3': 1000, 'v4':1000000, 'v5':1000000000,
'v6':1000000000000000000, 'v7':1000000000000000000000000000, 'v8':1000,
'v9':10000, 'v10':100000, 'v11':1000000, 'v12':1000000000,
'v13':1000000000000, 'v14':1000000000000000, 'v15':1000000000000000000, 'v16':6.110257,
'v17':219.969248
}



def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)


def check(s):
    if s!= "":

        try:
            ss= float(s)
            return ss
        except:
            return None


class Method3:

    def textSonDurum(self, x):

        if self.checkBox.isChecked():
            num_format= "{:e}"


        else:
            num_format= "{}"


        map11= {'v1': self.v1, 'v2': self.v2, 'v3': self.v3, 'v4':self.v4, 'v5':self.v5,
        'v6':self.v6, 'v7':self.v7, 'v8':self.v8,
        'v9':self.v9, 'v10':self.v10,
        'v11':self.v11, 'v12':self.v12,
        'v13':self.v13, 'v14':self.v14, 'v15':self.v15, 'v16':self.v16, 'v17':self.v17
        }

        map22= {'v1': lambda tt: self.v1.setText(num_format.format(tt*1)),
                 'v2': lambda tt: self.v2.setText(num_format.format(tt*0.000000001)),
                  'v3': lambda tt: self.v3.setText(num_format.format(tt*1000)),
                  'v4':lambda tt: self.v4.setText(num_format.format(tt*1000000)),
                  'v5':lambda tt: self.v5.setText(num_format.format(tt*1000000000)),
                  'v6':lambda tt: self.v6.setText(num_format.format(tt*1000000000000000000)),
                  'v7':lambda tt: self.v7.setText(num_format.format(tt*1000000000000000000000000000)),
                  'v8':lambda tt: self.v8.setText(num_format.format(tt*1000)),
                  'v9':lambda tt: self.v9.setText(num_format.format(tt*10000)),
                  'v10':lambda tt: self.v10.setText(num_format.format(tt*100000)),
                  'v11':lambda tt: self.v11.setText(num_format.format(tt*1000000)),
                  'v12':lambda tt: self.v12.setText(num_format.format(tt*1000000000)),
                  'v13':lambda tt: self.v13.setText(num_format.format(tt*1000000000000)),
                  'v14':lambda tt: self.v14.setText(num_format.format(tt*1000000000000000)),
                  'v15':lambda tt: self.v15.setText(num_format.format(tt*1000000000000000000)),
                  'v16':lambda tt: self.v16.setText(num_format.format(tt*6.110257)),
                  'v17':lambda tt: self.v17.setText(num_format.format(tt*219.969248))
                  }


        s= map11[x]

        s= s.text()



        tt= check(s)
        if tt != None:

            tt= (1/kk[x])*tt

            for i in map22:
                if i != x:
                    func= map22[i]
                    func(tt)

        else:
            self.v1.setText("")
            self.v2.setText("")
            self.v3.setText("")
            self.v4.setText("")
            self.v5.setText("")
            self.v6.setText("")
            self.v7.setText("")
            self.v8.setText("")
            self.v9.setText("")
            self.v10.setText("")
            self.v11.setText("")
            self.v12.setText("")
            self.v13.setText("")
            self.v14.setText("")
            self.v15.setText("")
            self.v16.setText("")
            self.v17.setText("")
