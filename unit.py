# -*- encoding:utf-8 -*-
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import re
import sys, os
from PyQt5.uic import loadUiType
import pandas as pd
from PyQt5.QtGui import *
import ast

from Method1 import Method1
from method2 import Method2
from method3 import Method3
from method4 import Method4
from Method5 import Method5

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)


FORM_CLASS,_=loadUiType(resource_path("unittool.ui"))


class Main(QMainWindow, FORM_CLASS):
    def __init__(self):
        super(Main, self).__init__()

        self.setupUi(self)
        self.Handel_Buttons1()
        self.Handel_Buttons2()
        self.Handel_Buttons3()
        self.Handel_Buttons4()
        self.Handel_Buttons5()
        self.setWindowIcon(QIcon(resource_path('icons/unit converter ICON.ico')))
        self.setWindowTitle("Unit Converter")
        quit = QAction("Quit", self)
        quit.triggered.connect(self.closeEvent)


    def closeEvent(self, event):
         close = QMessageBox.question(self, "QUIT", "Are you sure want to close program?",QMessageBox.Yes | QMessageBox.No)
         if close == QMessageBox.Yes:
             QApplication.closeAllWindows()
             event.accept()

         else:
             event.ignore()



    def Handel_Buttons1(self):
        self.l1.textEdited.connect(lambda *args: Method1.textSonDurum(self, 'l1'))
        self.l2.textEdited.connect(lambda *args: Method1.textSonDurum(self, 'l2'))
        self.l3.textEdited.connect(lambda *args: Method1.textSonDurum(self, 'l3'))
        self.l4.textEdited.connect(lambda *args: Method1.textSonDurum(self, 'l4'))
        self.l5.textEdited.connect(lambda *args: Method1.textSonDurum(self, 'l5'))
        self.l6.textEdited.connect(lambda *args: Method1.textSonDurum(self, 'l6'))
        self.l7.textEdited.connect(lambda *args: Method1.textSonDurum(self, 'l7'))
        self.l8.textEdited.connect(lambda *args: Method1.textSonDurum(self, 'l8'))
        self.l9.textEdited.connect(lambda *args: Method1.textSonDurum(self, 'l9'))
        self.l10.textEdited.connect(lambda *args: Method1.textSonDurum(self, 'l10'))
        self.l11.textEdited.connect(lambda *args: Method1.textSonDurum(self, 'l11'))
        self.l12.textEdited.connect(lambda *args: Method1.textSonDurum(self, 'l12'))
        self.l13.textEdited.connect(lambda *args: Method1.textSonDurum(self, 'l13'))
        self.l14.textEdited.connect(lambda *args: Method1.textSonDurum(self, 'l14'))
        self.l15.textEdited.connect(lambda *args: Method1.textSonDurum(self, 'l15'))
        self.l16.textEdited.connect(lambda *args: Method1.textSonDurum(self, 'l16'))
        self.l17.textEdited.connect(lambda *args: Method1.textSonDurum(self, 'l17'))
        self.l18.textEdited.connect(lambda *args: Method1.textSonDurum(self, 'l18'))
        self.l19.textEdited.connect(lambda *args: Method1.textSonDurum(self, 'l19'))
        self.l20.textEdited.connect(lambda *args: Method1.textSonDurum(self, 'l20'))
        self.l21.textEdited.connect(lambda *args: Method1.textSonDurum(self, 'l21'))
        self.l22.textEdited.connect(lambda *args: Method1.textSonDurum(self, 'l22'))
        self.l23.textEdited.connect(lambda *args: Method1.textSonDurum(self, 'l23'))
        self.l24.textEdited.connect(lambda *args: Method1.textSonDurum(self, 'l24'))
        self.l25.textEdited.connect(lambda *args: Method1.textSonDurum(self, 'l25'))
        self.l26.textEdited.connect(lambda *args: Method1.textSonDurum(self, 'l26'))
        self.l27.textEdited.connect(lambda *args: Method1.textSonDurum(self, 'l27'))
        self.l28.textEdited.connect(lambda *args: Method1.textSonDurum(self, 'l28'))
        self.l29.textEdited.connect(lambda *args: Method1.textSonDurum(self, 'l29'))


    def Handel_Buttons2(self):
        self.d1.textEdited.connect(lambda *args: Method2.textSonDurum(self, 'd1'))
        self.d2.textEdited.connect(lambda *args: Method2.textSonDurum(self, 'd2'))
        self.d3.textEdited.connect(lambda *args: Method2.textSonDurum(self, 'd3'))
        self.d4.textEdited.connect(lambda *args: Method2.textSonDurum(self, 'd4'))
        self.d5.textEdited.connect(lambda *args: Method2.textSonDurum(self, 'd5'))
        self.d6.textEdited.connect(lambda *args: Method2.textSonDurum(self, 'd6'))
        self.d7.textEdited.connect(lambda *args: Method2.textSonDurum(self, 'd7'))
        self.d8.textEdited.connect(lambda *args: Method2.textSonDurum(self, 'd8'))
        self.d9.textEdited.connect(lambda *args: Method2.textSonDurum(self, 'd9'))
        self.d10.textEdited.connect(lambda *args: Method2.textSonDurum(self, 'd10'))
        self.d11.textEdited.connect(lambda *args: Method2.textSonDurum(self, 'd11'))
        self.d12.textEdited.connect(lambda *args: Method2.textSonDurum(self, 'd12'))
        self.d13.textEdited.connect(lambda *args: Method2.textSonDurum(self, 'd13'))
        self.d14.textEdited.connect(lambda *args: Method2.textSonDurum(self, 'd14'))
        self.d15.textEdited.connect(lambda *args: Method2.textSonDurum(self, 'd15'))
        self.d16.textEdited.connect(lambda *args: Method2.textSonDurum(self, 'd16'))
        self.d17.textEdited.connect(lambda *args: Method2.textSonDurum(self, 'd17'))



    def Handel_Buttons3(self):
        self.v1.textEdited.connect(lambda *args: Method3.textSonDurum(self, 'v1'))
        self.v2.textEdited.connect(lambda *args: Method3.textSonDurum(self, 'v2'))
        self.v3.textEdited.connect(lambda *args: Method3.textSonDurum(self, 'v3'))
        self.v4.textEdited.connect(lambda *args: Method3.textSonDurum(self, 'v4'))
        self.v5.textEdited.connect(lambda *args: Method3.textSonDurum(self, 'v5'))
        self.v6.textEdited.connect(lambda *args: Method3.textSonDurum(self, 'v6'))
        self.v7.textEdited.connect(lambda *args: Method3.textSonDurum(self, 'v7'))
        self.v8.textEdited.connect(lambda *args: Method3.textSonDurum(self, 'v8'))
        self.v9.textEdited.connect(lambda *args: Method3.textSonDurum(self, 'v9'))
        self.v10.textEdited.connect(lambda *args: Method3.textSonDurum(self, 'v10'))
        self.v11.textEdited.connect(lambda *args: Method3.textSonDurum(self, 'v11'))
        self.v12.textEdited.connect(lambda *args: Method3.textSonDurum(self, 'v12'))
        self.v13.textEdited.connect(lambda *args: Method3.textSonDurum(self, 'v13'))
        self.v14.textEdited.connect(lambda *args: Method3.textSonDurum(self, 'v14'))
        self.v15.textEdited.connect(lambda *args: Method3.textSonDurum(self, 'v15'))
        self.v16.textEdited.connect(lambda *args: Method3.textSonDurum(self, 'v16'))
        self.v17.textEdited.connect(lambda *args: Method3.textSonDurum(self, 'v17'))


    def Handel_Buttons4(self):
        self.w1.textEdited.connect(lambda *args: Method4.textSonDurum(self, 'w1'))
        self.w2.textEdited.connect(lambda *args: Method4.textSonDurum(self, 'w2'))
        self.w3.textEdited.connect(lambda *args: Method4.textSonDurum(self, 'w3'))
        self.w4.textEdited.connect(lambda *args: Method4.textSonDurum(self, 'w4'))
        self.w5.textEdited.connect(lambda *args: Method4.textSonDurum(self, 'w5'))
        self.w6.textEdited.connect(lambda *args: Method4.textSonDurum(self, 'w6'))
        self.w7.textEdited.connect(lambda *args: Method4.textSonDurum(self, 'w7'))
        self.w8.textEdited.connect(lambda *args: Method4.textSonDurum(self, 'w8'))
        self.w9.textEdited.connect(lambda *args: Method4.textSonDurum(self, 'w9'))
        self.w10.textEdited.connect(lambda *args: Method4.textSonDurum(self, 'w10'))
        self.w11.textEdited.connect(lambda *args: Method4.textSonDurum(self, 'w11'))
        self.w12.textEdited.connect(lambda *args: Method4.textSonDurum(self, 'w12'))
        self.w13.textEdited.connect(lambda *args: Method4.textSonDurum(self, 'w13'))
        self.w14.textEdited.connect(lambda *args: Method4.textSonDurum(self, 'w14'))
        self.w15.textEdited.connect(lambda *args: Method4.textSonDurum(self, 'w15'))
        self.w16.textEdited.connect(lambda *args: Method4.textSonDurum(self, 'w16'))


    def Handel_Buttons5(self):
        self.t1.textEdited.connect(lambda *args: Method5.textSonDurum(self, 't1'))
        self.t2.textEdited.connect(lambda *args: Method5.textSonDurum(self, 't2'))
        self.t3.textEdited.connect(lambda *args: Method5.textSonDurum(self, 't3'))
        self.t4.textEdited.connect(lambda *args: Method5.textSonDurum(self, 't4'))
        self.t5.textEdited.connect(lambda *args: Method5.textSonDurum(self, 't5'))
        self.t6.textEdited.connect(lambda *args: Method5.textSonDurum(self, 't6'))
        self.t7.textEdited.connect(lambda *args: Method5.textSonDurum(self, 't7'))
        self.t8.textEdited.connect(lambda *args: Method5.textSonDurum(self, 't8'))
        self.t9.textEdited.connect(lambda *args: Method5.textSonDurum(self, 't9'))
        self.t10.textEdited.connect(lambda *args: Method5.textSonDurum(self, 't10'))
        self.t11.textEdited.connect(lambda *args: Method5.textSonDurum(self, 't11'))
        self.t12.textEdited.connect(lambda *args: Method5.textSonDurum(self, 't12'))
        self.t13.textEdited.connect(lambda *args: Method5.textSonDurum(self, 't13'))
        self.t14.textEdited.connect(lambda *args: Method5.textSonDurum(self, 't14'))
        self.t15.textEdited.connect(lambda *args: Method5.textSonDurum(self, 't15'))
        self.t16.textEdited.connect(lambda *args: Method5.textSonDurum(self, 't16'))
        self.t17.textEdited.connect(lambda *args: Method5.textSonDurum(self, 't17'))




def main1():

    app=QApplication(sys.argv)
    window=Main()
    window.show()
    app.exec_()


if __name__=='__main__':
    main1()
