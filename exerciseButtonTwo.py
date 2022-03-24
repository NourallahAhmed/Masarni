# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:\Ghada\4thYear\GradProject\application\exerciseButtonTwo.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1280, 800)
        self.soundname = QtWidgets.QLabel(Dialog)
        self.soundname.setGeometry(QtCore.QRect(10, 10, 1246, 102))
        self.soundname.setStyleSheet("background: rgb(0, 195, 122);\n"
"border-radius: 10px 10px 20px 20px;\n"
"opacity: 1;")
        self.soundname.setText("")
        self.soundname.setObjectName("soundname")
        self.backbutton = QtWidgets.QPushButton(Dialog)
        self.backbutton.setGeometry(QtCore.QRect(30, 20, 31, 31))
        self.backbutton.setStyleSheet("border-radius: 15px 15px 35px 35px;\n"
"background-color: rgb(208, 201, 199);")
        self.backbutton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("F:\\Ghada\\4thYear\\GradProject\\application\\images/back.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.backbutton.setIcon(icon)
        self.backbutton.setObjectName("backbutton")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(400, 130, 491, 41))
        self.label.setStyleSheet("border-radius: 10px 10px 20px 20px;\n"
"font: 16pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(190, 190, 190);\n"
"opacity: 1;")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(400, 680, 491, 41))
        self.label_2.setStyleSheet("border-radius: 20px 20px 35px 35px;\n"
"font: 16pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(190, 190, 190);\n"
"opacity: 1;")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.nextbutton = QtWidgets.QPushButton(Dialog)
        self.nextbutton.setGeometry(QtCore.QRect(400, 730, 491, 41))
        self.nextbutton.setStyleSheet("border-radius: 20px 20px 35px 35px;\n"
"background-color: rgb(238, 84, 69);\n"
"color: rgb(255, 0, 0);\n"
"\n"
"color: rgb(255, 255, 255);\n"
"\n"
"font: 75 16pt \"MS Shell Dlg 2\";")
        self.nextbutton.setObjectName("nextbutton")
        self.Sbutton = QtWidgets.QPushButton(Dialog)
        self.Sbutton.setGeometry(QtCore.QRect(470, 210, 31, 31))
        self.Sbutton.setStyleSheet("border-radius: 15px 15px 35px 35px;\n"
"background-color: rgb(208, 201, 199);")
        self.Sbutton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("F:\\Ghada\\4thYear\\GradProject\\application\\images/speaker-interface-audio-symbol.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Sbutton.setIcon(icon1)
        self.Sbutton.setObjectName("Sbutton")
        self.wordname = QtWidgets.QLabel(Dialog)
        self.wordname.setGeometry(QtCore.QRect(450, 180, 401, 81))
        self.wordname.setStyleSheet("background: rgb(0, 195, 122);\n"
"font: 8pt \"Myriad Hebrew\";\n"
"border-radius: 10px 10px 20px 20px;\n"
"opacity: 1;")
        self.wordname.setObjectName("wordname")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(770, 280, 321, 301))
        self.label_4.setStyleSheet("background-color: rgb(252, 252, 252);\n"
"border-radius: 20px 20px 35px 35px;\n"
"opacity: 1;\n"
"")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.Sbutton_4 = QtWidgets.QPushButton(Dialog)
        self.Sbutton_4.setGeometry(QtCore.QRect(250, 620, 31, 31))
        self.Sbutton_4.setStyleSheet("border-radius: 15px 15px 35px 35px;\n"
"background-color: rgb(208, 201, 199);")
        self.Sbutton_4.setText("")
        self.Sbutton_4.setIcon(icon1)
        self.Sbutton_4.setObjectName("Sbutton_4")
        self.B2 = QtWidgets.QPushButton(Dialog)
        self.B2.setGeometry(QtCore.QRect(240, 610, 221, 51))
        self.B2.setStyleSheet("border-radius: 20px 20px 35px 35px;\n"
"font: 16pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(190, 190, 190);\n"
"opacity: 1;")
        self.B2.setObjectName("B2")
        self.Sbutton_5 = QtWidgets.QPushButton(Dialog)
        self.Sbutton_5.setGeometry(QtCore.QRect(840, 620, 31, 31))
        self.Sbutton_5.setStyleSheet("border-radius: 15px 15px 35px 35px;\n"
"background-color: rgb(208, 201, 199);")
        self.Sbutton_5.setText("")
        self.Sbutton_5.setIcon(icon1)
        self.Sbutton_5.setObjectName("Sbutton_5")
        self.B1 = QtWidgets.QPushButton(Dialog)
        self.B1.setGeometry(QtCore.QRect(830, 610, 221, 51))
        self.B1.setStyleSheet("border-radius: 20px 20px 35px 35px;\n"
"font: 16pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(190, 190, 190);\n"
"opacity: 1;")
        self.B1.setObjectName("B1")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(190, 280, 321, 301))
        self.label_5.setStyleSheet("background-color: rgb(252, 252, 252);\n"
"border-radius: 20px 20px 35px 35px;\n"
"opacity: 1;\n"
"")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.B1.raise_()
        self.B2.raise_()
        self.wordname.raise_()
        self.soundname.raise_()
        self.backbutton.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.nextbutton.raise_()
        self.Sbutton.raise_()
        self.label_4.raise_()
        self.Sbutton_4.raise_()
        self.Sbutton_5.raise_()
        self.label_5.raise_()

        self.B1.clicked.connect(self.ButtonOne)
        self.B2.clicked.connect(self.ButtonTwo)




        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def ButtonTwo(self):
        self.label_2.setText("                     Well Done!    ")
        self.label_2.setStyleSheet("border-radius: 20px 20px 35px 35px;\n"
                "background-color: rgb(15, 212, 48);\n"
                    "font: 75 18pt \"MS Shell Dlg 2\";\n"
                    "opacity: 1;")
    def ButtonOne(self):
        self.label_2.setText("                     Try Again!    ")
        self.label_2.setStyleSheet("border-radius: 20px 20px 35px 35px;\n"
        "background-color: rgb(255, 42, 0);\n" "font: 75 18pt \"MS Shell Dlg 2\";\n" "opacity: 1;")

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "       Which one has the target sound"))
        self.nextbutton.setText(_translate("Dialog", "Done"))
        self.wordname.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:26pt; color:#ffffff;\">قاف</span></p></body></html>"))
        self.B2.setWhatsThis(_translate("Dialog", "<html><head/><body><p align=\"right\">منبه</p></body></html>"))
        self.B2.setText(_translate("Dialog", "منبه"))
        self.B1.setWhatsThis(_translate("Dialog", "<html><head/><body><p align=\"right\">منبه</p></body></html>"))
        self.B1.setText(_translate("Dialog", "قطة"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
