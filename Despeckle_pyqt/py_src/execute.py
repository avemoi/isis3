'''
Created on Sep 28, 2015

@author: enos
'''

from PyQt4.QtCore import QThread
from PyQt4.QtCore import SIGNAL
import sys
import subprocess

try:  
    from PyQt4.QtCore import QString  
except ImportError:  
        # we are using Python3 so QString is not defined  
    QString = str

class Execute(QThread):
    """
    Create new thread to execute the script
    so that the Gui interface doesn't freeze.
    It takes the command from the setCmd() 
    and it executes it in a subprocess When it finished
    or when it stops, it sends a message to the caller
    and executes the method given.
    """
    
    def __init__(self):
        QThread.__init__(self)
        print("execute constructor")
        self.output=[]
             
    def run(self):
        print("enter run")
        self.runScript()
        self.emit(SIGNAL("finished(bool)"),True)
        print("finished from run")

    def stop(self):
        self.terminate()
        self.p.kill()
        self.emit(SIGNAL("finished(bool)"),False)
        
    def setCmd(self,cmd):
        self.cmd = cmd   
        print(cmd)
    
    def runScript(self):    
        self.p = subprocess.Popen(self.cmd,shell=True,stdout=subprocess.PIPE)
        for line in self.p.stdout:
            line = line.rstrip()
            line=line.decode(sys.stdout.encoding)
            self.emit(SIGNAL("setOutput(QString)"), line)
            
           
            
       
    
    