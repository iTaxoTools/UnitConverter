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

kk= {'d1': 1, 'd2': 0.001, 'd3': 100, 'd4':1000, 'd5':1000000,
'd6':1000000, 'd7':1000000000, 'd8':1000000000000,
'd9':10, 'd10':0.0001799856, 'd11':0.0005399568, 'd12':39.370079,
'd13':1.093613, 'd14':3.28084, 'd15':0.0002071237, 'd16':0.0006213712,
'd17':0.0000000000000106
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


class Method2:

    def textSonDurum(self, x):

        if self.checkBox.isChecked():
            num_format= "{:e}"


        else:
            num_format= "{}"


        map11= {'d1': self.d1, 'd2': self.d2, 'd3': self.d3, 'd4':self.d4, 'd5':self.d5,
        'd6':self.d6, 'd7':self.d7, 'd8':self.d8,
        'd9':self.d9, 'd10':self.d10,
        'd11':self.d11, 'd12':self.d12,
        'd13':self.d13, 'd14':self.d14, 'd15':self.d15, 'd16':self.d16, 'd17':self.d17
        }

        map22= {'d1': lambda tt: self.d1.setText(num_format.format(tt*1)),
                 'd2': lambda tt: self.d2.setText(num_format.format(tt*0.001)),
                  'd3': lambda tt: self.d3.setText(num_format.format(tt*100)),
                  'd4':lambda tt: self.d4.setText(num_format.format(tt*1000)),
                  'd5':lambda tt: self.d5.setText(num_format.format(tt*1000000)),
                  'd6':lambda tt: self.d6.setText(num_format.format(tt*1000000)),
                  'd7':lambda tt: self.d7.setText(num_format.format(tt*1000000000)),
                  'd8':lambda tt: self.d8.setText(num_format.format(tt*1000000000000)),
                  'd9':lambda tt: self.d9.setText(num_format.format(tt*10)),
                  'd10':lambda tt: self.d10.setText(num_format.format(tt*0.0001799856)),
                  'd11':lambda tt: self.d11.setText(num_format.format(tt*0.0005399568)),
                  'd12':lambda tt: self.d12.setText(num_format.format(tt*39.370079)),
                  'd13':lambda tt: self.d13.setText(num_format.format(tt*1.093613)),
                  'd14':lambda tt: self.d14.setText(num_format.format(tt*3.28084)),
                  'd15':lambda tt: self.d15.setText(num_format.format(tt*0.0002071237)),
                  'd16':lambda tt: self.d16.setText(num_format.format(tt*0.0006213712)),
                  'd17':lambda tt: self.d17.setText(num_format.format(tt*0.0000000000000106))
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
            self.d1.setText("")
            self.d2.setText("")
            self.d3.setText("")
            self.d4.setText("")
            self.d5.setText("")
            self.d6.setText("")
            self.d7.setText("")
            self.d8.setText("")
            self.d9.setText("")
            self.d10.setText("")
            self.d11.setText("")
            self.d12.setText("")
            self.d13.setText("")
            self.d14.setText("")
            self.d15.setText("")
            self.d16.setText("")
            self.d17.setText("")
