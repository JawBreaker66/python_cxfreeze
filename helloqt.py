# -*- coding: utf-8 -*-
"""
Created on Fri Dec 30 10:21:48 2016

@author: Daniel
"""

#!/usr/bin/env python3
#-*- coding: utf-8 -*-

"""
helloqt.py
PyQt5 で Hello, world!
cxfreeze with
#cxfreeze.bat --base-name=Win32GUI path@helloqt.py
"""

import sys
from PyQt5 import QtWidgets



def main():
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QMainWindow()
    button = QtWidgets.QPushButton("Hello, PyQt!")
    window.setCentralWidget(button)
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()