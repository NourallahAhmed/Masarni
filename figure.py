# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:\Ghada\4thYear\GradProject\application\figure.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog_figure(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1280, 800)
        Dialog.setStyleSheet("background-color: rgb(235, 235, 235);")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 10, 1191, 101))
        self.label.setStyleSheet("border-radius: 25px 25px 35px 35px;\n"
"font: 20pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(60, 130, 1191, 651))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap(r"E:\graduation project\application\images\sounds.jpeg"))
        self.label_2.setScaledContents(False)
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; color:#ee5445;\">Use this figure to help you know the name of the different areas in your vocal tract</span></p><p align=\"center\"><span style=\" font-size:18pt; color:#ee5445;\">and the place of every sound you will learn: </span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog_figure()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
