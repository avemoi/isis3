
'''
Created on Sep 14, 2015

@author: enos
'''

import sys
import subprocess
from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import SIGNAL 
from popup import MyPopup
from subprocess import Popen
from statsPop import StatsPopup  
from execute import Execute


try:  
    from PyQt4.QtCore import QString  
except ImportError:  
        # we are using Python3 so QString is not defined  
    QString = str

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

class Gui_Main(QtGui.QMainWindow):
    """
    The main window of the app
    """

    def __init__(self,main):
        
        """
        Parent constructor call,
        call setup for gui, 
        create thread object for 
        the script and connect signals
        to slots
        """
        super(Gui_Main, self).__init__()
        self.setupUi(main)   
        self.execute = Execute()
        self.connect(self.execute, SIGNAL("setOutput(QString)"),self.setOutput)
        self.connect(self.execute, SIGNAL("finished(bool)"),self.finished)
        self.step = 0

    def setupUi(self, MainWindow):
        """
        Create gui widget etc 
        and connect signals to slots
        """
        MainWindow.setObjectName(_fromUtf8("Despeckle"))
        MainWindow.resize(716, 873)
        
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        
        self.widget = QtGui.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(10, 750, 291, 41))
        self.widget.setObjectName(_fromUtf8("widget"))
        
        self.progressBar = QtGui.QProgressBar(self.widget)
        self.progressBar.setGeometry(QtCore.QRect(107, 10, 221, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        
        self.widget_2 = QtGui.QWidget(self.centralwidget)
        self.widget_2.setGeometry(QtCore.QRect(410, 750, 291, 41))
        self.widget_2.setObjectName(_fromUtf8("widget_2"))
        
        self.widget_3 = QtGui.QWidget(self.centralwidget)
        self.widget_3.setGeometry(QtCore.QRect(10, 40, 691, 331))
        self.widget_3.setObjectName(_fromUtf8("widget_3"))

        MainWindow.setCentralWidget(self.centralwidget)

        self.textEdit = QtGui.QTextEdit(self.widget_3)
        self.textEdit.setGeometry(QtCore.QRect(110, 50, 501, 31))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))

        self.textEdit_2 = QtGui.QTextEdit(self.widget_3)
        self.textEdit_2.setGeometry(QtCore.QRect(110, 100, 501, 31))
        self.textEdit_2.setObjectName(_fromUtf8("textEdit_2"))

        self.textEdit_3 = QtGui.QTextEdit(self.widget_3)
        self.textEdit_3.setGeometry(QtCore.QRect(110, 150, 501, 31))
        self.textEdit_3.setObjectName(_fromUtf8("textEdit_3"))

        self.textEdit_4 = QtGui.QTextEdit(self.widget_3)
        self.textEdit_4.setGeometry(QtCore.QRect(110, 200, 251, 31))
        self.textEdit_4.setObjectName(_fromUtf8("textEdit_4"))

        self.textEdit_5 = QtGui.QTextEdit(self.widget_3)
        self.textEdit_5.setGeometry(QtCore.QRect(110, 250, 251, 31))
        self.textEdit_5.setObjectName(_fromUtf8("textEdit_5"))
        
        self.plainTextEdit = QtGui.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(119, 420, 501, 321))
        self.plainTextEdit.setObjectName(_fromUtf8("plainTextEdit"))
        self.plainTextEdit.setReadOnly(True)
  
        self.label = QtGui.QLabel(self.widget_2)
        self.label.setGeometry(QtCore.QRect(20, 10, 201, 21))
        self.label.setObjectName(_fromUtf8("label"))

        self.label_2 = QtGui.QLabel(self.widget_3)
        self.label_2.setGeometry(QtCore.QRect(30, 50, 41, 31))
        self.label_2.setObjectName(_fromUtf8("label_2"))

        self.label_3 = QtGui.QLabel(self.widget_3)
        self.label_3.setGeometry(QtCore.QRect(30, 100, 21, 31))
        self.label_3.setObjectName(_fromUtf8("label_3"))

        self.label_4 = QtGui.QLabel(self.widget_3)
        self.label_4.setGeometry(QtCore.QRect(30, 150, 51, 31))
        self.label_4.setObjectName(_fromUtf8("label_4"))

        self.label_5 = QtGui.QLabel(self.widget_3)
        self.label_5.setGeometry(QtCore.QRect(30, 200, 81, 31))
        self.label_5.setObjectName(_fromUtf8("label_5"))

        self.label_6 = QtGui.QLabel(self.widget_3)
        self.label_6.setGeometry(QtCore.QRect(30, 250, 51, 31))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        
        self.label_7 = QtGui.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(310, 380, 101, 31))
        self.label_7.setObjectName(_fromUtf8("label_7"))

        self.label_8 = QtGui.QLabel(self.widget_3)
        self.label_8.setGeometry(QtCore.QRect(450, 200, 151, 20))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        
        self.label_9 = QtGui.QLabel(self.widget_3)
        self.label_9.setGeometry(QtCore.QRect(450, 250, 151, 20))
        self.label_9.setObjectName(_fromUtf8("label_9"))

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("/opt/Despeckle_pyqt/icons/view_tree.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        self.pushButton = QtGui.QPushButton(self.widget_3)
        self.pushButton.setGeometry(QtCore.QRect(630, 50, 41, 31))
        self.pushButton.setText(_fromUtf8(""))
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(42, 42))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton.clicked.connect(self.inputButtonClicked)
        
        self.pushButton_2 = QtGui.QPushButton(self.widget_3)
        self.pushButton_2.setGeometry(QtCore.QRect(630, 100, 41, 31))
        self.pushButton_2.setText(_fromUtf8(""))
        self.pushButton_2.setIcon(icon)
        self.pushButton_2.setIconSize(QtCore.QSize(42, 42))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_2.clicked.connect(self.outputButtonClicked)

        self.pushButton_3 = QtGui.QPushButton(self.widget_3)
        self.pushButton_3.setGeometry(QtCore.QRect(630, 150, 41, 31))
        self.pushButton_3.setText(_fromUtf8(""))
        self.pushButton_3.setIcon(icon)
        self.pushButton_3.setIconSize(QtCore.QSize(42, 42))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.pushButton_3.clicked.connect(self.inputKernelButtonClicked)
        
        self.pushButton_4 = QtGui.QPushButton(self.widget_3)
        self.pushButton_4.setGeometry(QtCore.QRect(630, 200, 41, 31))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.pushButton_4.setIcon(icon)
        self.pushButton_4.setIconSize(QtCore.QSize(42, 42))
        self.pushButton_4.clicked.connect(self.statsButton)
        
        self.pushButton_5 = QtGui.QPushButton(self.widget_3)
        self.pushButton_5.setGeometry(QtCore.QRect(630, 250, 41, 31))
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.pushButton_5.setIcon(icon)
        self.pushButton_5.setIconSize(QtCore.QSize(42, 42))
        self.pushButton_5.clicked.connect(self.statsButton2)
        
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 716, 20))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        
        self.menu_File = QtGui.QMenu(self.menubar)
        self.menu_File.setObjectName(_fromUtf8("menu_File"))
        self.menu_Help = QtGui.QMenu(self.menubar)
        self.menu_Help.setObjectName(_fromUtf8("menu_Help"))
        self.menu_Help.triggered.connect(self.aboutClicked)

        MainWindow.setMenuBar(self.menubar)

        self.toolBar = QtGui.QToolBar(MainWindow)
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)

        self.action_Run = QtGui.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("/opt/Despeckle_pyqt/icons/guiRun.png")), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.action_Run.setIcon(icon1)
        self.action_Run.setObjectName(_fromUtf8("action_Run"))
        self.action_Run.triggered.connect(self.action_Run_Clicked)

        self.actionStop = QtGui.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8("/opt/Despeckle_pyqt/icons/guiStop.png")), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.actionStop.setIcon(icon2)
        self.actionStop.setObjectName(_fromUtf8("actionStop"))
        self.actionStop.triggered.connect(self.action_Stop_Clicked)

        self.action_Exit = QtGui.QAction(MainWindow)
                
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8("/opt/Despeckle_pyqt/icons/fileclose.png")), QtGui.QIcon.Normal, QtGui.QIcon.On)
        
        self.action_Exit.setIcon(icon3)
        self.action_Exit.setObjectName(_fromUtf8("action_Exit"))
        self.action_Exit.triggered.connect(QtGui.qApp.quit)
        
        self.toolBar.addAction(self.action_Run)
        self.toolBar.addAction(self.actionStop)
        self.toolBar.addAction(self.action_Exit)
        self.toolBar.addSeparator()
        
        self.action_About_Despeckle = QtGui.QAction(MainWindow)
        self.action_About_Despeckle.setObjectName(_fromUtf8("action_About_Despeckle"))
        
        self.menu_File.addAction(self.action_Run)
        self.menu_File.addAction(self.actionStop)
        self.menu_File.addAction(self.action_Exit)
        self.menu_File.addSeparator()
        self.menu_Help.addAction(self.action_About_Despeckle)
        
        self.menubar.addAction(self.menu_File.menuAction())
        self.menubar.addAction(self.menu_Help.menuAction())

        self.retranslateUi(MainWindow)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)
                
    def retranslateUi(self, MainWindow):
        
        MainWindow.setWindowTitle(_translate("Despeckle", "Despeckle", None))
        
        self.label.setText(_translate("MainWindow", "ERROR", None))
        self.label_2.setText(_translate("MainWindow", "FROM", None))
        self.label_3.setText(_translate("MainWindow", "TO", None))
        self.label_4.setText(_translate("MainWindow", "KERNEL", None))
        self.label_5.setText(_translate("MainWindow", "ITERATIONS", None))
        self.label_6.setText(_translate("MainWindow", "L value", None))
        self.label_7.setText(_translate("MainWindow", "Console Output", None))
        self.label_8.setText(_translate("MainWindow", "Input image statistics", None))
        self.label_9.setText(_translate("MainWindow", "Output image statistics", None))
        
        self.menu_File.setTitle(_translate("MainWindow", "&File", None))
        self.menu_Help.setTitle(_translate("MainWindow", "&Help", None))
        
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar", None))
        
        self.action_Run.setText(_translate("MainWindow", "&Run", None))
        self.actionStop.setText(_translate("MainWindow", "Stop", None))
        self.action_Exit.setText(_translate("MainWindow", "&Exit", None))
        self.action_About_Despeckle.setText(_translate("MainWindow", "&About Despeckle", None))

    def inputButtonClicked(self):
        """
        When button pushed, select input .cub file
        and set the path to textedit field and prevent 
        user from changing path manualy
        """
        filename=QtGui.QFileDialog.getOpenFileName(None, 'Select file',"*.cub","*.cub")
        self.textEdit.setText(filename)
        self.textEdit.setEnabled(0)
        
    def outputButtonClicked(self):
        """
        When button pushed, select output .cub file
        and set the path to textedit field and prevent 
        user from changing path manualy
        """
        filename = QtGui.QFileDialog.getSaveFileName(None,"Select file",".cub",".cub")
        
        self.textEdit_2.setText(filename)
        self.textEdit_2.setEnabled(0)

    def inputKernelButtonClicked(self):
        """
        When button pushed, select kernel.txt file
        and set the path to textedit field and prevent 
        user from changing path manualy
        """
        filename=QtGui.QFileDialog.getOpenFileName(None, 'Select file',"*.txt","*.txt")
        self.textEdit_3.setText(filename)
        self.textEdit_3.setEnabled(0)

    def action_Run_Clicked(self):
        """
        Main function of the program. 
        Gets the paths, sets default values
        when new values aren't given,sets
        the command to the thread object (execute)
        and starts the thread.
        Also sets the output of the bottom label
        and the progress bar
        """
        
        input_cub_path    = self.textEdit.toPlainText()
        output_cub_path   = self.textEdit_2.toPlainText()
        input_kernel_path = self.textEdit_3.toPlainText()
        l_value           = self.textEdit_5.toPlainText()
        iterations        = self.textEdit_4.toPlainText()
        
        if(not l_value):
            l_value='-l 0.08'
        else:
            l_value='-l '+ l_value
                        
        if(not iterations):
            iterations='-i 100'
            self.maxIterations = 100
        else:
            self.maxIterations = int(iterations)
            iterations='-i ' + iterations        
        
        # Set max number to progress bar --> number of total iterations, 100 by default    
        self.progressBar.setMaximum(self.maxIterations)
        
        if( not input_cub_path or not output_cub_path or not input_kernel_path):
            print("Error")
        else:
            self.cmd="sh /opt/Despeckle_pyqt/Despeckle/a_despeckle.sh "+ input_cub_path+' '+ input_kernel_path+' '+ ' '+output_cub_path +' '+l_value+' ' +iterations
            
            self.execute.setCmd(self.cmd)
            
            self.execute.start()
            
            print("is finished",self.execute.isFinished())
            
    def finished(self,completed):
        if (self.execute.isRunning()):
            return
        if (completed):
            print("Thread finished")
            self.label.setText("Finished")
        else:
            print("stopped")
            self.label.setText("Cancelled")
     
    def setOutput(self,mystr):
        """
        Redirects stdout given from signal
        to plainTextEdit and send given 
        string to bar and label
        """
        self.plainTextEdit.appendPlainText(mystr)
        self.setOutputBar(mystr)
        self.setOutputLabel(mystr)       
    
    def setOutputBar(self,mystr):
        """
        In bash script is echoed
        the word "Iteration" following
        a number showing us the current
        iteration, so when our line starts
        with the word "Iteration" we take 
        the string after that word (the number),
        we cast it to integer and we set
        the value of the progress bar 
        """
        if(mystr.startswith("Iteration")):
            currentIteration = int( mystr[9:] )
            self.progressBar.setValue(currentIteration)       
    
    def setOutputLabel(self,mystr):
        """
        In bash script is echoed
        the word "Iteration" following
        a number showing us the current
        iteration, so when our line starts
        with the word "Iteration" we take 
        the whole line (string) and we
        set the value of the label  
        """
        if(mystr.startswith("Iteration")):
            self.label.setText(mystr)        

    def action_Stop_Clicked(self):
        """
        A not-an-elegant
        way to stop the thread 
        """
        self.execute.stop()
             
    def statsButton(self):
        """
        When button pushed, a stats
        frame pops up with the stats
        of the input image.
        """
        path = self.textEdit.toPlainText()
        if (not path):
            pass
        else:
            self.stats1 = StatsPopup(path)
            self.stats1.start()   
        
    def statsButton2(self):
        """
        When button pushed, a stats
        frame pops up with the stats
        of the output image.
        """
        path = self.textEdit_2.toPlainText()
        if (not path):
            pass
        else:
            self.stats2 = StatsPopup(path)
            self.stats2.start()
         
    def aboutClicked(self):
        """
        When button pushed, pops up
        a frame with a text read from
        a file
        """
        text = []  
        file = open("/opt/Despeckle_pyqt/about.txt", 'r')
        for line in file:
            text.append(line)

        self.about = MyPopup("about")
        self.about.setText("".join(text))
        







