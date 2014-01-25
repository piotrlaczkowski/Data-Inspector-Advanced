# -*- coding: utf-8 -*-
"""
Created on 12.2.2013
@author: Piotr Laczkowski piotr.laczkowski@gmail.com

Script version: v5.0

SCRIPT DESCRIPTION:
    This script is ment to make a report of existing data files. 
    It allows using multiple modules that are provided separetly in folder modules
    as a python scripts.
"""
#! Data Inspector Qt designer window
#!==========================================================================

#! used to parse files more easily
from __future__ import with_statement
import numpy as np
from numpy import *

from matplotlib.backends.backend_qt4agg import NavigationToolbar2QTAgg as NavigationToolbar
from matplotlib.ticker import OldScalarFormatter, MaxNLocator
import matplotlib.ticker as ticker
from matplotlib.figure import Figure
from matplotlib.lines import Line2D
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
import pylab
from pylab import *
import PyQt4
from PyQt4 import *
import sys, os, random, subprocess,glob
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtWebKit import QWebView
from PyQt4.QtWebKit import QWebPage
#!external materials
import fnmatch
#for configuration GUI
import formlayout
from formlayout import *
#for delimiter detection
import csv
#! import the MainWindow widget from the converted .ui files
from DIA_main_window import Ui_MainWindow

class DesignerMainWindow(QtGui.QMainWindow, Ui_MainWindow):
    """Customization for Qt Designer created window"""
    
     #!=======================================initialization=============================================
    def __init__(self, parent = None):
        #! initialization of the superclass
        super(DesignerMainWindow, self).__init__(parent)     
        self.setupUi(self)
        #title
        self.setWindowTitle("Data Inspector - Advanced")
        
        #! automatic adding  modules to the combo box
        for files in os.listdir("modules"):
            if files.endswith("_module.py"):
#                print files
                self.combo_module.addItem(files)
        
        #! setting base directory
        self.dir = str(os.getcwd()) + '/'
        self.edit_path.setText(self.dir)

        #! connecting signals with slots
        QtCore.QObject.connect(self.btn_folder, QtCore.SIGNAL("clicked()"), self.folder)
        QtCore.QObject.connect(self.btn_find, QtCore.SIGNAL("clicked()"), self.search)
        QtCore.QObject.connect(self.btn_go, QtCore.SIGNAL("clicked()"), self.go)
        QtCore.QObject.connect(self.btn_PDF, QtCore.SIGNAL("clicked()"), self.PDFreport)
        #! link interaction
        self.connect(self.web_data,SIGNAL("linkClicked(const QUrl &)"),self.setImageFilename)
        

      
       
    #!=======================================definitions=============================================

    def folder(self):
        self.dir = QFileDialog.getExistingDirectory(self,"Choose your path", self.dir)
        self.dir = str(self.dir)
        self.edit_path.setText(self.dir + '')
    
    def search(self):
        #! loading start page
        self.web_data.load(QUrl('wait.html'))
        self.web_data.page().setLinkDelegationPolicy(QWebPage.DelegateAllLinks)
        
        #! searching files
        searchFiles = SearchFiles(str(self.edit_path.text()))
        ext = str(self.edit_ext.text())
        searchFiles.search(ext)
        
        #! at the end of thumbnails generating and html creation we will display results
        self.web_data.load(QUrl('report.html'))
        self.web_data.page().setLinkDelegationPolicy(QWebPage.DelegateAllLinks) # send linkClicked signal for every link

    def go(self):
        wdir=str(os.getcwd())
        filename = str(self.edit_selected.text())
        #platform independent path handling
        command = sys.executable +' '+ os.path.join(wdir,'modules',str(self.combo_module.currentText())) +' ' + filename
        print('system independent command=',command)
        os.system(str(command))

        
        
    def findBegining(self,filename):
        '''searching for a given string in a file (default is setup in line 112 to be _begining_)'''
        for n,line in enumerate(open(filename)):
            if "_begining_" in line: 
                print "_begining_ found at line=",n+1
        return n+1
        
   
    def setImageFilename(self, url):
        # set indicator
        filename = url.path()[1:]
        self.edit_selected.setText(filename)
        #! set metadata to be displayed
        try:
            file = open(filename, 'r')
            counter = 0
            self.browser_meta.clear()
            for line in file:
                counter += 1
                try:
                    #automatic begining search with findBegining function
                    beg=self.findBegining(file)
                except Exception:
                    #standard append up to 10 lines
                    beg=10
                    if counter < beg:  #reading metadata!!!!!
                        self.browser_meta.append(line)
        except Exception:
              print "metafile does not exist: %s"%(filename)

