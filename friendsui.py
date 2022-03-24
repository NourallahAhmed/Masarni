# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:\Ghada\4thYear\GradProject\application\Friendslist.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1272, 854)
        self.level_name = QtWidgets.QLabel(Dialog)
        self.level_name.setGeometry(QtCore.QRect(0, 0, 1271, 102))
        self.level_name.setStyleSheet("background-color: rgb(238, 238, 0);\n"
"background-color: rgb(255, 247, 23);\n"
"opacity: 1;")
        self.level_name.setObjectName("level_name")
        self.sound_d = QtWidgets.QPushButton(Dialog)
        self.sound_d.setGeometry(QtCore.QRect(850, 400, 201, 121))
        self.sound_d.setStyleSheet("font: 75 20pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 193, 8);\n"
"border-radius: 25px 25px 35px 35px;\n"
"opacity: 1;")
        self.sound_d.setObjectName("sound_d")
        self.sound_b = QtWidgets.QPushButton(Dialog)
        self.sound_b.setGeometry(QtCore.QRect(920, 260, 131, 121))
        self.sound_b.setStyleSheet("font: 75 20pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 247, 23);\n"
"border-radius: 25px 25px 35px 35px;\n"
"opacity: 1;")
        self.sound_b.setObjectName("sound_b")
        self.sound_z = QtWidgets.QPushButton(Dialog)
        self.sound_z.setGeometry(QtCore.QRect(350, 400, 481, 121))
        self.sound_z.setStyleSheet("font: 75 20pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 247, 23);\n"
"border-radius: 25px 25px 35px 35px;\n"
"opacity: 1;")
        self.sound_z.setObjectName("sound_z")
        self.sound_ch = QtWidgets.QPushButton(Dialog)
        self.sound_ch.setGeometry(QtCore.QRect(700, 260, 181, 121))
        self.sound_ch.setStyleSheet("font: 75 20pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 250, 107);\n"
"border-radius: 25px 25px 35px 35px;\n"
"opacity: 1;")
        self.sound_ch.setObjectName("sound_ch")
        self.sound_s = QtWidgets.QPushButton(Dialog)
        self.sound_s.setGeometry(QtCore.QRect(150, 260, 521, 111))
        self.sound_s.setStyleSheet("font: 75 20pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 219, 12);\n"
"border-radius: 25px 25px 35px 35px;\n"
"opacity: 1;")
        self.sound_s.setObjectName("sound_s")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(130, 240, 941, 431))
        self.label.setStyleSheet("font: 75 20pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 25px 25px 35px 35px;\n"
"opacity: 1;")
        self.label.setObjectName("label")
        self.label.raise_()
        self.sound_ch.raise_()
        self.sound_b.raise_()
        self.sound_d.raise_()
        self.level_name.raise_()
        self.sound_z.raise_()
        self.sound_s.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.level_name.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:36pt; color:#ffffff;\">Friends Level</span></p></body></html>"))
        self.sound_d.setText(_translate("Dialog", "/d/=د"))
        self.sound_b.setText(_translate("Dialog", "/b/=ب"))
        self.sound_z.setText(_translate("Dialog", "/z/=ز"))
        self.sound_ch.setText(_translate("Dialog", "/ʃ/=ش"))
        self.sound_s.setText(_translate("Dialog", "/s/=س"))
        self.label.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" color:#fff717;\"><br/></span></p><p align=\"center\"><span style=\" color:#fff717;\"><br/></span></p><p align=\"center\"><span style=\" color:#fff717;\"><br/></span></p><p align=\"center\"><span style=\" color:#fff717;\"><br/></span></p><p align=\"center\"><span style=\" color:#fff717;\">Choose a sound</span></p><p align=\"center\"><span style=\" color:#fff717;\"><br/></span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
