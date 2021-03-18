# -*- encoding:utf-8 -*-
import sys, os
from PyQt5.QtCore import QDir
from PyQt5.QtWidgets import *
import re
import sys, os

import pandas as pd
from PyQt5.QtGui import *
import ast


kk= {'t1': 1, 't2': 1000, 't3': 1000000, 't4':1000000000, 't5':1000000000000,
't6':1000000000000000, 't7':0.01666667,
't8':0.0002777778, 't9':0.000011574074,
't10':0.000001653439, 't11':0.0000003805175, 't12':0.00000003170979,
't13':0.0000000003170979, 't14':0.000000003170979,
't15':0.00000000003170979, 't16':0.0000001268392, 't17':1860000000000000000000000000000000000000000
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


class Method5:
    kk= {'t1': 1, 't2': 1000, 't3': 1000000, 't4':1000000000, 't5':1000000000000,
    't6':1000000000000000, 't7':0.01666667,
    't8':0.0002777778, 't9':0.000011574074,
    't10':0.000001653439, 't11':0.0000003805175, 't12':0.00000003170979,
    't13':0.0000000003170979, 't14':0.000000003170979,
    't15':0.00000000003170979, 't16':0.0000001268392, 't17':1860000000000000000000000000000000000000000
    }

    def textSonDurum(self, x):


        if self.checkBox.isChecked():
            num_format= "{:e}"

        else:
            num_format= "{}"


        map1= {'t1': self.t1, 't2': self.t2, 't3': self.t3, 't4':self.t4, 't5':self.t5,
        't6':self.t6, 't7':self.t7, 't8':self.t8, 't9':self.t9, 't10':self.t10,
        't11':self.t11, 't12':self.t12,
        't13':self.t13, 't14':self.t14, 't15':self.t15, 't16':self.t16, 't17':self.t17}


        map2= {'t1': lambda tt: self.t1.setText(num_format.format(tt*1)),
                 't2': lambda tt: self.t2.setText(num_format.format(tt*1000)),
                  't3': lambda tt: self.t3.setText(num_format.format(tt*1000000)),
                  't4':lambda tt: self.t4.setText(num_format.format(tt*1000000000)),
                  't5':lambda tt: self.t5.setText(num_format.format(tt*1000000000000)),
                  't6':lambda tt: self.t6.setText(num_format.format(tt*1000000000000000)),
                  't7':lambda tt: self.t7.setText(num_format.format(tt*0.01666667)),
                  't8':lambda tt: self.t8.setText(num_format.format(tt*0.0002777778)),
                  't9':lambda tt: self.t9.setText(num_format.format(tt*0.000011574074)),
                  't10':lambda tt: self.t10.setText(num_format.format(tt*0.000001653439)),
                  't11':lambda tt: self.t11.setText(num_format.format(tt*0.0000003805175)),
                  't12':lambda tt: self.t12.setText(num_format.format(tt*0.00000003170979)),
                  't13':lambda tt: self.t13.setText(num_format.format(tt*0.0000000003170979)),
                  't14':lambda tt: self.t14.setText(num_format.format(tt*0.000000003170979)),
                  't15':lambda tt: self.t15.setText(num_format.format(tt*0.00000000003170979)),
                  't16':lambda tt: self.t16.setText(num_format.format(tt*0.0000001268392)),
                  't17':lambda tt: self.t17.setText(num_format.format(tt*1860000000000000000000000000000000000000000))
                  }


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

            self.t1.setText("")
            self.t2.setText("")
            self.t3.setText("")
            self.t4.setText("")
            self.t5.setText("")
            self.t6.setText("")
            self.t7.setText("")
            self.t8.setText("")
            self.t9.setText("")
            self.t10.setText("")
            self.t11.setText("")
            self.t12.setText("")
            self.t13.setText("")
            self.t14.setText("")
            self.t15.setText("")
            self.t16.setText("")
            self.t17.setText("")
