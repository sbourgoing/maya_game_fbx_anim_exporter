# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\gsq_sbourgoing\Documents\Git\maya_game_fbx_anim_exporter\resources\ui\main_window.ui'
#
# Created: Wed Nov  6 13:18:44 2019
#      by: pyside2-uic  running on PySide2 2.0.0~alpha0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_win_mayaGameFbxExporter(object):
    def setupUi(self, win_mayaGameFbxExporter):
        win_mayaGameFbxExporter.setObjectName("win_mayaGameFbxExporter")
        win_mayaGameFbxExporter.resize(1085, 1092)
        self.centralwidget = QtWidgets.QWidget(win_mayaGameFbxExporter)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.grpAnim = QtWidgets.QGroupBox(self.centralwidget)
        self.grpAnim.setObjectName("grpAnim")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.grpAnim)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.lblCharacterRoot = QtWidgets.QLabel(self.grpAnim)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblCharacterRoot.sizePolicy().hasHeightForWidth())
        self.lblCharacterRoot.setSizePolicy(sizePolicy)
        self.lblCharacterRoot.setObjectName("lblCharacterRoot")
        self.horizontalLayout_5.addWidget(self.lblCharacterRoot)
        self.cbCharacterList = QtWidgets.QComboBox(self.grpAnim)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cbCharacterList.sizePolicy().hasHeightForWidth())
        self.cbCharacterList.setSizePolicy(sizePolicy)
        self.cbCharacterList.setEditable(False)
        self.cbCharacterList.setObjectName("cbCharacterList")
        self.horizontalLayout_5.addWidget(self.cbCharacterList)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem)
        self.verticalLayout_4.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.chkUseClip = QtWidgets.QCheckBox(self.grpAnim)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.chkUseClip.sizePolicy().hasHeightForWidth())
        self.chkUseClip.setSizePolicy(sizePolicy)
        self.chkUseClip.setObjectName("chkUseClip")
        self.verticalLayout_3.addWidget(self.chkUseClip)
        self.grp_animOptions = QtWidgets.QGroupBox(self.grpAnim)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.grp_animOptions.sizePolicy().hasHeightForWidth())
        self.grp_animOptions.setSizePolicy(sizePolicy)
        self.grp_animOptions.setObjectName("grp_animOptions")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.grp_animOptions)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout.setContentsMargins(0, -1, -1, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.rdoTimeSlider = QtWidgets.QRadioButton(self.grp_animOptions)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rdoTimeSlider.sizePolicy().hasHeightForWidth())
        self.rdoTimeSlider.setSizePolicy(sizePolicy)
        self.rdoTimeSlider.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.rdoTimeSlider.setChecked(True)
        self.rdoTimeSlider.setObjectName("rdoTimeSlider")
        self.horizontalLayout.addWidget(self.rdoTimeSlider)
        self.rdoTimeStartEnd = QtWidgets.QRadioButton(self.grp_animOptions)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rdoTimeStartEnd.sizePolicy().hasHeightForWidth())
        self.rdoTimeStartEnd.setSizePolicy(sizePolicy)
        self.rdoTimeStartEnd.setChecked(False)
        self.rdoTimeStartEnd.setObjectName("rdoTimeStartEnd")
        self.horizontalLayout.addWidget(self.rdoTimeStartEnd)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lblStartEnd = QtWidgets.QLabel(self.grp_animOptions)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblStartEnd.sizePolicy().hasHeightForWidth())
        self.lblStartEnd.setSizePolicy(sizePolicy)
        self.lblStartEnd.setMinimumSize(QtCore.QSize(0, 0))
        self.lblStartEnd.setObjectName("lblStartEnd")
        self.horizontalLayout_2.addWidget(self.lblStartEnd)
        self.lineEdit = QtWidgets.QLineEdit(self.grp_animOptions)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_2.addWidget(self.lineEdit)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.grp_animOptions)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_2.sizePolicy().hasHeightForWidth())
        self.lineEdit_2.setSizePolicy(sizePolicy)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout_2.addWidget(self.lineEdit_2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.verticalLayout_3.addWidget(self.grp_animOptions)
        self.horizontalLayout_4.addLayout(self.verticalLayout_3)
        spacerItem2 = QtWidgets.QSpacerItem(200, 20, QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        self.verticalLayout_4.addLayout(self.horizontalLayout_4)
        self.tableWidget = QtWidgets.QTableWidget(self.grpAnim)
        self.tableWidget.setProperty("showDropIndicator", True)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setHighlightSections(True)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(True)
        self.verticalLayout_4.addWidget(self.tableWidget)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton = QtWidgets.QPushButton(self.grpAnim)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_3.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.grpAnim)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_3.addWidget(self.pushButton_2)
        self.verticalLayout_4.addLayout(self.horizontalLayout_3)
        self.verticalLayout.addWidget(self.grpAnim)
        win_mayaGameFbxExporter.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(win_mayaGameFbxExporter)
        self.statusbar.setObjectName("statusbar")
        win_mayaGameFbxExporter.setStatusBar(self.statusbar)

        self.retranslateUi(win_mayaGameFbxExporter)
        QtCore.QMetaObject.connectSlotsByName(win_mayaGameFbxExporter)

    def retranslateUi(self, win_mayaGameFbxExporter):
        win_mayaGameFbxExporter.setWindowTitle(QtWidgets.QApplication.translate("win_mayaGameFbxExporter", "MainWindow", None, -1))
        self.grpAnim.setTitle(QtWidgets.QApplication.translate("win_mayaGameFbxExporter", "Animation Options", None, -1))
        self.lblCharacterRoot.setText(QtWidgets.QApplication.translate("win_mayaGameFbxExporter", "Character Root:", None, -1))
        self.chkUseClip.setText(QtWidgets.QApplication.translate("win_mayaGameFbxExporter", "Use Animation Clips", None, -1))
        self.grp_animOptions.setTitle(QtWidgets.QApplication.translate("win_mayaGameFbxExporter", "Time range", None, -1))
        self.rdoTimeSlider.setText(QtWidgets.QApplication.translate("win_mayaGameFbxExporter", "Time Slider", None, -1))
        self.rdoTimeStartEnd.setText(QtWidgets.QApplication.translate("win_mayaGameFbxExporter", "Start/End", None, -1))
        self.lblStartEnd.setText(QtWidgets.QApplication.translate("win_mayaGameFbxExporter", "Start/End:", None, -1))
        self.tableWidget.horizontalHeaderItem(0).setText(QtWidgets.QApplication.translate("win_mayaGameFbxExporter", "SubAnim Name", None, -1))
        self.tableWidget.horizontalHeaderItem(1).setText(QtWidgets.QApplication.translate("win_mayaGameFbxExporter", "Start", None, -1))
        self.tableWidget.horizontalHeaderItem(2).setText(QtWidgets.QApplication.translate("win_mayaGameFbxExporter", "End", None, -1))
        self.pushButton.setText(QtWidgets.QApplication.translate("win_mayaGameFbxExporter", "Add SubAnim", None, -1))
        self.pushButton_2.setText(QtWidgets.QApplication.translate("win_mayaGameFbxExporter", "Remove SubAnim", None, -1))

