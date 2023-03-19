# -----------------------------------------------------------------------------
# Copyright © 2023 Pietro Caporale
# Licensed under the GPL v3 license
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation.
# (see LICENSE.txt for details)
# -----------------------------------------------------------------------------

import sys
import os
import platform
import subprocess
from functools import partial
import shlex
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, \
    QLabel, QFileDialog, QComboBox, QDialog, QDialogButtonBox
from PyQt6 import QtCore, QtGui, QtWidgets


""" Public parameters. """
APP_NAME = "Run Shell Scripts"
VERS = "Version 1.0"
CONTACT = "development.point@yahoo.com"
WORK_DIR = os.getcwd()
MIN_WIDTH = 320
WIN_HEIGHT = 500
LASTDIR_FILE = "lastdir.txt"
FAVDIR_FILE = "favdir.txt"
BT_CTRL_COL = "color: #46e350;"
BT_LABEL = "color: #ff5c33;"
BT_REF_LINE = "color: #e1a26a;"
INIT_FILE = ".init"
WIN_PARAM = "0,0,0,0"
MULTIPROCESSING = 1
SCRIPTS_SUFFIX = ".sh"


def reload_script():
    """ Function reload script to update all new parameters. """
    os.execl(sys.executable, sys.executable, *sys.argv)


def writeInit(winParam):
    """ Function to update init file. """
    file1 = open(INIT_FILE, "w")
    file1.writelines(winParam)
    file1.close()


def readInit():
    """ Function to read init param.

        window position (not resize)
    """
    global WIN_PARAM
    # if exist
    if os.path.exists(INIT_FILE):
        file1 = open(INIT_FILE, "r")
        winParam = file1.readline()
        winParam = winParam.replace("\n", "")
        if winParam != "":
            WIN_PARAM = winParam
        file1.close()
    else:
        # if not exist
        writeInit(WIN_PARAM)


def writeWorkDir(folder_selected):
    """ Function to update last folder used. """
    file1 = open(LASTDIR_FILE, "w")
    file1.writelines(folder_selected)
    file1.close()


def writeFavDir(folder_selected):
    """ Function to update new favourite folder. """
    file1 = open(FAVDIR_FILE, "a")
    file1.write(folder_selected+"\n")
    file1.close()


def delFavDir(folder_selected, onlyck):
    """ Function to remove favourite folder.

        If onlyck is True, not reload script.
    """
    with open(FAVDIR_FILE, "r") as f:
        lines = f.readlines()
        with open(FAVDIR_FILE, "w") as new_f:
            for line in lines:
                if not line.startswith(folder_selected):
                    new_f.write(line)
    writeWorkDir(os.getcwd())
    if onlyck is False:
        reload_script()


def readFavDir():
    """ Function to read favourite folder. """
    favList = []
    if os.path.exists(FAVDIR_FILE):
        file1 = open(FAVDIR_FILE, "r")
        with open(FAVDIR_FILE, "r") as file1:
            for line in file1:
                line = line.replace("\n", "")
                favList.append(line)
            file1.close()
    return favList


def readLastDir():
    """ Function to read last used folder. """
    global WORK_DIR
    # if exist
    if os.path.exists(LASTDIR_FILE):
        file1 = open(LASTDIR_FILE, "r")
        folder_selected = file1.readline()
        folder_selected = folder_selected.replace("\n", "")
        if folder_selected != "":
            WORK_DIR = folder_selected
        file1.close()
    else:
        # if not exist
        writeWorkDir(WORK_DIR)
    # check if not exist lastdir
    if not os.path.exists(WORK_DIR):
        WORK_DIR = os.getcwd()
        print("Lastdir not exist, refreshed!")
        checkFavouritestDir()  # if not found folder checks all favFolder


def checkFavouritestDir():
    """ Check if exists each favFolder

        If not exist delete from file favdir.txt
    """
    favList = readFavDir()
    for fav in favList:
        if not os.path.exists(fav):
            delFavDir(fav, True)


class SelectNewFolder(QtWidgets.QWidget):
    """ Class to open a new window for using FileDialog to select new folder.
        Update LASTDIR_FILE and reload script to load new parameters.
    """

    def __init__(self, parent=None):
        super().__init__(parent)
        folder_selected = QFileDialog.getExistingDirectory(self,
                                                           ("Set folder"),
                                                           WORK_DIR,
                                                           options=QFileDialog.
                                                           Option.
                                                           DontUseNativeDialog)
        if len(folder_selected) != 0:
            writeWorkDir(folder_selected)
            reload_script()
        self.close


