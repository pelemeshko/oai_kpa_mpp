# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'oai_kpa_mpp_widget_qt.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1056, 791)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.line_10 = QtWidgets.QFrame(Form)
        self.line_10.setMinimumSize(QtCore.QSize(0, 10))
        self.line_10.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_10.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_10.setObjectName("line_10")
        self.gridLayout.addWidget(self.line_10, 5, 2, 1, 1)
        self.line = QtWidgets.QFrame(Form)
        self.line.setMinimumSize(QtCore.QSize(0, 10))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 5, 0, 1, 1)
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
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.tab)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_4 = QtWidgets.QLabel(self.tab)
        self.label_4.setObjectName("label_4")
        self.gridLayout_4.addWidget(self.label_4, 6, 0, 1, 1)
        self.line_4 = QtWidgets.QFrame(self.tab)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.gridLayout_4.addWidget(self.line_4, 2, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.tab)
        self.label_7.setObjectName("label_7")
        self.gridLayout_4.addWidget(self.label_7, 8, 0, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.tab)
        self.label_8.setObjectName("label_8")
        self.gridLayout_4.addWidget(self.label_8, 7, 0, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.tab)
        self.label_9.setObjectName("label_9")
        self.gridLayout_4.addWidget(self.label_9, 1, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.tab)
        self.label_6.setObjectName("label_6")
        self.gridLayout_4.addWidget(self.label_6, 3, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setObjectName("label_2")
        self.gridLayout_4.addWidget(self.label_2, 5, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setObjectName("label_3")
        self.gridLayout_4.addWidget(self.label_3, 1, 0, 1, 1)
        self.line_5 = QtWidgets.QFrame(self.tab)
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.gridLayout_4.addWidget(self.line_5, 2, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.tab)
        self.label_5.setObjectName("label_5")
        self.gridLayout_4.addWidget(self.label_5, 4, 0, 1, 1)
        self.ch1_u0_spinbox = QtWidgets.QDoubleSpinBox(self.tab)
        self.ch1_u0_spinbox.setMinimum(-15.0)
        self.ch1_u0_spinbox.setMaximum(15.0)
        self.ch1_u0_spinbox.setProperty("value", -5.0)
        self.ch1_u0_spinbox.setObjectName("ch1_u0_spinbox")
        self.gridLayout_4.addWidget(self.ch1_u0_spinbox, 3, 1, 1, 1)
        self.ch1_u1_spinbox = QtWidgets.QDoubleSpinBox(self.tab)
        self.ch1_u1_spinbox.setMinimum(-15.0)
        self.ch1_u1_spinbox.setMaximum(15.0)
        self.ch1_u1_spinbox.setProperty("value", 5.0)
        self.ch1_u1_spinbox.setObjectName("ch1_u1_spinbox")
        self.gridLayout_4.addWidget(self.ch1_u1_spinbox, 4, 1, 1, 1)
        self.ch1_N_spinbox = QtWidgets.QSpinBox(self.tab)
        self.ch1_N_spinbox.setMaximum(125)
        self.ch1_N_spinbox.setProperty("value", 3)
        self.ch1_N_spinbox.setObjectName("ch1_N_spinbox")
        self.gridLayout_4.addWidget(self.ch1_N_spinbox, 5, 1, 1, 1)
        self.ch1_M_spinbox = QtWidgets.QSpinBox(self.tab)
        self.ch1_M_spinbox.setMaximum(255)
        self.ch1_M_spinbox.setProperty("value", 1)
        self.ch1_M_spinbox.setObjectName("ch1_M_spinbox")
        self.gridLayout_4.addWidget(self.ch1_M_spinbox, 6, 1, 1, 1)
        self.ch1_T_spinbox = QtWidgets.QSpinBox(self.tab)
        self.ch1_T_spinbox.setMaximum(65535)
        self.ch1_T_spinbox.setProperty("value", 100)
        self.ch1_T_spinbox.setObjectName("ch1_T_spinbox")
        self.gridLayout_4.addWidget(self.ch1_T_spinbox, 7, 1, 1, 1)
        self.ch1_t_spinbox = QtWidgets.QDoubleSpinBox(self.tab)
        self.ch1_t_spinbox.setMaximum(25.5)
        self.ch1_t_spinbox.setProperty("value", 5.0)
        self.ch1_t_spinbox.setObjectName("ch1_t_spinbox")
        self.gridLayout_4.addWidget(self.ch1_t_spinbox, 8, 1, 1, 1)
        self.horizontalLayout_3.addLayout(self.gridLayout_4)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.tab_2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label_10 = QtWidgets.QLabel(self.tab_2)
        self.label_10.setObjectName("label_10")
        self.gridLayout_5.addWidget(self.label_10, 6, 0, 1, 1)
        self.line_6 = QtWidgets.QFrame(self.tab_2)
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.gridLayout_5.addWidget(self.line_6, 2, 1, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.tab_2)
        self.label_11.setObjectName("label_11")
        self.gridLayout_5.addWidget(self.label_11, 8, 0, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.tab_2)
        self.label_12.setObjectName("label_12")
        self.gridLayout_5.addWidget(self.label_12, 7, 0, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.tab_2)
        self.label_13.setObjectName("label_13")
        self.gridLayout_5.addWidget(self.label_13, 1, 1, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.tab_2)
        self.label_14.setObjectName("label_14")
        self.gridLayout_5.addWidget(self.label_14, 3, 0, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.tab_2)
        self.label_15.setObjectName("label_15")
        self.gridLayout_5.addWidget(self.label_15, 5, 0, 1, 1)
        self.label_16 = QtWidgets.QLabel(self.tab_2)
        self.label_16.setObjectName("label_16")
        self.gridLayout_5.addWidget(self.label_16, 1, 0, 1, 1)
        self.line_7 = QtWidgets.QFrame(self.tab_2)
        self.line_7.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.gridLayout_5.addWidget(self.line_7, 2, 0, 1, 1)
        self.label_17 = QtWidgets.QLabel(self.tab_2)
        self.label_17.setObjectName("label_17")
        self.gridLayout_5.addWidget(self.label_17, 4, 0, 1, 1)
        self.ch2_u0_spinbox = QtWidgets.QDoubleSpinBox(self.tab_2)
        self.ch2_u0_spinbox.setMinimum(-15.0)
        self.ch2_u0_spinbox.setMaximum(15.0)
        self.ch2_u0_spinbox.setProperty("value", -3.0)
        self.ch2_u0_spinbox.setObjectName("ch2_u0_spinbox")
        self.gridLayout_5.addWidget(self.ch2_u0_spinbox, 3, 1, 1, 1)
        self.ch2_u1_spinbox = QtWidgets.QDoubleSpinBox(self.tab_2)
        self.ch2_u1_spinbox.setMinimum(-15.0)
        self.ch2_u1_spinbox.setMaximum(15.0)
        self.ch2_u1_spinbox.setProperty("value", 3.0)
        self.ch2_u1_spinbox.setObjectName("ch2_u1_spinbox")
        self.gridLayout_5.addWidget(self.ch2_u1_spinbox, 4, 1, 1, 1)
        self.ch2_N_spinbox = QtWidgets.QSpinBox(self.tab_2)
        self.ch2_N_spinbox.setMaximum(125)
        self.ch2_N_spinbox.setProperty("value", 5)
        self.ch2_N_spinbox.setObjectName("ch2_N_spinbox")
        self.gridLayout_5.addWidget(self.ch2_N_spinbox, 5, 1, 1, 1)
        self.ch2_M_spinbox = QtWidgets.QSpinBox(self.tab_2)
        self.ch2_M_spinbox.setMaximum(255)
        self.ch2_M_spinbox.setProperty("value", 2)
        self.ch2_M_spinbox.setObjectName("ch2_M_spinbox")
        self.gridLayout_5.addWidget(self.ch2_M_spinbox, 6, 1, 1, 1)
        self.ch2_T_spinbox = QtWidgets.QSpinBox(self.tab_2)
        self.ch2_T_spinbox.setMaximum(65535)
        self.ch2_T_spinbox.setProperty("value", 200)
        self.ch2_T_spinbox.setObjectName("ch2_T_spinbox")
        self.gridLayout_5.addWidget(self.ch2_T_spinbox, 7, 1, 1, 1)
        self.ch2_t_spinbox = QtWidgets.QDoubleSpinBox(self.tab_2)
        self.ch2_t_spinbox.setMaximum(25.5)
        self.ch2_t_spinbox.setProperty("value", 15.0)
        self.ch2_t_spinbox.setObjectName("ch2_t_spinbox")
        self.gridLayout_5.addWidget(self.ch2_t_spinbox, 8, 1, 1, 1)
        self.horizontalLayout_2.addLayout(self.gridLayout_5)
        self.tabWidget.addTab(self.tab_2, "")
        self.verticalLayout_4.addWidget(self.tabWidget)
        self.verticalLayout_3.addLayout(self.verticalLayout_4)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.en_ch1_pushbutton = QtWidgets.QPushButton(self.userFrame)
        self.en_ch1_pushbutton.setObjectName("en_ch1_pushbutton")
        self.horizontalLayout_6.addWidget(self.en_ch1_pushbutton)
        self.en_ch2_pushbutton = QtWidgets.QPushButton(self.userFrame)
        self.en_ch2_pushbutton.setObjectName("en_ch2_pushbutton")
        self.horizontalLayout_6.addWidget(self.en_ch2_pushbutton)
        self.verticalLayout_3.addLayout(self.horizontalLayout_6)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.dis_ch1_pushbutton = QtWidgets.QPushButton(self.userFrame)
        self.dis_ch1_pushbutton.setObjectName("dis_ch1_pushbutton")
        self.horizontalLayout.addWidget(self.dis_ch1_pushbutton)
        self.dis_ch2_pushbutton = QtWidgets.QPushButton(self.userFrame)
        self.dis_ch2_pushbutton.setObjectName("dis_ch2_pushbutton")
        self.horizontalLayout.addWidget(self.dis_ch2_pushbutton)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.gridLayout_2.addLayout(self.verticalLayout_3, 0, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 0, 4, 1, 1)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem2, 7, 0, 1, 2)
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

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Модуль генерации помех"))
        self.label_4.setText(_translate("Form", "Кол-во воздействий"))
        self.label_7.setText(_translate("Form", "Длительность импульсов, мс"))
        self.label_8.setText(_translate("Form", "Период воздействий, мс"))
        self.label_9.setText(_translate("Form", "Значение"))
        self.label_6.setText(_translate("Form", "Уровень низкого напряжения, В"))
        self.label_2.setText(_translate("Form", "Кол-во импульсов"))
        self.label_3.setText(_translate("Form", "Параметры сигнала"))
        self.label_5.setText(_translate("Form", "Уровень высокого напряжения, В"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Form", "Канал 1"))
        self.label_10.setText(_translate("Form", "Кол-во воздействий"))
        self.label_11.setText(_translate("Form", "Длительность импульсов, мс"))
        self.label_12.setText(_translate("Form", "Период воздействий, мс"))
        self.label_13.setText(_translate("Form", "Значение"))
        self.label_14.setText(_translate("Form", "Уровень низкого напряжения, В"))
        self.label_15.setText(_translate("Form", "Кол-во импульсов"))
        self.label_16.setText(_translate("Form", "Параметры сигнала"))
        self.label_17.setText(_translate("Form", "Уровень высокого напряжения, В"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Form", "Канал 2"))
        self.en_ch1_pushbutton.setText(_translate("Form", "Вкл. Канал 1"))
        self.en_ch2_pushbutton.setText(_translate("Form", "Вкл. Канал 2"))
        self.dis_ch1_pushbutton.setText(_translate("Form", "Откл. Канал 1"))
        self.dis_ch2_pushbutton.setText(_translate("Form", "Откл. Канал 2"))
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
