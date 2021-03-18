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

kk= {'w1': 1, 'w2': 0.001, 'w3': 0.002204623, 'w4':0.03527397, 'w5':100,
'w6':1000, 'w7':1000000, 'w8':1000000000,
'w9':1000000000000, 'w10':60200000000000000000, 'w11': 60200000000000000000000,
'w12':0.000001, 'w13':0.000000001,
'w14':0.00001, 'w15':5, 'w16':0.000002204623
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


class Method4:

    def textSonDurum(self, x):

        if self.checkBox.isChecked():
            num_format= "{:e}"


        else:
            num_format= "{}"


        map11= {'w1': self.w1, 'w2': self.w2, 'w3': self.w3, 'w4':self.w4, 'w5':self.w5,
        'w6':self.w6, 'w7':self.w7, 'w8':self.w8,
        'w9':self.w9, 'w10':self.w10,
        'w11':self.w11, 'w12':self.w12,
        'w13':self.w13, 'w14':self.w14, 'w15':self.w15, 'w16':self.w16
        }

        kk= {'w1': 1, 'w2': 0.001, 'w3': 0.002204623, 'w4':0.03527397, 'w5':100,
        'w6':1000, 'w7':1000000, 'w8':1000000000,
        'w9':1000000000000, 'w10':60200000000000000000, 'w11': 60200000000000000000000,
        'w12':0.000001, 'w13':0.000000001,
        'w14':0.00001, 'w15':5, 'w16':0.000002204623
        }

        map22= {'w1': lambda tt: self.w1.setText(num_format.format(tt*1)),
                 'w2': lambda tt: self.w2.setText(num_format.format(tt*0.001)),
                  'w3': lambda tt: self.w3.setText(num_format.format(tt*0.002204623)),
                  'w4':lambda tt: self.w4.setText(num_format.format(tt*0.03527397)),
                  'w5':lambda tt: self.w5.setText(num_format.format(tt*100)),
                  'w6':lambda tt: self.w6.setText(num_format.format(tt*1000)),
                  'w7':lambda tt: self.w7.setText(num_format.format(tt*1000000)),
                  'w8':lambda tt: self.w8.setText(num_format.format(tt*1000000000)),
                  'w9':lambda tt: self.w9.setText(num_format.format(tt*1000000000000)),
                  'w10':lambda tt: self.w10.setText(num_format.format(tt*60200000000000000000)),
                  'w11':lambda tt: self.w11.setText(num_format.format(tt*60200000000000000000000)),
                  'w12':lambda tt: self.w12.setText(num_format.format(tt*0.000001)),
                  'w13':lambda tt: self.w13.setText(num_format.format(tt*0.000000001)),
                  'w14':lambda tt: self.w14.setText(num_format.format(tt*0.00001)),
                  'w15':lambda tt: self.w15.setText(num_format.format(tt*5)),
                  'w16':lambda tt: self.w16.setText(num_format.format(tt*0.000002204623))
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
            self.w1.setText("")
            self.w2.setText("")
            self.w3.setText("")
            self.w4.setText("")
            self.w5.setText("")
            self.w6.setText("")
            self.w7.setText("")
            self.w8.setText("")
            self.w9.setText("")
            self.w10.setText("")
            self.w11.setText("")
            self.w12.setText("")
            self.w13.setText("")
            self.w14.setText("")
            self.w15.setText("")
            self.w16.setText("")
