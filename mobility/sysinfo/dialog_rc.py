# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog.ui'
#
# Created: Tue Jun 22 15:13:47 2010
#      by: PySide uic UI code generator
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(678, 556)
        self.gridLayout = QtGui.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtGui.QTabWidget(Dialog)
        self.tabWidget.setObjectName("tabWidget")
        self.generaltab = QtGui.QWidget()
        self.generaltab.setObjectName("generaltab")
        self.gridLayout_5 = QtGui.QGridLayout(self.generaltab)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label_17 = QtGui.QLabel(self.generaltab)
        self.label_17.setObjectName("label_17")
        self.gridLayout_5.addWidget(self.label_17, 0, 0, 1, 2)
        self.curLanguageLineEdit = QtGui.QLineEdit(self.generaltab)
        self.curLanguageLineEdit.setMouseTracking(False)
        self.curLanguageLineEdit.setFocusPolicy(QtCore.Qt.NoFocus)
        self.curLanguageLineEdit.setAcceptDrops(False)
        self.curLanguageLineEdit.setObjectName("curLanguageLineEdit")
        self.gridLayout_5.addWidget(self.curLanguageLineEdit, 0, 2, 1, 2)
        self.label_28 = QtGui.QLabel(self.generaltab)
        self.label_28.setObjectName("label_28")
        self.gridLayout_5.addWidget(self.label_28, 1, 0, 1, 2)
        self.countryCodeLabel = QtGui.QLabel(self.generaltab)
        self.countryCodeLabel.setObjectName("countryCodeLabel")
        self.gridLayout_5.addWidget(self.countryCodeLabel, 1, 2, 1, 1)
        self.label_29 = QtGui.QLabel(self.generaltab)
        self.label_29.setObjectName("label_29")
        self.gridLayout_5.addWidget(self.label_29, 2, 0, 1, 2)
        self.languagesComboBox = QtGui.QComboBox(self.generaltab)
        self.languagesComboBox.setObjectName("languagesComboBox")
        self.gridLayout_5.addWidget(self.languagesComboBox, 2, 2, 1, 2)
        self.label_30 = QtGui.QLabel(self.generaltab)
        self.label_30.setObjectName("label_30")
        self.gridLayout_5.addWidget(self.label_30, 3, 0, 1, 1)
        self.versionComboBox = QtGui.QComboBox(self.generaltab)
        self.versionComboBox.setObjectName("versionComboBox")
        self.versionComboBox.addItem("")
        self.versionComboBox.setItemText(0, "")
        self.versionComboBox.addItem("")
        self.versionComboBox.addItem("")
        self.versionComboBox.addItem("")
        self.gridLayout_5.addWidget(self.versionComboBox, 3, 1, 1, 2)
        self.versionLineEdit = QtGui.QLineEdit(self.generaltab)
        self.versionLineEdit.setMouseTracking(False)
        self.versionLineEdit.setFocusPolicy(QtCore.Qt.NoFocus)
        self.versionLineEdit.setAcceptDrops(False)
        self.versionLineEdit.setObjectName("versionLineEdit")
        self.gridLayout_5.addWidget(self.versionLineEdit, 3, 3, 1, 2)
        self.label_31 = QtGui.QLabel(self.generaltab)
        self.label_31.setObjectName("label_31")
        self.gridLayout_5.addWidget(self.label_31, 4, 0, 1, 2)
        self.featureComboBox = QtGui.QComboBox(self.generaltab)
        self.featureComboBox.setObjectName("featureComboBox")
        self.featureComboBox.addItem("")
        self.featureComboBox.setItemText(0, "")
        self.featureComboBox.addItem("")
        self.featureComboBox.addItem("")
        self.featureComboBox.addItem("")
        self.featureComboBox.addItem("")
        self.featureComboBox.addItem("")
        self.featureComboBox.addItem("")
        self.featureComboBox.addItem("")
        self.featureComboBox.addItem("")
        self.featureComboBox.addItem("")
        self.featureComboBox.addItem("")
        self.featureComboBox.addItem("")
        self.featureComboBox.addItem("")
        self.featureComboBox.addItem("")
        self.gridLayout_5.addWidget(self.featureComboBox, 4, 2, 1, 2)
        self.featuresLineEdit = QtGui.QLineEdit(self.generaltab)
        self.featuresLineEdit.setMouseTracking(False)
        self.featuresLineEdit.setFocusPolicy(QtCore.Qt.NoFocus)
        self.featuresLineEdit.setAcceptDrops(False)
        self.featuresLineEdit.setObjectName("featuresLineEdit")
        self.gridLayout_5.addWidget(self.featuresLineEdit, 4, 4, 1, 1)
        spacerItem = QtGui.QSpacerItem(20, 291, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_5.addItem(spacerItem, 5, 1, 1, 1)
        self.tabWidget.addTab(self.generaltab, "")
        self.sysdevicetab = QtGui.QWidget()
        self.sysdevicetab.setObjectName("sysdevicetab")
        self.gridLayout_6 = QtGui.QGridLayout(self.sysdevicetab)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.batteryLevelBar = QtGui.QProgressBar(self.sysdevicetab)
        self.batteryLevelBar.setMaximum(100)
        self.batteryLevelBar.setProperty("value", 0)
        self.batteryLevelBar.setObjectName("batteryLevelBar")
        self.gridLayout_6.addWidget(self.batteryLevelBar, 0, 0, 1, 1)
        self.groupBox_4 = QtGui.QGroupBox(self.sysdevicetab)
        self.groupBox_4.setObjectName("groupBox_4")
        self.gridLayout_12 = QtGui.QGridLayout(self.groupBox_4)
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.radioButton = QtGui.QRadioButton(self.groupBox_4)
        self.radioButton.setMouseTracking(False)
        self.radioButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.radioButton.setCheckable(True)
        self.radioButton.setObjectName("radioButton")
        self.gridLayout_12.addWidget(self.radioButton, 0, 0, 1, 1)
        self.radioButton_2 = QtGui.QRadioButton(self.groupBox_4)
        self.radioButton_2.setEnabled(True)
        self.radioButton_2.setMouseTracking(False)
        self.radioButton_2.setFocusPolicy(QtCore.Qt.NoFocus)
        self.radioButton_2.setCheckable(True)
        self.radioButton_2.setObjectName("radioButton_2")
        self.gridLayout_12.addWidget(self.radioButton_2, 1, 0, 1, 1)
        self.radioButton_3 = QtGui.QRadioButton(self.groupBox_4)
        self.radioButton_3.setMouseTracking(False)
        self.radioButton_3.setFocusPolicy(QtCore.Qt.NoFocus)
        self.radioButton_3.setCheckable(True)
        self.radioButton_3.setObjectName("radioButton_3")
        self.gridLayout_12.addWidget(self.radioButton_3, 2, 0, 1, 1)
        self.radioButton_4 = QtGui.QRadioButton(self.groupBox_4)
        self.radioButton_4.setMouseTracking(False)
        self.radioButton_4.setFocusPolicy(QtCore.Qt.NoFocus)
        self.radioButton_4.setCheckable(True)
        self.radioButton_4.setObjectName("radioButton_4")
        self.gridLayout_12.addWidget(self.radioButton_4, 3, 0, 1, 1)
        self.gridLayout_6.addWidget(self.groupBox_4, 0, 2, 3, 1)
        spacerItem1 = QtGui.QSpacerItem(298, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem1, 1, 0, 1, 2)
        self.label_32 = QtGui.QLabel(self.sysdevicetab)
        self.label_32.setObjectName("label_32")
        self.gridLayout_6.addWidget(self.label_32, 2, 0, 1, 1)
        self.ImeiLabel = QtGui.QLabel(self.sysdevicetab)
        self.ImeiLabel.setObjectName("ImeiLabel")
        self.gridLayout_6.addWidget(self.ImeiLabel, 2, 1, 1, 1)
        self.label_33 = QtGui.QLabel(self.sysdevicetab)
        self.label_33.setObjectName("label_33")
        self.gridLayout_6.addWidget(self.label_33, 3, 0, 1, 1)
        self.imsiLabel = QtGui.QLabel(self.sysdevicetab)
        self.imsiLabel.setObjectName("imsiLabel")
        self.gridLayout_6.addWidget(self.imsiLabel, 3, 1, 1, 1)
        self.label_34 = QtGui.QLabel(self.sysdevicetab)
        self.label_34.setObjectName("label_34")
        self.gridLayout_6.addWidget(self.label_34, 4, 0, 1, 1)
        self.manufacturerLabel = QtGui.QLabel(self.sysdevicetab)
        self.manufacturerLabel.setObjectName("manufacturerLabel")
        self.gridLayout_6.addWidget(self.manufacturerLabel, 4, 1, 1, 1)
        self.label_35 = QtGui.QLabel(self.sysdevicetab)
        self.label_35.setObjectName("label_35")
        self.gridLayout_6.addWidget(self.label_35, 5, 0, 1, 1)
        self.modelLabel = QtGui.QLabel(self.sysdevicetab)
        self.modelLabel.setObjectName("modelLabel")
        self.gridLayout_6.addWidget(self.modelLabel, 5, 1, 1, 1)
        self.label_36 = QtGui.QLabel(self.sysdevicetab)
        self.label_36.setObjectName("label_36")
        self.gridLayout_6.addWidget(self.label_36, 6, 0, 1, 1)
        self.productLabel = QtGui.QLabel(self.sysdevicetab)
        self.productLabel.setObjectName("productLabel")
        self.gridLayout_6.addWidget(self.productLabel, 6, 1, 1, 1)
        self.deviceLockPushButton = QtGui.QPushButton(self.sysdevicetab)
        self.deviceLockPushButton.setEnabled(False)
        self.deviceLockPushButton.setMouseTracking(True)
        self.deviceLockPushButton.setFocusPolicy(QtCore.Qt.NoFocus)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/unlocked/general_unlock.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap(":/locked/general_locked.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.deviceLockPushButton.setIcon(icon)
        self.deviceLockPushButton.setIconSize(QtCore.QSize(32, 32))
        self.deviceLockPushButton.setCheckable(True)
        self.deviceLockPushButton.setChecked(False)
        self.deviceLockPushButton.setObjectName("deviceLockPushButton")
        self.gridLayout_6.addWidget(self.deviceLockPushButton, 7, 0, 1, 1)
        self.label_2 = QtGui.QLabel(self.sysdevicetab)
        self.label_2.setObjectName("label_2")
        self.gridLayout_6.addWidget(self.label_2, 7, 1, 1, 1)
        self.label_37 = QtGui.QLabel(self.sysdevicetab)
        self.label_37.setObjectName("label_37")
        self.gridLayout_6.addWidget(self.label_37, 8, 0, 1, 1)
        self.simStatusLabel = QtGui.QLabel(self.sysdevicetab)
        self.simStatusLabel.setObjectName("simStatusLabel")
        self.gridLayout_6.addWidget(self.simStatusLabel, 8, 1, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(201, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem2, 8, 2, 1, 1)
        self.label_38 = QtGui.QLabel(self.sysdevicetab)
        self.label_38.setObjectName("label_38")
        self.gridLayout_6.addWidget(self.label_38, 9, 0, 1, 1)
        self.profileLabel = QtGui.QLabel(self.sysdevicetab)
        self.profileLabel.setObjectName("profileLabel")
        self.gridLayout_6.addWidget(self.profileLabel, 9, 1, 1, 1)
        self.label_39 = QtGui.QLabel(self.sysdevicetab)
        self.label_39.setObjectName("label_39")
        self.gridLayout_6.addWidget(self.label_39, 10, 0, 1, 1)
        self.inputMethodLabel = QtGui.QLabel(self.sysdevicetab)
        self.inputMethodLabel.setObjectName("inputMethodLabel")
        self.gridLayout_6.addWidget(self.inputMethodLabel, 10, 1, 1, 1)
        self.label_9 = QtGui.QLabel(self.sysdevicetab)
        self.label_9.setObjectName("label_9")
        self.gridLayout_6.addWidget(self.label_9, 11, 0, 1, 1)
        self.bluetoothPowerLabel = QtGui.QLabel(self.sysdevicetab)
        self.bluetoothPowerLabel.setObjectName("bluetoothPowerLabel")
        self.gridLayout_6.addWidget(self.bluetoothPowerLabel, 11, 1, 1, 1)
        self.tabWidget.addTab(self.sysdevicetab, "")
        self.sysdisplaytab = QtGui.QWidget()
        self.sysdisplaytab.setObjectName("sysdisplaytab")
        self.gridLayout_7 = QtGui.QGridLayout(self.sysdisplaytab)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_40 = QtGui.QLabel(self.sysdisplaytab)
        self.label_40.setObjectName("label_40")
        self.horizontalLayout_8.addWidget(self.label_40)
        self.brightnessLabel = QtGui.QLabel(self.sysdisplaytab)
        self.brightnessLabel.setObjectName("brightnessLabel")
        self.horizontalLayout_8.addWidget(self.brightnessLabel)
        self.gridLayout_7.addLayout(self.horizontalLayout_8, 0, 0, 1, 1)
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_41 = QtGui.QLabel(self.sysdisplaytab)
        self.label_41.setObjectName("label_41")
        self.horizontalLayout_7.addWidget(self.label_41)
        self.colorDepthLabel = QtGui.QLabel(self.sysdisplaytab)
        self.colorDepthLabel.setObjectName("colorDepthLabel")
        self.horizontalLayout_7.addWidget(self.colorDepthLabel)
        self.gridLayout_7.addLayout(self.horizontalLayout_7, 1, 0, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_3 = QtGui.QLabel(self.sysdisplaytab)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.orientationLabel = QtGui.QLabel(self.sysdisplaytab)
        self.orientationLabel.setObjectName("orientationLabel")
        self.horizontalLayout.addWidget(self.orientationLabel)
        self.gridLayout_7.addLayout(self.horizontalLayout, 2, 0, 1, 1)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_4 = QtGui.QLabel(self.sysdisplaytab)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)
        self.contrastLabel = QtGui.QLabel(self.sysdisplaytab)
        self.contrastLabel.setObjectName("contrastLabel")
        self.horizontalLayout_2.addWidget(self.contrastLabel)
        self.gridLayout_7.addLayout(self.horizontalLayout_2, 3, 0, 1, 1)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_5 = QtGui.QLabel(self.sysdisplaytab)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_3.addWidget(self.label_5)
        self.dpiWidthLabel = QtGui.QLabel(self.sysdisplaytab)
        self.dpiWidthLabel.setObjectName("dpiWidthLabel")
        self.horizontalLayout_3.addWidget(self.dpiWidthLabel)
        self.gridLayout_7.addLayout(self.horizontalLayout_3, 4, 0, 1, 1)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_6 = QtGui.QLabel(self.sysdisplaytab)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_4.addWidget(self.label_6)
        self.dpiHeightLabel = QtGui.QLabel(self.sysdisplaytab)
        self.dpiHeightLabel.setObjectName("dpiHeightLabel")
        self.horizontalLayout_4.addWidget(self.dpiHeightLabel)
        self.gridLayout_7.addLayout(self.horizontalLayout_4, 5, 0, 1, 1)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_8 = QtGui.QLabel(self.sysdisplaytab)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_5.addWidget(self.label_8)
        self.physicalWidthLabel = QtGui.QLabel(self.sysdisplaytab)
        self.physicalWidthLabel.setObjectName("physicalWidthLabel")
        self.horizontalLayout_5.addWidget(self.physicalWidthLabel)
        self.gridLayout_7.addLayout(self.horizontalLayout_5, 6, 0, 1, 1)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_7 = QtGui.QLabel(self.sysdisplaytab)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_6.addWidget(self.label_7)
        self.physicalHeightLabel = QtGui.QLabel(self.sysdisplaytab)
        self.physicalHeightLabel.setObjectName("physicalHeightLabel")
        self.horizontalLayout_6.addWidget(self.physicalHeightLabel)
        self.gridLayout_7.addLayout(self.horizontalLayout_6, 7, 0, 1, 1)
        self.tabWidget.addTab(self.sysdisplaytab, "")
        self.sysmemorytab = QtGui.QWidget()
        self.sysmemorytab.setObjectName("sysmemorytab")
        self.gridLayout_13 = QtGui.QGridLayout(self.sysmemorytab)
        self.gridLayout_13.setObjectName("gridLayout_13")
        self.storageTreeWidget = QtGui.QTreeWidget(self.sysmemorytab)
        self.storageTreeWidget.setObjectName("storageTreeWidget")
        self.gridLayout_13.addWidget(self.storageTreeWidget, 0, 0, 1, 1)
        self.tabWidget.addTab(self.sysmemorytab, "")
        self.sysnetworktab = QtGui.QWidget()
        self.sysnetworktab.setObjectName("sysnetworktab")
        self.gridLayout_4 = QtGui.QGridLayout(self.sysnetworktab)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.groupBox_5 = QtGui.QGroupBox(self.sysnetworktab)
        self.groupBox_5.setObjectName("groupBox_5")
        self.gridLayout_3 = QtGui.QGridLayout(self.groupBox_5)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.netStatusComboBox = QtGui.QComboBox(self.groupBox_5)
        self.netStatusComboBox.setObjectName("netStatusComboBox")
        self.netStatusComboBox.addItem("")
        self.netStatusComboBox.setItemText(0, "")
        self.netStatusComboBox.addItem("")
        self.netStatusComboBox.addItem("")
        self.netStatusComboBox.addItem("")
        self.netStatusComboBox.addItem("")
        self.netStatusComboBox.addItem("")
        self.netStatusComboBox.addItem("")
        self.gridLayout_3.addWidget(self.netStatusComboBox, 0, 0, 1, 1)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem3, 0, 1, 1, 1)
        self.label_42 = QtGui.QLabel(self.groupBox_5)
        self.label_42.setObjectName("label_42")
        self.gridLayout_3.addWidget(self.label_42, 1, 0, 1, 1)
        self.cellNetworkStatusLabel = QtGui.QLabel(self.groupBox_5)
        self.cellNetworkStatusLabel.setFrameShadow(QtGui.QFrame.Sunken)
        self.cellNetworkStatusLabel.setObjectName("cellNetworkStatusLabel")
        self.gridLayout_3.addWidget(self.cellNetworkStatusLabel, 1, 2, 1, 1)
        self.label_43 = QtGui.QLabel(self.groupBox_5)
        self.label_43.setObjectName("label_43")
        self.gridLayout_3.addWidget(self.label_43, 2, 0, 1, 2)
        self.signalLevelProgressBar = QtGui.QProgressBar(self.groupBox_5)
        self.signalLevelProgressBar.setProperty("value", 0)
        self.signalLevelProgressBar.setObjectName("signalLevelProgressBar")
        self.gridLayout_3.addWidget(self.signalLevelProgressBar, 2, 2, 1, 1)
        self.label_44 = QtGui.QLabel(self.groupBox_5)
        self.label_44.setObjectName("label_44")
        self.gridLayout_3.addWidget(self.label_44, 3, 0, 1, 1)
        self.macAddressLabel = QtGui.QLabel(self.groupBox_5)
        self.macAddressLabel.setObjectName("macAddressLabel")
        self.gridLayout_3.addWidget(self.macAddressLabel, 3, 2, 1, 1)
        self.label_45 = QtGui.QLabel(self.groupBox_5)
        self.label_45.setObjectName("label_45")
        self.gridLayout_3.addWidget(self.label_45, 4, 0, 1, 1)
        self.InterfaceLabel = QtGui.QLabel(self.groupBox_5)
        self.InterfaceLabel.setObjectName("InterfaceLabel")
        self.gridLayout_3.addWidget(self.InterfaceLabel, 4, 2, 1, 1)
        self.label = QtGui.QLabel(self.groupBox_5)
        self.label.setObjectName("label")
        self.gridLayout_3.addWidget(self.label, 5, 0, 1, 2)
        self.primaryModeLabel = QtGui.QLabel(self.groupBox_5)
        self.primaryModeLabel.setObjectName("primaryModeLabel")
        self.gridLayout_3.addWidget(self.primaryModeLabel, 5, 2, 1, 1)
        self.operatorNameLabel = QtGui.QLabel(self.groupBox_5)
        self.operatorNameLabel.setObjectName("operatorNameLabel")
        self.gridLayout_3.addWidget(self.operatorNameLabel, 6, 2, 1, 1)
        self.label_52 = QtGui.QLabel(self.groupBox_5)
        self.label_52.setObjectName("label_52")
        self.gridLayout_3.addWidget(self.label_52, 6, 0, 1, 1)
        self.gridLayout_4.addWidget(self.groupBox_5, 0, 0, 1, 1)
        self.groupBox_6 = QtGui.QGroupBox(self.sysnetworktab)
        self.groupBox_6.setObjectName("groupBox_6")
        self.gridLayout_2 = QtGui.QGridLayout(self.groupBox_6)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_46 = QtGui.QLabel(self.groupBox_6)
        self.label_46.setObjectName("label_46")
        self.gridLayout_2.addWidget(self.label_46, 0, 0, 1, 1)
        self.cellIdLabel = QtGui.QLabel(self.groupBox_6)
        self.cellIdLabel.setFrameShape(QtGui.QFrame.StyledPanel)
        self.cellIdLabel.setFrameShadow(QtGui.QFrame.Sunken)
        self.cellIdLabel.setObjectName("cellIdLabel")
        self.gridLayout_2.addWidget(self.cellIdLabel, 0, 1, 1, 1)
        self.label_47 = QtGui.QLabel(self.groupBox_6)
        self.label_47.setObjectName("label_47")
        self.gridLayout_2.addWidget(self.label_47, 1, 0, 1, 1)
        self.locationAreaCodeLabel = QtGui.QLabel(self.groupBox_6)
        self.locationAreaCodeLabel.setFrameShape(QtGui.QFrame.StyledPanel)
        self.locationAreaCodeLabel.setFrameShadow(QtGui.QFrame.Sunken)
        self.locationAreaCodeLabel.setObjectName("locationAreaCodeLabel")
        self.gridLayout_2.addWidget(self.locationAreaCodeLabel, 1, 1, 1, 1)
        self.label_48 = QtGui.QLabel(self.groupBox_6)
        self.label_48.setObjectName("label_48")
        self.gridLayout_2.addWidget(self.label_48, 2, 0, 1, 1)
        self.currentMMCLabel = QtGui.QLabel(self.groupBox_6)
        self.currentMMCLabel.setFrameShape(QtGui.QFrame.StyledPanel)
        self.currentMMCLabel.setFrameShadow(QtGui.QFrame.Sunken)
        self.currentMMCLabel.setObjectName("currentMMCLabel")
        self.gridLayout_2.addWidget(self.currentMMCLabel, 2, 1, 1, 1)
        spacerItem4 = QtGui.QSpacerItem(136, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem4, 2, 2, 1, 1)
        self.label_50 = QtGui.QLabel(self.groupBox_6)
        self.label_50.setObjectName("label_50")
        self.gridLayout_2.addWidget(self.label_50, 3, 0, 1, 1)
        self.currentMNCLabel = QtGui.QLabel(self.groupBox_6)
        self.currentMNCLabel.setFrameShape(QtGui.QFrame.StyledPanel)
        self.currentMNCLabel.setFrameShadow(QtGui.QFrame.Sunken)
        self.currentMNCLabel.setObjectName("currentMNCLabel")
        self.gridLayout_2.addWidget(self.currentMNCLabel, 3, 1, 1, 1)
        spacerItem5 = QtGui.QSpacerItem(136, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem5, 3, 2, 1, 1)
        self.label_49 = QtGui.QLabel(self.groupBox_6)
        self.label_49.setObjectName("label_49")
        self.gridLayout_2.addWidget(self.label_49, 4, 0, 1, 1)
        self.homeMMCLabel = QtGui.QLabel(self.groupBox_6)
        self.homeMMCLabel.setFrameShape(QtGui.QFrame.StyledPanel)
        self.homeMMCLabel.setFrameShadow(QtGui.QFrame.Sunken)
        self.homeMMCLabel.setObjectName("homeMMCLabel")
        self.gridLayout_2.addWidget(self.homeMMCLabel, 4, 1, 1, 1)
        spacerItem6 = QtGui.QSpacerItem(135, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem6, 4, 2, 1, 1)
        self.label_51 = QtGui.QLabel(self.groupBox_6)
        self.label_51.setObjectName("label_51")
        self.gridLayout_2.addWidget(self.label_51, 5, 0, 1, 1)
        self.homeMNCLabel = QtGui.QLabel(self.groupBox_6)
        self.homeMNCLabel.setFrameShape(QtGui.QFrame.StyledPanel)
        self.homeMNCLabel.setFrameShadow(QtGui.QFrame.Sunken)
        self.homeMNCLabel.setObjectName("homeMNCLabel")
        self.gridLayout_2.addWidget(self.homeMNCLabel, 5, 1, 1, 1)
        spacerItem7 = QtGui.QSpacerItem(135, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem7, 5, 2, 1, 1)
        self.gridLayout_4.addWidget(self.groupBox_6, 1, 0, 1, 1)
        spacerItem8 = QtGui.QSpacerItem(20, 213, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_4.addItem(spacerItem8, 1, 1, 1, 1)
        self.tabWidget.addTab(self.sysnetworktab, "")
        self.screenTab = QtGui.QWidget()
        self.screenTab.setObjectName("screenTab")
        self.gridLayout_17 = QtGui.QGridLayout(self.screenTab)
        self.gridLayout_17.setObjectName("gridLayout_17")
        self.saverInhibitedCheckBox = QtGui.QCheckBox(self.screenTab)
        self.saverInhibitedCheckBox.setObjectName("saverInhibitedCheckBox")
        self.gridLayout_17.addWidget(self.saverInhibitedCheckBox, 0, 0, 1, 3)
        spacerItem9 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_17.addItem(spacerItem9, 1, 1, 1, 2)
        self.tabWidget.addTab(self.screenTab, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "System Information", None, QtGui.QApplication.UnicodeUTF8))
        self.label_17.setText(QtGui.QApplication.translate("Dialog", "Current Language:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_28.setText(QtGui.QApplication.translate("Dialog", "Current Country:", None, QtGui.QApplication.UnicodeUTF8))
        self.countryCodeLabel.setText(QtGui.QApplication.translate("Dialog", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.label_29.setText(QtGui.QApplication.translate("Dialog", "Available Languages:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_30.setText(QtGui.QApplication.translate("Dialog", "Version", None, QtGui.QApplication.UnicodeUTF8))
        self.versionComboBox.setItemText(1, QtGui.QApplication.translate("Dialog", "Os", None, QtGui.QApplication.UnicodeUTF8))
        self.versionComboBox.setItemText(2, QtGui.QApplication.translate("Dialog", "QtCore", None, QtGui.QApplication.UnicodeUTF8))
        self.versionComboBox.setItemText(3, QtGui.QApplication.translate("Dialog", "Firmware", None, QtGui.QApplication.UnicodeUTF8))
        self.label_31.setText(QtGui.QApplication.translate("Dialog", "Feature supported", None, QtGui.QApplication.UnicodeUTF8))
        self.featureComboBox.setItemText(1, QtGui.QApplication.translate("Dialog", "Bluetooth", None, QtGui.QApplication.UnicodeUTF8))
        self.featureComboBox.setItemText(2, QtGui.QApplication.translate("Dialog", "Camera", None, QtGui.QApplication.UnicodeUTF8))
        self.featureComboBox.setItemText(3, QtGui.QApplication.translate("Dialog", "FmRadio", None, QtGui.QApplication.UnicodeUTF8))
        self.featureComboBox.setItemText(4, QtGui.QApplication.translate("Dialog", "Irda", None, QtGui.QApplication.UnicodeUTF8))
        self.featureComboBox.setItemText(5, QtGui.QApplication.translate("Dialog", "Led", None, QtGui.QApplication.UnicodeUTF8))
        self.featureComboBox.setItemText(6, QtGui.QApplication.translate("Dialog", "Memcard", None, QtGui.QApplication.UnicodeUTF8))
        self.featureComboBox.setItemText(7, QtGui.QApplication.translate("Dialog", "Usb", None, QtGui.QApplication.UnicodeUTF8))
        self.featureComboBox.setItemText(8, QtGui.QApplication.translate("Dialog", "Vibrate", None, QtGui.QApplication.UnicodeUTF8))
        self.featureComboBox.setItemText(9, QtGui.QApplication.translate("Dialog", "WLan", None, QtGui.QApplication.UnicodeUTF8))
        self.featureComboBox.setItemText(10, QtGui.QApplication.translate("Dialog", "Sim", None, QtGui.QApplication.UnicodeUTF8))
        self.featureComboBox.setItemText(11, QtGui.QApplication.translate("Dialog", "Location", None, QtGui.QApplication.UnicodeUTF8))
        self.featureComboBox.setItemText(12, QtGui.QApplication.translate("Dialog", "VideoOut", None, QtGui.QApplication.UnicodeUTF8))
        self.featureComboBox.setItemText(13, QtGui.QApplication.translate("Dialog", "Haptics", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.generaltab), QtGui.QApplication.translate("Dialog", "General", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_4.setTitle(QtGui.QApplication.translate("Dialog", "Power state", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButton.setText(QtGui.QApplication.translate("Dialog", "Unknown Power", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButton_2.setText(QtGui.QApplication.translate("Dialog", "Battery Power", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButton_3.setText(QtGui.QApplication.translate("Dialog", "Wall Power", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButton_4.setText(QtGui.QApplication.translate("Dialog", "Wall Power charging Battery", None, QtGui.QApplication.UnicodeUTF8))
        self.label_32.setText(QtGui.QApplication.translate("Dialog", "IMEI:", None, QtGui.QApplication.UnicodeUTF8))
        self.ImeiLabel.setText(QtGui.QApplication.translate("Dialog", "xx", None, QtGui.QApplication.UnicodeUTF8))
        self.label_33.setText(QtGui.QApplication.translate("Dialog", "IMSI:", None, QtGui.QApplication.UnicodeUTF8))
        self.imsiLabel.setText(QtGui.QApplication.translate("Dialog", "xx", None, QtGui.QApplication.UnicodeUTF8))
        self.label_34.setText(QtGui.QApplication.translate("Dialog", "Manufacturer:", None, QtGui.QApplication.UnicodeUTF8))
        self.manufacturerLabel.setText(QtGui.QApplication.translate("Dialog", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.label_35.setText(QtGui.QApplication.translate("Dialog", "Model", None, QtGui.QApplication.UnicodeUTF8))
        self.modelLabel.setText(QtGui.QApplication.translate("Dialog", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.label_36.setText(QtGui.QApplication.translate("Dialog", "Product:", None, QtGui.QApplication.UnicodeUTF8))
        self.productLabel.setText(QtGui.QApplication.translate("Dialog", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Dialog", "Device lock", None, QtGui.QApplication.UnicodeUTF8))
        self.label_37.setText(QtGui.QApplication.translate("Dialog", "Sim status:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_38.setText(QtGui.QApplication.translate("Dialog", "current Profile:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_39.setText(QtGui.QApplication.translate("Dialog", "Input method:", None, QtGui.QApplication.UnicodeUTF8))
        self.inputMethodLabel.setText(QtGui.QApplication.translate("Dialog", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("Dialog", "Bluetooth power:", None, QtGui.QApplication.UnicodeUTF8))
        self.bluetoothPowerLabel.setText(QtGui.QApplication.translate("Dialog", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.sysdevicetab), QtGui.QApplication.translate("Dialog", "Device", None, QtGui.QApplication.UnicodeUTF8))
        self.label_40.setText(QtGui.QApplication.translate("Dialog", "Brightness", None, QtGui.QApplication.UnicodeUTF8))
        self.label_41.setText(QtGui.QApplication.translate("Dialog", "Color Depth", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Dialog", "Orientation", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("Dialog", "Contrast", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("Dialog", "DPI Width", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("Dialog", "DPI Height", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("Dialog", "Physical Width", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("Dialog", "Physical Height", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.sysdisplaytab), QtGui.QApplication.translate("Dialog", "Display", None, QtGui.QApplication.UnicodeUTF8))
        self.storageTreeWidget.headerItem().setText(0, QtGui.QApplication.translate("Dialog", "Volume Name", None, QtGui.QApplication.UnicodeUTF8))
        self.storageTreeWidget.headerItem().setText(1, QtGui.QApplication.translate("Dialog", "Type of Volume", None, QtGui.QApplication.UnicodeUTF8))
        self.storageTreeWidget.headerItem().setText(2, QtGui.QApplication.translate("Dialog", "Total Disk Space", None, QtGui.QApplication.UnicodeUTF8))
        self.storageTreeWidget.headerItem().setText(3, QtGui.QApplication.translate("Dialog", "Available Disk Space", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.sysmemorytab), QtGui.QApplication.translate("Dialog", "Storage", None, QtGui.QApplication.UnicodeUTF8))
        self.netStatusComboBox.setItemText(1, QtGui.QApplication.translate("Dialog", "Gsm", None, QtGui.QApplication.UnicodeUTF8))
        self.netStatusComboBox.setItemText(2, QtGui.QApplication.translate("Dialog", "Cdma", None, QtGui.QApplication.UnicodeUTF8))
        self.netStatusComboBox.setItemText(3, QtGui.QApplication.translate("Dialog", "Wcdma", None, QtGui.QApplication.UnicodeUTF8))
        self.netStatusComboBox.setItemText(4, QtGui.QApplication.translate("Dialog", "Wlan", None, QtGui.QApplication.UnicodeUTF8))
        self.netStatusComboBox.setItemText(5, QtGui.QApplication.translate("Dialog", "Ethernet", None, QtGui.QApplication.UnicodeUTF8))
        self.netStatusComboBox.setItemText(6, QtGui.QApplication.translate("Dialog", "Bluetooth", None, QtGui.QApplication.UnicodeUTF8))
        self.label_42.setText(QtGui.QApplication.translate("Dialog", "Network Status", None, QtGui.QApplication.UnicodeUTF8))
        self.cellNetworkStatusLabel.setText(QtGui.QApplication.translate("Dialog", ".", None, QtGui.QApplication.UnicodeUTF8))
        self.label_43.setText(QtGui.QApplication.translate("Dialog", "Network Signal Strength", None, QtGui.QApplication.UnicodeUTF8))
        self.signalLevelProgressBar.setFormat(QtGui.QApplication.translate("Dialog", "%v", None, QtGui.QApplication.UnicodeUTF8))
        self.label_44.setText(QtGui.QApplication.translate("Dialog", "MAC address:", None, QtGui.QApplication.UnicodeUTF8))
        self.macAddressLabel.setText(QtGui.QApplication.translate("Dialog", ".", None, QtGui.QApplication.UnicodeUTF8))
        self.label_45.setText(QtGui.QApplication.translate("Dialog", "Interface Name:", None, QtGui.QApplication.UnicodeUTF8))
        self.InterfaceLabel.setText(QtGui.QApplication.translate("Dialog", ".", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Dialog", "Network Mode:", None, QtGui.QApplication.UnicodeUTF8))
        self.primaryModeLabel.setText(QtGui.QApplication.translate("Dialog", "test", None, QtGui.QApplication.UnicodeUTF8))
        self.operatorNameLabel.setText(QtGui.QApplication.translate("Dialog", ".", None, QtGui.QApplication.UnicodeUTF8))
        self.label_52.setText(QtGui.QApplication.translate("Dialog", "Network Name", None, QtGui.QApplication.UnicodeUTF8))
        self.label_46.setText(QtGui.QApplication.translate("Dialog", "Cell Id:", None, QtGui.QApplication.UnicodeUTF8))
        self.cellIdLabel.setText(QtGui.QApplication.translate("Dialog", ".", None, QtGui.QApplication.UnicodeUTF8))
        self.label_47.setText(QtGui.QApplication.translate("Dialog", "Location Area Code", None, QtGui.QApplication.UnicodeUTF8))
        self.locationAreaCodeLabel.setText(QtGui.QApplication.translate("Dialog", ".", None, QtGui.QApplication.UnicodeUTF8))
        self.label_48.setText(QtGui.QApplication.translate("Dialog", "Current MMC:", None, QtGui.QApplication.UnicodeUTF8))
        self.currentMMCLabel.setText(QtGui.QApplication.translate("Dialog", ".", None, QtGui.QApplication.UnicodeUTF8))
        self.label_50.setText(QtGui.QApplication.translate("Dialog", "Current MNC:", None, QtGui.QApplication.UnicodeUTF8))
        self.currentMNCLabel.setText(QtGui.QApplication.translate("Dialog", ".", None, QtGui.QApplication.UnicodeUTF8))
        self.label_49.setText(QtGui.QApplication.translate("Dialog", "Home MMC:", None, QtGui.QApplication.UnicodeUTF8))
        self.homeMMCLabel.setText(QtGui.QApplication.translate("Dialog", ".", None, QtGui.QApplication.UnicodeUTF8))
        self.label_51.setText(QtGui.QApplication.translate("Dialog", "Home MNC:", None, QtGui.QApplication.UnicodeUTF8))
        self.homeMNCLabel.setText(QtGui.QApplication.translate("Dialog", ".", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.sysnetworktab), QtGui.QApplication.translate("Dialog", "Network", None, QtGui.QApplication.UnicodeUTF8))
        self.saverInhibitedCheckBox.setText(QtGui.QApplication.translate("Dialog", "Screen Saver Inhibited", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.screenTab), QtGui.QApplication.translate("Dialog", "Screen Saver", None, QtGui.QApplication.UnicodeUTF8))

import examples_rc
