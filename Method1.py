# -*- encoding:utf-8 -*-
import sys, os
from PyQt5.QtCore import QDir
from PyQt5.QtWidgets import *
import re
import sys, os

import pandas as pd
from PyQt5.QtGui import *
import ast


kk= {'l1': 1, 'l2': 0.001, 'l3': 0.001, 'l4':0.000001, 'l5':0.000000001, 'l6':0.001, 'l7':0.000001, 'l8':0.000000001, 'l9':0.000000000001, 'l10':1000, 'l11':1, 'l12':0.001,
'l13':0.000001, 'l14':0.001, 'l15':1000, 'l16':1, 'l17':0.001,
'l18':1000, 'l19':1000000, 'l20':1000000000, 'l21':1000000, 'l22':1000, 'l23':1, 'l24':0.001,
'l25':1, 'l26':1000, 'l27':1000000, 'l28':1000000000, 'l29':1000000000000}



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


class Method1:

    def textSonDurum(self, x):

        if self.checkBox.isChecked():
            num_format= "{:e}"


        else:
            num_format= "{}"


        map1= {'l1': self.l1, 'l2': self.l2, 'l3': self.l3, 'l4':self.l4, 'l5':self.l5, 'l6':self.l6, 'l7':self.l7, 'l8':self.l8, 'l9':self.l9, 'l10':self.l10,
        'l11':self.l11, 'l12':self.l12,
        'l13':self.l13, 'l14':self.l14, 'l15':self.l15, 'l16':self.l16, 'l17':self.l17,
        'l18':self.l18, 'l19':self.l19, 'l20':self.l20, 'l21':self.l21, 'l22':self.l22, 'l23':self.l23, 'l24':self.l24,
        'l25':self.l25, 'l26':self.l26, 'l27':self.l27, 'l28':self.l28, 'l29':self.l29}

        map2= {'l1': lambda tt: self.l1.setText(num_format.format(tt*1)),
                 'l2': lambda tt: self.l2.setText(num_format.format(tt*0.001)),
                  'l3': lambda tt: self.l3.setText(num_format.format(tt*0.001)),
                  'l4':lambda tt: self.l4.setText(num_format.format(tt*0.000001)),
                  'l5':lambda tt: self.l5.setText(num_format.format(tt*0.000000001)),
                  'l6':lambda tt: self.l6.setText(num_format.format(float(tt*0.001))),
                  'l7':lambda tt: self.l7.setText(num_format.format(tt*0.000001)),
                  'l8':lambda tt: self.l8.setText(num_format.format(tt*0.000000001)),
                  'l9':lambda tt: self.l9.setText(num_format.format(tt*0.000000000001)),
                  'l10':lambda tt: self.l10.setText(num_format.format(tt*1000)),
                  'l11':lambda tt: self.l11.setText(num_format.format(tt*1)),
                  'l12':lambda tt: self.l12.setText(num_format.format(tt*0.001)),
                  'l13':lambda tt: self.l13.setText(num_format.format(tt*0.000001)),
                  'l14':lambda tt: self.l14.setText(num_format.format(tt*0.001)),
                  'l15':lambda tt: self.l15.setText(num_format.format(tt*1000)),
                  'l16':lambda tt: self.l16.setText(num_format.format(tt*1)),
                  'l17':lambda tt: self.l17.setText(num_format.format(tt*0.001)),
                  'l18':lambda tt: self.l18.setText(num_format.format(tt*1000)),
                  'l19':lambda tt: self.l19.setText(num_format.format(tt*1000000)),
                  'l20':lambda tt: self.l20.setText(num_format.format(tt*1000000000)),
                  'l21':lambda tt: self.l21.setText(num_format.format(tt*1000000)),
                  'l22':lambda tt: self.l22.setText(num_format.format(tt*1000)),
                  'l23':lambda tt: self.l23.setText(num_format.format(tt*1)),
                  'l24':lambda tt: self.l24.setText(num_format.format(tt*0.001)),
                  'l25':lambda tt: self.l25.setText(num_format.format(tt*1)),
                  'l26':lambda tt: self.l26.setText(num_format.format(tt*1000)),
                  'l27':lambda tt: self.l27.setText(num_format.format(tt*1000000)),
                  'l28':lambda tt: self.l28.setText(num_format.format(tt*1000000000)),
                  'l29':lambda tt: self.l29.setText(num_format.format(tt*1000000000000))}
        print(x)

        s= map1[x]

        s= s.text()



        tt= check(s)
        if tt != None:

            tt= (1/kk[x])*tt

            for i in map2:
                if i != x:
                    func= map2[i]
                    func(tt)

        else:
            map1['l1'].setText("")
            map1['l2'].setText("")
            map1['l3'].setText("")
            map1['l4'].setText("")
            map1['l5'].setText("")
            map1['l6'].setText("")
            map1['l7'].setText("")
            self.l8.setText("")
            self.l9.setText("")
            self.l10.setText("")
            self.l11.setText("")
            self.l12.setText("")
            self.l13.setText("")
            self.l14.setText("")
            self.l15.setText("")
            self.l16.setText("")
            self.l17.setText("")
            self.l18.setText("")
            self.l19.setText("")
            self.l20.setText("")
            self.l21.setText("")
            self.l22.setText("")
            self.l23.setText("")
            self.l24.setText("")
            self.l25.setText("")
            self.l26.setText("")
            self.l27.setText("")
            self.l28.setText("")
            self.l29.setText("")
