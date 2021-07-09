# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
import cadquery as cq

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(569, 680)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 571, 731))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(260, 20, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(120, 60, 321, 181))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("pics/фланец3.png"))
        self.label_2.setObjectName("label_2")
        self.groupBox = QtWidgets.QGroupBox(self.tab)
        self.groupBox.setGeometry(QtCore.QRect(50, 260, 461, 191))
        self.groupBox.setObjectName("groupBox")
        self.cbRazFl = QtWidgets.QComboBox(self.groupBox)
        self.cbRazFl.setGeometry(QtCore.QRect(200, 90, 91, 22))
        self.cbRazFl.setObjectName("cbRazFl")
        self.cbRazFl.addItem("")
        self.cbRazFl.addItem("")
        self.cbRazFl.addItem("")
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(180, 90, 21, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_7 = QtWidgets.QLabel(self.tab)
        self.label_7.setGeometry(QtCore.QRect(110, 500, 201, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.cbFormatFl = QtWidgets.QComboBox(self.tab)
        self.cbFormatFl.setGeometry(QtCore.QRect(320, 500, 151, 22))
        self.cbFormatFl.setObjectName("cbFormatFl")
        self.cbFormatFl.addItem("")
        self.cbFormatFl.addItem("")
        self.cbFormatFl.addItem("")
        self.cbFormatFl.addItem("")
        self.cbFormatFl.addItem("")
        self.cbFormatFl.addItem("")
        self.cbFormatFl.addItem("")
        self.buSaveFl = QtWidgets.QPushButton(self.tab)
        self.buSaveFl.setGeometry(QtCore.QRect(170, 580, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.buSaveFl.setFont(font)
        self.buSaveFl.setStyleSheet("background-color: rgb(0, 0, 127);\n"
"color: rgb(255, 255, 255);")
        self.buSaveFl.setObjectName("buSaveFl")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.label_3 = QtWidgets.QLabel(self.tab_2)
        self.label_3.setGeometry(QtCore.QRect(280, 40, 41, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.tab_2)
        self.label_4.setGeometry(QtCore.QRect(80, 70, 441, 181))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("pics/вал2.png"))
        self.label_4.setObjectName("label_4")
        self.buSaveVal = QtWidgets.QPushButton(self.tab_2)
        self.buSaveVal.setGeometry(QtCore.QRect(170, 580, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.buSaveVal.setFont(font)
        self.buSaveVal.setStyleSheet("background-color: rgb(0, 0, 127);\n"
"color: rgb(255, 255, 255);")
        self.buSaveVal.setObjectName("buSaveVal")
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_2.setGeometry(QtCore.QRect(50, 280, 461, 191))
        self.groupBox_2.setObjectName("groupBox_2")
        self.cbRazVal = QtWidgets.QComboBox(self.groupBox_2)
        self.cbRazVal.setGeometry(QtCore.QRect(200, 40, 91, 22))
        self.cbRazVal.setObjectName("cbRazVal")
        self.cbRazVal.addItem("")
        self.cbRazVal.addItem("")
        self.cbRazVal.addItem("")
        self.label_6 = QtWidgets.QLabel(self.groupBox_2)
        self.label_6.setGeometry(QtCore.QRect(180, 40, 21, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.cbRazVal_2 = QtWidgets.QComboBox(self.groupBox_2)
        self.cbRazVal_2.setGeometry(QtCore.QRect(200, 100, 91, 22))
        self.cbRazVal_2.setObjectName("cbRazVal_2")
        self.cbRazVal_2.addItem("")
        self.cbRazVal_2.addItem("")
        self.cbRazVal_2.addItem("")
        self.label_9 = QtWidgets.QLabel(self.groupBox_2)
        self.label_9.setGeometry(QtCore.QRect(180, 100, 21, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_8 = QtWidgets.QLabel(self.tab_2)
        self.label_8.setGeometry(QtCore.QRect(110, 500, 201, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.cbFormatVal = QtWidgets.QComboBox(self.tab_2)
        self.cbFormatVal.setGeometry(QtCore.QRect(320, 500, 151, 22))
        self.cbFormatVal.setObjectName("cbFormatVal")
        self.cbFormatVal.addItem("")
        self.cbFormatVal.addItem("")
        self.cbFormatVal.addItem("")
        self.cbFormatVal.addItem("")
        self.cbFormatVal.addItem("")
        self.cbFormatVal.addItem("")
        self.cbFormatVal.addItem("")
        self.tabWidget.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 569, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.flan()
        self.val()

    def flan(self):
        self.buSaveFl.clicked.connect(self.save1)

    def val(self):
        self.buSaveVal.clicked.connect(self.saveVal)

    def saveVal(self):
        print('зашел в вал')
        circle_radius = int(ui.cbRazVal.currentText()) / 5
        thickness = -int(ui.cbRazVal_2.currentText())
        circle_radius2 = circle_radius + 7
        thickness2 = thickness * (-2)
        circle_radius3 = circle_radius - 4
        thickness3 = thickness2

        circle_radius31 = circle_radius3 + 5

        circle_radius4 = circle_radius / 3
        thickness4 = thickness / (-3)

        a1 = (
           cq.Workplane("front")
           .circle(circle_radius)
           .extrude(thickness)
           .chamfer(1)
        )

        a2 = (
           cq.Workplane("front")
           .circle(circle_radius2)
           .extrude(thickness2)
        )

        a3 = (
           cq.Workplane("front").workplane(thickness2)
           .circle(circle_radius3)
           .extrude(thickness3)
        )

        a31 = (cq.Workplane("front").workplane(thickness2).circle(circle_radius2).workplane(offset=5.0).circle(circle_radius31).loft(combine=True))

        a4 = (
           cq.Workplane("front").workplane(thickness2+thickness3)
           .circle(circle_radius4)
           .extrude(thickness4)
        )

        result = a1.add(a2).add(a31).add(a3).add(a4)
        cq.exporters.export(result,f'prod/result_val.{ui.cbFormatVal.currentText()}')

    def save1(self):
        if int(ui.cbRazFl.currentText()) == 52:
            D = 165 / 2
            h = 34
            D1 = 127
            d = 52 / 2
            D4 = 84 / 2
            circleHole = 19 / 2
            ringB = 88.5
            ringL = 76.5 / 2

        elif int(ui.cbRazFl.currentText()) == 65:
            D = 190 / 2
            h = 37
            D1 = 149
            d = 65 / 2
            D4 = 100 / 2
            circleHole = 23 / 2
            ringB = 107.6
            ringL = 95.6 / 2

        elif int(ui.cbRazFl.currentText()) == 80:
            D = 210 / 2
            h = 40
            D1 = 168
            d = 80 / 2
            D4 = 118 / 2
            circleHole = 23 / 2
            ringB = 129.8
            ringL = 117.8 / 2

        r = cq.Workplane("front").circle(D)
        result = r.extrude(h)
        result = result.faces(">Z").circle(D4).extrude(h / 2)
        result = (
            result
                .faces(">Z")
                .workplane()
                .polygon(6, D1, forConstruction=True)
                .vertices()
                .hole(circleHole))

        a1 = (
            cq.Workplane("front")
                .circle(ringL)
                .extrude(h)
        )

        a1 = a1.faces(">Z").workplane().hole(d)

        result = result.faces("<Z").workplane().hole(ringB, 8)

        result = result.faces(">Z").workplane().hole(d)
        cq.exporters.export(result,f'prod/result_fl.{ui.cbFormatVal.currentText()}')



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Генератор деталей"))
        self.label.setText(_translate("MainWindow", "Фланец"))
        self.groupBox.setTitle(_translate("MainWindow", "Задать размеры"))
        self.cbRazFl.setItemText(0, _translate("MainWindow", "52"))
        self.cbRazFl.setItemText(1, _translate("MainWindow", "65"))
        self.cbRazFl.setItemText(2, _translate("MainWindow", "80"))
        self.label_5.setText(_translate("MainWindow", "d"))
        self.label_7.setText(_translate("MainWindow", "Выберите формат экспорта"))
        self.cbFormatFl.setItemText(0, _translate("MainWindow", "STL"))
        self.cbFormatFl.setItemText(1, _translate("MainWindow", "STEP"))
        self.cbFormatFl.setItemText(2, _translate("MainWindow", "DXF"))
        self.cbFormatFl.setItemText(3, _translate("MainWindow", "SVG"))
        self.cbFormatFl.setItemText(4, _translate("MainWindow", "AMF"))
        self.cbFormatFl.setItemText(5, _translate("MainWindow", "TJS"))
        self.cbFormatFl.setItemText(6, _translate("MainWindow", "VRML"))
        self.buSaveFl.setText(_translate("MainWindow", "Сохранить"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Фланец"))
        self.label_3.setText(_translate("MainWindow", "Вал"))
        self.buSaveVal.setText(_translate("MainWindow", "Сохранить"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Задать размеры"))
        self.cbRazVal.setItemText(0, _translate("MainWindow", "85"))
        self.cbRazVal.setItemText(1, _translate("MainWindow", "95"))
        self.cbRazVal.setItemText(2, _translate("MainWindow", "110"))
        self.label_6.setText(_translate("MainWindow", "L"))
        self.cbRazVal_2.setItemText(0, _translate("MainWindow", "15"))
        self.cbRazVal_2.setItemText(1, _translate("MainWindow", "20"))
        self.cbRazVal_2.setItemText(2, _translate("MainWindow", "25"))
        self.label_9.setText(_translate("MainWindow", "d"))
        self.label_8.setText(_translate("MainWindow", "Выберите формат экспорта"))
        self.cbFormatVal.setItemText(0, _translate("MainWindow", "STL"))
        self.cbFormatVal.setItemText(1, _translate("MainWindow", "STEP"))
        self.cbFormatVal.setItemText(2, _translate("MainWindow", "DXF"))
        self.cbFormatVal.setItemText(3, _translate("MainWindow", "SVG"))
        self.cbFormatVal.setItemText(4, _translate("MainWindow", "AMF"))
        self.cbFormatVal.setItemText(5, _translate("MainWindow", "TJS"))
        self.cbFormatVal.setItemText(6, _translate("MainWindow", "VRML"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Вал"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

