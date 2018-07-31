'''
Created on Sep 10, 2015

@author: enos
'''


from PyQt4 import QtCore, QtGui
import subprocess
import sys
from popup import MyPopup


class StatsPopup(MyPopup):
    """
    Inherit from MyPopup (just a popup frame),
    run the stats script and place the results
    to the new frame
    """
    def __init__(self,path):
        
        MyPopup.__init__(self, path)
        
        
        self.cmd="stats FROM="+path
        
        
        
        
    def start(self):
        self.myRun()
        
    
        
    def myRun(self):
        
        self.p = subprocess.Popen(self.cmd,shell=True,stdout=subprocess.PIPE)
        for line in self.p.stdout:
            line = line.rstrip()
            line=line.decode(sys.stdout.encoding)
            self.plainTextEdit.appendPlainText(line)
        
        

        
        

