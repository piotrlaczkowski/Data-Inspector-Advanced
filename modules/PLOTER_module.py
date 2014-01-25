# defining character coding
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 11:17:23 2012
@author: Piotr Laczkowski piotr.laczkowski@gmail.com

SCRIPT DESCRIPTION:
    This script is ment to ease the plotting process and simple data analysis.
    It can be extended by its own modules in the form of python scripts.
"""
#! DIA MODULE FOR PLOTTING
#!==========================================================================
#! used to parse files more easily
from __future__ import with_statement, division
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
import sys, os, random
from PyQt4.QtCore import *
from PyQt4.QtGui import *

import math
import scipy
from scipy import *

#! for inset
from matplotlib.offsetbox import OffsetImage,AnnotationBbox
from matplotlib._png import read_png

#for delimiter deterction (sniffing)
import csv

#! import the MainWindow widget from the converted .ui files
from PLOT_main_window import Ui_MainWindow

class DesignerMainWindow(QtGui.QMainWindow, Ui_MainWindow):
    """Customization for Qt Designer created window"""
    
     #!=======================================initialization=============================================
    def __init__(self, parent = None):
        """Initializing some parameters at start"""
        #! initialization of the superclass
        super(DesignerMainWindow, self).__init__(parent)     
        self.setupUi(self) 
   
        #! defining short-filename that will be used as a figures title
        shortpath = os.path.basename(filename)
        try:
            '''trying with filename and tex'''
            st=u'%s'%(shortpath[:-4])
            self.edit_title.setText("$"+st.replace('_','\,')+"$")
            #self.edit_title.setText(shortpath[:-4])
        except Exception:
            '''when tex and filename does not work we will use simple title'''
            self.edit_title.setText(u'TITLE')
			
        #! drawing command
        self.Draw()
        
        #! setting tesla gauss conversion for x axis display - if necessary uncomment
        #self.edit_divx.setText('1e4')

        
        #! connecting the signals with the slots
        QtCore.QObject.connect(self.btn_pythonize, QtCore.SIGNAL("clicked()"), self.SavePython)
        QtCore.QObject.connect(self.btn_SaveFigs, QtCore.SIGNAL("clicked()"), self.SavePlot)

        #! connecting changes of edits:
        self.connect(self.edit_xlabel, SIGNAL('editingFinished ()'), self.on_change)
        self.connect(self.edit_ylabel, SIGNAL('editingFinished ()'), self.on_change)
        self.connect(self.edit_title, SIGNAL('editingFinished ()'), self.on_change)
        self.connect(self.edit_label, SIGNAL('editingFinished ()'), self.on_change)
        self.connect(self.edit_xmin, SIGNAL('editingFinished ()'), self.on_change)
        self.connect(self.edit_xmax, SIGNAL('editingFinished ()'), self.on_change)
        self.connect(self.edit_ymin, SIGNAL('editingFinished ()'), self.on_change)
        self.connect(self.edit_ymax, SIGNAL('editingFinished ()'), self.on_change)
        self.connect(self.edit_divx, SIGNAL('editingFinished ()'), self.on_change)
        self.connect(self.edit_multx, SIGNAL('editingFinished ()'), self.on_change)
        self.connect(self.edit_divy, SIGNAL('editingFinished ()'), self.on_change)
        self.connect(self.edit_multy, SIGNAL('editingFinished ()'), self.on_change)
        self.connect(self.edit_inset, SIGNAL('editingFinished ()'), self.on_change)
        self.connect(self.edit_dt, SIGNAL('editingFinished ()'), self.on_change)
        self.connect(self.edit_dH, SIGNAL('editingFinished ()'), self.on_change)
        self.connect(self.edit_dH2, SIGNAL('editingFinished ()'), self.on_change)
        self.connect(self.edit_smooth, SIGNAL('editingFinished ()'), self.on_change)
        self.connect(self.edit_degree, SIGNAL('editingFinished ()'), self.on_change)
        #! connecting changes of checkboxes
        self.connect(self.check_grid, SIGNAL('stateChanged(int)'), self.on_change)
        self.connect(self.check_label, SIGNAL('stateChanged(int)'), self.on_change)
        self.connect(self.check_tight, SIGNAL('stateChanged(int)'), self.on_change)
        self.connect(self.check_xlim, SIGNAL('stateChanged(int)'), self.on_change)
        self.connect(self.check_ylim, SIGNAL('stateChanged(int)'), self.on_change)
        self.connect(self.check_derivate, SIGNAL('stateChanged(int)'), self.on_change)
        self.connect(self.check_invertx, SIGNAL('stateChanged(int)'), self.on_change)
        self.connect(self.check_inverty, SIGNAL('stateChanged(int)'), self.on_change)
        #! connecting changes of sliders
        self.connect(self.slide_start, SIGNAL('valueChanged(int)'), self.on_change)
        self.connect(self.slide_stop, SIGNAL('valueChanged(int)'), self.on_change)
        self.connect(self.slide_xsize, SIGNAL('valueChanged(int)'), self.on_change)
        self.connect(self.slide_xnr, SIGNAL('valueChanged(int)'), self.on_change)
        self.connect(self.slide_xsizeticks, SIGNAL('valueChanged(int)'), self.on_change)
        self.connect(self.slide_ysize, SIGNAL('valueChanged(int)'), self.on_change)
        self.connect(self.slide_ynr, SIGNAL('valueChanged(int)'), self.on_change)
        self.connect(self.slide_ysizeticks, SIGNAL('valueChanged(int)'), self.on_change)
        self.connect(self.slide_titlesize, SIGNAL('valueChanged(int)'), self.on_change)
        self.connect(self.slide_zoom, SIGNAL('valueChanged(int)'), self.on_change)
        self.connect(self.slide_posx, SIGNAL('valueChanged(int)'), self.on_change)
        self.connect(self.slide_posy, SIGNAL('valueChanged(int)'), self.on_change)
       
        #! connecting changes for spins boxes
        self.connect(self.combo_x, SIGNAL('currentIndexChanged(int)'), self.on_change)
        self.connect(self.combo_y, SIGNAL('currentIndexChanged(int)'), self.on_change)

        #! adding combo boxes items for x and y columns selection and labels for all columns
        #! firs we need to detect how many columns we have
        infile = open(filename,"r")
        #detecting file delimiter
        global delim
        delimiter = csv.Sniffer().sniff(infile.readlines()[40], ['\t',',',';',' '])
        delim=delimiter.delimiter
        print('found delimiter=',delim)
        #reading file
        col_nbr=genfromtxt(filename,dtype=float,delimiter=delim,skip_header=30,skip_footer=self.slide_stop.value(),unpack=True)
        print u"found %s columns in the file"%(len(col_nbr))
        
        
        #! adding variables to column choice for x and y 
        for i in range(len(col_nbr)):
            #print "i=",i+1
            self.combo_x.addItem(str(i+1))
            self.combo_y.addItem(str(i+1))

            
        #setting y to start with second column and not the first one
        self.combo_y.setCurrentIndex(1)

       
    #!=======================================definitions=============================================

    def on_change(self):
        """Clearing and redrawing the figure canvas after some changes"""
        #! clearing
        self.mpl.canvas.ax.clear()
        #! redrawing
        self.Draw()

    def read_data(self,filename):
        """reading data from the input file depending on the selected column number
            First the tab delimiter will be tried-if this does not work automatic 
            recognition of the delimiter will be used"""
        infile = open(filename,"r")
        
        global X
        global Y
        try:
            X,Y=genfromtxt(infile,dtype=float,delimiter=delim,skip_header=self.slide_start.value()+10, skip_footer=self.slide_stop.value(),usecols=(self.combo_x.currentIndex(),self.combo_y.currentIndex()),unpack=True)
#            print u"tab delimiter option was used"
        except Exception:
            X,Y=genfromtxt(infile,dtype=float,skip_header=self.slide_start.value()+10, skip_footer=self.slide_stop.value(),usecols=(self.combo_x.currentIndex(),self.combo_y.currentIndex()),unpack=True)
#            print u"empyt delimiter was used - lookes for empty spaces"
        return X,Y

    def Draw(self):
        
        """Drawing X and Y on the canvas. In this definition all necessary data
        correction are performed"""
        
        #! setting up gobal variables for parsing to another funtions      
        global X
        global Y
        #!----------------------------------------------------Corrections Start        
        #! rerading data-file Y0 is for correction
        X,Y0=self.read_data(filename)

          
        #! derivative, linear, and B^2 corrections
        R = float(self.edit_dt.text())
        E = float(self.edit_dH.text())
        EE = float(self.edit_dH2.text())
        
        #! creating final for Y list after corrections
        Y=[]
        
        #! field derivative correction for Y0 saved in Y
        '''to jest miejsce gdzie przemanazam wszystkie element listy X0 przez korekte derivative'''
        for index,y in enumerate(Y0):
            Y.append(Y0[index] + (float(X[index])*float(E))+ ((float(index)/float(len(Y0)))*float(R)) + (float(X[index])*float(X[index])*float(EE)))
        #!----------------------------------------------------Corrections END
        
        #!----------------------------------------------------Customization of the plot
        #! setting up ticks numbers for X and Y from slider
        majorLocatorX = MaxNLocator(self.slide_xnr.value())
        majorLocatorY = MaxNLocator(self.slide_ynr.value())
        #! definition of MPL
        MPL=self.mpl.canvas.ax

#        print u"MPL signature=",MPL
        MPL.set_title(str(self.edit_title.text()),fontsize=self.slide_titlesize.value())
        MPL.set_xlabel(self.edit_xlabel.text(),fontsize=self.slide_xsize.value())
        MPL.set_ylabel(self.edit_ylabel.text(),fontsize=self.slide_ysize.value())
        #self.ticker.set_major_locator(MaxNLocator(4))
        MPL.xaxis.set_major_locator(majorLocatorX)
        MPL.yaxis.set_major_locator(majorLocatorY)

        ticker.ScalarFormatter(useOffset=True, useMathText=True)  #- for offset - but need to be adapted
       
        for t in MPL.get_xticklabels():
            t.set_fontsize(self.slide_xsizeticks.value())
            
        for t in MPL.get_yticklabels():
            t.set_fontsize(self.slide_ysizeticks.value())
        
        # grid verification
        if self.check_grid.isChecked():
             MPL.get_xaxis().grid(True)
             MPL.get_yaxis().grid(True)

        
        #!----------------------------------------------------Further corrections
        # applying corrections for Y
        try:
            Y=[i*float(self.edit_multy.text())/float(self.edit_divy.text()) for i in Y]
        except Exception:
            pass
        
        # applying corrections for X
        try:
            X=[i*float(self.edit_multx.text())/float(self.edit_divx.text()) for i in X]
        except Exception:
            pass

        #___________Smoothing____________
        degree = eval(str(self.edit_smooth.text()))
#        print "smooth degree was set to be =", degree
        
        def on_smooth(data,degree,dropVals=False):
	       smoothed=[]
	       for i in range(degree,len(data)-degree):
	           point=data[i:i+degree]
	           smoothed.append((sum(point)/degree))
	       if dropVals: return smoothed
	
	       smoothed=[smoothed[0]]* int((degree+(degree/2)))+smoothed
	       while len(smoothed)<len(data):smoothed.append(smoothed[-1])
	       return smoothed
      
        #! derivate correction check
        if self.check_derivate.isChecked():
            ''' when derivate of degree n is taken on y we need to make same number of points in x making x[n:]'''            
            Y=diff(Y, n=int(self.edit_degree.text()), axis=-1)
            X=X[int(self.edit_degree.text()):]
            
        # invert X verification
        if self.check_invertx.isChecked():
#            X=ma.masked_where(X<0,X)
            X=ma.masked_less_equal(X,0)
            X=[1./i for i in X]
            #! changing xlabel
            acctualx= self.edit_xlabel.text()
            if acctualx[0:3]!="$1/":
                newlabel="$1/ %s $"%(str(acctualx).strip('$'))
                self.edit_xlabel.setText(newlabel)

            
        # invert Y verification
        if self.check_inverty.isChecked():
#            Y=ma.masked_where(Y!=0,Y)
            Y=ma.masked_less_equal(Y,0)
            Y=[1./i for i in Y]
            #! changing xlabel
            acctualy= self.edit_ylabel.text()
            if acctualy[0:3]!="$1/":
                newlabel="$1/ %s $"%(str(acctualy).strip('$'))
                self.edit_ylabel.setText(newlabel)

            
        #! Plotting command
        MPL.plot(X,on_smooth(Y,degree), 'ro-',label=str(self.edit_label.text()),linewidth = 3,picker=1)

        #! limitation on axis        
        if self.check_xlim.isChecked():
            print u"limits X are set..."
            MPL.set_xlim(eval(str(self.edit_xmin.text())),eval(str(self.edit_xmax.text())))
        if self.check_ylim.isChecked():
            print u"limits Y are set..."
            MPL.set_ylim(eval(str(self.edit_ymin.text())),eval(str(self.edit_ymax.text())))
            
        wdir=str(os.getcwd())
        
        if eval(str(self.edit_inset.text()))!=0:
            inset = read_png(wdir + "/insets/"+str(self.edit_inset.text())+".png")
#            print "inset file=",inset            
            imagebox = OffsetImage(inset, zoom = float(eval(str(self.slide_zoom.value())))/100)
            ab = AnnotationBbox(imagebox, xy=(float(eval(str(self.slide_posx.value())))/100,float(eval(str(self.slide_posy.value())))/100), xycoords='axes fraction')
            #self.axes.add_artist(ab)
            MPL.add_artist(ab)  #MPL=self.mpl.canvas.ax

        # legend verification
        if self.check_label.isChecked():
            MPL.legend(shadow=True, loc=0, borderaxespad=0.,fancybox=True)
            #print "legend enabled"
			
       #! tight layout verification
        if self.check_tight.isChecked():
            try:
                
                self.mpl.canvas.fig.tight_layout()
#                print u"tighted"
            except Exception:
#                print u"exception in tight layout occured"
                pass
            #print "legend enabled"   
        
      
        self.mpl.canvas.draw()
        


    def SavePython(self):
        """Saving data as a python script"""
        print u"saving python script"
        #! GUI for script name selection
        shortpath = os.path.basename(filename)
        save_path2 = QFileDialog.getSaveFileName(self,"", shortpath +".py")
        fpy=open(save_path2,"w")
        #! what will be written
        fpy.write('#_________________________saved python script_______________ \n')
        fpy.write('from __future__ import division \n')
        fpy.write('import math \n')
        fpy.write('import numpy \n')
        fpy.write('import pylab \n')
        fpy.write('from pylab import * \n')
        fpy.flush()
        #! writing datapoints
        fpy.write('X=')
        #fpy.write(''.join(str(X)))
        fpy.write(str(X))
        fpy.write('\n')
        fpy.write('Y=')
        fpy.write(''.join(str(Y)))
        fpy.write('\n')
        fpy.flush()
        #writing configuration
        #fpy.write('majorLocatorX=MaxNLocator('+ str(self.sliderXn.value()) +') \n')
        #fpy.write('majorLocatorY=MaxNLocator('+ str(self.sliderYn.value()) +') \n')
        fpy.write("xlabel('$"+ self.edit_xlabel.text()+"$') \n")
        fpy.write("ylabel('$"+ self.edit_ylabel.text()+"$') \n")
        #fpy.write('xaxis.set_major_locator(majorLocatorX) \n')
        #fpy.write('yaxis.set_major_locator(majorLocatorY) \n')
        #plotting
        
        fpy.write("plot(X, Y, 'ro-',")
        fpy.write("label='"+str(self.edit_label.text())+"', ")
        fpy.write('linewidth=3, ')
        fpy.write('picker=2) \n')
        
        #fpy.write("plot(X,Y,'o--') \n")
        fpy.write("show() \n")

        fpy.flush()
        fpy.close()

    def SavePlot(self):
        shortpath = os.path.basename(filename)
        file_choices2 = "svg (*.svg)|*.svg"
        
        path2 = unicode(QFileDialog.getSaveFileName(self, 
                        'Save svg file', str(shortpath[:-5])+'.svg', 
                        file_choices2))     
                        
        if path2:
            
            self.mpl.canvas.print_figure(path2, dpi=100)
            self.statusBar().showMessage('Saved to %s' % path2, 2000)
        
        file_choices = "PNG (*.png)|*.png"
        
        path = unicode(QFileDialog.getSaveFileName(self, 
                        'Save png file',str(shortpath[:-5])+ '.png', 
                        file_choices))
        
        if path:
            self.mpl.canvas.print_figure(path, dpi=100)
            self.statusBar().showMessage('Saved to %s' % path, 2000)


#!=======================================usuall command for starting GUI=============================================	

def main():
    app = QtGui.QApplication(sys.argv)  # create the GUI application
    dmw = DesignerMainWindow()          # instantiate the main window
    dmw.show()                          # show it
    sys.exit(app.exec_())

#! defining used file 
if __name__ == "__main__":
    print u"used sys.args=",sys.argv
    filename = sys.argv[1]
    main()


