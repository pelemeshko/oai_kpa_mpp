# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'oai_kpa_mpp_widget_qt.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1056, 791)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.userFrame = QtWidgets.QFrame(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.userFrame.sizePolicy().hasHeightForWidth())
        self.userFrame.setSizePolicy(sizePolicy)
        self.userFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.userFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.userFrame.setObjectName("userFrame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.userFrame)
        self.gridLayout_2.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.gridLayout_2.setContentsMargins(5, 5, 5, 0)
        self.gridLayout_2.setSpacing(5)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label = QtWidgets.QLabel(self.userFrame)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_4.addWidget(self.label)
        self.line_2 = QtWidgets.QFrame(self.userFrame)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout_4.addWidget(self.line_2)
        self.tabWidget = QtWidgets.QTabWidget(self.userFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setMinimumSize(QtCore.QSize(400, 250))
        self.tabWidget.setMaximumSize(QtCore.QSize(400, 250))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.formLayoutWidget = QtWidgets.QWidget(self.tab)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 10, 375, 186))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.formLayoutWidget)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_4 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout_4.addWidget(self.label_4, 3, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_7.setObjectName("label_7")
        self.gridLayout_4.addWidget(self.label_7, 7, 1, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_8.setObjectName("label_8")
        self.gridLayout_4.addWidget(self.label_8, 6, 1, 1, 1)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.gridLayout_4.addWidget(self.lineEdit_4, 7, 2, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_9.setObjectName("label_9")
        self.gridLayout_4.addWidget(self.label_9, 1, 2, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout_4.addWidget(self.lineEdit_2, 5, 2, 1, 1)
        self.radioButton_2 = QtWidgets.QRadioButton(self.formLayoutWidget)
        self.radioButton_2.setObjectName("radioButton_2")
        self.gridLayout_4.addWidget(self.radioButton_2, 3, 0, 1, 1)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.gridLayout_4.addWidget(self.lineEdit_5, 3, 2, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout_4.addWidget(self.lineEdit, 4, 2, 1, 1)
        self.radioButton = QtWidgets.QRadioButton(self.formLayoutWidget)
        self.radioButton.setObjectName("radioButton")
        self.gridLayout_4.addWidget(self.radioButton, 5, 0, 1, 1)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout_4.addWidget(self.lineEdit_3, 6, 2, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(10, 5, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem, 2, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout_4.addWidget(self.label_5, 4, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.gridLayout_4.addWidget(self.label_6, 5, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout_4.addWidget(self.label_3, 1, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout_4.addWidget(self.label_2, 1, 0, 1, 1)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.formLayoutWidget_2 = QtWidgets.QWidget(self.tab_2)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(10, 10, 375, 186))
        self.formLayoutWidget_2.setObjectName("formLayoutWidget_2")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.formLayoutWidget_2)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label_10 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_10.setObjectName("label_10")
        self.gridLayout_5.addWidget(self.label_10, 3, 1, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_11.setObjectName("label_11")
        self.gridLayout_5.addWidget(self.label_11, 7, 1, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_12.setObjectName("label_12")
        self.gridLayout_5.addWidget(self.label_12, 6, 1, 1, 1)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.gridLayout_5.addWidget(self.lineEdit_6, 7, 2, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_13.setObjectName("label_13")
        self.gridLayout_5.addWidget(self.label_13, 1, 2, 1, 1)
        self.lineEdit_7 = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.gridLayout_5.addWidget(self.lineEdit_7, 5, 2, 1, 1)
        self.radioButton_3 = QtWidgets.QRadioButton(self.formLayoutWidget_2)
        self.radioButton_3.setObjectName("radioButton_3")
        self.gridLayout_5.addWidget(self.radioButton_3, 3, 0, 1, 1)
        self.lineEdit_8 = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.gridLayout_5.addWidget(self.lineEdit_8, 3, 2, 1, 1)
        self.lineEdit_9 = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.gridLayout_5.addWidget(self.lineEdit_9, 4, 2, 1, 1)
        self.radioButton_4 = QtWidgets.QRadioButton(self.formLayoutWidget_2)
        self.radioButton_4.setObjectName("radioButton_4")
        self.gridLayout_5.addWidget(self.radioButton_4, 5, 0, 1, 1)
        self.lineEdit_10 = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.gridLayout_5.addWidget(self.lineEdit_10, 6, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(10, 5, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem1, 2, 1, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_14.setObjectName("label_14")
        self.gridLayout_5.addWidget(self.label_14, 4, 1, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_15.setObjectName("label_15")
        self.gridLayout_5.addWidget(self.label_15, 5, 1, 1, 1)
        self.label_16 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_16.setObjectName("label_16")
        self.gridLayout_5.addWidget(self.label_16, 1, 1, 1, 1)
        self.label_17 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_17.setObjectName("label_17")
        self.gridLayout_5.addWidget(self.label_17, 1, 0, 1, 1)
        self.tabWidget.addTab(self.tab_2, "")
        self.verticalLayout_4.addWidget(self.tabWidget)
        self.verticalLayout_3.addLayout(self.verticalLayout_4)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.pushButton = QtWidgets.QPushButton(self.userFrame)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_6.addWidget(self.pushButton)
        self.pushButton_3 = QtWidgets.QPushButton(self.userFrame)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_6.addWidget(self.pushButton_3)
        self.verticalLayout_3.addLayout(self.horizontalLayout_6)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_2 = QtWidgets.QPushButton(self.userFrame)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton_4 = QtWidgets.QPushButton(self.userFrame)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout.addWidget(self.pushButton_4)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem2)
        self.gridLayout_2.addLayout(self.verticalLayout_3, 0, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem3, 0, 4, 1, 1)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem4, 7, 0, 1, 2)
        self.cycle_window_ = QtWidgets.QSpinBox(self.userFrame)
        self.cycle_window_.setMinimumSize(QtCore.QSize(50, 25))
        self.cycle_window_.setMaximum(99999)
        self.cycle_window_.setSingleStep(1)
        self.cycle_window_.setStepType(QtWidgets.QAbstractSpinBox.DefaultStepType)
        self.cycle_window_.setProperty("value", 600)
        self.cycle_window_.setDisplayIntegerBase(10)
        self.cycle_window_.setObjectName("cycle_window_")
        self.gridLayout_3.addWidget(self.cycle_window_, 5, 1, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.turn_on_30V_ = QtWidgets.QPushButton(self.userFrame)
        self.turn_on_30V_.setMinimumSize(QtCore.QSize(75, 25))
        self.turn_on_30V_.setMaximumSize(QtCore.QSize(100, 16777215))
        self.turn_on_30V_.setObjectName("turn_on_30V_")
        self.horizontalLayout_4.addWidget(self.turn_on_30V_)
        self.turn_on_0V_ = QtWidgets.QPushButton(self.userFrame)
        self.turn_on_0V_.setMinimumSize(QtCore.QSize(75, 25))
        self.turn_on_0V_.setObjectName("turn_on_0V_")
        self.horizontalLayout_4.addWidget(self.turn_on_0V_)
        self.turn_on_minus_30V_ = QtWidgets.QPushButton(self.userFrame)
        self.turn_on_minus_30V_.setMinimumSize(QtCore.QSize(75, 25))
        self.turn_on_minus_30V_.setObjectName("turn_on_minus_30V_")
        self.horizontalLayout_4.addWidget(self.turn_on_minus_30V_)
        self.gridLayout_3.addLayout(self.horizontalLayout_4, 2, 0, 1, 2)
        self.line_3 = QtWidgets.QFrame(self.userFrame)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.gridLayout_3.addWidget(self.line_3, 1, 0, 1, 2)
        self.label_21 = QtWidgets.QLabel(self.userFrame)
        self.label_21.setCursor(QtGui.QCursor(QtCore.Qt.UpArrowCursor))
        self.label_21.setAlignment(QtCore.Qt.AlignCenter)
        self.label_21.setObjectName("label_21")
        self.gridLayout_3.addWidget(self.label_21, 0, 0, 1, 2)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.cycle_DEP_start_ = QtWidgets.QPushButton(self.userFrame)
        self.cycle_DEP_start_.setMinimumSize(QtCore.QSize(75, 25))
        self.cycle_DEP_start_.setObjectName("cycle_DEP_start_")
        self.horizontalLayout_5.addWidget(self.cycle_DEP_start_)
        self.cycle_DEP_stop_ = QtWidgets.QPushButton(self.userFrame)
        self.cycle_DEP_stop_.setMinimumSize(QtCore.QSize(75, 25))
        self.cycle_DEP_stop_.setObjectName("cycle_DEP_stop_")
        self.horizontalLayout_5.addWidget(self.cycle_DEP_stop_)
        self.gridLayout_3.addLayout(self.horizontalLayout_5, 6, 0, 1, 2)
        self.label_22 = QtWidgets.QLabel(self.userFrame)
        self.label_22.setObjectName("label_22")
        self.gridLayout_3.addWidget(self.label_22, 5, 0, 1, 1)
        self.label_18 = QtWidgets.QLabel(self.userFrame)
        self.label_18.setAlignment(QtCore.Qt.AlignCenter)
        self.label_18.setObjectName("label_18")
        self.gridLayout_3.addWidget(self.label_18, 3, 0, 1, 2)
        self.gridLayout_2.addLayout(self.gridLayout_3, 0, 3, 1, 1)
        self.gridLayout.addWidget(self.userFrame, 0, 0, 1, 1)
        self.line_10 = QtWidgets.QFrame(Form)
        self.line_10.setMinimumSize(QtCore.QSize(0, 10))
        self.line_10.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_10.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_10.setObjectName("line_10")
        self.gridLayout.addWidget(self.line_10, 5, 2, 1, 1)
        self.coreGLayout = QtWidgets.QGridLayout()
        self.coreGLayout.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.coreGLayout.setObjectName("coreGLayout")
        self.moduleSerialNumberLEdit = QtWidgets.QLineEdit(Form)
        self.moduleSerialNumberLEdit.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.moduleSerialNumberLEdit.sizePolicy().hasHeightForWidth())
        self.moduleSerialNumberLEdit.setSizePolicy(sizePolicy)
        self.moduleSerialNumberLEdit.setMinimumSize(QtCore.QSize(150, 30))
        self.moduleSerialNumberLEdit.setMaximumSize(QtCore.QSize(2000, 16777215))
        self.moduleSerialNumberLEdit.setText("")
        self.moduleSerialNumberLEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.moduleSerialNumberLEdit.setObjectName("moduleSerialNumberLEdit")
        self.coreGLayout.addWidget(self.moduleSerialNumberLEdit, 1, 1, 1, 1)
        self.connectionPButton = QtWidgets.QPushButton(Form)
        self.connectionPButton.setEnabled(True)
        self.connectionPButton.setMinimumSize(QtCore.QSize(150, 30))
        self.connectionPButton.setMaximumSize(QtCore.QSize(2000, 30))
        self.connectionPButton.setFlat(False)
        self.connectionPButton.setObjectName("connectionPButton")
        self.coreGLayout.addWidget(self.connectionPButton, 1, 2, 1, 1)
        self.statusLineEdit = QtWidgets.QLineEdit(Form)
        self.statusLineEdit.setMinimumSize(QtCore.QSize(0, 30))
        self.statusLineEdit.setObjectName("statusLineEdit")
        self.coreGLayout.addWidget(self.statusLineEdit, 1, 0, 1, 1)
        self.gridLayout.addLayout(self.coreGLayout, 6, 0, 1, 1)
        self.line = QtWidgets.QFrame(Form)
        self.line.setMinimumSize(QtCore.QSize(0, 10))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 5, 0, 1, 1)

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Модуль генерации помех"))
        self.label_4.setText(_translate("Form", "Амплитуда, В"))
        self.label_7.setText(_translate("Form", "Длительность импульса, мкс"))
        self.label_8.setText(_translate("Form", "Период, мкс"))
        self.label_9.setText(_translate("Form", "Значение"))
        self.radioButton_2.setText(_translate("Form", "Синусоидальный"))
        self.radioButton.setText(_translate("Form", "Импульсный"))
        self.label_5.setText(_translate("Form", "Период, мкс"))
        self.label_6.setText(_translate("Form", "Амплитуда, В"))
        self.label_3.setText(_translate("Form", "Параметры сигнала"))
        self.label_2.setText(_translate("Form", "Тип сигнала"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Form", "Канал 1"))
        self.label_10.setText(_translate("Form", "Амплитуда, В"))
        self.label_11.setText(_translate("Form", "Длительность импульса, мкс"))
        self.label_12.setText(_translate("Form", "Период, мкс"))
        self.label_13.setText(_translate("Form", "Значение"))
        self.radioButton_3.setText(_translate("Form", "Синусоидальный"))
        self.radioButton_4.setText(_translate("Form", "Импульсный"))
        self.label_14.setText(_translate("Form", "Период, мкс"))
        self.label_15.setText(_translate("Form", "Амплитуда, В"))
        self.label_16.setText(_translate("Form", "Параметры сигнала"))
        self.label_17.setText(_translate("Form", "Тип сигнала"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Form", "Канал 2"))
        self.pushButton.setText(_translate("Form", "Вкл. Канал 1"))
        self.pushButton_3.setText(_translate("Form", "Вкл. Канал 2"))
        self.pushButton_2.setText(_translate("Form", "Откл. Канал 1"))
        self.pushButton_4.setText(_translate("Form", "Откл. Канал 2"))
        self.turn_on_30V_.setText(_translate("Form", "30 В"))
        self.turn_on_0V_.setText(_translate("Form", "0 В"))
        self.turn_on_minus_30V_.setText(_translate("Form", "-30 В"))
        self.label_21.setText(_translate("Form", "Поле ДЭП"))
        self.cycle_DEP_start_.setText(_translate("Form", "Старт"))
        self.cycle_DEP_stop_.setText(_translate("Form", "Стоп"))
        self.label_22.setText(_translate("Form", "Период, с"))
        self.label_18.setText(_translate("Form", "Циклическое воздействие"))
        self.moduleSerialNumberLEdit.setPlaceholderText(_translate("Form", "Serial Number"))
        self.connectionPButton.setText(_translate("Form", "Подключение"))
