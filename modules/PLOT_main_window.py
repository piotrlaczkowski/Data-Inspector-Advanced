# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PLOT_v30_main.ui'
#
# Created: Thu Dec 19 12:12:56 2013
#      by: PyQt4 UI code generator 4.10.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1183, 632)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout_4 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.mpl = MplWidget(self.centralwidget)
        self.mpl.setMinimumSize(QtCore.QSize(650, 558))
        self.mpl.setObjectName(_fromUtf8("mpl"))
        self.gridLayout_4.addWidget(self.mpl, 0, 0, 1, 1)
        self.line_20 = QtGui.QFrame(self.centralwidget)
        self.line_20.setFrameShape(QtGui.QFrame.HLine)
        self.line_20.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_20.setObjectName(_fromUtf8("line_20"))
        self.gridLayout_4.addWidget(self.line_20, 1, 0, 1, 2)
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setTabPosition(QtGui.QTabWidget.North)
        self.tabWidget.setElideMode(QtCore.Qt.ElideLeft)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.gridLayout_2 = QtGui.QGridLayout(self.tab)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.horizontalLayout_11 = QtGui.QHBoxLayout()
        self.horizontalLayout_11.setSizeConstraint(QtGui.QLayout.SetNoConstraint)
        self.horizontalLayout_11.setObjectName(_fromUtf8("horizontalLayout_11"))
        self.l_x = QtGui.QLabel(self.tab)
        self.l_x.setObjectName(_fromUtf8("l_x"))
        self.horizontalLayout_11.addWidget(self.l_x)
        self.combo_x = QtGui.QComboBox(self.tab)
        self.combo_x.setMaximumSize(QtCore.QSize(50, 16777215))
        self.combo_x.setObjectName(_fromUtf8("combo_x"))
        self.horizontalLayout_11.addWidget(self.combo_x)
        self.l_y = QtGui.QLabel(self.tab)
        self.l_y.setObjectName(_fromUtf8("l_y"))
        self.horizontalLayout_11.addWidget(self.l_y)
        self.combo_y = QtGui.QComboBox(self.tab)
        self.combo_y.setMaximumSize(QtCore.QSize(50, 16777215))
        self.combo_y.setObjectName(_fromUtf8("combo_y"))
        self.horizontalLayout_11.addWidget(self.combo_y)
        self.l_start = QtGui.QLabel(self.tab)
        self.l_start.setObjectName(_fromUtf8("l_start"))
        self.horizontalLayout_11.addWidget(self.l_start)
        self.slide_start = QtGui.QSlider(self.tab)
        self.slide_start.setMinimum(1)
        self.slide_start.setProperty("value", 10)
        self.slide_start.setOrientation(QtCore.Qt.Horizontal)
        self.slide_start.setObjectName(_fromUtf8("slide_start"))
        self.horizontalLayout_11.addWidget(self.slide_start)
        self.l_stop = QtGui.QLabel(self.tab)
        self.l_stop.setObjectName(_fromUtf8("l_stop"))
        self.horizontalLayout_11.addWidget(self.l_stop)
        self.slide_stop = QtGui.QSlider(self.tab)
        self.slide_stop.setMinimum(1)
        self.slide_stop.setProperty("value", 10)
        self.slide_stop.setOrientation(QtCore.Qt.Horizontal)
        self.slide_stop.setObjectName(_fromUtf8("slide_stop"))
        self.horizontalLayout_11.addWidget(self.slide_stop)
        self.gridLayout_2.addLayout(self.horizontalLayout_11, 0, 0, 1, 1)
        self.line_17 = QtGui.QFrame(self.tab)
        self.line_17.setFrameShape(QtGui.QFrame.HLine)
        self.line_17.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_17.setObjectName(_fromUtf8("line_17"))
        self.gridLayout_2.addWidget(self.line_17, 1, 0, 1, 1)
        self.horizontalLayout_10 = QtGui.QHBoxLayout()
        self.horizontalLayout_10.setObjectName(_fromUtf8("horizontalLayout_10"))
        self.l_xlabel = QtGui.QLabel(self.tab)
        self.l_xlabel.setObjectName(_fromUtf8("l_xlabel"))
        self.horizontalLayout_10.addWidget(self.l_xlabel)
        self.edit_xlabel = QtGui.QLineEdit(self.tab)
        self.edit_xlabel.setMaximumSize(QtCore.QSize(80, 16777215))
        self.edit_xlabel.setObjectName(_fromUtf8("edit_xlabel"))
        self.horizontalLayout_10.addWidget(self.edit_xlabel)
        self.l_xsize = QtGui.QLabel(self.tab)
        self.l_xsize.setObjectName(_fromUtf8("l_xsize"))
        self.horizontalLayout_10.addWidget(self.l_xsize)
        self.slide_xsize = QtGui.QSlider(self.tab)
        self.slide_xsize.setMinimum(8)
        self.slide_xsize.setProperty("value", 20)
        self.slide_xsize.setOrientation(QtCore.Qt.Horizontal)
        self.slide_xsize.setObjectName(_fromUtf8("slide_xsize"))
        self.horizontalLayout_10.addWidget(self.slide_xsize)
        self.gridLayout_2.addLayout(self.horizontalLayout_10, 2, 0, 1, 1)
        self.horizontalLayout_12 = QtGui.QHBoxLayout()
        self.horizontalLayout_12.setObjectName(_fromUtf8("horizontalLayout_12"))
        self.l_x_ticks = QtGui.QLabel(self.tab)
        self.l_x_ticks.setObjectName(_fromUtf8("l_x_ticks"))
        self.horizontalLayout_12.addWidget(self.l_x_ticks)
        self.slide_xnr = QtGui.QSlider(self.tab)
        self.slide_xnr.setMinimum(3)
        self.slide_xnr.setMaximum(20)
        self.slide_xnr.setProperty("value", 5)
        self.slide_xnr.setOrientation(QtCore.Qt.Horizontal)
        self.slide_xnr.setObjectName(_fromUtf8("slide_xnr"))
        self.horizontalLayout_12.addWidget(self.slide_xnr)
        self.l_xsizeticks = QtGui.QLabel(self.tab)
        self.l_xsizeticks.setObjectName(_fromUtf8("l_xsizeticks"))
        self.horizontalLayout_12.addWidget(self.l_xsizeticks)
        self.slide_xsizeticks = QtGui.QSlider(self.tab)
        self.slide_xsizeticks.setMinimum(8)
        self.slide_xsizeticks.setProperty("value", 18)
        self.slide_xsizeticks.setOrientation(QtCore.Qt.Horizontal)
        self.slide_xsizeticks.setObjectName(_fromUtf8("slide_xsizeticks"))
        self.horizontalLayout_12.addWidget(self.slide_xsizeticks)
        self.gridLayout_2.addLayout(self.horizontalLayout_12, 3, 0, 1, 1)
        self.line_16 = QtGui.QFrame(self.tab)
        self.line_16.setFrameShape(QtGui.QFrame.HLine)
        self.line_16.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_16.setObjectName(_fromUtf8("line_16"))
        self.gridLayout_2.addWidget(self.line_16, 4, 0, 1, 1)
        self.horizontalLayout_13 = QtGui.QHBoxLayout()
        self.horizontalLayout_13.setObjectName(_fromUtf8("horizontalLayout_13"))
        self.l_ylabel = QtGui.QLabel(self.tab)
        self.l_ylabel.setObjectName(_fromUtf8("l_ylabel"))
        self.horizontalLayout_13.addWidget(self.l_ylabel)
        self.edit_ylabel = QtGui.QLineEdit(self.tab)
        self.edit_ylabel.setMaximumSize(QtCore.QSize(80, 16777215))
        self.edit_ylabel.setObjectName(_fromUtf8("edit_ylabel"))
        self.horizontalLayout_13.addWidget(self.edit_ylabel)
        self.l_ysize = QtGui.QLabel(self.tab)
        self.l_ysize.setObjectName(_fromUtf8("l_ysize"))
        self.horizontalLayout_13.addWidget(self.l_ysize)
        self.slide_ysize = QtGui.QSlider(self.tab)
        self.slide_ysize.setMinimum(8)
        self.slide_ysize.setProperty("value", 20)
        self.slide_ysize.setOrientation(QtCore.Qt.Horizontal)
        self.slide_ysize.setObjectName(_fromUtf8("slide_ysize"))
        self.horizontalLayout_13.addWidget(self.slide_ysize)
        self.gridLayout_2.addLayout(self.horizontalLayout_13, 5, 0, 1, 1)
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.l_y_ticks = QtGui.QLabel(self.tab)
        self.l_y_ticks.setObjectName(_fromUtf8("l_y_ticks"))
        self.horizontalLayout_8.addWidget(self.l_y_ticks)
        self.slide_ynr = QtGui.QSlider(self.tab)
        self.slide_ynr.setMinimum(3)
        self.slide_ynr.setMaximum(20)
        self.slide_ynr.setProperty("value", 5)
        self.slide_ynr.setOrientation(QtCore.Qt.Horizontal)
        self.slide_ynr.setObjectName(_fromUtf8("slide_ynr"))
        self.horizontalLayout_8.addWidget(self.slide_ynr)
        self.l_ysizeticks = QtGui.QLabel(self.tab)
        self.l_ysizeticks.setObjectName(_fromUtf8("l_ysizeticks"))
        self.horizontalLayout_8.addWidget(self.l_ysizeticks)
        self.slide_ysizeticks = QtGui.QSlider(self.tab)
        self.slide_ysizeticks.setMinimum(8)
        self.slide_ysizeticks.setProperty("value", 18)
        self.slide_ysizeticks.setOrientation(QtCore.Qt.Horizontal)
        self.slide_ysizeticks.setObjectName(_fromUtf8("slide_ysizeticks"))
        self.horizontalLayout_8.addWidget(self.slide_ysizeticks)
        self.gridLayout_2.addLayout(self.horizontalLayout_8, 6, 0, 1, 1)
        self.line_19 = QtGui.QFrame(self.tab)
        self.line_19.setFrameShape(QtGui.QFrame.HLine)
        self.line_19.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_19.setObjectName(_fromUtf8("line_19"))
        self.gridLayout_2.addWidget(self.line_19, 7, 0, 1, 1)
        self.horizontalLayout_9 = QtGui.QHBoxLayout()
        self.horizontalLayout_9.setObjectName(_fromUtf8("horizontalLayout_9"))
        self.l_title = QtGui.QLabel(self.tab)
        self.l_title.setObjectName(_fromUtf8("l_title"))
        self.horizontalLayout_9.addWidget(self.l_title)
        self.edit_title = QtGui.QLineEdit(self.tab)
        self.edit_title.setMaximumSize(QtCore.QSize(100, 16777215))
        self.edit_title.setObjectName(_fromUtf8("edit_title"))
        self.horizontalLayout_9.addWidget(self.edit_title)
        self.l_label = QtGui.QLabel(self.tab)
        self.l_label.setObjectName(_fromUtf8("l_label"))
        self.horizontalLayout_9.addWidget(self.l_label)
        self.edit_label = QtGui.QLineEdit(self.tab)
        self.edit_label.setMaximumSize(QtCore.QSize(100, 16777215))
        self.edit_label.setObjectName(_fromUtf8("edit_label"))
        self.horizontalLayout_9.addWidget(self.edit_label)
        self.l_titlesize = QtGui.QLabel(self.tab)
        self.l_titlesize.setObjectName(_fromUtf8("l_titlesize"))
        self.horizontalLayout_9.addWidget(self.l_titlesize)
        self.slide_titlesize = QtGui.QSlider(self.tab)
        self.slide_titlesize.setMinimum(8)
        self.slide_titlesize.setProperty("value", 10)
        self.slide_titlesize.setOrientation(QtCore.Qt.Horizontal)
        self.slide_titlesize.setObjectName(_fromUtf8("slide_titlesize"))
        self.horizontalLayout_9.addWidget(self.slide_titlesize)
        self.gridLayout_2.addLayout(self.horizontalLayout_9, 8, 0, 1, 1)
        self.line_23 = QtGui.QFrame(self.tab)
        self.line_23.setFrameShape(QtGui.QFrame.HLine)
        self.line_23.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_23.setObjectName(_fromUtf8("line_23"))
        self.gridLayout_2.addWidget(self.line_23, 9, 0, 1, 1)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.l_inset = QtGui.QLabel(self.tab)
        self.l_inset.setObjectName(_fromUtf8("l_inset"))
        self.horizontalLayout_5.addWidget(self.l_inset)
        self.edit_inset = QtGui.QLineEdit(self.tab)
        self.edit_inset.setMaximumSize(QtCore.QSize(25, 16777215))
        self.edit_inset.setObjectName(_fromUtf8("edit_inset"))
        self.horizontalLayout_5.addWidget(self.edit_inset)
        self.l_zoom = QtGui.QLabel(self.tab)
        self.l_zoom.setObjectName(_fromUtf8("l_zoom"))
        self.horizontalLayout_5.addWidget(self.l_zoom)
        self.slide_zoom = QtGui.QSlider(self.tab)
        self.slide_zoom.setProperty("value", 70)
        self.slide_zoom.setSliderPosition(70)
        self.slide_zoom.setOrientation(QtCore.Qt.Horizontal)
        self.slide_zoom.setObjectName(_fromUtf8("slide_zoom"))
        self.horizontalLayout_5.addWidget(self.slide_zoom)
        self.l_pox = QtGui.QLabel(self.tab)
        self.l_pox.setObjectName(_fromUtf8("l_pox"))
        self.horizontalLayout_5.addWidget(self.l_pox)
        self.slide_posx = QtGui.QSlider(self.tab)
        self.slide_posx.setProperty("value", 80)
        self.slide_posx.setOrientation(QtCore.Qt.Horizontal)
        self.slide_posx.setObjectName(_fromUtf8("slide_posx"))
        self.horizontalLayout_5.addWidget(self.slide_posx)
        self.l_posy = QtGui.QLabel(self.tab)
        self.l_posy.setObjectName(_fromUtf8("l_posy"))
        self.horizontalLayout_5.addWidget(self.l_posy)
        self.slide_posy = QtGui.QSlider(self.tab)
        self.slide_posy.setProperty("value", 80)
        self.slide_posy.setOrientation(QtCore.Qt.Horizontal)
        self.slide_posy.setObjectName(_fromUtf8("slide_posy"))
        self.horizontalLayout_5.addWidget(self.slide_posy)
        self.gridLayout_2.addLayout(self.horizontalLayout_5, 10, 0, 1, 1)
        self.line_25 = QtGui.QFrame(self.tab)
        self.line_25.setFrameShape(QtGui.QFrame.HLine)
        self.line_25.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_25.setObjectName(_fromUtf8("line_25"))
        self.gridLayout_2.addWidget(self.line_25, 11, 0, 1, 1)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.check_grid = QtGui.QCheckBox(self.tab)
        self.check_grid.setObjectName(_fromUtf8("check_grid"))
        self.horizontalLayout_2.addWidget(self.check_grid)
        self.check_label = QtGui.QCheckBox(self.tab)
        self.check_label.setChecked(False)
        self.check_label.setObjectName(_fromUtf8("check_label"))
        self.horizontalLayout_2.addWidget(self.check_label)
        self.check_tight = QtGui.QCheckBox(self.tab)
        self.check_tight.setEnabled(True)
        self.check_tight.setAutoFillBackground(False)
        self.check_tight.setChecked(True)
        self.check_tight.setObjectName(_fromUtf8("check_tight"))
        self.horizontalLayout_2.addWidget(self.check_tight)
        self.gridLayout_2.addLayout(self.horizontalLayout_2, 12, 0, 1, 1)
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.gridLayout = QtGui.QGridLayout(self.tab_2)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.check_xlim = QtGui.QCheckBox(self.tab_2)
        self.check_xlim.setObjectName(_fromUtf8("check_xlim"))
        self.horizontalLayout_4.addWidget(self.check_xlim)
        self.l_xmin = QtGui.QLabel(self.tab_2)
        self.l_xmin.setObjectName(_fromUtf8("l_xmin"))
        self.horizontalLayout_4.addWidget(self.l_xmin)
        self.edit_xmin = QtGui.QLineEdit(self.tab_2)
        self.edit_xmin.setMaximumSize(QtCore.QSize(80, 16777215))
        self.edit_xmin.setObjectName(_fromUtf8("edit_xmin"))
        self.horizontalLayout_4.addWidget(self.edit_xmin)
        self.l_xmax = QtGui.QLabel(self.tab_2)
        self.l_xmax.setObjectName(_fromUtf8("l_xmax"))
        self.horizontalLayout_4.addWidget(self.l_xmax)
        self.edit_xmax = QtGui.QLineEdit(self.tab_2)
        self.edit_xmax.setMaximumSize(QtCore.QSize(80, 16777215))
        self.edit_xmax.setObjectName(_fromUtf8("edit_xmax"))
        self.horizontalLayout_4.addWidget(self.edit_xmax)
        self.gridLayout.addLayout(self.horizontalLayout_4, 0, 0, 1, 2)
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.check_ylim = QtGui.QCheckBox(self.tab_2)
        self.check_ylim.setObjectName(_fromUtf8("check_ylim"))
        self.horizontalLayout_7.addWidget(self.check_ylim)
        self.l_ymin = QtGui.QLabel(self.tab_2)
        self.l_ymin.setObjectName(_fromUtf8("l_ymin"))
        self.horizontalLayout_7.addWidget(self.l_ymin)
        self.edit_ymin = QtGui.QLineEdit(self.tab_2)
        self.edit_ymin.setMaximumSize(QtCore.QSize(80, 16777215))
        self.edit_ymin.setObjectName(_fromUtf8("edit_ymin"))
        self.horizontalLayout_7.addWidget(self.edit_ymin)
        self.l_ymax = QtGui.QLabel(self.tab_2)
        self.l_ymax.setObjectName(_fromUtf8("l_ymax"))
        self.horizontalLayout_7.addWidget(self.l_ymax)
        self.edit_ymax = QtGui.QLineEdit(self.tab_2)
        self.edit_ymax.setMaximumSize(QtCore.QSize(80, 16777215))
        self.edit_ymax.setObjectName(_fromUtf8("edit_ymax"))
        self.horizontalLayout_7.addWidget(self.edit_ymax)
        self.gridLayout.addLayout(self.horizontalLayout_7, 1, 0, 1, 2)
        self.line_21 = QtGui.QFrame(self.tab_2)
        self.line_21.setFrameShape(QtGui.QFrame.HLine)
        self.line_21.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_21.setObjectName(_fromUtf8("line_21"))
        self.gridLayout.addWidget(self.line_21, 2, 0, 1, 2)
        self.horizontalLayout_14 = QtGui.QHBoxLayout()
        self.horizontalLayout_14.setObjectName(_fromUtf8("horizontalLayout_14"))
        self.label = QtGui.QLabel(self.tab_2)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_14.addWidget(self.label)
        self.edit_smooth = QtGui.QLineEdit(self.tab_2)
        self.edit_smooth.setMaximumSize(QtCore.QSize(22, 16777215))
        self.edit_smooth.setObjectName(_fromUtf8("edit_smooth"))
        self.horizontalLayout_14.addWidget(self.edit_smooth)
        self.combo_smooth = QtGui.QComboBox(self.tab_2)
        self.combo_smooth.setMinimumSize(QtCore.QSize(100, 0))
        self.combo_smooth.setObjectName(_fromUtf8("combo_smooth"))
        self.combo_smooth.addItem(_fromUtf8(""))
        self.combo_smooth.addItem(_fromUtf8(""))
        self.combo_smooth.addItem(_fromUtf8(""))
        self.combo_smooth.addItem(_fromUtf8(""))
        self.combo_smooth.addItem(_fromUtf8(""))
        self.horizontalLayout_14.addWidget(self.combo_smooth)
        self.l_dt = QtGui.QLabel(self.tab_2)
        self.l_dt.setObjectName(_fromUtf8("l_dt"))
        self.horizontalLayout_14.addWidget(self.l_dt)
        self.edit_dt = QtGui.QLineEdit(self.tab_2)
        self.edit_dt.setMaximumSize(QtCore.QSize(25, 16777215))
        self.edit_dt.setObjectName(_fromUtf8("edit_dt"))
        self.horizontalLayout_14.addWidget(self.edit_dt)
        self.l_dH = QtGui.QLabel(self.tab_2)
        self.l_dH.setObjectName(_fromUtf8("l_dH"))
        self.horizontalLayout_14.addWidget(self.l_dH)
        self.edit_dH = QtGui.QLineEdit(self.tab_2)
        self.edit_dH.setMaximumSize(QtCore.QSize(25, 16777215))
        self.edit_dH.setObjectName(_fromUtf8("edit_dH"))
        self.horizontalLayout_14.addWidget(self.edit_dH)
        self.l_dH2 = QtGui.QLabel(self.tab_2)
        self.l_dH2.setObjectName(_fromUtf8("l_dH2"))
        self.horizontalLayout_14.addWidget(self.l_dH2)
        self.edit_dH2 = QtGui.QLineEdit(self.tab_2)
        self.edit_dH2.setMaximumSize(QtCore.QSize(25, 16777215))
        self.edit_dH2.setObjectName(_fromUtf8("edit_dH2"))
        self.horizontalLayout_14.addWidget(self.edit_dH2)
        self.gridLayout.addLayout(self.horizontalLayout_14, 3, 0, 1, 2)
        self.line_22 = QtGui.QFrame(self.tab_2)
        self.line_22.setFrameShape(QtGui.QFrame.HLine)
        self.line_22.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_22.setObjectName(_fromUtf8("line_22"))
        self.gridLayout.addWidget(self.line_22, 4, 0, 1, 2)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.l_divy = QtGui.QLabel(self.tab_2)
        self.l_divy.setObjectName(_fromUtf8("l_divy"))
        self.horizontalLayout_6.addWidget(self.l_divy)
        self.edit_divy = QtGui.QLineEdit(self.tab_2)
        self.edit_divy.setMaximumSize(QtCore.QSize(35, 16777215))
        self.edit_divy.setObjectName(_fromUtf8("edit_divy"))
        self.horizontalLayout_6.addWidget(self.edit_divy)
        self.l_multy = QtGui.QLabel(self.tab_2)
        self.l_multy.setObjectName(_fromUtf8("l_multy"))
        self.horizontalLayout_6.addWidget(self.l_multy)
        self.edit_multy = QtGui.QLineEdit(self.tab_2)
        self.edit_multy.setMaximumSize(QtCore.QSize(35, 16777215))
        self.edit_multy.setObjectName(_fromUtf8("edit_multy"))
        self.horizontalLayout_6.addWidget(self.edit_multy)
        self.l_divx = QtGui.QLabel(self.tab_2)
        self.l_divx.setObjectName(_fromUtf8("l_divx"))
        self.horizontalLayout_6.addWidget(self.l_divx)
        self.edit_divx = QtGui.QLineEdit(self.tab_2)
        self.edit_divx.setMaximumSize(QtCore.QSize(35, 16777215))
        self.edit_divx.setText(_fromUtf8("1"))
        self.edit_divx.setObjectName(_fromUtf8("edit_divx"))
        self.horizontalLayout_6.addWidget(self.edit_divx)
        self.l_multx = QtGui.QLabel(self.tab_2)
        self.l_multx.setObjectName(_fromUtf8("l_multx"))
        self.horizontalLayout_6.addWidget(self.l_multx)
        self.edit_multx = QtGui.QLineEdit(self.tab_2)
        self.edit_multx.setMaximumSize(QtCore.QSize(35, 16777215))
        self.edit_multx.setObjectName(_fromUtf8("edit_multx"))
        self.horizontalLayout_6.addWidget(self.edit_multx)
        self.gridLayout.addLayout(self.horizontalLayout_6, 5, 0, 1, 2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.l_derivy = QtGui.QLabel(self.tab_2)
        self.l_derivy.setObjectName(_fromUtf8("l_derivy"))
        self.horizontalLayout_3.addWidget(self.l_derivy)
        self.check_derivate = QtGui.QCheckBox(self.tab_2)
        self.check_derivate.setText(_fromUtf8(""))
        self.check_derivate.setObjectName(_fromUtf8("check_derivate"))
        self.horizontalLayout_3.addWidget(self.check_derivate)
        self.l_degree = QtGui.QLabel(self.tab_2)
        self.l_degree.setObjectName(_fromUtf8("l_degree"))
        self.horizontalLayout_3.addWidget(self.l_degree)
        self.edit_degree = QtGui.QLineEdit(self.tab_2)
        self.edit_degree.setMaximumSize(QtCore.QSize(24, 16777215))
        self.edit_degree.setObjectName(_fromUtf8("edit_degree"))
        self.horizontalLayout_3.addWidget(self.edit_degree)
        self.line = QtGui.QFrame(self.tab_2)
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.horizontalLayout_3.addWidget(self.line)
        self.check_invertx = QtGui.QCheckBox(self.tab_2)
        self.check_invertx.setObjectName(_fromUtf8("check_invertx"))
        self.horizontalLayout_3.addWidget(self.check_invertx)
        self.check_inverty = QtGui.QCheckBox(self.tab_2)
        self.check_inverty.setObjectName(_fromUtf8("check_inverty"))
        self.horizontalLayout_3.addWidget(self.check_inverty)
        self.gridLayout.addLayout(self.horizontalLayout_3, 6, 0, 1, 2)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.btn_pythonize = QtGui.QPushButton(self.tab_2)
        self.btn_pythonize.setObjectName(_fromUtf8("btn_pythonize"))
        self.horizontalLayout.addWidget(self.btn_pythonize)
        self.btn_SaveFigs = QtGui.QPushButton(self.tab_2)
        self.btn_SaveFigs.setObjectName(_fromUtf8("btn_SaveFigs"))
        self.horizontalLayout.addWidget(self.btn_SaveFigs)
        self.gridLayout.addLayout(self.horizontalLayout, 7, 1, 1, 1)
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.gridLayout_4.addWidget(self.tabWidget, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1183, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.l_x.setText(_translate("MainWindow", "X", None))
        self.l_y.setText(_translate("MainWindow", "Y", None))
        self.l_start.setText(_translate("MainWindow", "Start", None))
        self.l_stop.setText(_translate("MainWindow", "Stop", None))
        self.l_xlabel.setText(_translate("MainWindow", "X Label", None))
        self.edit_xlabel.setText(_translate("MainWindow", "$H\\,[T]$", None))
        self.l_xsize.setText(_translate("MainWindow", "X size", None))
        self.l_x_ticks.setText(_translate("MainWindow", "X Ticks Nr", None))
        self.l_xsizeticks.setText(_translate("MainWindow", "X size ticks", None))
        self.l_ylabel.setText(_translate("MainWindow", "Y Label", None))
        self.edit_ylabel.setText(_translate("MainWindow", "$V\\,[V]$", None))
        self.l_ysize.setText(_translate("MainWindow", "Y size", None))
        self.l_y_ticks.setText(_translate("MainWindow", "Y Ticks Nr", None))
        self.l_ysizeticks.setText(_translate("MainWindow", "Y size ticks", None))
        self.l_title.setText(_translate("MainWindow", "Title", None))
        self.edit_title.setText(_translate("MainWindow", "$ Title $", None))
        self.l_label.setText(_translate("MainWindow", "Label:", None))
        self.edit_label.setText(_translate("MainWindow", "$ label $", None))
        self.l_titlesize.setText(_translate("MainWindow", "title size", None))
        self.l_inset.setText(_translate("MainWindow", "Inset:", None))
        self.edit_inset.setText(_translate("MainWindow", "0", None))
        self.l_zoom.setText(_translate("MainWindow", "Zoom", None))
        self.l_pox.setText(_translate("MainWindow", "PosX", None))
        self.l_posy.setText(_translate("MainWindow", "PosY", None))
        self.check_grid.setText(_translate("MainWindow", "Grid", None))
        self.check_label.setText(_translate("MainWindow", "Label", None))
        self.check_tight.setText(_translate("MainWindow", "Tight", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Basic Setup", None))
        self.check_xlim.setText(_translate("MainWindow", "X lim", None))
        self.l_xmin.setText(_translate("MainWindow", "X min:", None))
        self.l_xmax.setText(_translate("MainWindow", "X max:", None))
        self.check_ylim.setText(_translate("MainWindow", "Y lim", None))
        self.l_ymin.setText(_translate("MainWindow", "Y min:", None))
        self.l_ymax.setText(_translate("MainWindow", "Y max:", None))
        self.label.setText(_translate("MainWindow", "Smooth:", None))
        self.edit_smooth.setText(_translate("MainWindow", "1", None))
        self.combo_smooth.setItemText(0, _translate("MainWindow", "flat", None))
        self.combo_smooth.setItemText(1, _translate("MainWindow", "hanning", None))
        self.combo_smooth.setItemText(2, _translate("MainWindow", "hamming", None))
        self.combo_smooth.setItemText(3, _translate("MainWindow", "bartlett", None))
        self.combo_smooth.setItemText(4, _translate("MainWindow", "blackman", None))
        self.l_dt.setText(_translate("MainWindow", "dt", None))
        self.edit_dt.setText(_translate("MainWindow", "0", None))
        self.l_dH.setText(_translate("MainWindow", "dH", None))
        self.edit_dH.setText(_translate("MainWindow", "0", None))
        self.l_dH2.setText(_translate("MainWindow", "dH2", None))
        self.edit_dH2.setText(_translate("MainWindow", "0", None))
        self.l_divy.setText(_translate("MainWindow", "Div Y.", None))
        self.edit_divy.setText(_translate("MainWindow", "1", None))
        self.l_multy.setText(_translate("MainWindow", "Mult. Y", None))
        self.edit_multy.setText(_translate("MainWindow", "1", None))
        self.l_divx.setText(_translate("MainWindow", "Div X.", None))
        self.l_multx.setText(_translate("MainWindow", "Mult. X", None))
        self.edit_multx.setText(_translate("MainWindow", "1", None))
        self.l_derivy.setText(_translate("MainWindow", "Derivate Y:", None))
        self.l_degree.setText(_translate("MainWindow", "Degree:", None))
        self.edit_degree.setText(_translate("MainWindow", "1", None))
        self.check_invertx.setText(_translate("MainWindow", "Invert X", None))
        self.check_inverty.setText(_translate("MainWindow", "Invert Y", None))
        self.btn_pythonize.setText(_translate("MainWindow", "Pythonize", None))
        self.btn_SaveFigs.setText(_translate("MainWindow", "Save Figs", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Corrections", None))

from mplwidget import MplWidget