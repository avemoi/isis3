'''
Created on Sep 18, 2015

@author: enos
'''

from gui_main import Gui_Main
from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import pyqtSlot
from PyQt4.Qt import QProcess
import sys


def main():
    
    """
    This is the first function executed.
    Starts a new QApplication and 
    creates a new Gui_Main object.
    """
    
    app = QtGui.QApplication(sys.argv)
    Main = QtGui.QMainWindow()
    ui = Gui_Main(Main)
    Main.show()
    sys.exit(app.exec_())





if __name__ == '__main__':
    main()