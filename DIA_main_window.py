# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DIA.ui'
#
# Created: Fri Dec 20 13:07:37 2013
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
        MainWindow.resize(1158, 751)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.l_path = QtGui.QLabel(self.centralwidget)
        self.l_path.setObjectName(_fromUtf8("l_path"))
        self.horizontalLayout.addWidget(self.l_path)
        self.edit_path = QtGui.QLineEdit(self.centralwidget)
        self.edit_path.setMinimumSize(QtCore.QSize(631, 27))
        self.edit_path.setObjectName(_fromUtf8("edit_path"))
        self.horizontalLayout.addWidget(self.edit_path)
        self.btn_folder = QtGui.QPushButton(self.centralwidget)
        self.btn_folder.setText(_fromUtf8(""))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("icons/Folder.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_folder.setIcon(icon)
        self.btn_folder.setIconSize(QtCore.QSize(32, 32))
        self.btn_folder.setFlat(True)
        self.btn_folder.setObjectName(_fromUtf8("btn_folder"))
        self.horizontalLayout.addWidget(self.btn_folder)
        self.btn_find = QtGui.QPushButton(self.centralwidget)
        self.btn_find.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("icons/Radar.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_find.setIcon(icon1)
        self.btn_find.setIconSize(QtCore.QSize(32, 32))
        self.btn_find.setFlat(True)
        self.btn_find.setObjectName(_fromUtf8("btn_find"))
        self.horizontalLayout.addWidget(self.btn_find)
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.edit_ext = QtGui.QLineEdit(self.centralwidget)
        self.edit_ext.setMinimumSize(QtCore.QSize(50, 0))
        self.edit_ext.setMaximumSize(QtCore.QSize(50, 16777215))
        self.edit_ext.setObjectName(_fromUtf8("edit_ext"))
        self.horizontalLayout.addWidget(self.edit_ext)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.web_data = QtWebKit.QWebView(self.centralwidget)
        self.web_data.setMinimumSize(QtCore.QSize(1071, 531))
        self.web_data.setProperty("url", QtCore.QUrl(_fromUtf8("about:blank")))
        self.web_data.setObjectName(_fromUtf8("web_data"))
        self.gridLayout.addWidget(self.web_data, 1, 0, 1, 1)
        self.line = QtGui.QFrame(self.centralwidget)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.gridLayout.addWidget(self.line, 2, 0, 1, 1)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.l_selected = QtGui.QLabel(self.centralwidget)
        self.l_selected.setObjectName(_fromUtf8("l_selected"))
        self.horizontalLayout_3.addWidget(self.l_selected)
        self.edit_selected = QtGui.QLineEdit(self.centralwidget)
        self.edit_selected.setEnabled(False)
        self.edit_selected.setMinimumSize(QtCore.QSize(701, 0))
        self.edit_selected.setObjectName(_fromUtf8("edit_selected"))
        self.horizontalLayout_3.addWidget(self.edit_selected)
        self.gridLayout.addLayout(self.horizontalLayout_3, 3, 0, 1, 1)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.l_meta = QtGui.QLabel(self.centralwidget)
        self.l_meta.setObjectName(_fromUtf8("l_meta"))
        self.horizontalLayout_2.addWidget(self.l_meta)
        self.browser_meta = QtGui.QTextBrowser(self.centralwidget)
        self.browser_meta.setMinimumSize(QtCore.QSize(620, 0))
        self.browser_meta.setMaximumSize(QtCore.QSize(519, 39))
        self.browser_meta.setObjectName(_fromUtf8("browser_meta"))
        self.horizontalLayout_2.addWidget(self.browser_meta)
        self.combo_module = QtGui.QComboBox(self.centralwidget)
        self.combo_module.setMinimumSize(QtCore.QSize(300, 0))
        self.combo_module.setObjectName(_fromUtf8("combo_module"))
        self.horizontalLayout_2.addWidget(self.combo_module)
        self.btn_go = QtGui.QPushButton(self.centralwidget)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8("icons/Go.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_go.setIcon(icon2)
        self.btn_go.setIconSize(QtCore.QSize(32, 32))
        self.btn_go.setFlat(True)
        self.btn_go.setObjectName(_fromUtf8("btn_go"))
        self.horizontalLayout_2.addWidget(self.btn_go)
        self.btn_PDF = QtGui.QPushButton(self.centralwidget)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8("icons/PDF.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_PDF.setIcon(icon3)
        self.btn_PDF.setIconSize(QtCore.QSize(32, 32))
        self.btn_PDF.setFlat(True)
        self.btn_PDF.setObjectName(_fromUtf8("btn_PDF"))
        self.horizontalLayout_2.addWidget(self.btn_PDF)
        self.gridLayout.addLayout(self.horizontalLayout_2, 4, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1158, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.l_path.setText(_translate("MainWindow", "Path:", None))
        self.edit_path.setText(_translate("MainWindow", "\"DATA PATH TO CHOSE --------------------------------------------->\"", None))
        self.btn_folder.setToolTip(_translate("MainWindow", "Change current scan folder", None))
        self.btn_find.setToolTip(_translate("MainWindow", "Start scanning for files with specified extention.", None))
        self.label.setText(_translate("MainWindow", "ext:", None))
        self.edit_ext.setToolTip(_translate("MainWindow", "files extention to look for.", None))
        self.edit_ext.setText(_translate("MainWindow", ".data", None))
        self.l_selected.setText(_translate("MainWindow", "Selected File:", None))
        self.edit_selected.setToolTip(_translate("MainWindow", "selected file-path.", None))
        self.l_meta.setText(_translate("MainWindow", "Meta Data:", None))
        self.browser_meta.setToolTip(_translate("MainWindow", "files meta-data or header.", None))
        self.combo_module.setToolTip(_translate("MainWindow", "choice of a module that will be applied to a selected file.", None))
        self.btn_go.setToolTip(_translate("MainWindow", "aply selected module.", None))
        self.btn_go.setText(_translate("MainWindow", "GO", None))
        self.btn_PDF.setToolTip(_translate("MainWindow", "Gererate a PDF report from acctual html vew.", None))
        self.btn_PDF.setText(_translate("MainWindow", "PDF", None))

from PyQt4 import QtWebKit