#========================================================================PDF creation    
    def PDFreport(self):

        #setting up virtual document - replacing file path
        #TODO need to make this part platform independent (default sys is linux) - to be check
        if os.name=='posix':
            #'linux case'
            reportfile=str(open('report.html','r').read()).replace('file:////','/')
        else:
            #'case of windows'
            reportfile=str(open('report.html','r').read())
 
        print('html='+reportfile)
        document = QTextDocument()
        document.setHtml(reportfile)
        
        #setting up virtual printer
        printer = QPrinter()
        printer.setResolution(130)
        printer.setPageSize(QPrinter.A4)
        printer.setOutputFormat(QPrinter.PdfFormat)
        #choosing printing path
        path = QtGui.QFileDialog.getSaveFileName(
                self, 'Zapisz Plik', 'RAPORT', 'PDF(*.pdf)')
        printer.setOutputFileName(path)
        printer.setPageMargins(12, 16, 12, 20, QPrinter.Millimeter)
        #document settings
        document.setPageSize(QSizeF(printer.pageRect().size()))
        #printing
        document.print_(printer)
        print "Printing Report is done.."
        #preview
        self.statusbar.showMessage("Preview generation...",4000)
        self.handlePreview(document)


    def handlePreview(self,document):
        printer = QPrinter()
        dialog = QPrintPreviewDialog(printer)
        dialog.setWindowFlags(Qt.Window)
        dialog.setWindowTitle('Print preview: parse results')
        def preview(): document.print_(printer)
        dialog.paintRequested.connect(preview)
        dialog.exec_()

class HtmlReportGenerator(object):
  def __init__(self, filename):
    self.file = open(filename, 'w')

  def writeHeader(self):
    self.file.write('<html>\n<head>\n<title>Search Result Report</title>\n</head>\n<body>\n')

  def writeFooter(self):
    self.file.write('\n</body>\n</html>')
    self.file.close()

  def addDateLine(self, date):
    self.file.write('\n<h3>%s-%s-%s</h3>'%(str(date.year()), str(date.month()), str(date.day())))

  def addImage(self, filename):
    #item = item.replace('\\','/') # correct slashes for html
    line = '<a href="file:///'
    line += filename
    line += '"><img src="'
    line += 'file:///'
    line += filename + '.png'
    line += '" title="'
    #item = item.replace('/','\\') # to display path in tooltips in windows style
    line += filename
    line += '"></a>\n'
    self.file.write(line)


class ThumbnailGenerator(object):
  def __init__(self):
      #initializing parameters for search - can be based on formlayout
      datalist=[('Thumbs resolution:',65),
                ('Thumbs color:','green'),
                ('Thumbs linewidth:',4),
                ('Thumbs title size:',15),
                ('Overwrite Thumbs?',True),
                ('Empty thicks?',True)]
      self.TResol,self.TColor,self.TLinewidth,self.Ttitlesize,self.TOverwrite,self.Thicksempty=fedit(datalist, title="Thumbnails generation setup",comment="Please chosep desired parameters")


  def generate(self, filename):
      print "size of file=",os.path.getsize(filename)
      if os.path.getsize(filename)==0:
          print "file  " + str(filename) + "  was skipped as its empty..!!!"
          #os.remove(filename)
          print " file was skipped.."
          pass
      else:
       
       if self.TOverwrite==True:
           
        #detecting delimiter
        delimiter = csv.Sniffer().sniff(open(filename,'r').readlines()[30], ['\t',',',';',' ']).delimiter
        print ('delimiter=',delimiter)

        #creating list of found columns
        try:
            out_Load=genfromtxt(filename, dtype=float,delimiter=delimiter, comments='#', skip_header=2 ,filling_values=None, usecols=None, unpack=True)
        except Exception:
            print "Exception detected reading from 30th line"
            out_Load=genfromtxt(filename, dtype=float,delimiter=delimiter, comments='#', skip_header=30 ,filling_values=None,  usecols=None, unpack=True)

        #printing how many columns have been found 
