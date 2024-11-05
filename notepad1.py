# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'notepad_1.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        MainWindow.setDocumentMode(False)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Triangular)


        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setObjectName("textEdit")
        self.horizontalLayout_8.addWidget(self.textEdit)
        MainWindow.setCentralWidget(self.textEdit)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 434, 18))
        self.menubar.setObjectName("menubar")
        self.menufile = QtWidgets.QMenu(self.menubar)
        self.menufile.setObjectName("menufile")
        self.menuedit = QtWidgets.QMenu(self.menubar)
        self.menuedit.setObjectName("menuedit")
        self.menuview = QtWidgets.QMenu(self.menubar)

    




        self.menuview.setObjectName("menuview")
        MainWindow.setMenuBar(self.menubar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.toolBar.setMouseTracking(False)
        self.toolBar.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        MainWindow.insertToolBarBreak(self.toolBar)
        self.new_icon = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:/Users/Aneesh.s/OneDrive/Desktop/mixed circuit signal/add-file.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.new_icon.setIcon(icon)
        self.new_icon.setObjectName("new_icon")

        
        self.new_icon.triggered.connect(self.new_fun)

        self.actionopen = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("C:/Users/Aneesh.s/OneDrive/Desktop/mixed circuit signal/folder.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionopen.setIcon(icon1)
        self.actionopen.setObjectName("actionopen")
        self.actionsave = QtWidgets.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("C:/Users/Aneesh.s/OneDrive/Desktop/mixed circuit signal/diskette.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionsave.setIcon(icon2)
        self.actionsave.setObjectName("actionsave")

        self.actionsave.triggered.connect(self.save_fun)

        self.actioncut = QtWidgets.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("C:/Users/Aneesh.s/OneDrive/Desktop/mixed circuit signal/cut.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actioncut.setIcon(icon3)
        self.actioncut.setObjectName("actioncut")

        self.actioncut.triggered.connect(self.cut_fun)

        self.actioncopy = QtWidgets.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("C:/Users/Aneesh.s/OneDrive/Desktop/mixed circuit signal/copy-two-paper-sheets-interface-symbol.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actioncopy.setIcon(icon4)
        self.actioncopy.setObjectName("actioncopy")
        self.actioncopy.triggered.connect(self.copy_fun)

        self.actionOpen_in_Default_Viewer = QtWidgets.QAction(MainWindow)
        self.actionOpen_in_Default_Viewer.setObjectName("actionOpen_in_Default_Viewer")
        self.actionOpen_Folder_as_Workspace = QtWidgets.QAction(MainWindow)
        self.actionOpen_Folder_as_Workspace.setObjectName("actionOpen_Folder_as_Workspace")
        self.actionReload_From_Disk = QtWidgets.QAction(MainWindow)
        self.actionReload_From_Disk.setObjectName("actionReload_From_Disk")
        self.actionsave_2 = QtWidgets.QAction(MainWindow)
        self.actionsave_2.setObjectName("actionsave_2")
        self.actionSave_As = QtWidgets.QAction(MainWindow)
        self.actionSave_As.setObjectName("actionSave_As")
        self.actionSave_a_Copy_As = QtWidgets.QAction(MainWindow)
        self.actionSave_a_Copy_As.setObjectName("actionSave_a_Copy_As")
        self.actionSave_All = QtWidgets.QAction(MainWindow)
        self.actionSave_All.setObjectName("actionSave_All")
        self.actionRename = QtWidgets.QAction(MainWindow)
        self.actionRename.setObjectName("actionRename")
        self.actionColse = QtWidgets.QAction(MainWindow)
        self.actionColse.setObjectName("actionColse")
        self.actionClose_All = QtWidgets.QAction(MainWindow)
        self.actionClose_All.setObjectName("actionClose_All")
        self.actionMove_to_Recycle_Bin = QtWidgets.QAction(MainWindow)
        self.actionMove_to_Recycle_Bin.setObjectName("actionMove_to_Recycle_Bin")
        self.actionload_Session = QtWidgets.QAction(MainWindow)
        self.actionload_Session.setObjectName("actionload_Session")
        self.actionSave_Session = QtWidgets.QAction(MainWindow)
        self.actionSave_Session.setObjectName("actionSave_Session")
        self.actionprint = QtWidgets.QAction(MainWindow)
        self.actionprint.setObjectName("actionprint")
        self.actionprint_now = QtWidgets.QAction(MainWindow)
        self.actionprint_now.setObjectName("actionprint_now")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionpaste = QtWidgets.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("C:/Users/Aneesh.s/OneDrive/Desktop/mixed circuit signal/paste.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionpaste.setIcon(icon5)
        self.actionpaste.setObjectName("actionpaste")

        self.actionpaste.triggered.connect(self.paste_fun)

        self.actionDelete = QtWidgets.QAction(MainWindow)
        self.actionDelete.setObjectName("actionDelete")
        self.actionSelect_All = QtWidgets.QAction(MainWindow)
        self.actionSelect_All.setObjectName("actionSelect_All")
        self.actionBegin_End_Select = QtWidgets.QAction(MainWindow)
        self.actionBegin_End_Select.setObjectName("actionBegin_End_Select")
        self.actionBegin_End_Select_in_Coloumn_Mode = QtWidgets.QAction(MainWindow)
        self.actionBegin_End_Select_in_Coloumn_Mode.setObjectName("actionBegin_End_Select_in_Coloumn_Mode")
        self.actionInsert = QtWidgets.QAction(MainWindow)
        self.actionInsert.setObjectName("actionInsert")
        self.actionCopy_to_Clipboard = QtWidgets.QAction(MainWindow)
        self.actionCopy_to_Clipboard.setObjectName("actionCopy_to_Clipboard")
        self.actionIndent = QtWidgets.QAction(MainWindow)
        self.actionIndent.setObjectName("actionIndent")
        self.actionConvert_Case_to = QtWidgets.QAction(MainWindow)
        self.actionConvert_Case_to.setObjectName("actionConvert_Case_to")
        self.actionline_Operation = QtWidgets.QAction(MainWindow)
        self.actionline_Operation.setObjectName("actionline_Operation")
        self.actionZoom_out = QtWidgets.QAction(MainWindow)
        
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("C:/Users/Aneesh.s/OneDrive/Desktop/mixed circuit signal/magnifying-glass.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionZoom_out.setIcon(icon6)
        self.actionZoom_out.setObjectName("actionZoom_out")
        self.actionZoom_out.triggered.connect(self.zoomout_fun)
        self.actionundo = QtWidgets.QAction(MainWindow)
        self.actionundo.setObjectName("actionundo")
        self.actionredo = QtWidgets.QAction(MainWindow)
        self.actionredo.setObjectName("actionredo")
        self.actionZoom_in_1 = QtWidgets.QAction(MainWindow)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("C:/Users/Aneesh.s/OneDrive/Desktop/mixed circuit signal/zoom-in.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionZoom_in_1.setIcon(icon7)
        self.actionZoom_in_1.setObjectName("actionZoom_in_1")
        self.actionZoom_in_1.triggered.connect(self.zoomin_fun)
        self.menufile.addAction(self.new_icon)
        self.menufile.addAction(self.actionopen)

        self.actionopen.triggered.connect(self.open_fun)

        self.menufile.addAction(self.actionsave)
        self.menufile.addAction(self.actionsave_2)
        self.menufile.addAction(self.actionSave_As)
        self.menufile.addAction(self.actionRename)
        self.menufile.addAction(self.actionColse)
        self.menufile.addAction(self.actionClose_All)
        self.menufile.addAction(self.actionMove_to_Recycle_Bin)
        self.menufile.addSeparator()
        self.menufile.addSeparator()
        self.menufile.addAction(self.actionprint)
        self.menufile.addAction(self.actionprint_now)
        self.menufile.addSeparator()
        self.menufile.addAction(self.actionExit)
        self.menuedit.addAction(self.actioncut)
        self.menuedit.addAction(self.actioncopy)
        self.menuedit.addAction(self.actionpaste)
        self.menuedit.addAction(self.actionDelete)
        self.menuedit.addAction(self.actionSelect_All)
        self.menuedit.addAction(self.actionInsert)
        self.menuedit.addAction(self.actionundo)
        self.menuedit.addAction(self.actionredo)
        self.menuview.addAction(self.actionZoom_in_1)
        self.menuview.addAction(self.actionZoom_out)
        self.menubar.addAction(self.menufile.menuAction())
        self.menubar.addAction(self.menuedit.menuAction())
        self.menubar.addAction(self.menuview.menuAction())
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.new_icon)
        self.toolBar.addAction(self.actionopen)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionsave)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actioncut)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actioncopy)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionpaste)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionZoom_in_1)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionZoom_out)
        self.toolBar.addSeparator()

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Ente Book"))
        self.menufile.setTitle(_translate("MainWindow", "file"))
        self.menuedit.setTitle(_translate("MainWindow", "edit"))
        self.menuview.setTitle(_translate("MainWindow", "view"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.new_icon.setText(_translate("MainWindow", "new"))
        self.actionopen.setText(_translate("MainWindow", "open"))
        self.actionsave.setText(_translate("MainWindow", "save"))
        self.actioncut.setText(_translate("MainWindow", "cut"))

        self.actioncopy.setText(_translate("MainWindow", "copy"))
        self.actionOpen_in_Default_Viewer.setText(_translate("MainWindow", "Open in Default Viewer"))
        self.actionOpen_Folder_as_Workspace.setText(_translate("MainWindow", "Open Folder as Workspace"))
        self.actionReload_From_Disk.setText(_translate("MainWindow", "Reload From Disk"))
        self.actionsave_2.setText(_translate("MainWindow", "save"))
        self.actionSave_As.setText(_translate("MainWindow", "Save As.."))
        self.actionSave_a_Copy_As.setText(_translate("MainWindow", "Save a Copy As.."))
        self.actionSave_All.setText(_translate("MainWindow", "Save All"))
        self.actionRename.setText(_translate("MainWindow", "Rename..."))
        self.actionColse.setText(_translate("MainWindow", "Colse"))
        self.actionClose_All.setText(_translate("MainWindow", "Close All"))
        self.actionMove_to_Recycle_Bin.setText(_translate("MainWindow", "Move to Recycle Bin"))
        self.actionload_Session.setText(_translate("MainWindow", "load Session"))
        self.actionSave_Session.setText(_translate("MainWindow", "Save Session"))
        self.actionprint.setText(_translate("MainWindow", "print"))
        self.actionprint_now.setText(_translate("MainWindow", "print now"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionpaste.setText(_translate("MainWindow", "paste"))
        self.actionDelete.setText(_translate("MainWindow", "Delete"))
        self.actionSelect_All.setText(_translate("MainWindow", "Select All"))
        self.actionBegin_End_Select.setText(_translate("MainWindow", "Begin/End Select"))
        self.actionBegin_End_Select_in_Coloumn_Mode.setText(_translate("MainWindow", "Begin/End Select in Coloumn Mode"))
        self.actionInsert.setText(_translate("MainWindow", "Insert"))
        self.actionCopy_to_Clipboard.setText(_translate("MainWindow", "Copy to Clipboard"))
        self.actionIndent.setText(_translate("MainWindow", "Indent"))
        self.actionConvert_Case_to.setText(_translate("MainWindow", "Convert Case to"))
        self.actionline_Operation.setText(_translate("MainWindow", "line Operation"))
        self.actionZoom_out.setText(_translate("MainWindow", "Zoom out"))
        self.actionundo.setText(_translate("MainWindow", "undo"))
        self.actionredo.setText(_translate("MainWindow", "redo"))
        self.actionZoom_in_1.setText(_translate("MainWindow", "Zoom in"))
    
    def cut_fun(self):
        self.textEdit.cut()
    def paste_fun(self):
        self.textEdit.paste()
    def copy_fun(self):
        self.textEdit.copy()
    def save_fun(self):
        self.textEdit.saveGeometry()
        file_path=QFileDialog.getSaveFileName(self.menufile,'Open',"",'text(*.txt)')
        content = self.textEdit.toPlainText()
        with open(file_path[0], 'w') as f:
            f.write(content)



    def zoomin_fun(self):
        self.textEdit.zoomIn()
    def zoomout_fun(self):
        self.textEdit.zoomOut()
    def new_fun(self,MainWindow ):
    #    _translate = QtCore.QCoreApplication.translate
       self.textEdit.clear()
       
    #    MainWindow.setWindowTitle(_translate("MainWindow", "Untitled"))
    def open_fun(self):
        open_1= QFileDialog.getOpenFileName(self.menufile,'Open',"",'text(*.txt)')
        with open(open_1[0],'r')as f:
            filetext=f.read()
            self.textEdit.setPlainText(filetext)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())