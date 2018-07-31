'''
Created on Sep 19, 2015

@author: enos
'''


from PyQt4 import QtCore, QtGui
import subprocess
import sys

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class MyPopup(QtGui.QFrame):
    """
    Create a generic class to be
    inherited from others to be used 
    for popup frames.
    """
    def __init__(self,str):
        super(MyPopup, self).__init__()

        self.title = str
        
        self.setupUi()
        
    def setupUi(self):
        
        #self.statsFrame = Frame
        
        self.setObjectName(_fromUtf8(self.title))
        self.resize(427, 433)
        self.setFrameShape(QtGui.QFrame.StyledPanel)
        self.setFrameShadow(QtGui.QFrame.Raised)
        
        
        self.plainTextEdit = QtGui.QPlainTextEdit(self)
        self.plainTextEdit.setGeometry(QtCore.QRect(27, 40, 371, 331))
        self.plainTextEdit.setObjectName(_fromUtf8("plainTextEdit"))
        
        
        self.plainTextEdit.setReadOnly(True)
        
        
        
        self.pushButton = QtGui.QPushButton(self)
        self.pushButton.setGeometry(QtCore.QRect(316, 400, 83, 24))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
      
        
        
        self.label = QtGui.QLabel()
        self.label.setGeometry(QtCore.QRect(170, 10, 61, 16))
        self.label.setObjectName(_fromUtf8("label"))

        self.retranslateUi(self)
        
        
        
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.close)
        
        QtCore.QMetaObject.connectSlotsByName(self)
        
        self.show()
        
        #self.myRun(self.cmd)
        
    
    
        
    def setText(self,str):
        self.plainTextEdit.appendPlainText(str)
    
    def getText(self):
        return self.plainTextEdit.toPlainText()
    
    def setLabelText(self,str):
        self.label.setText(_translate("Frame", str, None))
    
    def retranslateUi(self, Frame):
        Frame.setWindowTitle(_translate(self.title, self.title, None))
        self.pushButton.setText(_translate("Frame", "Close", None))
        #self.label.setText(_translate("Frame", "Statistics", None))
        
    

        
        