#        print 'found %s variables'%(str(len(out_Load)))
        
        #clearing missing data or empty columns
        missing_list=[]
        for i in range(len(out_Load)):
            missing_list.append(isnan(out_Load)[i][0])
        #loop for determinating number of non empty columns
        length=[]
        for i in range(len(out_Load)):
            if isnan(out_Load)[i][0]==False:
                length.append(i)
            else:
                pass
        
        #!loading only valable columns      
        try:
            out_Load=genfromtxt(filename, dtype=float,delimiter=delimiter, comments='#', skip_header=2 ,filling_values=None,  usecols=length, unpack=True)
        except Exception:
            print "Exception detected reading from 30th line"
            out_Load=genfromtxt(filename, dtype=float,delimiter=delimiter, comments='#', skip_header=30 ,filling_values=None,  usecols=length, unpack=True)
        
        
        #iterating on columns without the first one X
        for colNbr in range(len(out_Load))[1:]:
            #we need comon x for all so index 0 is not for plotting
            if len(out_Load)<2:
                #here we create subplots on the same axis characterized by different ColNb
                figure(1)
                ax1=plt.subplot(len(out_Load)-1,1,colNbr)
                ax1.plot(out_Load[0],out_Load[colNbr],label="$col \, %s$"%(colNbr+1),linewidth=self.TLinewidth,color=self.TColor)
                if self.Thicksempty==True:
                    ax1.set_yticklabels([])
                    ax1.set_xticklabels([])
                plt.legend(loc=0,shadow=True)
                
            if len(out_Load)>2:
                #here we create subplots on the same axis characterized by different ColNbr
                figure(1)
                ax1=plt.subplot(floor((len(out_Load)))/2,2,colNbr) 
                ax1.plot(out_Load[0],out_Load[colNbr],label="$col \, %s$"%(colNbr+1),linewidth=self.TLinewidth,color=self.TColor)
                if self.Thicksempty==True:
                     ax1.set_yticklabels([])
                     ax1.set_xticklabels([])
                plt.legend(loc=0,shadow=True,prop={'size':18})

        #! assuring that tex is not used in the names of the files        
        matplotlib.rc('text',usetex =False)
        
        #naming thumbnail
        try:
            plt.suptitle(os.path.basename(filename),size=self.Ttitlesize)
        except Exception:
            plt.suptitle('title')
            #print 'title was changed due to an error' 
            pass

        #! tight layout
        try:
            plt.tight_layout()
#            print "tighted figure layout"
        except Exception:
            pass
        
        #saving thumbnail
        savefig(str(filename)+'.png',dpi=self.TResol)#*len(out_Load)/2)
        plt.clf()
        
        #! appending metabrowser self.browser_meta.append(line)
        D=DesignerMainWindow()
        D.browser_meta.clear()
        D.browser_meta.append("proceeding %s ....."%(os.path.basename(filename)))
        


class SearchFiles(object):
  def __init__(self, dir):
    self.dir = dir
    self.thumbGen = ThumbnailGenerator()
    self.reportGen = HtmlReportGenerator("report.html")

  def gen_find(self,filepat,top):
    for path, dirlist, filelist in os.walk(top):
        for name in fnmatch.filter(filelist,filepat):
            yield os.path.join(path,name)
            
  def search(self, ext):
    print 'searching......'
    #finding out how many files is in this directory with specified extenction
    totalFiles=len(glob.glob(os.path.join(self.dir,'*'+ ext)))
    print "found %s files in this folder"%(totalFiles)
  
    names = self.gen_find("*"+ext, self.dir)
    # write report header
    self.reportGen.writeHeader()
    #some old search by date options - that can be resurected if further versions
    #oldDate = QDate() # welches datum, ich glaube 2000...
    #progress bar calibration
    bar = ProgressBar(total=totalFiles)
    bar.show()
    i=0
    for name in names:
        #some old search by date options - that can be resurected if further versions
        #newDate = self.getFileDate(name)
        #if newDate <> oldDate:
        #  self.reportGen.addDateLine(newDate)
        #  oldDate = newDate
        print name
     
        # generate Thumbnail, if not already existing
        self.thumbGen.generate(name)
        i+=1
        bar.update_progressbar(i)
        # html report file
        self.reportGen.addImage(name)
        #refreshing GUI events - prevent window freezing
        QtGui.QApplication.processEvents()
        
    self.reportGen.writeFooter()
    print "FINISHED"

#===========================================for progress bar...
class ProgressBar(QtGui.QWidget):
    def __init__(self, parent=None, total=100):
        super(ProgressBar, self).__init__(parent)
        self.name_line = QtGui.QLineEdit()

        self.progressbar = QtGui.QProgressBar()
        self.progressbar.setMinimum(1)
        self.progressbar.setMaximum(total)

        main_layout = QtGui.QGridLayout()
        main_layout.addWidget(self.progressbar, 0, 0)

        self.setLayout(main_layout)
        self.setWindowTitle("Files Scan Progress")

    def update_progressbar(self, val):
        self.progressbar.setValue(val)   
        
#!=======================================usuall command for starting GUI=============================================	

def main():
    app = QtGui.QApplication(sys.argv)  # create the GUI application
    dmw = DesignerMainWindow()  # instantiate the main window
    dmw.show()  # show it
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()


