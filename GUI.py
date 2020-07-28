# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Spectroscope(object):
    def setupUi(self, Spectroscope):
        Spectroscope.setObjectName("Spectroscope")
        Spectroscope.resize(1365, 561)
        self.centralwidget = QtWidgets.QWidget(Spectroscope)
        self.centralwidget.setObjectName("centralwidget")
        self.portButton = QtWidgets.QPushButton(self.centralwidget)
        self.portButton.setGeometry(QtCore.QRect(130, 20, 93, 28))
        self.portButton.setObjectName("portButton")
        self.fileButton = QtWidgets.QPushButton(self.centralwidget)
        self.fileButton.setGeometry(QtCore.QRect(130, 50, 93, 28))
        self.fileButton.setObjectName("fileButton")
        self.passesButton = QtWidgets.QPushButton(self.centralwidget)
        self.passesButton.setGeometry(QtCore.QRect(130, 80, 93, 28))
        self.passesButton.setObjectName("passesButton")
        self.portLine = QtWidgets.QLineEdit(self.centralwidget)
        self.portLine.setGeometry(QtCore.QRect(10, 20, 113, 22))
        self.portLine.setObjectName("portLine")
        self.fileLine = QtWidgets.QLineEdit(self.centralwidget)
        self.fileLine.setGeometry(QtCore.QRect(10, 50, 113, 22))
        self.fileLine.setObjectName("fileLine")
        self.passesLine = QtWidgets.QLineEdit(self.centralwidget)
        self.passesLine.setGeometry(QtCore.QRect(10, 80, 113, 22))
        self.passesLine.setObjectName("passesLine")
        self.Graph = QtWidgets.QGraphicsView(self.centralwidget)
        self.Graph.setGeometry(QtCore.QRect(230, 20, 551, 501))
        self.Graph.setObjectName("Graph")
        self.startButton = QtWidgets.QPushButton(self.centralwidget)
        self.startButton.setGeometry(QtCore.QRect(10, 190, 211, 71))
        self.startButton.setObjectName("startButton")
        self.accelButton = QtWidgets.QPushButton(self.centralwidget)
        self.accelButton.setGeometry(QtCore.QRect(130, 110, 93, 28))
        self.accelButton.setObjectName("accelButton")
        self.accelLine = QtWidgets.QLineEdit(self.centralwidget)
        self.accelLine.setGeometry(QtCore.QRect(10, 110, 113, 22))
        self.accelLine.setObjectName("accelLine")
        self.fourierButton = QtWidgets.QPushButton(self.centralwidget)
        self.fourierButton.setGeometry(QtCore.QRect(10, 280, 211, 71))
        self.fourierButton.setObjectName("fourierButton")
        self.fourierGraph = QtWidgets.QGraphicsView(self.centralwidget)
        self.fourierGraph.setGeometry(QtCore.QRect(800, 20, 551, 501))
        self.fourierGraph.setObjectName("fourierGraph")
        Spectroscope.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Spectroscope)
        self.statusbar.setObjectName("statusbar")
        Spectroscope.setStatusBar(self.statusbar)

        self.retranslateUi(Spectroscope)
        QtCore.QMetaObject.connectSlotsByName(Spectroscope)

    def retranslateUi(self, Spectroscope):
        _translate = QtCore.QCoreApplication.translate
        Spectroscope.setWindowTitle(_translate("Spectroscope", "MainWindow"))
        self.portButton.setText(_translate("Spectroscope", "Set port"))
        self.fileButton.setText(_translate("Spectroscope", "Set file"))
        self.passesButton.setText(_translate("Spectroscope", "Set number"))
        self.portLine.setText(_translate("Spectroscope", "Port"))
        self.fileLine.setText(_translate("Spectroscope", "Filename"))
        self.passesLine.setText(_translate("Spectroscope", "Number of passes"))
        self.startButton.setText(_translate("Spectroscope", "START"))
        self.accelButton.setText(_translate("Spectroscope", "Set power"))
        self.accelLine.setText(_translate("Spectroscope", "Accel power"))
        self.fourierButton.setText(_translate("Spectroscope", "FOURIER TRANSFORMATION"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Spectroscope = QtWidgets.QMainWindow()
    ui = Ui_Spectroscope()
    ui.setupUi(Spectroscope)
    Spectroscope.show()
    sys.exit(app.exec_())