class CustomDialog(QDialog):
    """ Class to open an Alert Dialog for space at the end of folder name """

    def __init__(self, verticalLayout):
        super().__init__()
        self.setWindowTitle("Alert!")
        QBtn = QDialogButtonBox.StandardButton.Abort
        self.buttonBox = QDialogButtonBox(QBtn)
        self.buttonBox.rejected.connect(self.reject)
        self.layout = verticalLayout
        message = QLabel(
            "You have to remove space character at the end of the folder name!"
            )
        self.layout.addWidget(message)
        self.layout.addWidget(self.buttonBox)
        self.setLayout(verticalLayout)


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        global MIN_WIDTH, SCRIPTS_SUFFIX, BT_CTRL_COL, BT_LABEL, BT_REF_LINE
        readLastDir()
        favList = readFavDir()
        readInit()
        if platform.system() == "Windows":
            SCRIPTS_SUFFIX = ".bat"
            BT_CTRL_COL = "color: #000080;"
            BT_LABEL = "color: #4d0f00;"
            BT_REF_LINE = "color: #553111;"

        self.setWindowTitle(APP_NAME)
        self.centralwidget = QtWidgets.QWidget()
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_2 = \
            QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_2.addWidget(self.frame)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)
        self.setCentralWidget(self.centralwidget)

        """ If found space at the end of folder name """
        if WORK_DIR[-1] == ' ':
            self.dlg = CustomDialog(self.verticalLayout_3)
            self.dlg.exec()
            exit()

        """ Create but_refreshFolder to reload folder files """
        self.but_refreshFolder = QPushButton("Refresh folder")
        self.but_refreshFolder.\
            setStyleSheet(BT_CTRL_COL+"padding: 5px;margin-top: 3px;\
                          margin-left: 50px;margin-right: 50px;")
        self.verticalLayout.addWidget(self.but_refreshFolder)
        self.but_refreshFolder.clicked.connect(self.refreshFolder)

        """ Create label_info """
        args = WORK_DIR.split("/")
        self.label_info = QLabel("Work on > "+args[len(args)-1])
        font = self.label_info.font()
        font.setPointSize(12)
        self.label_info.setFont(font)
        self.label_info.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_info.setMinimumHeight(30)
        self.label_info.setStyleSheet(BT_LABEL)
        self.label_info.setObjectName("label_info")
        self.verticalLayout.addWidget(self.label_info)

        """ Create ComboBox and add all favourites folder from txt file

            Check if working folder is present in the list.
            If present set hidefavbut flag to True.
        """
        self.combo_setFavoriteFolder = QComboBox(self)
        hidefavbut = False
        self.combo_setFavoriteFolder.addItem("")
        for fav in favList:
            self.combo_setFavoriteFolder.addItem(fav)
            if fav == WORK_DIR:
                hidefavbut = True
        self.verticalLayout.addWidget(self.combo_setFavoriteFolder)

        """ Check if WORK_DIR is in favourites list.

            If is present add delFavoriteFolder button.
            If not add the new folder in combo text.
        """
        idx = self.combo_setFavoriteFolder.findText(WORK_DIR)
        if idx != -1:
            self.combo_setFavoriteFolder.setCurrentIndex(idx)
            self.but_delFavoriteFolder = \
                QPushButton("Delete from favorites folders")
            self.but_delFavoriteFolder.\
                setStyleSheet(BT_CTRL_COL + "padding: 5px;margin-top: 3px")
            self.verticalLayout.addWidget(self.but_delFavoriteFolder)
            self.but_delFavoriteFolder.clicked.connect(self.delFavoriteFolder)
        else:
            self.combo_setFavoriteFolder.setItemText(0, WORK_DIR)
            self.combo_setFavoriteFolder.setCurrentIndex(0)
        self.combo_setFavoriteFolder.currentTextChanged.\
            connect(self.on_combobox_changed)

        """ Create addFavoriteFolder button.
            If hidefavbut flag is on hide it.
        """
        self.but_addFavoriteFolder = QPushButton("Add to favorites folders")
        self.but_addFavoriteFolder.\
            setStyleSheet(BT_CTRL_COL +
                          "padding: 5px;margin-top: 3px;font-weight: bold")
        self.verticalLayout.addWidget(self.but_addFavoriteFolder)
        self.but_addFavoriteFolder.clicked.connect(self.addFavoriteFolder)
        if hidefavbut:
            self.but_addFavoriteFolder.hide()

        """ Create SelectNewFolder button.
            Select self.w flag to None.
        """
        self.but_SelectNewFolder = QPushButton("Select new folder")
        self.but_SelectNewFolder.setStyleSheet(BT_CTRL_COL+"padding: 5px;")
        self.verticalLayout.addWidget(self.but_SelectNewFolder)
        self.but_SelectNewFolder.clicked.connect(self.SelectNewFolder)
        self.w = None  # No external window yet.

        """ Create sh buttons, for each sh file presents in folder.

            Set frame height, on buttons quantity.
            Set window app width on max name's len of the sh files.
        """
        files = sorted([f for f in os.listdir(WORK_DIR)
                        if f.endswith(SCRIPTS_SUFFIX)])
        # for x in files: print(x)

        """ set frame height for manage button height """
        qsh = len(files)
        if qsh > 0:
            self.frame.setMinimumSize(QtCore.QSize(0, 35*qsh))

        """ Loop to create buttons """
        nlist = 0  # Using to set obj name and height position
        while nlist < qsh:
            fileName = files[nlist]
            # Set width from name len of sh files
            if len(fileName)*7 > (MIN_WIDTH):
                MIN_WIDTH = len(fileName)*7
            but = QtWidgets.\
                QPushButton('{}'.format(fileName), self.frame)
            but.setObjectName("but"+str(nlist))
            but.setText(fileName)
            self.verticalLayout_3.addWidget(but)
            but.clicked.connect(partial(self.execCommand, fileName))
            nlist = nlist+1

        """ Label to fill remaining space """
        self.fill_label = QtWidgets.QLabel(self.frame)
        self.fill_label.setObjectName("fill_label")
        self.verticalLayout_3.addWidget(self.fill_label)

        """ Setting width on len of sh files name """
        if MIN_WIDTH > 1280:
            MIN_WIDTH = 1280
        self.resize(MIN_WIDTH, WIN_HEIGHT)

        """ Create reference line. """
        self.label_reference = QLabel("by pit | " + VERS + " | " + CONTACT)
        font = self.label_reference.font()
        font.setPointSize(8)
        self.label_reference.setFont(font)
        self.label_reference.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_reference.setMinimumHeight(30)
        self.label_reference.setStyleSheet(BT_REF_LINE)
        self.label_reference.setObjectName("label_reference")
        self.verticalLayout.addWidget(self.label_reference)

    def getWindowPos(self):
        """ Get window position values """
        t = self.geometry().getCoords()
        win_pos = str(t[0])+","+str(t[1])+","+str(t[2])+","+str(t[3])
        return win_pos

    def setWindowPos(self):
        """ Set window position """
        args = WIN_PARAM.split(",")
        if int(args[0]) != 0 and int(args[1]) != 0 and \
                int(args[2]) != 0 and int(args[3]) != 0:
            self.move(int(args[0]), int(args[1]))
        # self.resize(int(args[2]), int(args[3]))

    def closeEvent(self, a0: QtGui.QCloseEvent) -> None:
        """ On close write window coords on init file """
        writeInit(self.getWindowPos())
        return super().closeEvent(a0)

    def showEvent(self, a0: QtGui.QShowEvent) -> None:
        """ On show set windows position """
        self.setWindowPos()
        return super().showEvent(a0)

    """
    Linux Manjaro
    add to bash profile .zshrc
    export QT_LOGGING_RULES='*=false'
    change Exec in the .desktop in
    Exec=env QT_LOGGING_RULES='*=false' ~/path/run_sh  > /dev/null
    """

    @staticmethod
    def execCommand(param):
        """ Method to exec command. """
        value = format(param)
        print("---WORK_DIR:"+WORK_DIR)
        if SCRIPTS_SUFFIX == ".bat":
            # Windows
            finalcmd = WORK_DIR
            p = subprocess.Popen(value, cwd=finalcmd)
            stdout, stderr = p.communicate()
        else:
            # Linux
            finalcmd = WORK_DIR + "/"+value
            finalcmd = "konsole --profile='Profile sh' -e " +\
                finalcmd + " > /dev/null"
            # konsole --profile="Profile 1"
            args = shlex.split(finalcmd)
            # print("finalcmd:"+finalcmd)
            if MULTIPROCESSING == 1:
                subprocess.Popen(args, cwd=WORK_DIR)
            else:
                subprocess.run(args, cwd=WORK_DIR)

    def addFavoriteFolder(self):
        """ Method Add to favorites folders. """
        writeInit(self.getWindowPos())
        writeFavDir(WORK_DIR)
        reload_script()

    def SelectNewFolder(self):
        """ Method Select new folder. """
        writeInit(self.getWindowPos())
        if self.w is None:
            self.w = SelectNewFolder(self)
            self.w = None

    def on_combobox_changed(self, value):
        """ Method on combobox changed event. """
        writeInit(self.getWindowPos())
        writeWorkDir(value)
        reload_script()

    def delFavoriteFolder(self):
        """ Method remove working folder from favourites. """
        writeInit(self.getWindowPos())
        delFavDir(WORK_DIR, False)
        reload_script()

    def refreshFolder(self):
        """ Method remove working folder from favourites. """
        writeInit(self.getWindowPos())
        reload_script()


app = QApplication(sys.argv)
app.setWindowIcon(QtGui.QIcon(os.getcwd()+"/run_sh.png"))
window = MainWindow()
window.show()
app.exec()