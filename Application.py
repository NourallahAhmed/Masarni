from PyQt5 import QtWidgets, QtGui, QtWidgets, QtCore, QtMultimedia
from PyQt5.QtWidgets import QApplication, QWidget, QDialog, QPushButton, QHBoxLayout, QVBoxLayout, QLabel, QSlider, QStyle, QSizePolicy, QFileDialog
from PyQt5.QtGui import QIcon, QMovie #icon and gif
from PyQt5.QtGui import  QIcon, QPalette, QPixmap #for colors and images
from PyQt5.uic import loadUi #for Qdesign files
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtCore import Qt, QUrl, QRect, QCoreApplication 
from enemiesListui import Ui_Form
from friendsui import Ui_Dialog
from familyui import Ui_MainWindow_family 
from figure import Ui_Dialog_figure
import sys

class log(QDialog):
    def __init__(self):
        super(log,self).__init__()
        loadUi(r"E:\graduation project\application\welcomepage.ui",self)
        global name
        name= self.learnername
        self.startButton.clicked.connect(self.gonext)
    def gonext(self):
        global category
        category=categories()
        widget.addWidget(category)
        widget.setCurrentIndex(widget.currentIndex()+1)

class categories(QDialog):
    def __init__(self):
        super(categories,self).__init__()
        loadUi(r"E:\graduation project\application\categories.ui",self)
        global name
        self.hi.setText("                   Welcome " + name.text()) 
        self.enemieslevel.clicked.connect(self.Enemies) #to class enemies
        self.friendslevel.clicked.connect(self.Friends) #to class friends
        self.familylevel.clicked.connect(self.Family)   #to class family
        self.figureButton.clicked.connect(self.figure)
    def figure(self):
        self.Dialog = QtWidgets.QDialog()
        self.ui = Ui_Dialog_figure()
        self.ui.setupUi(self.Dialog)
        self.Dialog.show()

    def Enemies(self):
        self.ui = Ui_Form()
        self.enemies_form = QtWidgets.QWidget()
        self.ui.setupUi(self.enemies_form)
        self.enemies_form.show()
        self.ui.sound_q.clicked.connect(self.qaf)
        self.ui.sound_glottal.clicked.connect(self.glottal)
        self.ui.sound_h.clicked.connect(self.h)
        self.ui.sound_H.clicked.connect(self.H)# /??/ 
        self.ui.sound_3.clicked.connect(self.ain)#??????
        self.ui.sound_8in.clicked.connect(self.gain)#??????
        self.ui.sound_g.clicked.connect(self.gim)#??????
        self.ui.sound_T.clicked.connect(self.T)
        self.ui.sound_D.clicked.connect(self.D)
        self.ui.sound_S.clicked.connect(self.S)
        self.ui.sound_Z.clicked.connect(self.Z)
        self.ui.sound_r.clicked.connect(self.r)
        self.ui.sound_w.clicked.connect(self.w)
        self.ui.sound_j.clicked.connect(self.j)
        #self.ui.backbutton.clicked.connect(self.back)

    def Friends(self):
        self.Dialog = QtWidgets.QDialog()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self.Dialog)
        self.Dialog.show()  
        self.ui.sound_b.clicked.connect(self.b)
        self.ui.sound_d.clicked.connect(self.d)
        self.ui.sound_ch.clicked.connect(self.ch)
        self.ui.sound_z.clicked.connect(self.z)
        self.ui.sound_s.clicked.connect(self.s)
        #self.ui.backbutton.clicked.connect(self.back)

    def Family(self):
        self.MainWindow = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow_family ()
        self.ui.setupUi(self.MainWindow)
        self.MainWindow.show()
        self.ui.sound_m.clicked.connect(self.m)
        self.ui.sound_n.clicked.connect(self.n)
        self.ui.sound_f.clicked.connect(self.f)
        self.ui.sound_t.clicked.connect(self.t)
        self.ui.sound_k.clicked.connect(self.k)
        self.ui.sound_x.clicked.connect(self.x)
        self.ui.sound_l.clicked.connect(self.l)

        #self.ui.backbutton.clicked.connect(self.back)
  
    def back(self):
        widget.setCurrentIndex(widget.currentIndex()-1)
#======================================================================================================================================================================
###enemies    
    def qaf(self):
        global widget_stack #list 
        global widget

        if len(widget_stack) >0: # ?????????? ???? ?????? ?????? ???????????? ???? ?????????? ???? ?????? ???? ???? ????????
            first_element_index = get_index_of_widget(w=widget, w_widget_to_get_index_for=widget_stack[0]) #take the first index in the list and get its index in the whole program
        else:
            first_element_index = None # ?????? ???????? ?????????? ?????????????? ???????????? 

        
        len_widget_stack = len(widget_stack)
        for i in range(len_widget_stack):
            widget, widget_stack = remove_last_widget(w=widget, w_widget_stack=widget_stack)
        
        qaf_var=soundform()
        qaf_var.label_2.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\soundvideo\q.mp4")))
        #qaf_var.label_2.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\videos\enemies\q .mp4")))
        qaf_var.tips.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">1. /q/ sounds a bit like the start of </span><span style=\" font-size:14pt; color:#00c37a;\">\u2018cau</span><span style=\" font-size:14pt;\">ght\u2019 but<br/>further back in the mouth, directly </span><span style=\" font-size:14pt; color:#00c37a;\">above <br/>the throat</span><span style=\" font-size:14pt;\">. </span></p></body></html>", None))
        qaf_var.tips_2.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">2. It is similar to a </span><span style=\" font-size:12pt; color:#00c37a;\">clicking sound</span><span style=\" font-size:12pt;\"> but produced with the <br/>tongue in the </span><span style=\" font-size:12pt; color:#00c37a;\">very back</span><span style=\" font-size:12pt;\"> of the mouth, it is made in <br/>cartoons when a character </span><span style=\" font-size:12pt; color:#00c37a;\">glups down</span><span style=\" font-size:12pt;\"> a drink.</span></p></body></html>", None))
        qaf_var.tips_3.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">3. Raise the </span><span style=\" font-size:14pt; color:#00c37a;\">back of your tongue</span><span style=\" font-size:14pt;\"> and place it <br/>against the </span><span style=\" font-size:14pt; color:#00c37a;\">uvula</span><span style=\" font-size:14pt;\"> (check the figure <br/>illustrated earlier). </span></p></body></html>", None))
        qaf_var.tips_4.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">4. Completely </span><span style=\" font-size:14pt; color:#00c37a;\">block</span><span style=\" font-size:14pt;\"> the airflow, with your lips <br/></span><span style=\" font-size:14pt; color:#00c37a;\">rounded and relaxed</span><span style=\" font-size:14pt; color:#000000;\">, then let the air out. </span></p></body></html>", None))
        #instances
        qafword1=wordform()
        qafword2=wordform()
        qafword3=wordform()
        qafword4=wordform()
        
        #words
        qafword1.wordlable.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; color:#ee5445;\">????</span><span style=\" font-size:20pt; color:#000000;\">??????</span><span style=\" font-size:20pt; color:#000000;\">    Quran</span></p><p align=\"center\"><br/></p></body></html>",None))
        qafword2.wordlable.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; color:#ee5445;\">????</span><span style=\" font-size:20pt; color:#000000;\">????</span><span style=\" font-size:20pt; color:#000000;\">     Story</span></p><p align=\"center\"><br/></p></body></html>",None))
        qafword3.wordlable.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; color:#ee5445;\">????</span><span style=\" font-size:20pt; color:#000000;\">??????</span><span style=\" font-size:20pt; color:#000000;\">    Village</span></p><p align=\"center\"><br/></p></body></html>",None))
        qafword4.wordlable.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; color:#ee5445;\">????</span><span style=\" font-size:20pt; color:#000000;\">????????</span><span style=\" font-size:20pt; color:#000000;\">    Law</span></p><p align=\"center\"><br/></p></body></html>",None))

        #images
        qafword1.image.setPixmap(QPixmap(r"E:\graduation project\application\images\????????.JPG"))
        qafword1.image.setScaledContents(True)
        qafword2.image.setPixmap(QPixmap(r"E:\graduation project\application\images\??????.JPG"))
        qafword2.image.setScaledContents(True)
        qafword3.image.setPixmap(QPixmap(r"E:\graduation project\application\images\????????.JPG"))
        qafword3.image.setScaledContents(True)
        qafword4.image.setPixmap(QPixmap(r"E:\graduation project\application\images\??????????.JPG"))
        qafword4.image.setScaledContents(True)

        #audios
        qafword1.wordsound.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\????????.m4a")))
        qafword2.wordsound.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\??????.m4a")))
        qafword3.wordsound.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\????????.m4a")))
        qafword4.wordsound.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\??????????.mp3")))

        #exercises

        qex=ex()#firs button  
        qex_2=ex_2() #second button
        qex_3=ex_2()
        cong=congrat()
        
        qex.wordname.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:26pt; color:#ffffff;\"> /q/</span></p></body></html>")
        qex.soundname.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:26pt; color:#ffffff;\">Sound /q/</span></p></body></html>")
        qex_2.wordname.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:26pt; color:#ffffff;\"> /q/</span></p></body></html>")
        qex_2.soundname.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:26pt; color:#ffffff;\">Sound /q/</span></p></body></html>")
        qex_3.wordname.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:26pt; color:#ffffff;\"> /q/</span></p></body></html>")
        qex_3.soundname.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:26pt; color:#ffffff;\">Sound /q/</span></p></body></html>")
        qex.B1.setText ("????????")
        qex.wordsoundb1.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\????????.m4a")))
        qex.B2.setText ("??????")
        qex.wordsoundb2.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\??????.m4a")))
        qex_2.B2.setText("??????")
        qex_2.wordsoundb2.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\??????.m4a")))
        qex_2.B1.setText("??????")
        qex_2.wordsoundb1.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\??????.m4a")))
        qex_3.B2.setText("??????")
        qex_3.wordsoundb2.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\??????.mp3")))
        qex_3.B1.setText("????????")
        qex_3.wordsoundb1.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\????????.m4a")))

        #ex-images 
        qex.label_5.setPixmap(QPixmap(r"E:\graduation project\application\images\????????.jpg"))
        qex.label_5.setScaledContents(True)
        qex.label_4.setPixmap(QPixmap(r"E:\graduation project\application\images\??????.jpg"))
        qex.label_4.setScaledContents(True)

        qex_2.label_4.setPixmap(QPixmap(r"E:\graduation project\application\images\??????.JPG"))
        qex_2.label_4.setScaledContents(True)
        qex_2.label_5.setPixmap(QPixmap(r"E:\graduation project\application\images\??????.jpg"))
        qex_2.label_5.setScaledContents(True)

        qex_3.label_4.setPixmap(QPixmap(r"E:\graduation project\application\images\??????.jpg"))
        qex_3.label_4.setScaledContents(True)
        qex_3.label_5.setPixmap(QPixmap(r"E:\graduation project\application\images\????????.jpg"))
        qex_3.label_5.setScaledContents(True)
        widgets_to_add = [qaf_var, qafword1, qafword2, qafword3, qafword4, qex, qex_2, qex_3, cong]
        #widgets arrangment 
        if first_element_index is None:
            for x in widgets_to_add: 
                my_add_widget(w=widget, w_widget_stack=widget_stack, w_to_add=x)

        else:
            for i,x in enumerate(widgets_to_add): #i = index x = element
                my_add_widget(w=widget, w_widget_stack=widget_stack, w_to_add=x, index_to_insert_at= first_element_index +i )
        widget.setCurrentWidget(widgets_to_add[0])
    def glottal(self):
        global widget_stack
        global widget

        if len(widget_stack) >0:
            first_element_index = get_index_of_widget(w=widget, w_widget_to_get_index_for=widget_stack[0])
        else:
            first_element_index = None

        len_widget_stack = len(widget_stack)
        for i in range(len_widget_stack):
            widget, widget_stack = remove_last_widget(w=widget, w_widget_stack=widget_stack)

        glottal=soundform()        
        glottal.label_2.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\soundvideo\glottal.mp4")))
        glottal.tips.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\"><span style=\" font-family:'Arial','sans-serif'; font-size:14pt; color:#000000;\">1. Hamza is the </span><span style=\" font-family:'Arial','sans-serif'; font-size:14pt; color:#00c37a;\">obstruction</span><span style=\" font-family:'Arial','sans-serif'; font-size:14pt; color:#000000;\"> of airflow in the vocal<br/>tract when the vocal cords </span><span style=\" font-family:'Arial','sans-serif'; font-size:14pt; color:#00c37a;\">tight together</span><span style=\" font-family:'Arial','sans-serif'; font-size:14pt; color:#000000;\"> and <br/>do not let the air go through them.</span></p></body></html>", None))
        glottal.tips_2.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\"><span style=\" font-family:'Arial','sans-serif'; font-size:14pt; color:#000000;\">2. It is like the </span><span style=\" font-family:'Arial','sans-serif'; font-size:14pt; color:#00c37a;\">glottal stop</span><span style=\" font-family:'Arial','sans-serif'; font-size:14pt; color:#000000;\"> between vowel sounds in<br/>a phrase such as 'sea-</span><span style=\" font-family:'Arial','sans-serif'; font-size:14pt; color:#00c37a;\">ea</span><span style=\" font-family:'Arial','sans-serif'; font-size:14pt; color:#000000;\">gle'\u00a0 or '</span><span style=\" font-family:'Arial','sans-serif'; font-size:14pt; color:#00c37a;\">o</span><span style=\" font-family:'Arial','sans-serif'; font-size:14pt; color:#000000;\">h-</span><span style=\" font-family:'Arial','sans-serif'; font-size:14pt; color:#00c37a;\">o</span><span style=\" font-family:'Arial','sans-serif'; font-size:14pt; color:#000000;\">h' or <br/>in an exclamation of hurt '</span><span style=\" font-family:'Arial','sans-seri"
                        "f'; font-size:14pt; color:#00c37a;\">ou</span><span style=\" font-family:'Arial','sans-serif'; font-size:14pt; color:#000000;\">ch!'</span></p></body></html>", None))
        glottal.tips_3.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\"><span style=\" font-family:'Arial','sans-serif'; font-size:14pt; color:#000000;\">3. It is pronounced in words that start with a vowel,<br/>ike '</span><span style=\" font-family:'Arial','sans-serif'; font-size:14pt; color:#00c37a;\">o</span><span style=\" font-family:'Arial','sans-serif'; font-size:14pt; color:#000000;\">ur', '</span><span style=\" font-family:'Arial','sans-serif'; font-size:14pt; color:#00c37a;\">i</span><span style=\" font-family:'Arial','sans-serif'; font-size:14pt; color:#000000;\">f' and '</span><span style=\" font-family:'Arial','sans-serif'; font-size:14pt; color:#00c37a;\">i</span><span style=\" font-family:'Arial','sans-serif'; font-size:14pt; color:#000000;\">t'.</span></p></body></html>", None))
        glottal.tips_4.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\"><span style=\" font-family:'Arial','sans-serif'; font-size:14pt; color:#000000;\">4. Pay attention to</span><span style=\" font-family:'Arial','sans-serif'; font-size:14pt; color:#00c37a;\"> 'the catch'</span><span style=\" font-family:'Arial','sans-serif'; font-size:14pt; color:#000000;\"> in your </span><span style=\" font-family:'Arial','sans-serif'; font-size:14pt; color:#00c37a;\">throat</span><span style=\" font-family:'Arial','sans-serif'; font-size:14pt; color:#000000;\"> when<br/>\u00a0you pronounce the first vowel.</span></p></body></html>", None))
        #instances
        glottalword1=wordform()
        glottalword2=wordform()
        glottalword3=wordform()
        glottalword4=wordform()
        glottalword5=wordform()
        glottalword6=wordform()
        glottalword7=wordform()
        glottalword8=wordform()
        
        #words
        glottalword1.wordlable.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; color:#ee5445;\">??</span><span style=\" font-size:20pt; color:#000000;\">????</span><span style=\" font-size:20pt; color:#000000;\">    Lion</span></p><p align=\"center\"><br/></p></body></html>",None))
        glottalword2.wordlable.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; color:#ee5445;\">??</span><span style=\" font-size:20pt; color:#000000;\">??????????</span><span style=\" font-size:20pt; color:#000000;\">    Bus</span></p><p align=\"center\"><br/></p></body></html>",None))
        glottalword3.wordlable.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; color:#ee5445;\">??</span><span style=\" font-size:20pt; color:#000000;\">??????</span><span style=\" font-size:20pt; color:#000000;\">    needle</span></p><p align=\"center\"><br/></p></body></html>",None))
        glottalword4.wordlable.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; color:#000000;\">????</span><span style=\" font-size:20pt; color:#ee5445;\">????</span><span style=\" font-size:20pt; color:#000000;\">????</span><span style=\" font-size:20pt; color:#000000;\">     Transfer </span></p><p align=\"center\"><br/></p></body></html>",None))
        glottalword5.wordlable.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; color:#000000;\">????</span><span style=\" font-size:20pt; color:#ee5445;\">????</span><span style=\" font-size:20pt; color:#000000;\">????</span><span style=\" font-size:20pt; color:#000000;\">     poverty </span></p><p align=\"center\"><br/></p></body></html>",None))
        glottalword6.wordlable.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; color:#000000;\">??????</span><span style=\" font-size:20pt; color:#ee5445;\">??</span><span style=\" font-size:20pt; color:#000000;\">   Slow </span></p><p align=\"center\"><br/></p></body></html>",None))
        glottalword7.wordlable.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; color:#000000;\">??????</span><span style=\" font-size:20pt; color:#ee5445;\">??</span><span style=\" font-size:20pt; color:#000000;\">   Race </span></p><p align=\"center\"><br/></p></body></html>",None))
        glottalword8.wordlable.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; color:#000000;\">????</span><span style=\" font-size:20pt; color:#ee5445;\">??</span><span style=\" font-size:20pt; color:#000000;\">????</span><span style=\" font-size:20pt; color:#ee5445;\">??</span><span style=\" font-size:20pt; color:#000000;\">   Pearl </span></p><p align=\"center\"><br/></p></body></html>",None))   
        #images
        glottalword1.image.setPixmap(QPixmap(r"E:\graduation project\application\images\??????.JPG"))
        glottalword1.image.setScaledContents(True)
        glottalword2.image.setPixmap(QPixmap(r"E:\graduation project\application\images\??????????????.JPG"))
        glottalword2.image.setScaledContents(True)
        glottalword3.image.setPixmap(QPixmap(r"E:\graduation project\application\images\????????.JPG"))
        glottalword3.image.setScaledContents(True)
        glottalword4.image.setPixmap(QPixmap(r"E:\graduation project\application\images\??????.jfif"))
        glottalword4.image.setScaledContents(True)
        glottalword5.image.setPixmap(QPixmap(r"E:\graduation project\application\images\??????.jfif"))
        glottalword5.image.setScaledContents(True)
        glottalword6.image.setPixmap(QPixmap(r"E:\graduation project\application\images\????????.png"))
        glottalword6.image.setScaledContents(True)
        glottalword7.image.setPixmap(QPixmap(r"E:\graduation project\application\images\????????.JPG"))
        glottalword7.image.setScaledContents(True)
        glottalword8.image.setPixmap(QPixmap(r"E:\graduation project\application\images\????????.JPG"))
        glottalword8.image.setScaledContents(True)
         #audios
        glottalword1.wordsound.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\??????.m4a")))
        glottalword2.wordsound.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\??????????????.m4a")))
        glottalword3.wordsound.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\????????.m4a")))
        glottalword4.wordsound.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\??????.m4a")))
        glottalword5.wordsound.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\??????.m4a")))
        glottalword6.wordsound.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\????????.m4a")))
        glottalword7.wordsound.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\????????.m4a")))
        glottalword8.wordsound.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\????????????.m4a")))
        #exercises
        glottalex=ex()#first button  
        glottalex_2=ex()#first button  
        glottalex_3=ex_2()#second button  
        cong=congrat()
        
        glottalex.wordname.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:26pt; color:#ffffff;\">/??/</span></p></body></html>")
        glottalex.soundname.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:26pt; color:#ffffff;\">Sound /??/</span></p></body></html>")
        glottalex_2.wordname.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:26pt; color:#ffffff;\">/??/</span></p></body></html>")
        glottalex_2.soundname.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:26pt; color:#ffffff;\">Sound /??/</span></p></body></html>")
        glottalex_3.wordname.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:26pt; color:#ffffff;\">/??/</span></p></body></html>")
        glottalex_3.soundname.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:26pt; color:#ffffff;\">Sound /??/</span></p></body></html>")
        glottalex.B1.setText ("??????")
        glottalex.wordsoundb1.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\??????.m4a")))
        glottalex.B2.setText ("????????")
        glottalex.wordsoundb2.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\????????.mp3")))
        glottalex_2.B1.setText("????????")
        glottalex_2.wordsoundb1.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\????????.m4a")))
        glottalex_2.B2.setText("????????")
        glottalex_2.wordsoundb2.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\????????.mp3")))
        glottalex_3.wordsoundb1.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\??????.mp3")))
        glottalex_3.wordsoundb2.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\????????????.m4a")))
        glottalex_3.B1.setText("??????")
        glottalex_3.B2.setText("????????")
        #images
        glottalex.label_5.setPixmap(QPixmap(r"E:\graduation project\application\images\??????.jpg"))
        glottalex.label_5.setScaledContents(True)
        glottalex.label_4.setPixmap(QPixmap(r"E:\graduation project\application\images\????????.JPG"))
        glottalex.label_4.setScaledContents(True)
        glottalex_2.label_4.setPixmap(QPixmap(r"E:\graduation project\application\images\????????.JPG"))
        glottalex_2.label_4.setScaledContents(True)
        glottalex_2.label_5.setPixmap(QPixmap(r"E:\graduation project\application\images\????????.jpg"))
        glottalex_2.label_5.setScaledContents(True)
        glottalex_3.label_5.setPixmap(QPixmap(r"E:\graduation project\application\images\??????.jpg"))
        glottalex_3.label_5.setScaledContents(True)
        glottalex_3.label_4.setPixmap(QPixmap(r"E:\graduation project\application\images\????????.jpg"))
        glottalex_3.label_4.setScaledContents(True)
        widgets_to_add = [glottal, glottalword1, glottalword2, glottalword3, glottalword4, glottalword5, glottalword6, glottalword7,glottalword8 ,glottalex, glottalex_2, glottalex_3, cong]
        #widgets arrangment 
        if first_element_index is None:
            
            for x in widgets_to_add: 
                my_add_widget(w=widget, w_widget_stack=widget_stack, w_to_add=x)

        else:
            for i,x in enumerate(widgets_to_add): 
                my_add_widget(w=widget, w_widget_stack=widget_stack, w_to_add=x, index_to_insert_at= first_element_index +i )

        widget.setCurrentWidget(widgets_to_add[0])  
    def h(self, tips):
        global widget_stack
        global widget

        if len(widget_stack) >0:
            first_element_index = get_index_of_widget(w=widget, w_widget_to_get_index_for=widget_stack[0])
        else:
            first_element_index = None

        len_widget_stack = len(widget_stack)
        for i in range(len_widget_stack):
            widget, widget_stack = remove_last_widget(w=widget, w_widget_stack=widget_stack)
        h=soundform()
        h.label_2.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\soundvideo\h.mp4")))
        h.tips.setText(QCoreApplication.translate("Dialog",u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt;\">1. It resembles the </span><span style=\" font-family:'Calibri','sans-serif'; font-size:16pt; color:#00c37a;\">\u2018h\u2019</span><span style=\" font-family:'Calibri','sans-serif'; font-size:16pt;\"> in \u2018</span><span style=\" font-family:'Calibri','sans-serif'; font-size:16pt; color:#00c37a;\">h</span><span style=\" font-family:'Calibri','sans-serif'; font-size:16pt;\">orse\u2019.<br/></span></p></body></html>", None))
        h.tips_2.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">2. Imagine </span><span style=\" font-size:14pt; color:#00c37a;\">exhaling</span><span style=\" font-size:14pt;\"> a strong and </span><span style=\" font-size:14pt; color:#00c37a;\">deep breath</span><span style=\" font-size:14pt;\">, it is like <br/>what you make when you </span><span style=\" font-size:14pt; color:#00c37a;\">yawn.</span></p></body></html>", None))
        h.tips_3.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">3. Open your </span><span style=\" font-size:14pt; color:#00c37a;\">vocal cords</span><span style=\" font-size:14pt;\"> and Let a </span><span style=\" font-size:14pt; color:#00c37a;\">gush of air</span><span style=\" font-size:14pt;\"> run <br/>through them.</span></p></body></html>", None))
        h.tips_4.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">4. Put your hand in front of your mouth and </span><span style=\" font-size:14pt; color:#00c37a;\">feel   <br/>the air </span><span style=\" font-size:14pt;\">coming out.</span></p></body></html>", None))        #instances
        
        #instances
        hword1=wordform()
        hword2=wordform()
        hword3=wordform()
        hword4=wordform()
        hword5=wordform()
        hword6=wordform()
        hword7=wordform()
        
        #words
        hword1.wordlable.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; color:#ee5445;\">????</span><span style=\" font-size:20pt; color:#000000;\">??????</span><span style=\" font-size:20pt; color:#000000;\">    Crescent</span>     </p><p align=\"center\"><br/></p>  </body></html>",None))
        hword2.wordlable.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; color:#ee5445;\">????</span><span style=\" font-size:20pt; color:#000000;\">????</span><span style=\" font-size:20pt; color:#000000;\">    Pyramid</span>     </p><p align=\"center\"><br/></p>  </body></html>",None))
        hword3.wordlable.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; color:#ee5445;\">????</span><span style=\" font-size:20pt; color:#000000;\">??</span><span style=\" font-size:20pt; color:#ee5445;\">????</span><span style=\" font-size:20pt; color:#000000;\">??</span><span style=\" font-size:20pt; color:#000000;\">     Hoopoe</span></p><p align=\"center\"><br/></p></body></html>",None))   
        hword4.wordlable.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; color:#000000;\">????</span><span style=\" font-size:20pt; color:#ee5445;\">????</span><span style=\" font-size:20pt; color:#000000;\">????</span>         <span style=\" font-size:20pt; color:#000000;\">   Cave </span>       </p><p align=\"center\"><br/></p>   </body></html>",None))
        hword5.wordlable.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; color:#000000;\">????</span><span style=\" font-size:20pt; color:#ee5445;\">????</span><span style=\" font-size:20pt; color:#000000;\">????</span>         <span style=\" font-size:20pt; color:#000000;\">   Arrow </span>       </p><p align=\"center\"><br/></p>   </body></html>",None))
        hword6.wordlable.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; color:#000000;\">????</span><span style=\" font-size:20pt; color:#ee5445;\">????</span><span style=\" font-size:20pt; color:#000000;\">????</span>         <span style=\" font-size:20pt; color:#000000;\">   River </span>       </p><p align=\"center\"><br/></p>   </body></html>",None))
        hword7.wordlable.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; color:#000000;\">????????</span><span style=\" font-size:20pt; color:#ee5445;\">????</span><span style=\" font-size:20pt; color:#000000;\">   ALarm </span></p><p align=\"center\"><br/></p></body></html>",None))
        #images
        hword1.image.setPixmap(QPixmap(r"E:\graduation project\application\images\????????.JPG"))
        hword1.image.setScaledContents(True)
        hword2.image.setPixmap(QPixmap(r"E:\graduation project\application\images\??????.JPG"))
        hword2.image.setScaledContents(True)
        hword3.image.setPixmap(QPixmap(r"E:\graduation project\application\images\????????.JPG"))
        hword3.image.setScaledContents(True)
        hword4.image.setPixmap(QPixmap(r"E:\graduation project\application\images\??????.JPG"))
        hword4.image.setScaledContents(True)
        hword5.image.setPixmap(QPixmap(r"E:\graduation project\application\images\??????.JPG"))
        hword5.image.setScaledContents(True)
        hword6.image.setPixmap(QPixmap(r"E:\graduation project\application\images\??????.JPG"))
        hword6.image.setScaledContents(True)
        hword7.image.setPixmap(QPixmap(r"E:\graduation project\application\images\????????.JPG"))
        hword7.image.setScaledContents(True)
        #audios
        hword1.wordsound.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\????????.m4a")))
        hword2.wordsound.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\??????.m4a")))
        hword3.wordsound.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\????????.m4a")))
        hword4.wordsound.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\??????.m4a")))
        hword5.wordsound.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\??????.m4a")))
        hword6.wordsound.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\??????.m4a")))
        hword7.wordsound.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\????????.m4a")))
        #exercises
        hex=ex_2()#second button
        hex_2=ex()#first button
        hex_3=ex_2()#second button
        cong=congrat()
        hex.wordname.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:26pt; color:#ffffff;\"> /h/  </span></p></body></html>")
        hex.soundname.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:26pt; color:#ffffff;\">Sound  /h/  </span></p></body></html>")
        hex_2.wordname.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:26pt; color:#ffffff;\"> /h/  </span></p></body></html>")
        hex_2.soundname.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:26pt; color:#ffffff;\">Sound  /h/  </span></p></body></html>")
        hex_3.wordname.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:26pt; color:#ffffff;\"> /h/  </span></p></body></html>")
        hex_3.soundname.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:26pt; color:#ffffff;\">Sound  /h/  </span></p></body></html>")
        hex.B1.setText ("??????")
        hex.B2.setText ("??????")
        hex.wordsoundb1.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\??????.mp3")))
        hex.wordsoundb2.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\??????.m4a")))
        hex_2.B1.setText("??????")
        hex_2.B2.setText("??????")
        hex_2.wordsoundb2.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\??????.m4a")))
        hex_2.wordsoundb1.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\??????.m4a")))
        hex_3.B1.setText("????????")
        hex_3.B2.setText("????????")
        hex_3.wordsoundb1.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\????????.mp3")))
        hex_3.wordsoundb2.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\????????.m4a")))
        #images
        hex.label_5.setPixmap(QPixmap(r"E:\graduation project\application\images\??????.jfif"))
        hex.label_5.setScaledContents(True)
        hex.label_4.setPixmap(QPixmap(r"E:\graduation project\application\images\??????.JPG"))
        hex.label_4.setScaledContents(True)
        hex_2.label_5.setPixmap(QPixmap(r"E:\graduation project\application\images\??????.JPG"))
        hex_2.label_5.setScaledContents(True)
        hex_2.label_4.setPixmap(QPixmap(r"E:\graduation project\application\images\??????.jpg"))
        hex_2.label_4.setScaledContents(True)
        hex_3.label_5.setPixmap(QPixmap(r"E:\graduation project\application\images\????????.jpg"))
        hex_3.label_5.setScaledContents(True)
        hex_3.label_4.setPixmap(QPixmap(r"E:\graduation project\application\images\????????.jpg"))
        hex_3.label_4.setScaledContents(True)
        widgets_to_add = [h, hword1, hword2, hword3, hword4, hword5, hword6, hword7, hex, hex_2, hex_3,cong]
        #widgets arrangment 
        if first_element_index is None:
            
            for x in widgets_to_add: 
                my_add_widget(w=widget, w_widget_stack=widget_stack, w_to_add=x)

        else:
            for i,x in enumerate(widgets_to_add): 
                my_add_widget(w=widget, w_widget_stack=widget_stack, w_to_add=x, index_to_insert_at= first_element_index +i )

        widget.setCurrentWidget(widgets_to_add[0])    
    def H(self):
        global widget_stack
        global widget
        if len(widget_stack) >0:
            first_element_index = get_index_of_widget(w=widget, w_widget_to_get_index_for=widget_stack[0])
        else:
            first_element_index = None

        len_widget_stack = len(widget_stack)
        for i in range(len_widget_stack):
            widget, widget_stack = remove_last_widget(w=widget, w_widget_stack=widget_stack) 
        H=soundform()
        H.label_2.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\soundvideo\H (2).mp4")))
        H.tips.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">1. It is similar to the sound you make when you try <br/>to </span><span style=\" font-size:14pt; color:#00c37a;\">wipe your glasses</span><span style=\" font-size:14pt;\"> or shine your mirror.</span></p></body></html>", None))
        H.tips_2.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">2. Open your mouth really wide in an</span><span style=\" font-size:12pt; color:#00c37a;\"> \u2018O\u2019 shape</span><span style=\" font-size:12pt;\">, just like <br/>they tell you to do at the dentist. keep your mouth wide<br/>and open and </span><span style=\" font-size:12pt; color:#00c37a;\">exhale</span><span style=\" font-size:12pt;\"> at the same time. Notice the air <br/>coming out will come from the </span><span style=\" font-size:12pt; color:#00c37a;\">back of your throat</span><span style=\" font-size:12pt;\">.</span></p></body></html>", None))
        H.tips_3.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">3. Push your </span><span style=\" font-size:12pt; color:#00c37a;\">epiglottis</span><span style=\" font-size:12pt;\"> backwards towards the wall of <br/>your mouth but </span><span style=\" font-size:12pt; color:#00c37a;\">not in contact</span><span style=\" font-size:12pt;\"> with it, and leave your <br/></span><span style=\" font-size:12pt; color:#00c37a;\">tongue</span><span style=\" font-size:12pt;\"> in a completely </span><span style=\" font-size:12pt; color:#00c37a;\">relaxed</span><span style=\" font-size:12pt;\"> position.</span></p></body></html>", None))
        H.tips_4.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">4. This will form a </span><span style=\" font-size:12pt; color:#00c37a;\">gap</span><span style=\" font-size:12pt;\"> between the wall of your mouth<br/>and the epiglottis,</span><span style=\" font-size:12pt; color:#00c37a;\"> push air</span><span style=\" font-size:12pt;\"> through this gap and <br/>the resulting </span><span style=\" font-size:12pt; color:#00c37a;\">friction</span><span style=\" font-size:12pt;\"> will produce /\u0127/.</span></p></body></html>", None))
        #instances
        Hword1=wordform()
        Hword2=wordform()
        Hword3=wordform()
        Hword4=wordform()
        Hword5=wordform()
        Hword6=wordform()
        Hword7=wordform()
        Hword8=wordform()
        Hword9=wordform()
        #words        
        Hword1.wordlable.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\">    <span style=\" font-size:20pt; color:#ee5445;\">????</span><span style=\" font-size:20pt; color:#000000;\">????</span><span style=\" font-size:20pt; color:#000000;\">    District </span>     </p><p align=\"center\"><br/></p>  </body></html>",None))
        Hword2.wordlable.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\">    <span style=\" font-size:20pt; color:#ee5445;\">????</span><span style=\" font-size:20pt; color:#000000;\">????</span><span style=\" font-size:20pt; color:#000000;\">    Whale </span>     </p><p align=\"center\"><br/></p>  </body></html>",None))
        Hword3.wordlable.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\">   <span style=\" font-size:20pt; color:#000000;\">????</span><span style=\" font-size:20pt; color:#ee5445;\">??????</span><span style=\" font-size:20pt; color:#000000;\">??</span>         <span style=\" font-size:20pt; color:#000000;\">   Sea </span>       </p><p align=\"center\"><br/></p>   </body></html>",None))
        Hword4.wordlable.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\">   <span style=\" font-size:20pt; color:#000000;\">????</span><span style=\" font-size:20pt; color:#ee5445;\">??????</span><span style=\" font-size:20pt; color:#000000;\">??</span>         <span style=\" font-size:20pt; color:#000000;\">   Coal </span>       </p><p align=\"center\"><br/></p>   </body></html>",None))
        Hword5.wordlable.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\">   <span style=\" font-size:20pt; color:#000000;\">????</span><span style=\" font-size:20pt; color:#ee5445;\">??????</span><span style=\" font-size:20pt; color:#000000;\">??</span>         <span style=\" font-size:20pt; color:#000000;\">   Melody </span>       </p><p align=\"center\"><br/></p>   </body></html>",None))
        Hword6.wordlable.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; color:#000000;\">??????</span><span style=\" font-size:20pt; color:#ee5445;\">????</span><span style=\" font-size:20pt; color:#000000;\">   Salt </span></p><p align=\"center\"><br/></p></body></html>",None))
        Hword7.wordlable.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; color:#000000;\">??????</span><span style=\" font-size:20pt; color:#ee5445;\">??</span><span style=\" font-size:20pt; color:#000000;\">   Theater </span></p><p align=\"center\"><br/></p></body></html>",None))
        Hword8.wordlable.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; color:#000000;\">??????</span><span style=\" font-size:20pt; color:#ee5445;\">??</span><span style=\" font-size:20pt; color:#000000;\">   Farmer </span></p><p align=\"center\"><br/></p></body></html>",None))
        Hword9.wordlable.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\">    <span style=\" font-size:20pt; color:#ee5445;\">????</span><span style=\" font-size:20pt; color:#000000;\">????</span><span style=\" font-size:20pt; color:#000000;\">    District </span>     </p><p align=\"center\"><br/></p>  </body></html>",None))

        #Audios
        Hword1.wordsound.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\????.m4a")))
        Hword2.wordsound.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\??????.m4a")))
        Hword3.wordsound.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\??????.mp3")))
        Hword4.wordsound.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\??????.mp3")))
        Hword5.wordsound.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\??????.mp3")))
        Hword6.wordsound.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\??????.m4a")))
        Hword7.wordsound.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\????????.m4a")))
        Hword8.wordsound.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\????????.m4a")))
        Hword9.wordsound.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\??????.m4a")))
        #images
        Hword1.image.setPixmap(QPixmap(r"E:\graduation project\application\images\????.JPG"))
        Hword1.image.setScaledContents(True)
        Hword2.image.setPixmap(QPixmap(r"E:\graduation project\application\images\??????.JPG"))
        Hword2.image.setScaledContents(True)
        Hword3.image.setPixmap(QPixmap(r"E:\graduation project\application\images\??????.JPG"))
        Hword3.image.setScaledContents(True)
        Hword4.image.setPixmap(QPixmap(r"E:\graduation project\application\images\??????.JPG"))
        Hword4.image.setScaledContents(True)
        Hword5.image.setPixmap(QPixmap(r"E:\graduation project\application\images\??????.png"))
        Hword5.image.setScaledContents(True)
        Hword6.image.setPixmap(QPixmap(r"E:\graduation project\application\images\??????.JPG"))
        Hword6.image.setScaledContents(True)
        Hword7.image.setPixmap(QPixmap(r"E:\graduation project\application\images\????????.JPG"))
        Hword7.image.setScaledContents(True)
        Hword8.image.setPixmap(QPixmap(r"E:\graduation project\application\images\????????.JPG"))
        Hword8.image.setScaledContents(True)
        Hword9.image.setPixmap(QPixmap(r"E:\graduation project\application\images\??????.JPG"))
        Hword9.image.setScaledContents(True)
        #exercises
        Hex=ex_2()#second button 
        Hex_2=ex_2()#second button
        Hex_3=ex()#first button 
        cong=congrat()
        Hex.wordname.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:26pt; color:#ffffff;\"> /??/ </span></p></body></html>")
        Hex.soundname.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:26pt; color:#ffffff;\">Sound  /??/  </span></p></body></html>")
        Hex_2.wordname.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:26pt; color:#ffffff;\"> /??/ </span></p></body></html>")
        Hex_2.soundname.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:26pt; color:#ffffff;\">Sound  /??/  </span></p></body></html>")
        Hex_3.wordname.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:26pt; color:#ffffff;\"> /??/ </span></p></body></html>")
        Hex_3.soundname.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:26pt; color:#ffffff;\">Sound  /??/  </span></p></body></html>")
        Hex.B1.setText ("??????")
        Hex.B2.setText ("??????")
        Hex.wordsoundb1.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\??????.mp3")))
        Hex.wordsoundb2.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\??????.m4a")))
        Hex_2.B1.setText("??????")
        Hex_2.B2.setText("????????")
        Hex_2.wordsoundb1.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\??????.mp3")))
        Hex_2.wordsoundb2.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\????????.m4a")))
        Hex_3.B1.setText("??????")
        Hex_3.B2.setText("??????")
        Hex_3.wordsoundb1.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\??????.mp3")))
        Hex_3.wordsoundb2.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\??????.mp3")))
        #images
        Hex.label_5.setPixmap(QPixmap(r"E:\graduation project\application\images\??????.jpg"))
        Hex.label_5.setScaledContents(True)
        Hex.label_4.setPixmap(QPixmap(r"E:\graduation project\application\images\??????.JPG"))
        Hex.label_4.setScaledContents(True)
        Hex_2.label_5.setPixmap(QPixmap(r"E:\graduation project\application\images\??????.JPG"))
        Hex_2.label_5.setScaledContents(True)
        Hex_2.label_4.setPixmap(QPixmap(r"E:\graduation project\application\images\????????.jpg"))
        Hex_2.label_4.setScaledContents(True)
        Hex_3.label_5.setPixmap(QPixmap(r"E:\graduation project\application\images\??????.jpg"))
        Hex_3.label_5.setScaledContents(True)
        Hex_3.label_4.setPixmap(QPixmap(r"E:\graduation project\application\images\??????.jpg"))
        Hex_3.label_4.setScaledContents(True)
        widgets_to_add = [H, Hword1, Hword2, Hword3, Hword4, Hword5, Hword6, Hword7, Hword8, Hword9, Hex, Hex_2, Hex_3, cong]

        #widgets arrangment 
        if first_element_index is None:
            
            for x in widgets_to_add: 
                my_add_widget(w=widget, w_widget_stack=widget_stack, w_to_add=x)

        else:
            for i,x in enumerate(widgets_to_add): 
                my_add_widget(w=widget, w_widget_stack=widget_stack, w_to_add=x, index_to_insert_at= first_element_index +i )

    
        widget.setCurrentWidget(widgets_to_add[0]) 
    def ain(self):
        global widget_stack
        global widget

        if len(widget_stack) >0:
            first_element_index = get_index_of_widget(w=widget, w_widget_to_get_index_for=widget_stack[0])
        else:
            first_element_index = None

        len_widget_stack = len(widget_stack)
        for i in range(len_widget_stack):
            widget, widget_stack = remove_last_widget(w=widget, w_widget_stack=widget_stack)

        
        ain=soundform()
        
        ain.label_2.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\soundvideo\??.mp4")))
        ain.tips.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\"><span style=\" font-family:'Calibri','sans-serif'; font-size:14pt;\">1. sometimes /\u0295/ is compared to a </span><span style=\" font-family:'Calibri','sans-serif'; font-size:14pt; color:#00c37a;\">choking sound</span><span style=\" font-family:'Calibri','sans-serif'; font-size:14pt;\">.<br/> Pretend to strangle yourself and shout out.</span></p></body></html>", None))
        ain.tips_2.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">2. Place your hand on your </span><span style=\" font-size:12pt; color:#00c37a;\">throat</span><span style=\" font-size:12pt;\"> and say </span><span style=\" font-size:12pt; color:#ee5445;\">/n/</span><span style=\" font-size:12pt;\">, feel <br/>the vibration, that is your </span><span style=\" font-size:12pt; color:#00c37a;\">vocal cords </span><span style=\" font-size:12pt;\">vibrating.<br/>if you mastered </span><span style=\" font-size:12pt; color:#00c37a;\">/\u0127/</span><span style=\" font-size:12pt;\">, try saying it but with </span><span style=\" font-size:12pt; color:#00c37a;\">vibrating</span><span style=\" font-size:12pt;\"><br/>your vocal cords.</span></p></body></html>", None))
        ain.tips_3.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\"><span style=\" font-size:13pt; color:#ee5445;\">3. Push your </span><span style=\" font-size:13pt; color:#ee5445;\">epiglottis</span><span style=\" font-size:13pt; color:#ee5445;\"> backwards to be in contact <br/>with the wall of your mouth and block the airstream. </span></p></body></html>", None))
        ain.tips_4.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\"><span style=\" font-family:'-apple-system','system-ui','BlinkMacSystemFont','Segoe UI','Roboto','Oxygen-Sans','Ubuntu','Cantarell','Helvetica Neue','sans-serif'; font-size:12pt; color:#000000;\">4. Try saying a </span><span style=\" font-family:'-apple-system','system-ui','BlinkMacSystemFont','Segoe UI','Roboto','Oxygen-Sans','Ubuntu','Cantarell','Helvetica Neue','sans-serif'; font-size:12pt; color:#ee5445;\">long '</span><span style=\" font-family:'-apple-system','system-ui','BlinkMacSystemFont','Segoe UI','Roboto','Oxygen-Sans','Ubuntu','Cantarell','Helvetica Neue','sans-serif'; font-size:12pt; font-style:italic; color:#ee5445;\">aaa'</span><span style=\" font-family:'-apple-system','system-ui','BlinkMacSystemFont','Segoe UI','Roboto','Oxygen-Sans','Ubuntu','Cantarell','Helvetica Neue','sans-serif'; font-size:12pt; color:#000000;\"> with your </span><span style=\" font-family:'-apple-system','system-ui','BlinkMacSystemFont','Segoe UI','Roboto','Oxygen-Sans','Ubuntu','Ca"
                        "ntarell','Helvetica Neue','sans-serif'; font-size:12pt; color:#00c37a;\">tongue root</span><span style=\" font-family:'-apple-system','system-ui','BlinkMacSystemFont','Segoe UI','Roboto','Oxygen-Sans','Ubuntu','Cantarell','Helvetica Neue','sans-serif'; font-size:12pt; color:#000000;\"> as deep in <br/>the pharynx as possible. Just keep repeating it, each time <br/>reaching </span><span style=\" font-family:'-apple-system','system-ui','BlinkMacSystemFont','Segoe UI','Roboto','Oxygen-Sans','Ubuntu','Cantarell','Helvetica Neue','sans-serif'; font-size:12pt; color:#00c37a;\">deeper</span><span style=\" font-family:'-apple-system','system-ui','BlinkMacSystemFont','Segoe UI','Roboto','Oxygen-Sans','Ubuntu','Cantarell','Helvetica Neue','sans-serif'; font-size:12pt; color:#000000;\"> and deeper with your tongue root\u00a0</span><span style=\" font-family:'-apple-system','system-ui','BlinkMacSystemFont','Segoe UI','Roboto','Oxygen-Sans','Ubuntu','Cantarell','Helvetica Neue','sans-serif'; font-size:12pt; font-style:ital"
                        "ic; color:#00c37a;\">without</span><span style=\" font-family:'-apple-system','system-ui','BlinkMacSystemFont','Segoe UI','Roboto','Oxygen-Sans','Ubuntu','Cantarell','Helvetica Neue','sans-serif'; font-size:12pt; color:#000000;\"><br/>lifting it up.\u00a0</span></p></body></html>", None))
        #instances
        ainword1=wordform()
        ainword2=wordform()
        ainword3=wordform()
        ainword4=wordform()
        ainword5=wordform()
        ainword6=wordform()
        ainword7=wordform()
        ainword8=wordform()
        ainword9=wordform()
        
        #words
        ainword1.wordlable.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\">    <span style=\" font-size:20pt; color:#ee5445;\">????</span><span style=\" font-size:20pt; color:#000000;\">????</span><span style=\" font-size:20pt; color:#000000;\">    Honey</span>     </p><p align=\"center\"><br/></p>  </body></html>",None))
        ainword2.wordlable.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\">    <span style=\" font-size:20pt; color:#ee5445;\">????</span><span style=\" font-size:20pt; color:#000000;\">????</span><span style=\" font-size:20pt; color:#000000;\">    Grape</span>     </p><p align=\"center\"><br/></p>  </body></html>",None))
        ainword3.wordlable.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\">    <span style=\" font-size:20pt; color:#ee5445;\">????</span><span style=\" font-size:20pt; color:#000000;\">????????</span><span style=\" font-size:20pt; color:#000000;\">    Bird</span>     </p><p align=\"center\"><br/></p>  </body></html>",None))
        ainword4.wordlable.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\">   <span style=\" font-size:20pt; color:#000000;\">????</span><span style=\" font-size:20pt; color:#ee5445;\">??????</span><span style=\" font-size:20pt; color:#000000;\">??</span>         <span style=\" font-size:20pt; color:#000000;\">   Hard </span>       </p><p align=\"center\"><br/></p>   </body></html>",None))
        ainword5.wordlable.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\">   <span style=\" font-size:20pt; color:#000000;\">????</span><span style=\" font-size:20pt; color:#ee5445;\">??????</span><span style=\" font-size:20pt; color:#000000;\">??</span>         <span style=\" font-size:20pt; color:#000000;\">   Hair </span>       </p><p align=\"center\"><br/></p>   </body></html>",None))
        ainword6.wordlable.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\">   <span style=\" font-size:20pt; color:#000000;\">????</span><span style=\" font-size:20pt; color:#ee5445;\">??????</span><span style=\" font-size:20pt; color:#000000;\">??</span>         <span style=\" font-size:20pt; color:#000000;\">   People </span>       </p><p align=\"center\"><br/></p>   </body></html>",None))
        ainword7.wordlable.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\">   <span style=\" font-size:20pt; color:#000000;\">????</span><span style=\" font-size:20pt; color:#ee5445;\">??????</span><span style=\" font-size:20pt; color:#000000;\">??????</span>         <span style=\" font-size:20pt; color:#000000;\">   Tired </span>       </p><p align=\"center\"><br/></p>   </body></html>",None))
        ainword8.wordlable.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\">   <span style=\" font-size:20pt; color:#000000;\">????</span><span style=\" font-size:20pt; color:#ee5445;\">??????</span><span style=\" font-size:20pt; color:#000000;\">????</span>         <span style=\" font-size:20pt; color:#000000;\">   Toy </span>       </p><p align=\"center\"><br/></p>   </body></html>",None))
        ainword9.wordlable.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; color:#000000;\">??????</span><span style=\" font-size:20pt; color:#ee5445;\">??</span><span style=\" font-size:20pt; color:#000000;\">   Arm </span></p><p align=\"center\"><br/></p></body></html>",None))

        #images
        ainword1.image.setPixmap(QPixmap(r"E:\graduation project\application\images\??????.JPG"))
        ainword1.image.setScaledContents(True)
        ainword2.image.setPixmap(QPixmap(r"E:\graduation project\application\images\??????.JPG"))
        ainword2.image.setScaledContents(True)
        ainword3.image.setPixmap(QPixmap(r"E:\graduation project\application\images\??????????.JPG"))
        ainword3.image.setScaledContents(True)
        ainword4.image.setPixmap(QPixmap(r"E:\graduation project\application\images\??????.JPG"))
        ainword4.image.setScaledContents(True)
        ainword5.image.setPixmap(QPixmap(r"E:\graduation project\application\images\??????.JPG"))
        ainword5.image.setScaledContents(True)
        ainword6.image.setPixmap(QPixmap(r"E:\graduation project\application\images\??????.JPG"))
        ainword6.image.setScaledContents(True)
        ainword7.image.setPixmap(QPixmap(r"E:\graduation project\application\images\??????????.JPG"))
        ainword7.image.setScaledContents(True)
        ainword8.image.setPixmap(QPixmap(r"E:\graduation project\application\images\????????.JPG"))
        ainword8.image.setScaledContents(True)
        ainword9.image.setPixmap(QPixmap(r"E:\graduation project\application\images\????????.JPG"))
        ainword9.image.setScaledContents(True)
        #audio
        ainword1.wordsound.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\??????.mp3")))
        ainword2.wordsound.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\??????.mp3")))
        ainword3.wordsound.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\??????????.mp3")))
        ainword4.wordsound.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\??????.mp3")))
        ainword5.wordsound.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\??????.mp3")))
        ainword6.wordsound.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\??????.mp3")))
        ainword7.wordsound.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\??????????.mp3")))
        ainword8.wordsound.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\????????.mp3")))
        ainword9.wordsound.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\????????.mp3")))
        #exercises
        ainex=ex_2()
        ainex_2=ex()
        ainex_3=ex_2()
        cong=congrat()
        ainex.wordname.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:26pt; color:#ffffff;\"> / ?? / </span></p></body></html>")
        ainex.soundname.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:26pt; color:#ffffff;\">Sound / ?? / </span></p></body></html>")
        ainex_2.wordname.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:26pt; color:#ffffff;\"> / ?? / </span></p></body></html>")
        ainex_2.soundname.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:26pt; color:#ffffff;\">Sound / ?? / </span></p></body></html>")
        ainex_3.wordname.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:26pt; color:#ffffff;\"> / ?? / </span></p></body></html>")
        ainex_3.soundname.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:26pt; color:#ffffff;\">Sound / ?? / </span></p></body></html>")

        ainex.B1.setText ("??????????")
        ainex.B2.setText ("??????")
        ainex.wordsoundb1.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\??????????.mp3")))
        ainex.wordsoundb2.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\??????.mp3")))

        ainex_2.B1.setText("??????")
        ainex_2.B2.setText("??????")
        ainex_2.wordsoundb1.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\??????.mp3")))
        ainex_2.wordsoundb2.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\??????.mp3")))
        ainex_3.B1.setText("??????")
        ainex_3.B2.setText("????????")
        ainex_3.wordsoundb1.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\??????.m4a")))
        ainex_3.wordsoundb2.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\????????.mp3")))

        #images
        ainex.label_5.setPixmap(QPixmap(r"E:\graduation project\application\images\??????????.jpg"))
        ainex.label_5.setScaledContents(True)
        ainex.label_4.setPixmap(QPixmap(r"E:\graduation project\application\images\??????.JPG"))
        ainex.label_4.setScaledContents(True)

        ainex_2.label_5.setPixmap(QPixmap(r"E:\graduation project\application\images\??????.JPG"))
        ainex_2.label_5.setScaledContents(True)
        ainex_2.label_4.setPixmap(QPixmap(r"E:\graduation project\application\images\??????.jpg"))
        ainex_2.label_4.setScaledContents(True)

        ainex_3.label_5.setPixmap(QPixmap(r"E:\graduation project\application\images\??????.jpg"))
        ainex_3.label_5.setScaledContents(True)
        ainex_3.label_4.setPixmap(QPixmap(r"E:\graduation project\application\images\????????.jpg"))
        ainex_3.label_4.setScaledContents(True)


        widgets_to_add = [ain, ainword1, ainword2, ainword3, ainword4, ainword5, ainword6, ainword7, ainex, ainex_2, ainex_3, cong]
        #widgets arrangment 
        if first_element_index is None:
            
            for x in widgets_to_add: 
                my_add_widget(w=widget, w_widget_stack=widget_stack, w_to_add=x)

        else:
            for i,x in enumerate(widgets_to_add): 
                my_add_widget(w=widget, w_widget_stack=widget_stack, w_to_add=x, index_to_insert_at= first_element_index +i )

    
        widget.setCurrentWidget(widgets_to_add[0])    
    def gain(self):
        global widget_stack
        global widget

        if len(widget_stack) >0:
            first_element_index = get_index_of_widget(w=widget, w_widget_to_get_index_for=widget_stack[0])
        else:
            first_element_index = None

        len_widget_stack = len(widget_stack)
        for i in range(len_widget_stack):
            widget, widget_stack = remove_last_widget(w=widget, w_widget_stack=widget_stack)

        
        gain=soundform()
        
        gain.label_2.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\soundvideo\?? .mp4")))
        gain.tips.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\"><span style=\" font-size:13pt;\">1. The difference between </span><span style=\" font-size:13pt; color:#ee5445;\">/x/</span><span style=\" font-size:13pt;\"> and</span><span style=\" font-size:13pt; color:#00c37a;\"> /\u0263/</span><span style=\" font-size:13pt;\"> is like the <br/>difference between </span><span style=\" font-size:13pt; color:#ee5445;\">/s/</span><span style=\" font-size:13pt;\"> and </span><span style=\" font-size:13pt; color:#00c37a;\">/z/</span><span style=\" font-size:13pt;\">, pronounce both of <br/>them placing your </span><span style=\" font-size:13pt; color:#00c37a;\">hand on your throat</span><span style=\" font-size:13pt;\"> and feel <br/>the vibration in /z/.</span></p></body></html>", None))
        gain.tips_2.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; color:#000000;\">2. </span><span style=\" font-size:14pt; color:#00c37a;\">/\u0263/</span><span style=\" font-size:14pt; color:#000000;\"> is like the </span><span style=\" font-size:14pt; color:#ee5445;\">/x/</span><span style=\" font-size:14pt; color:#000000;\"> sound but with </span><span style=\" font-size:14pt; color:#00c37a;\">vibrating<br/></span><span style=\" font-size:14pt; color:#000000;\">your vocal cords as in </span><span style=\" font-size:14pt; color:#00c37a;\">/z/</span><span style=\" font-size:14pt; color:#000000;\">.</span></p></body></html>", None))
        gain.tips_3.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; color:#000000;\">3. Place the </span><span style=\" font-size:14pt; color:#00c37a;\">back of your tongue</span><span style=\" font-size:14pt; color:#000000;\"> against the </span><span style=\" font-size:14pt; color:#00c37a;\">soft <br/>palate</span><span style=\" font-size:14pt; color:#000000;\">, but not completely in contact with it.</span></p></body></html>", None))
        gain.tips_4.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; color:#000000;\">4. Leave your tongue in position while allowing</span><br/><span style=\" font-size:14pt; color:#00c37a;\">voiced\u00a0air</span><span style=\" font-size:14pt; color:#000000;\"> to pass through the </span><span style=\" font-size:14pt; color:#00c37a;\">gab</span><span style=\" font-size:14pt; color:#000000;\"> created <br/>between your tongue and soft palate.</span></p></body></html>", None))
        #instances
        gainword1=wordform()
        gainword2=wordform()
        gainword3=wordform()
        gainword4=wordform()
        gainword5=wordform()
        gainword6=wordform()
        gainword7=wordform()
        
        #words
        gainword1.wordlable.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\">    <span style=\" font-size:20pt; color:#ee5445;\">????</span><span style=\" font-size:20pt; color:#000000;\">??????</span>   <span style=\" font-size:20pt; color:#000000;\">    Deaf</span>     </p><p align=\"center\"><br/></p>  </body></html>",None))
        gainword2.wordlable.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\">    <span style=\" font-size:20pt; color:#ee5445;\">????</span><span style=\" font-size:20pt; color:#000000;\">??????</span>   <span style=\" font-size:20pt; color:#000000;\">    Crow</span>     </p><p align=\"center\"><br/></p>  </body></html>",None))
        gainword3.wordlable.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\">   <span style=\" font-size:20pt; color:#000000;\">????</span><span style=\" font-size:20pt; color:#ee5445;\">??????</span><span style=\" font-size:20pt; color:#000000;\">????</span>         <span style=\" font-size:20pt; color:#000000;\">   Job </span>       </p><p align=\"center\"><br/></p>   </body></html>",None))
        gainword4.wordlable.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\">   <span style=\" font-size:20pt; color:#000000;\">????</span><span style=\" font-size:20pt; color:#ee5445;\">??????</span><span style=\" font-size:20pt; color:#000000;\">????</span>         <span style=\" font-size:20pt; color:#000000;\">   - </span>       </p><p align=\"center\"><br/></p>   </body></html>",None))
        gainword5.wordlable.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\">   <span style=\" font-size:20pt; color:#000000;\">??</span><span style=\" font-size:20pt; color:#ee5445;\">????</span><span style=\" font-size:20pt; color:#000000;\">????</span>         <span style=\" font-size:20pt; color:#000000;\">   Foam </span>       </p><p align=\"center\"><br/></p>   </body></html>",None))
        gainword6.wordlable.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\">   <span style=\" font-size:20pt; color:#000000;\">??</span><span style=\" font-size:20pt; color:#ee5445;\">????</span><span style=\" font-size:20pt; color:#000000;\">??????</span>         <span style=\" font-size:20pt; color:#000000;\">   Song </span>       </p><p align=\"center\"><br/></p>   </body></html>",None))
        gainword7.wordlable.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; color:#000000;\">????</span><span style=\" font-size:20pt; color:#ee5445;\">??</span><span style=\" font-size:20pt; color:#000000;\">????</span><span style=\" font-size:20pt; color:#ee5445;\">??</span><span style=\" font-size:20pt; color:#000000;\">???? </span><span style=\" font-size:20pt; color:#000000;\"> Parrots </span></p><p align=\"center\"><br/></p></body></html>",None))

        #images
        gainword1.image.setPixmap(QPixmap(r"E:\graduation project\application\images\??????????.JPG"))
        gainword1.image.setScaledContents(True)
        gainword2.image.setPixmap(QPixmap(r"E:\graduation project\application\images\????????.JPG"))
        gainword2.image.setScaledContents(True)
        gainword3.image.setPixmap(QPixmap(r"E:\graduation project\application\images\??????.jfif"))
        gainword3.image.setScaledContents(True)
        gainword4.image.setPixmap(QPixmap(r"E:\graduation project\application\images\??????.JPG"))
        gainword4.image.setScaledContents(True)
        gainword5.image.setPixmap(QPixmap(r"E:\graduation project\application\images\????????.JPG"))
        gainword5.image.setScaledContents(True)
        gainword6.image.setPixmap(QPixmap(r"E:\graduation project\application\images\??????????.JPG"))
        gainword6.image.setScaledContents(True)
        gainword7.image.setPixmap(QPixmap(r"E:\graduation project\application\images\????????????.jpg"))
        gainword7.image.setScaledContents(True)
        
        #Audio
        gainword1.wordsound.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\??????????.mp3")))
        gainword2.wordsound.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\????????.mp3")))
        gainword3.wordsound.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\??????.mp3")))
        gainword4.wordsound.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\??????.mp3")))
        gainword5.wordsound.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\????????.mp3")))
        gainword6.wordsound.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\??????????.mp3")))
        gainword7.wordsound.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\????????????.mp3")))

        #exercises
        gainex=ex_2()
        gainex_2=ex()
        gainex_3=ex()
        cong=congrat()
        
        gainex.wordname.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:26pt; color:#ffffff;\">/ ?? / </span></p></body></html>")
        gainex.soundname.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:26pt; color:#ffffff;\">Sound / ?? / </span></p></body></html>")
        gainex_2.wordname.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:26pt; color:#ffffff;\">/ ?? / </span></p></body></html>")
        gainex_2.soundname.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:26pt; color:#ffffff;\">Sound / ?? / </span></p></body></html>")
        gainex_3.wordname.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:26pt; color:#ffffff;\">/ ?? / </span></p></body></html>")
        gainex_3.soundname.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:26pt; color:#ffffff;\">Sound / ?? / </span></p></body></html>")

        gainex.B1.setText ("??????")
        gainex.B2.setText ("??????????")
        gainex.wordsoundb1.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\??????.mp3")))
        gainex.wordsoundb2.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\??????????.mp3")))
        gainex_2.B1.setText("??????")
        gainex_2.B2.setText("??????")
        gainex_2.wordsoundb1.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\??????.mp3")))
        gainex_2.wordsoundb2.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\??????.mp3")))
        gainex_3.B1.setText("????????????")
        gainex_3.B2.setText("??????")
        gainex_3.wordsoundb1.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\????????????.mp3")))
        gainex_3.wordsoundb2.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\??????.mp3")))

        #images
        gainex.label_5.setPixmap(QPixmap(r"E:\graduation project\application\images\??????.jpg"))
        gainex.label_5.setScaledContents(True)
        gainex.label_4.setPixmap(QPixmap(r"E:\graduation project\application\images\??????????.JPG"))
        gainex.label_4.setScaledContents(True)

        gainex_2.label_5.setPixmap(QPixmap(r"E:\graduation project\application\images\??????.JPG"))
        gainex_2.label_5.setScaledContents(True)
        gainex_2.label_4.setPixmap(QPixmap(r"E:\graduation project\application\images\??????.jpg"))
        gainex_2.label_4.setScaledContents(True)

        gainex_3.label_5.setPixmap(QPixmap(r"E:\graduation project\application\images\????????????.jpg"))
        gainex_3.label_5.setScaledContents(True)
        gainex_3.label_4.setPixmap(QPixmap(r"E:\graduation project\application\images\??????.jpg"))
        gainex_3.label_4.setScaledContents(True)
        widgets_to_add = [gain, gainword1, gainword2, gainword3, gainword4, gainword5, gainword6, gainword7, gainex, gainex_2, gainex_3, cong]

        #widgets arrangment 
        if first_element_index is None:
            
            for x in widgets_to_add: 
                my_add_widget(w=widget, w_widget_stack=widget_stack, w_to_add=x)

        else:
            for i,x in enumerate(widgets_to_add): 
                my_add_widget(w=widget, w_widget_stack=widget_stack, w_to_add=x, index_to_insert_at= first_element_index +i )

    
        widget.setCurrentWidget(widgets_to_add[0])   
    def gim(self):
        global widget_stack
        global widget

        if len(widget_stack) >0:
            first_element_index = get_index_of_widget(w=widget, w_widget_to_get_index_for=widget_stack[0])
        else:
            first_element_index = None

        len_widget_stack = len(widget_stack)
        for i in range(len_widget_stack):
            widget, widget_stack = remove_last_widget(w=widget, w_widget_stack=widget_stack)

        g=soundform()    
        g.label_2.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\soundvideo\g.mp4")))
        g.tips.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">1. It is similar to the </span><span style=\" font-size:14pt; color:#ee5445;\">/k/</span><span style=\" font-size:14pt;\"> sound, but with </span><span style=\" font-size:14pt; color:#00c37a;\">vibrating</span></p><p align=\"center\"><span style=\" font-size:14pt;\">your vocal cords.</span></p></body></html>", None))
        g.tips_2.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">2. Raise the </span><span style=\" font-size:14pt; color:#00c37a;\">back of your tongue</span><span style=\" font-size:14pt;\"> against the </span><span style=\" font-size:14pt; color:#00c37a;\">soft <br/>palate</span><span style=\" font-size:14pt;\"> and briefly</span><span style=\" font-size:14pt; color:#00c37a;\"> block </span><span style=\" font-size:14pt; color:#000000;\">the airflow.</span></p></body></html>", None))
        g.tips_3.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">3. </span><span style=\" font-size:14pt; color:#00c37a;\">release</span><span style=\" font-size:14pt;\"> the burst air.</span></p></body></html>", None))
        g.tips_4.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">4. make sure you are </span><span style=\" font-size:14pt; color:#00c37a;\">vibrating</span><span style=\" font-size:14pt;\"> your vocal cords by <br/>placing your hand on your </span><span style=\" font-size:14pt; color:#00c37a;\">throat</span><span style=\" font-size:14pt;\"> or </span><span style=\" font-size:14pt; color:#00c37a;\">Adam's apple</span><span style=\" font-size:14pt;\"><br/>and feel the vibration.</span></p></body></html>", None))
        #instances
        gword1=wordform()
        gword2=wordform()
        gword3=wordform()
        gword4=wordform()
        #gword5=wordform()
        #gword6=wordform()
        gword7=wordform()
        gword8=wordform()        
        gword9=wordform()
        #words
        gword1.wordlable.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\">    <span style=\" font-size:20pt; color:#ee5445;\">????</span><span style=\" font-size:20pt; color:#000000;\">????</span>   <span style=\" font-size:20pt; color:#000000;\">    Camel</span>     </p><p align=\"center\"><br/></p>  </body></html>",None))
        gword2.wordlable.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\">    <span style=\" font-size:20pt; color:#ee5445;\">????</span><span style=\" font-size:20pt; color:#000000;\">??????</span>   <span style=\" font-size:20pt; color:#000000;\">    Letter</span>     </p><p align=\"center\"><br/></p>  </body></html>",None))
        gword3.wordlable.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\">    <span style=\" font-size:20pt; color:#ee5445;\">????</span><span style=\" font-size:20pt; color:#000000;\">????????</span>   <span style=\" font-size:20pt; color:#000000;\">    Neighbors</span>     </p><p align=\"center\"><br/></p>  </body></html>",None))
        gword4.wordlable.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\">   <span style=\" font-size:20pt; color:#000000;\">??</span><span style=\" font-size:20pt; color:#ee5445;\">????</span><span style=\" font-size:20pt; color:#000000;\">????</span>         <span style=\" font-size:20pt; color:#000000;\">   Leg </span>       </p><p align=\"center\"><br/></p>   </body></html>",None))
        #gword5.wordlable.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\">   <span style=\" font-size:20pt; color:#000000;\">????</span><span style=\" font-size:20pt; color:#ee5445;\">????</span><span style=\" font-size:20pt; color:#000000;\">????</span>         <span style=\" font-size:20pt; color:#000000;\">   Stone </span>       </p><p align=\"center\"><br/></p>   </body></html>",None))
        #gword6.wordlable.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\">   <span style=\" font-size:20pt; color:#000000;\">????</span><span style=\" font-size:20pt; color:#ee5445;\">????</span><span style=\" font-size:20pt; color:#000000;\">????</span>         <span style=\" font-size:20pt; color:#000000;\">   Sausage </span>       </p><p align=\"center\"><br/></p>   </body></html>",None))
        gword7.wordlable.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; color:#000000;\">??????</span><span style=\" font-size:20pt; color:#ee5445;\">??</span><span style=\" font-size:20pt; color:#000000;\">   Snow </span></p><p align=\"center\"><br/></p></body></html>",None))
        gword8.wordlable.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; color:#000000;\">????</span><span style=\" font-size:20pt; color:#ee5445;\">??</span><span style=\" font-size:20pt; color:#000000;\">   Wave </span></p><p align=\"center\"><br/></p></body></html>",None))
        gword9.wordlable.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; color:#000000;\">????</span><span style=\" font-size:20pt; color:#ee5445;\">??</span><span style=\" font-size:20pt; color:#000000;\">   Tower </span></p><p align=\"center\"><br/></p></body></html>",None))
        #images
        gword1.image.setPixmap(QPixmap(r"E:\graduation project\application\images\??????.JPG"))
        gword1.image.setScaledContents(True)
        gword2.image.setPixmap(QPixmap(r"E:\graduation project\application\images\????????.JPG"))
        gword2.image.setScaledContents(True)
        gword3.image.setPixmap(QPixmap(r"E:\graduation project\application\images\??????????.JPG"))
        gword3.image.setScaledContents(True)
        gword4.image.setPixmap(QPixmap(r"E:\graduation project\application\images\??????.png"))
        gword4.image.setScaledContents(True)
        #gword5.image.setPixmap(QPixmap(r"E:\graduation project\application\images\??????.JPG"))
        #gword5.image.setScaledContents(True)
        #gword6.image.setPixmap(QPixmap(r"E:\graduation project\application\images\??????.JPG"))
        #gword6.image.setScaledContents(True)
        gword7.image.setPixmap(QPixmap(r"E:\graduation project\application\images\??????.JPG"))
        gword7.image.setScaledContents(True)
        gword8.image.setPixmap(QPixmap(r"E:\graduation project\application\images\??????.JPG"))
        gword8.image.setScaledContents(True)
        gword9.image.setPixmap(QPixmap(r"E:\graduation project\application\images\??????.JPG"))
        gword9.image.setScaledContents(True)

        #audios
        gword1.wordsound.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\??????.mp3")))
        gword2.wordsound.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\????????.mp3")))
        gword3.wordsound.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\??????????.mp3")))
        gword4.wordsound.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\??????.mp3")))
        #gword5.wordsound.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\??????.mp3")))
        #gword6.wordsound.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\??????.mp3")))
        gword7.wordsound.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\??????.mp3")))
        gword8.wordsound.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\??????.mp3")))
        gword9.wordsound.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\??????.mp3")))

        #exercises
        gimex=ex()
        gimex_2=ex()
        gimex_3=ex_2()
        cong=congrat()
        
        gimex.wordname.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:26pt; color:#ffffff;\">/ g / </span></p></body></html>")
        gimex.soundname.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:26pt; color:#ffffff;\">Sound  / g / </span></p></body></html>")
        gimex_2.wordname.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:26pt; color:#ffffff;\">/ g / </span></p></body></html>")
        gimex_2.soundname.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:26pt; color:#ffffff;\">Sound  / g / </span></p></body></html>")
        gimex_3.wordname.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:26pt; color:#ffffff;\">/ g / </span></p></body></html>")
        gimex_3.soundname.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:26pt; color:#ffffff;\">Sound  / g / </span></p></body></html>")

        gimex.B1.setText ("??????")
        gimex.B2.setText ("??????")
        gimex.wordsoundb1.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\??????.mp3")))
        gimex.wordsoundb2.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\??????.mp3")))

        gimex_2.B1.setText("??????")
        gimex_2.B2.setText("??????")
        gimex_2.wordsoundb1.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\??????.mp3")))
        gimex_2.wordsoundb2.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\??????.mp3")))

        gimex_3.B1.setText("??????")
        gimex_3.B2.setText("??????")
        gimex_3.wordsoundb1.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\??????.mp3")))
        gimex_3.wordsoundb2.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\??????.mp3")))

        #images
        gimex.label_5.setPixmap(QPixmap(r"E:\graduation project\application\images\??????.jpg"))
        gimex.label_5.setScaledContents(True)
        gimex.label_4.setPixmap(QPixmap(r"E:\graduation project\application\images\??????.JPG"))
        gimex.label_4.setScaledContents(True)

        gimex_2.label_5.setPixmap(QPixmap(r"E:\graduation project\application\images\??????.JPG"))
        gimex_2.label_5.setScaledContents(True)
        gimex_2.label_4.setPixmap(QPixmap(r"E:\graduation project\application\images\??????.jpg"))
        gimex_2.label_4.setScaledContents(True)

        gimex_3.label_5.setPixmap(QPixmap(r"E:\graduation project\application\images\??????.jpg"))
        gimex_3.label_5.setScaledContents(True)
        gimex_3.label_4.setPixmap(QPixmap(r"E:\graduation project\application\images\??????.jpg"))
        gimex_3.label_4.setScaledContents(True)

        widgets_to_add = [g, gword1, gword2, gword3, gword4, gword7, gword8, gword9, gimex, gimex_2, gimex_3, cong]

        #widgets arrangment 
        if first_element_index is None:
            
            for x in widgets_to_add: 
                my_add_widget(w=widget, w_widget_stack=widget_stack, w_to_add=x)

        else:
            for i,x in enumerate(widgets_to_add): 
                my_add_widget(w=widget, w_widget_stack=widget_stack, w_to_add=x, index_to_insert_at= first_element_index +i )

        widget.setCurrentWidget(widgets_to_add[0])    
    def T(self):
        global widget_stack
        global widget

        if len(widget_stack) >0:
            first_element_index = get_index_of_widget(w=widget, w_widget_to_get_index_for=widget_stack[0])
        else:
            first_element_index = None

        len_widget_stack = len(widget_stack)
        for i in range(len_widget_stack):
            widget, widget_stack = remove_last_widget(w=widget, w_widget_stack=widget_stack)

        
        T=soundform()
        
        T.label_2.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\soundvideo\T (2).mp4")))
        T.tips.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">1. /\u1e6d/ involves </span><span style=\" font-size:14pt; color:#00c37a;\">two</span><span style=\" font-size:14pt;\"> movements happen at the </span><span style=\" font-size:14pt; color:#00c37a;\">same</span><span style=\" font-size:14pt;\"><br/>time to be pronounced properly: </span></p></body></html>", None))
        T.tips_2.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\"><span style=\" font-family:'Calibri','sans-serif'; font-size:14pt;\">2. The first is raising the</span><span style=\" font-family:'Calibri','sans-serif'; font-size:14pt; color:#00c37a;\"> tip of your tongue</span><span style=\" font-family:'Calibri','sans-serif'; font-size:14pt;\"> to be in<br/>touch with the </span><span style=\" font-family:'Calibri','sans-serif'; font-size:14pt; color:#00c37a;\">alveolar ridge </span><span style=\" font-family:'Calibri','sans-serif'; font-size:14pt;\">(check the figure<br/>illustrated earlier) and </span><span style=\" font-family:'Calibri','sans-serif'; font-size:14pt; color:#00c37a;\">block</span><span style=\" font-family:'Calibri','sans-serif'; font-size:14pt;\"> the airstream.</span></p></body></html>", None))
        T.tips_3.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">3. The second is raising the </span><span style=\" font-size:14pt; color:#00c37a;\">back of your tongue </span><span style=\" font-size:14pt;\"><br/>without touching the </span><span style=\" font-size:14pt; color:#00c37a;\">roof of your mouth</span><span style=\" font-size:14pt;\">. <br/>Then </span><span style=\" font-size:14pt; color:#00c37a;\">release</span><span style=\" font-size:14pt;\"> the blocked airstream. </span></p></body></html>", None))
        T.tips_4.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">4. /\u1e6d/ is pronounced like a </span><span style=\" font-size:14pt; color:#00c37a;\">/t/</span><span style=\" font-size:14pt;\"> but with the back of <br/>your tongue raised towards the roof of your <br/>mouth </span><span style=\" font-size:14pt; color:#00c37a;\">without</span><span style=\" font-size:14pt;\"> being in contact with it. </span></p></body></html>", None))

        #instances
        Tword1=wordform()
        Tword2=wordform()
        Tword3=wordform()
        Tword4=wordform()
        Tword5=wordform()
        Tword6=wordform()
        Tword7=wordform()
        Tword8=wordform()
        Tword9=wordform()
        
        #words
        Tword1.wordlable.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\">    <span style=\" font-size:20pt; color:#ee5445;\">????</span><span style=\" font-size:20pt; color:#000000;\">????</span>   <span style=\" font-size:20pt; color:#000000;\">    Child</span>     </p><p align=\"center\"><br/></p>  </body></html>",None))
        Tword2.wordlable.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\">    <span style=\" font-size:20pt; color:#ee5445;\">????</span><span style=\" font-size:20pt; color:#000000;\">??????</span>   <span style=\" font-size:20pt; color:#000000;\">    Street</span>     </p><p align=\"center\"><br/></p>  </body></html>",None))
        Tword3.wordlable.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\">    <span style=\" font-size:20pt; color:#ee5445;\">????</span><span style=\" font-size:20pt; color:#000000;\">????</span>   <span style=\" font-size:20pt; color:#000000;\">    Mud</span>     </p><p align=\"center\"><br/></p>  </body></html>",None))
        Tword4.wordlable.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\">   <span style=\" font-size:20pt; color:#000000;\">????</span><span style=\" font-size:20pt; color:#ee5445;\">??????</span><span style=\" font-size:20pt; color:#000000;\">??</span>         <span style=\" font-size:20pt; color:#000000;\">   Line </span>       </p><p align=\"center\"><br/></p>   </body></html>",None))
        Tword5.wordlable.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\">   <span style=\" font-size:20pt; color:#000000;\">????</span><span style=\" font-size:20pt; color:#ee5445;\">??????</span><span style=\" font-size:20pt; color:#000000;\">????</span>         <span style=\" font-size:20pt; color:#000000;\">   Train </span>       </p><p align=\"center\"><br/></p>   </body></html>",None))
        Tword6.wordlable.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\">   <span style=\" font-size:20pt; color:#000000;\">????</span><span style=\" font-size:20pt; color:#ee5445;\">??????</span><span style=\" font-size:20pt; color:#000000;\">??</span>         <span style=\" font-size:20pt; color:#000000;\">   Rain </span>       </p><p align=\"center\"><br/></p>   </body></html>",None))
        Tword7.wordlable.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\">   <span style=\" font-size:20pt; color:#000000;\">????</span><span style=\" font-size:20pt; color:#ee5445;\">??????</span><span style=\" font-size:20pt; color:#000000;\">????</span>         <span style=\" font-size:20pt; color:#000000;\">   Duck </span>       </p><p align=\"center\"><br/></p>   </body></html>",None))
        Tword8.wordlable.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; color:#000000;\">??????</span><span style=\" font-size:20pt; color:#ee5445;\">??</span><span style=\" font-size:20pt; color:#000000;\">   String </span></p><p align=\"center\"><br/></p></body></html>",None))
        Tword9.wordlable.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; color:#000000;\">????????</span><span style=\" font-size:20pt; color:#ee5445;\">??</span><span style=\" font-size:20pt; color:#000000;\">   Ocean </span></p><p align=\"center\"><br/></p></body></html>",None))

        #images
        Tword1.image.setPixmap(QPixmap(r"E:\graduation project\application\images\??????.JPG"))
        Tword1.image.setScaledContents(True)
        Tword2.image.setPixmap(QPixmap(r"E:\graduation project\application\images\????????.JPG"))
        Tword2.image.setScaledContents(True)
        Tword3.image.setPixmap(QPixmap(r"E:\graduation project\application\images\??????.JPG"))
        Tword3.image.setScaledContents(True)
        Tword4.image.setPixmap(QPixmap(r"E:\graduation project\application\images\??????.png"))
        Tword4.image.setScaledContents(True)
        Tword5.image.setPixmap(QPixmap(r"E:\graduation project\application\images\??????.jfif"))
        Tword5.image.setScaledContents(True)
        Tword6.image.setPixmap(QPixmap(r"E:\graduation project\application\images\??????.JPG"))
        Tword6.image.setScaledContents(True)
        Tword7.image.setPixmap(QPixmap(r"E:\graduation project\application\images\??????.JPG"))
        Tword7.image.setScaledContents(True)
        Tword8.image.setPixmap(QPixmap(r"E:\graduation project\application\images\??????.JPG"))
        Tword8.image.setScaledContents(True)
        Tword9.image.setPixmap(QPixmap(r"E:\graduation project\application\images\????????.JPG"))
        Tword9.image.setScaledContents(True)

        #audios
        Tword1.wordsound.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\??????.mp3")))
        Tword2.wordsound.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\????????.mp3")))
        Tword3.wordsound.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\??????.mp3")))
        Tword4.wordsound.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\??????.mp3")))
        Tword5.wordsound.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\??????.mp3")))
        Tword6.wordsound.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\??????.mp3")))
        Tword7.wordsound.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\??????.mp3")))
        Tword8.wordsound.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\??????.mp3")))
        Tword9.wordsound.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\????????.mp3")))

        #exercises
        Tex=ex_2()
        Tex_2=ex_2()
        Tex_3=ex()
        cong=congrat()
        
        Tex.wordname.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:26pt; color:#ffffff;\">/???/ </span></p></body></html>")
        Tex.soundname.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:26pt; color:#ffffff;\">Sound /???/  </span></p></body></html>")
        Tex_2.wordname.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:26pt; color:#ffffff;\">/???/</span></p></body></html>")
        Tex_2.soundname.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:26pt; color:#ffffff;\"> Sound /???/ </span></p></body></html>")
        Tex_3.wordname.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:26pt; color:#ffffff;\">/???/ </span></p></body></html>")
        Tex_3.soundname.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:26pt; color:#ffffff;\">Sound /???/  </span></p></body></html>")

        Tex.B1.setText ("??????")
        Tex.B2.setText ("??????")
        Tex.wordsoundb1.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\??????.mp3")))
        Tex.wordsoundb2.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\??????.mp3")))


        Tex_2.B1.setText("????????")
        Tex_2.B2.setText("????????")
        Tex_2.wordsoundb1.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\????????.mp3")))
        Tex_2.wordsoundb2.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\????????.mp3")))

        Tex_3.B1.setText("??????")
        Tex_3.B2.setText("??????")
        Tex_3.wordsoundb1.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\??????.mp3")))
        Tex_3.wordsoundb2.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\??????.mp3")))

        #images
        Tex.label_5.setPixmap(QPixmap(r"E:\graduation project\application\images\??????.jpg"))
        Tex.label_5.setScaledContents(True)
        Tex.label_4.setPixmap(QPixmap(r"E:\graduation project\application\images\??????.JPG"))
        Tex.label_4.setScaledContents(True)
        Tex_2.label_5.setPixmap(QPixmap(r"E:\graduation project\application\images\????????.JPG"))
        Tex_2.label_5.setScaledContents(True)
        Tex_2.label_4.setPixmap(QPixmap(r"E:\graduation project\application\images\????????.jpg"))
        Tex_2.label_4.setScaledContents(True)
        Tex_3.label_5.setPixmap(QPixmap(r"E:\graduation project\application\images\??????.jpg"))
        Tex_3.label_5.setScaledContents(True)
        Tex_3.label_4.setPixmap(QPixmap(r"E:\graduation project\application\images\??????.jfif"))
        Tex_3.label_4.setScaledContents(True)
        widgets_to_add = [T, Tword1, Tword2, Tword3, Tword4, Tword5, Tword6, Tword7, Tword8, Tword9, Tex, Tex_2, Tex_3, cong]

        #widgets arrangment 
        if first_element_index is None:
            
            for x in widgets_to_add: 
                my_add_widget(w=widget, w_widget_stack=widget_stack, w_to_add=x)

        else:
            for i,x in enumerate(widgets_to_add): 
                my_add_widget(w=widget, w_widget_stack=widget_stack, w_to_add=x, index_to_insert_at= first_element_index +i )

    
        widget.setCurrentWidget(widgets_to_add[0])    
    def D(self):
        global widget_stack
        global widget

        if len(widget_stack) >0:
            first_element_index = get_index_of_widget(w=widget, w_widget_to_get_index_for=widget_stack[0])
        else:
            first_element_index = None

        len_widget_stack = len(widget_stack)
        for i in range(len_widget_stack):
            widget, widget_stack = remove_last_widget(w=widget, w_widget_stack=widget_stack)

        
        D=soundform()
        
        D.label_2.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\soundvideo\D (2).mp4")))
        D.tips.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">1. Place the </span><span style=\" font-size:14pt; color:#00c37a;\">tip of your tongue</span><span style=\" font-size:14pt;\"> to be in contact <br/>with the same position of the sound /t/ which is <br/>the </span><span style=\" font-size:14pt; color:#00c37a;\">alveolar ridge</span><span style=\" font-size:14pt;\">. </span></p></body></html>", None))
        D.tips_2.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">2. Press the </span><span style=\" font-size:14pt; color:#00c37a;\">sides</span><span style=\" font-size:14pt;\"> of your tongue to the </span><span style=\" font-size:14pt; color:#00c37a;\">roof</span><span style=\" font-size:14pt;\"> of <br/>your mouth and </span><span style=\" font-size:14pt; color:#00c37a;\">stop</span><span style=\" font-size:14pt;\"> the airstream from passing. </span></p></body></html>", None))
        D.tips_3.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">3. Raise the </span><span style=\" font-size:14pt; color:#00c37a;\">back</span><span style=\" font-size:14pt;\"> of your tongue towards the </span><span style=\" font-size:14pt; color:#00c37a;\">roof <br/></span><span style=\" font-size:14pt;\">of your mouth </span><span style=\" font-size:14pt; color:#00c37a;\">without</span><span style=\" font-size:14pt;\"> touching it. </span></p></body></html>", None))
        D.tips_4.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">4. then </span><span style=\" font-size:14pt; color:#00c37a;\">release</span><span style=\" font-size:14pt;\"> the air stream while </span><span style=\" font-size:14pt; color:#00c37a;\">vibrating</span><span style=\" font-size:14pt;\"> your <br/>vocal cords.To feel the vibration of your vocal cords <br/>place your hand on your </span><span style=\" font-size:14pt; color:#00c37a;\">throat</span><span style=\" font-size:14pt;\"> and pronounce </span><span style=\" font-size:14pt; color:#ee5445;\">/n/</span><span style=\" font-size:14pt;\">. </span></p></body></html>", None))
        #instances
        Dword1=wordform()
        Dword2=wordform()
        Dword3=wordform()
        Dword4=wordform()
        Dword5=wordform()
        Dword6=wordform()
        Dword7=wordform()
        Dword8=wordform()
        
        #words
        Dword1.wordlable.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\">    <span style=\" font-size:20pt; color:#ee5445;\">????</span><span style=\" font-size:20pt; color:#000000;\">??????</span>   <span style=\" font-size:20pt; color:#000000;\">    Pressure</span>     </p><p align=\"center\"><br/></p>  </body></html>",None))
        Dword2.wordlable.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\">    <span style=\" font-size:20pt; color:#ee5445;\">????</span><span style=\" font-size:20pt; color:#000000;\">????</span>   <span style=\" font-size:20pt; color:#000000;\">    Hit</span>     </p><p align=\"center\"><br/></p>  </body></html>",None))
        Dword3.wordlable.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\">   <span style=\" font-size:20pt; color:#000000;\">????</span><span style=\" font-size:20pt; color:#ee5445;\">????</span><span style=\" font-size:20pt; color:#000000;\">????</span>   <span style=\" font-size:20pt; color:#000000;\"> vegetable </span>     </p><p align=\"center\"><br/></p>  </body></html>",None))
        Dword4.wordlable.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\">   <span style=\" font-size:20pt; color:#000000;\">????</span><span style=\" font-size:20pt; color:#ee5445;\">??????</span><span style=\" font-size:20pt; color:#000000;\">??</span>         <span style=\" font-size:20pt; color:#000000;\">   Favor </span>       </p><p align=\"center\"><br/></p>   </body></html>",None))
        Dword5.wordlable.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\">   <span style=\" font-size:20pt; color:#000000;\">????</span><span style=\" font-size:20pt; color:#ee5445;\">??????</span><span style=\" font-size:20pt; color:#000000;\">??</span>         <span style=\" font-size:20pt; color:#000000;\">   Bone </span>       </p><p align=\"center\"><br/></p>   </body></html>",None))
        Dword6.wordlable.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; color:#000000;\">??????</span><span style=\" font-size:20pt; color:#ee5445;\">??</span><span style=\" font-size:20pt; color:#000000;\">   Eggs </span></p><p align=\"center\"><br/></p></body></html>",None))
        Dword7.wordlable.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; color:#000000;\">????</span><span style=\" font-size:20pt; color:#ee5445;\">??</span><span style=\" font-size:20pt; color:#000000;\">   Land </span></p><p align=\"center\"><br/></p></body></html>",None))
        Dword8.wordlable.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; color:#000000;\">????</span><span style=\" font-size:20pt; color:#ee5445;\">??</span><span style=\" font-size:20pt; color:#000000;\">   Illness </span></p><p align=\"center\"><br/></p></body></html>",None))
        #images
        Dword1.image.setPixmap(QPixmap(r"E:\graduation project\application\images\??????.JPG"))
        Dword1.image.setScaledContents(True)
        Dword2.image.setPixmap(QPixmap(r"E:\graduation project\application\images\??????.JPG"))
        Dword2.image.setScaledContents(True)
        Dword3.image.setPixmap(QPixmap(r"E:\graduation project\application\images\????????.jfif"))
        Dword3.image.setScaledContents(True)
        Dword4.image.setPixmap(QPixmap(r"E:\graduation project\application\images\??????.jfif"))
        Dword4.image.setScaledContents(True)
        Dword5.image.setPixmap(QPixmap(r"E:\graduation project\application\images\??????.JPG"))
        Dword5.image.setScaledContents(True)
        Dword6.image.setPixmap(QPixmap(r"E:\graduation project\application\images\??????.JPG"))
        Dword6.image.setScaledContents(True)
        Dword7.image.setPixmap(QPixmap(r"E:\graduation project\application\images\??????.JPG"))
        Dword7.image.setScaledContents(True)
        Dword8.image.setPixmap(QPixmap(r"E:\graduation project\application\images\??????.JPG"))
        Dword8.image.setScaledContents(True)
        #Audios
        Dword1.wordsound.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\??????.mp3")))
        Dword2.wordsound.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\??????.mp3")))
        Dword3.wordsound.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\????????.mp3")))
        Dword4.wordsound.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\??????.mp3")))
        Dword5.wordsound.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\??????.mp3")))
        Dword6.wordsound.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\??????.mp3")))
        Dword7.wordsound.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\??????.mp3")))
        Dword8.wordsound.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\??????.mp3")))


        #exercises
        Dex=ex_2()
        Dex_2=ex_2()
        Dex_3=ex()
        cong=congrat()
        
        Dex.wordname.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:26pt; color:#ffffff;\">/???/</span></p></body></html>")
        Dex.soundname.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:26pt; color:#ffffff;\">Sound  /???/ </span></p></body></html>")
        Dex_2.wordname.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:26pt; color:#ffffff;\">/???/</span></p></body></html>")
        Dex_2.soundname.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:26pt; color:#ffffff;\">Sound  /???/ </span></p></body></html>")
        Dex_3.wordname.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:26pt; color:#ffffff;\">/???/</span></p></body></html>")
        Dex_3.soundname.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:26pt; color:#ffffff;\">Sound  /???/ </span></p></body></html>")

        Dex.B1.setText ("??????")
        Dex.B2.setText ("??????")
        Dex.wordsoundb1.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\??????.mp3")))
        Dex.wordsoundb2.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\??????.mp3")))

        Dex_2.B1.setText("??????")
        Dex_2.B2.setText("??????")
        Dex_2.wordsoundb1.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\??????.mp3")))
        Dex_2.wordsoundb2.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\??????.mp3")))

        Dex_3.B1.setText("??????")
        Dex_3.B2.setText("????????")
        Dex_3.wordsoundb1.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\??????.mp3")))
        Dex_3.wordsoundb2.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\????????.mp3")))

        #images
        Dex.label_5.setPixmap(QPixmap(r"E:\graduation project\application\images\??????.jfif"))
        Dex.label_5.setScaledContents(True)
        Dex.label_4.setPixmap(QPixmap(r"E:\graduation project\application\images\??????.JPG"))
        Dex.label_4.setScaledContents(True)

        Dex_2.label_5.setPixmap(QPixmap(r"E:\graduation project\application\images\??????.jpg"))
        Dex_2.label_5.setScaledContents(True)
        Dex_2.label_4.setPixmap(QPixmap(r"E:\graduation project\application\images\??????.jfif"))
        Dex_2.label_4.setScaledContents(True)

        Dex_3.label_5.setPixmap(QPixmap(r"E:\graduation project\application\images\??????.jpg"))
        Dex_3.label_5.setScaledContents(True)
        Dex_3.label_4.setPixmap(QPixmap(r"E:\graduation project\application\images\????????.png"))
        Dex_3.label_4.setScaledContents(True)

        widgets_to_add = [D, Dword1, Dword2, Dword3, Dword4, Dword5, Dword6, Dword7, Dword8, Dex, Dex_2, Dex_3, cong]

        #widgets arrangment 
        if first_element_index is None:
            
            for x in widgets_to_add: 
                my_add_widget(w=widget, w_widget_stack=widget_stack, w_to_add=x)

        else:
            for i,x in enumerate(widgets_to_add): 
                my_add_widget(w=widget, w_widget_stack=widget_stack, w_to_add=x, index_to_insert_at= first_element_index +i )

    
        widget.setCurrentWidget(widgets_to_add[0])   
    def S(self):
        global widget_stack
        global widget

        if len(widget_stack) >0:
            first_element_index = get_index_of_widget(w=widget, w_widget_to_get_index_for=widget_stack[0])
        else:
            first_element_index = None

        len_widget_stack = len(widget_stack)
        for i in range(len_widget_stack):
            widget, widget_stack = remove_last_widget(w=widget, w_widget_stack=widget_stack)

        
        S=soundform()
        
        S.label_2.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\soundvideo\S (2).mp4")))
        S.tips.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">1. Take the </span><span style=\" font-size:14pt; color:#00c37a;\">tip</span><span style=\" font-size:14pt;\"> of your tongue </span><span style=\" font-size:14pt; color:#00c37a;\">downwards</span><span style=\" font-size:14pt;\"> behind <br/>your lower front teeth.</span></p></body></html>", None))
        S.tips_2.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">2. Raise the </span><span style=\" font-size:14pt; color:#00c37a;\">back</span><span style=\" font-size:14pt;\"> of your tongue towards the </span><span style=\" font-size:14pt; color:#00c37a;\">roof</span><span style=\" font-size:14pt;\"><br/>of your mouth but not in touch with it, with your <br/></span><span style=\" font-size:14pt; color:#00c37a;\">lips</span><span style=\" font-size:14pt;\"> taking the shape of an </span><span style=\" font-size:14pt; color:#00c37a;\">\u2018O\u2019 </span><span style=\" font-size:14pt;\">.</span></p></body></html>", None))
        S.tips_3.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">3. </span><span style=\" font-size:14pt; color:#00c37a;\">Push</span><span style=\" font-size:14pt;\"> air and the resulting </span><span style=\" font-size:14pt; color:#00c37a;\">friction</span><span style=\" font-size:14pt;\"> will create<br/>the sound.</span></p></body></html>", None))
        S.tips_4.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">4. It is like</span><span style=\" font-size:14pt; color:#ee5445;\"> /s/</span><span style=\" font-size:14pt;\"> sound but </span><span style=\" font-size:14pt; color:#00c37a;\">heavier</span><span style=\" font-size:14pt;\"> because you </span><span style=\" font-size:14pt; color:#000000;\">raise</span><span style=\" font-size:14pt;\"><br/>the </span><span style=\" font-size:14pt; color:#00c37a;\">back or your tongue</span><span style=\" font-size:14pt;\">.</span></p></body></html>", None))
    
        #instances
        Sword1=wordform()
        Sword2=wordform()
        Sword3=wordform()
        Sword4=wordform()
        Sword5=wordform()
        Sword6=wordform()
        Sword7=wordform()
        Sword8=wordform()
        
        #words
        Sword1.wordlable.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\">    <span style=\" font-size:20pt; color:#ee5445;\">????</span><span style=\" font-size:20pt; color:#000000;\">??????</span>   <span style=\" font-size:20pt; color:#000000;\">     Image</span>     </p><p align=\"center\"><br/></p>  </body></html>",None))
        Sword2.wordlable.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\">    <span style=\" font-size:20pt; color:#ee5445;\">????</span><span style=\" font-size:20pt; color:#000000;\">????</span>   <span style=\" font-size:20pt; color:#000000;\">    Summer</span>     </p><p align=\"center\"><br/></p>  </body></html>",None))
        Sword3.wordlable.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\">    <span style=\" font-size:20pt; color:#ee5445;\">????</span><span style=\" font-size:20pt; color:#000000;\">????</span>   <span style=\" font-size:20pt; color:#000000;\">    Patience</span>     </p><p align=\"center\"><br/></p>  </body></html>",None))
        Sword4.wordlable.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\">   <span style=\" font-size:20pt; color:#000000;\">????</span><span style=\" font-size:20pt; color:#ee5445;\">??????</span><span style=\" font-size:20pt; color:#000000;\">??</span>         <span style=\" font-size:20pt; color:#000000;\">   Chapter </span>       </p><p align=\"center\"><br/></p>   </body></html>",None))
        Sword5.wordlable.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\">   <span style=\" font-size:20pt; color:#000000;\">????</span><span style=\" font-size:20pt; color:#ee5445;\">??????</span><span style=\" font-size:20pt; color:#000000;\">??</span>         <span style=\" font-size:20pt; color:#000000;\">   Egypt </span>       </p><p align=\"center\"><br/></p>   </body></html>",None))
        Sword6.wordlable.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; color:#000000;\">??????</span><span style=\" font-size:20pt; color:#ee5445;\">??</span><span style=\" font-size:20pt; color:#000000;\">   Cage </span></p><p align=\"center\"><br/></p></body></html>",None))
        Sword7.wordlable.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; color:#000000;\">??????</span><span style=\" font-size:20pt; color:#ee5445;\">??</span><span style=\" font-size:20pt; color:#000000;\">   scissors </span></p><p align=\"center\"><br/></p></body></html>",None))
        Sword8.wordlable.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; color:#000000;\">??????</span><span style=\" font-size:20pt; color:#ee5445;\">??</span><span style=\" font-size:20pt; color:#000000;\">   Dance </span></p><p align=\"center\"><br/></p></body></html>",None))
        #images
        Sword1.image.setPixmap(QPixmap(r"E:\graduation project\application\images\????????.png"))
        Sword1.image.setScaledContents(True)
        Sword2.image.setPixmap(QPixmap(r"E:\graduation project\application\images\??????.JPG"))
        Sword2.image.setScaledContents(True)
        Sword3.image.setPixmap(QPixmap(r"E:\graduation project\application\images\??????.JPG"))
        Sword3.image.setScaledContents(True)
        Sword4.image.setPixmap(QPixmap(r"E:\graduation project\application\images\??????.jpg"))
        Sword4.image.setScaledContents(True)
        Sword5.image.setPixmap(QPixmap(r"E:\graduation project\application\images\??????.JPG"))
        Sword5.image.setScaledContents(True)
        Sword6.image.setPixmap(QPixmap(r"E:\graduation project\application\images\??????.JPG"))
        Sword6.image.setScaledContents(True)
        Sword7.image.setPixmap(QPixmap(r"E:\graduation project\application\images\??????.JPG"))
        Sword7.image.setScaledContents(True)
        Sword8.image.setPixmap(QPixmap(r"E:\graduation project\application\images\??????.JPG"))
        Sword8.image.setScaledContents(True)
        #audios
        Sword1.wordsound.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\????????.mp3")))
        Sword2.wordsound.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\??????.mp3")))
        Sword3.wordsound.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\??????.mp3")))
        Sword4.wordsound.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\??????.mp3")))
        Sword5.wordsound.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\??????.mp3")))
        Sword6.wordsound.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\??????.mp3")))
        Sword7.wordsound.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\??????.mp3")))
        Sword8.wordsound.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\??????.mp3")))

        #exercises
        S_ex=ex_2()
        S_ex_2=ex()
        S_ex_3=ex_2()
        cong=congrat()
        
        S_ex.wordname.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:26pt; color:#ffffff;\">/S/</span></p></body></html>")
        S_ex.soundname.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:26pt; color:#ffffff;\">Sound /S/</span></p></body></html>")
        S_ex_2.wordname.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:26pt; color:#ffffff;\">/S/</span></p></body></html>")
        S_ex_2.soundname.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:26pt; color:#ffffff;\">Sound /S/</span></p></body></html>")
        S_ex_3.wordname.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:26pt; color:#ffffff;\">/S/</span></p></body></html>")
        S_ex_3.soundname.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:26pt; color:#ffffff;\">Sound /S/</span></p></body></html>")

        S_ex.B1.setText ("??????")
        S_ex.B2.setText ("??????")
        S_ex.wordsoundb1.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\??????.mp3")))
        S_ex.wordsoundb2.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\??????.mp3")))
        S_ex_2.B1.setText("??????")
        S_ex_2.B2.setText("????????")
        S_ex_2.wordsoundb1.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\??????.mp3")))
        S_ex_2.wordsoundb2.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\????????.mp3")))
        S_ex_3.B2.setText("??????")
        S_ex_3.B1.setText("??????")
        S_ex_3.wordsoundb2.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\??????.mp3")))
        S_ex_3.wordsoundb1.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\??????.m4a")))

        #images
        S_ex.label_5.setPixmap(QPixmap(r"E:\graduation project\application\images\??????.jpg"))
        S_ex.label_5.setScaledContents(True)
        S_ex.label_4.setPixmap(QPixmap(r"E:\graduation project\application\images\??????.JPG"))
        S_ex.label_4.setScaledContents(True)

        S_ex_2.label_5.setPixmap(QPixmap(r"E:\graduation project\application\images\??????.jpg"))
        S_ex_2.label_5.setScaledContents(True)
        S_ex_2.label_4.setPixmap(QPixmap(r"E:\graduation project\application\images\????????.JPG"))
        S_ex_2.label_4.setScaledContents(True)

        S_ex_3.label_5.setPixmap(QPixmap(r"E:\graduation project\application\images\??????.jpg"))
        S_ex_3.label_5.setScaledContents(True)
        S_ex_3.label_4.setPixmap(QPixmap(r"E:\graduation project\application\images\??????.jpg"))
        S_ex_3.label_4.setScaledContents(True)

    
        widgets_to_add = [S, Sword1, Sword2, Sword3, Sword4, Sword5, Sword6, Sword7, Sword8, S_ex, S_ex_2, S_ex_3, cong]

        #widgets arrangment 
        if first_element_index is None:
            
            for x in widgets_to_add: 
                my_add_widget(w=widget, w_widget_stack=widget_stack, w_to_add=x)

        else:
            for i,x in enumerate(widgets_to_add): 
                my_add_widget(w=widget, w_widget_stack=widget_stack, w_to_add=x, index_to_insert_at= first_element_index +i )

    
        widget.setCurrentWidget(widgets_to_add[0])    
    def Z(self):
        global widget_stack
        global widget

        if len(widget_stack) >0:
            first_element_index = get_index_of_widget(w=widget, w_widget_to_get_index_for=widget_stack[0])
        else:
            first_element_index = None

        len_widget_stack = len(widget_stack)
        for i in range(len_widget_stack):
            widget, widget_stack = remove_last_widget(w=widget, w_widget_stack=widget_stack)

        
        Z=soundform()
        
        Z.label_2.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\soundvideo\Z.mp4")))
        Z.tips.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\"><span style=\" font-family:'Calibri','sans-serif'; font-size:14pt; color:#000000;\">1. Place the </span><span style=\" font-family:'Calibri','sans-serif'; font-size:14pt; color:#00c37a;\">tip</span><span style=\" font-family:'Calibri','sans-serif'; font-size:14pt; color:#000000;\"> of your tongue against the </span><span style=\" font-family:'Calibri','sans-serif'; font-size:14pt; color:#00c37a;\">alveolar <br/>ridge </span><span style=\" font-family:'Calibri','sans-serif'; font-size:12pt; font-weight:600;\">(the bony part behind your upper front teeth)</span><span style=\" font-family:'Calibri','sans-serif'; font-size:14pt; font-weight:600;\">.</span></p></body></html>", None))
        Z.tips_2.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">2. At the same time, raise the </span><span style=\" font-size:14pt; color:#00c37a;\">back</span><span style=\" font-size:14pt;\"> of your tongue <br/>towards the </span><span style=\" font-size:14pt; color:#00c37a;\">roof</span><span style=\" font-size:14pt;\"> of your mouth.</span></p></body></html>", None))
        Z.tips_3.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">3. </span><span style=\" font-size:14pt; color:#00c37a;\">Spread</span><span style=\" font-size:14pt;\"> your lips like you are slightly smiling,<br/>and </span><span style=\" font-size:14pt; color:#00c37a;\">push</span><span style=\" font-size:14pt;\"> air.</span></p></body></html>", None))
        Z.tips_4.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">4. Try saying </span><span style=\" font-size:14pt; color:#ee5445;\">/s/</span><span style=\" font-size:14pt;\"> but with </span><span style=\" font-size:14pt; color:#00c37a;\">vibrating</span><span style=\" font-size:14pt;\"> your vocal <br/>cords and </span><span style=\" font-size:14pt; color:#00c37a;\">raising</span><span style=\" font-size:14pt;\"> the back of your tongue.</span></p></body></html>", None))
        #instances
        Zword1=wordform()
        Zword2=wordform()
        Zword3=wordform()
        Zword4=wordform()
        Zword5=wordform()
        
        #words 
        Zword1.wordlable.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\">    <span style=\" font-size:20pt; color:#ee5445;\">????</span><span style=\" font-size:20pt; color:#000000;\">??</span>   <span style=\" font-size:20pt; color:#000000;\">    thought </span>     </p><p align=\"center\"><br/></p>  </body></html>",None))
        Zword2.wordlable.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\">          <span style=\" font-size:20pt; color:#ee5445;\">????</span><span style=\" font-size:20pt; color:#000000;\">??????</span><span style=\" font-size:20pt; color:#000000;\">  Circumstances </span>     </p><p align=\"center\"><br/></p>  </body></html>",None))
        Zword3.wordlable.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\">   <span style=\" font-size:20pt; color:#000000;\">????</span><span style=\" font-size:20pt; color:#ee5445;\">??????</span><span style=\" font-size:20pt; color:#000000;\">??</span>         <span style=\" font-size:20pt; color:#000000;\">   Ban </span>       </p><p align=\"center\"><br/></p>   </body></html>",None))
        Zword4.wordlable.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\">   <span style=\" font-size:20pt; color:#000000;\">????</span><span style=\" font-size:20pt; color:#ee5445;\">????</span><span style=\" font-size:20pt; color:#000000;\">??</span>         <span style=\" font-size:20pt; color:#000000;\">   Employee </span>       </p><p align=\"center\"><br/></p>   </body></html>",None))
        Zword5.wordlable.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; color:#000000;\">????</span><span style=\" font-size:20pt; color:#ee5445;\">??</span><span style=\" font-size:20pt; color:#000000;\">   Luck </span></p><p align=\"center\"><br/></p></body></html>",None))
        
        #images
        Zword1.image.setPixmap(QPixmap(r"E:\graduation project\application\images\????.png"))
        Zword1.image.setScaledContents(True)
        Zword2.image.setPixmap(QPixmap(r"E:\graduation project\application\images\????????.JPG"))
        Zword2.image.setScaledContents(True)
        Zword3.image.setPixmap(QPixmap(r"E:\graduation project\application\images\??????.png"))
        Zword3.image.setScaledContents(True)
        Zword4.image.setPixmap(QPixmap(r"E:\graduation project\application\images\????????.JPG"))
        Zword4.image.setScaledContents(True)
        Zword5.image.setPixmap(QPixmap(r"E:\graduation project\application\images\????.JPG"))
        Zword5.image.setScaledContents(True)
        #Aduio
        Zword1.wordsound.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\????.mp3")))
        Zword2.wordsound.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\????????.mp3")))
        Zword3.wordsound.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\??????.mp3")))
        Zword4.wordsound.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\????????.mp3")))
        Zword5.wordsound.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\????.mp3")))

        #exercises
        Z_ex=ex_2()
        Z_ex_2=ex_2()
        Z_ex_3=ex()
        cong=congrat()
        
        Z_ex.wordname.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:26pt; color:#ffffff;\"> /Z/ </span></p></body></html>")
        Z_ex.soundname.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:26pt; color:#ffffff;\"> sound /Z/</span></p></body></html>")
        Z_ex_2.wordname.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:26pt; color:#ffffff;\"> /Z/ </span></p></body></html>")
        Z_ex_2.soundname.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:26pt; color:#ffffff;\"> sound /Z/</span></p></body></html>")
        Z_ex_3.wordname.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:26pt; color:#ffffff;\"> /Z/ </span></p></body></html>")
        Z_ex_3.soundname.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:26pt; color:#ffffff;\"> sound /Z/</span></p></body></html>")

        Z_ex.B1.setText ("????????")
        Z_ex.B2.setText ("????")
        Z_ex.wordsoundb1.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\????????.mp3")))
        Z_ex.wordsoundb2.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\????.mp3")))

        Z_ex_2.B1.setText("????")
        Z_ex_2.B2.setText("??????")
        Z_ex_2.wordsoundb1.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\????.m4a")))
        Z_ex_2.wordsoundb2.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\??????.mp3")))
        Z_ex_3.B1.setText("????????")
        Z_ex_3.B2.setText("????????")
        Z_ex_3.wordsoundb1.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\????????.mp3")))
        Z_ex_3.wordsoundb2.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\????????.mp3")))

        #images
        Z_ex.label_5.setPixmap(QPixmap(r"E:\graduation project\application\images\????????.jpg"))
        Z_ex.label_5.setScaledContents(True)
        Z_ex.label_4.setPixmap(QPixmap(r"E:\graduation project\application\images\????.png"))
        Z_ex.label_4.setScaledContents(True)

        Z_ex_2.label_5.setPixmap(QPixmap(r"E:\graduation project\application\images\????.JPG"))
        Z_ex_2.label_5.setScaledContents(True)
        Z_ex_2.label_4.setPixmap(QPixmap(r"E:\graduation project\application\images\??????.png"))
        Z_ex_2.label_4.setScaledContents(True)

        Z_ex_3.label_5.setPixmap(QPixmap(r"E:\graduation project\application\images\????????.jpg"))
        Z_ex_3.label_5.setScaledContents(True)
        Z_ex_3.label_4.setPixmap(QPixmap(r"E:\graduation project\application\images\????????.jfif"))
        Z_ex_3.label_4.setScaledContents(True)

        widgets_to_add = [Z, Zword1, Zword2, Zword3, Zword4, Zword5, Z_ex, Z_ex_2, Z_ex_3, cong]

        #widgets arrangment 
        if first_element_index is None:
            
            for x in widgets_to_add: 
                my_add_widget(w=widget, w_widget_stack=widget_stack, w_to_add=x)

        else:
            for i,x in enumerate(widgets_to_add): 
                my_add_widget(w=widget, w_widget_stack=widget_stack, w_to_add=x, index_to_insert_at= first_element_index +i )

    
        widget.setCurrentWidget(widgets_to_add[0])   
    def r(self):
        global widget_stack
        global widget

        if len(widget_stack) >0:
            first_element_index = get_index_of_widget(w=widget, w_widget_to_get_index_for=widget_stack[0])
        else:
            first_element_index = None

        len_widget_stack = len(widget_stack)
        for i in range(len_widget_stack):
            widget, widget_stack = remove_last_widget(w=widget, w_widget_stack=widget_stack)

        
        r=soundform()
        
        r.label_2.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\soundvideo\r.mp4")))
        r.tips.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">1. Train your tongue in front of a mirror by lifting it<br/>up and down </span><span style=\" font-size:14pt; color:#00c37a;\">behind your teeth</span><span style=\" font-size:14pt;\"> so you get <br/>used to the </span><span style=\" font-size:14pt; color:#00c37a;\">position</span><span style=\" font-size:14pt;\"> of your tongue.</span></p></body></html>", None))
        r.tips_2.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt;\">2. it is also similar to the </span><span style=\" font-size:16pt; color:#00c37a;\">position</span><span style=\" font-size:16pt;\"> of tongue<br/>in the </span><span style=\" font-size:16pt; color:#00c37a;\">/n/</span><span style=\" font-size:16pt;\"> sound.</span></p></body></html>", None))
        r.tips_3.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">3. loosely touch your </span><span style=\" font-size:14pt; color:#00c37a;\">alveolar ridge</span><span style=\" font-size:14pt;\"> (</span><span style=\" font-size:14pt; color:#ee5445;\">the bony part <br/>behind your upper front teeth</span><span style=\" font-size:14pt;\">) with the <br/></span><span style=\" font-size:14pt; color:#00c37a;\">tip of your tongue </span><span style=\" font-size:14pt;\">without pressing it.</span></p></body></html>", None))
        r.tips_4.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">4. Keep your tongue as </span><span style=\" font-size:14pt; color:#00c37a;\">flat as possible</span><span style=\" font-size:14pt;\"> and relaxed.<br/>Force </span><span style=\" font-size:14pt; color:#00c37a;\">air from above</span><span style=\" font-size:14pt;\"> your tongue and let the <br/>passing air</span><span style=\" font-size:14pt; color:#00c37a;\"> flap</span><span style=\" font-size:14pt;\"> it. </span></p></body></html>", None))
        #instances
        rword1=wordform()
        rword2=wordform()
        rword3=wordform()
        rword4=wordform()
        rword5=wordform()
        rword6=wordform()
        rword7=wordform()
        rword8=wordform()
        rword9=wordform()

        #words
        rword1.wordlable.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\">    <span style=\" font-size:20pt; color:#ee5445;\">??</span><span style=\" font-size:20pt; color:#000000;\">??????</span>   <span style=\" font-size:20pt; color:#000000;\">    Feather </span>     </p><p align=\"center\"><br/></p>  </body></html>",None))
        rword2.wordlable.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\">    <span style=\" font-size:20pt; color:#ee5445;\">??</span><span style=\" font-size:20pt; color:#000000;\">??????</span>   <span style=\" font-size:20pt; color:#000000;\">    Pomegranate </span>     </p><p align=\"center\"><br/></p>  </body></html>",None))
        rword3.wordlable.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\">    <span style=\" font-size:20pt; color:#ee5445;\">??</span><span style=\" font-size:20pt; color:#000000;\">????</span>   <span style=\" font-size:20pt; color:#000000;\">    Number</span>     </p><p align=\"center\"><br/></p>  </body></html>",None))
        rword4.wordlable.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\">   <span style=\" font-size:20pt; color:#000000;\">????</span><span style=\" font-size:20pt; color:#ee5445;\">??</span><span style=\" font-size:20pt; color:#000000;\">??</span>         <span style=\" font-size:20pt; color:#000000;\">   Lightning </span>       </p><p align=\"center\"><br/></p>   </body></html>",None))
        rword5.wordlable.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\">   <span style=\" font-size:20pt; color:#000000;\">????</span><span style=\" font-size:20pt; color:#ee5445;\">??</span><span style=\" font-size:20pt; color:#000000;\">????</span>         <span style=\" font-size:20pt; color:#000000;\">   Fire </span>       </p><p align=\"center\"><br/></p>   </body></html>",None))
        rword6.wordlable.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\">   <span style=\" font-size:20pt; color:#000000;\">????</span><span style=\" font-size:20pt; color:#ee5445;\">??</span><span style=\" font-size:20pt; color:#000000;\">??</span>         <span style=\" font-size:20pt; color:#000000;\">   Monkey </span>       </p><p align=\"center\"><br/></p>   </body></html>",None))
        rword7.wordlable.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; color:#000000;\">??????</span><span style=\" font-size:20pt; color:#ee5445;\">??</span><span style=\" font-size:20pt; color:#000000;\">   Month </span></p><p align=\"center\"><br/></p></body></html>",None))
        rword8.wordlable.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; color:#000000;\">????</span><span style=\" font-size:20pt; color:#ee5445;\">??</span><span style=\" font-size:20pt; color:#000000;\">????</span><span style=\" font-size:20pt; color:#ee5445;\">??</span><span style=\" font-size:20pt; color:#000000;\">   Bed </span></p><p align=\"center\"><br/></p></body></html>",None))        
        rword9.wordlable.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; color:#000000;\">??????</span><span style=\" font-size:20pt; color:#ee5445;\">??</span><span style=\" font-size:20pt; color:#000000;\">   Moon </span></p><p align=\"center\"><br/></p></body></html>",None))

        #images
        rword1.image.setPixmap(QPixmap(r"E:\graduation project\application\images\????????.JPG"))
        rword1.image.setScaledContents(True)
        rword2.image.setPixmap(QPixmap(r"E:\graduation project\application\images\????????.JPG"))
        rword2.image.setScaledContents(True)
        rword3.image.setPixmap(QPixmap(r"E:\graduation project\application\images\??????.JPG"))
        rword3.image.setScaledContents(True)
        rword4.image.setPixmap(QPixmap(r"E:\graduation project\application\images\??????.JPG"))
        rword4.image.setScaledContents(True)
        rword5.image.setPixmap(QPixmap(r"E:\graduation project\application\images\????????.JPG"))
        rword5.image.setScaledContents(True)
        rword6.image.setPixmap(QPixmap(r"E:\graduation project\application\images\??????.JPG"))
        rword6.image.setScaledContents(True)
        rword7.image.setPixmap(QPixmap(r"E:\graduation project\application\images\??????.JPG"))
        rword7.image.setScaledContents(True)
        rword8.image.setPixmap(QPixmap(r"E:\graduation project\application\images\????????.JPG"))
        rword8.image.setScaledContents(True)
        rword9.image.setPixmap(QPixmap(r"E:\graduation project\application\images\??????.JPG"))
        rword9.image.setScaledContents(True)

        #Audio
        rword1.wordsound.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\????????.mp3")))
        rword2.wordsound.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\????????.mp3")))
        rword3.wordsound.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\??????.mp3")))
        rword4.wordsound.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\??????.mp3")))
        rword5.wordsound.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\????????.mp3")))
        rword6.wordsound.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\??????.mp3")))
        rword7.wordsound.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\??????.mp3")))
        rword8.wordsound.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\????????.mp3")))
        rword9.wordsound.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\??????.mp3")))


        #exercises
        rex=ex()
        rex_2=ex_2()
        rex_3=ex()
        cong=congrat()
        
        rex.wordname.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:26pt; color:#ffffff;\">/r/</span></p></body></html>")
        rex.soundname.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:26pt; color:#ffffff;\"> sound /r/</span></p></body></html>")
        rex_2.wordname.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:26pt; color:#ffffff;\">/r/</span></p></body></html>")
        rex_2.soundname.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:26pt; color:#ffffff;\"> sound /r/</span></p></body></html>")
        rex_3.wordname.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:26pt; color:#ffffff;\">/r/</span></p></body></html>")
        rex_3.soundname.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:26pt; color:#ffffff;\"> sound /r/</span></p></body></html>")

        rex.B1.setText ("??????")
        rex.B2.setText ("??????")
        rex.wordsoundb1.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\??????.mp3")))
        rex.wordsoundb2.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\??????.m4a")))
        rex_2.B2.setText("????????")
        rex_2.B1.setText("??????")
        rex_2.wordsoundb2.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\????????.mp3")))
        rex_2.wordsoundb1.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\??????.mp3")))
        rex_3.B1.setText("????????")
        rex_3.B2.setText("????????")
        rex_3.wordsoundb1.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\????????.mp3")))
        rex_3.wordsoundb2.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\????????.mp3")))

        #images
        rex.label_5.setPixmap(QPixmap(r"E:\graduation project\application\images\??????.jpg"))
        rex.label_5.setScaledContents(True)
        rex.label_4.setPixmap(QPixmap(r"E:\graduation project\application\images\??????.JPG"))
        rex.label_4.setScaledContents(True)

        rex_2.label_5.setPixmap(QPixmap(r"E:\graduation project\application\images\????????.JPG"))
        rex_2.label_5.setScaledContents(True)
        rex_2.label_4.setPixmap(QPixmap(r"E:\graduation project\application\images\??????.jpg"))
        rex_2.label_4.setScaledContents(True)

        rex_3.label_5.setPixmap(QPixmap(r"E:\graduation project\application\images\????????.jpg"))
        rex_3.label_5.setScaledContents(True)
        rex_3.label_4.setPixmap(QPixmap(r"E:\graduation project\application\images\????????.jfif"))
        rex_3.label_4.setScaledContents(True)


        widgets_to_add = [r, rword1, rword2, rword3, rword4, rword5, rword6, rword7, rword8, rword9, rex, rex_2, rex_3, cong]

        #widgets arrangment 
        if first_element_index is None:
            
            for x in widgets_to_add: 
                my_add_widget(w=widget, w_widget_stack=widget_stack, w_to_add=x)

        else:
            for i,x in enumerate(widgets_to_add): 
                my_add_widget(w=widget, w_widget_stack=widget_stack, w_to_add=x, index_to_insert_at= first_element_index +i )

    
        widget.setCurrentWidget(widgets_to_add[0])
    def w(self):
        global widget_stack
        global widget

        if len(widget_stack) >0:
            first_element_index = get_index_of_widget(w=widget, w_widget_to_get_index_for=widget_stack[0])
        else:
            first_element_index = None

        len_widget_stack = len(widget_stack)
        for i in range(len_widget_stack):
            widget, widget_stack = remove_last_widget(w=widget, w_widget_stack=widget_stack)

        w=soundform()
        w.label_2.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\soundvideo\w.mp4")))


        #instances
        wword1=wordform()
        wword2=wordform()
        wword3=wordform()
        wword4=wordform()
        wword5=wordform()
        wword6=wordform()
        #wword7=wordform()
        #words
        wword1.wordlable.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\">    <span style=\" font-size:20pt; color:#ee5445;\">??</span><span style=\" font-size:20pt; color:#000000;\">??????</span>   <span style=\" font-size:20pt; color:#000000;\">    Homeland </span>     </p><p align=\"center\"><br/></p>  </body></html>",None))
        wword2.wordlable.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\">    <span style=\" font-size:20pt; color:#ee5445;\">??</span><span style=\" font-size:20pt; color:#000000;\">????</span>   <span style=\" font-size:20pt; color:#000000;\">    Boy </span>     </p><p align=\"center\"><br/></p>  </body></html>",None))
        wword3.wordlable.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\">    <span style=\" font-size:20pt; color:#000000;\">??????</span><span style=\" font-size:20pt; color:#ee5445;\">??</span><span style=\" font-size:20pt; color:#000000;\">??</span>  <span style=\" font-size:20pt; color:#000000;\">    Coffe</span>     </p><p align=\"center\"><br/></p>  </body></html>",None))
        wword4.wordlable.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\">   <span style=\" font-size:20pt; color:#000000;\">????</span><span style=\" font-size:20pt; color:#ee5445;\">????</span><span style=\" font-size:20pt; color:#000000;\">????</span>         <span style=\" font-size:20pt; color:#000000;\">   Parking </span>       </p><p align=\"center\"><br/></p>   </body></html>",None))
        wword5.wordlable.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\">   <span style=\" font-size:20pt; color:#000000;\">????????</span><span style=\" font-size:20pt; color:#ee5445;\">????</span>         <span style=\" font-size:20pt; color:#000000;\">   Cocoa </span>       </p><p align=\"center\"><br/></p>   </body></html>",None))
        wword6.wordlable.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\">  <span style=\" font-size:20pt; color:#000000;\">????</span><span style=\" font-size:20pt; color:#ee5445;\">????</span><span style=\" font-size:20pt; color:#000000;\">??????</span> <span style=\" font-size:20pt; color:#000000;\">    Signature </span>     </p><p align=\"center\"><br/></p>  </body></html>",None))
        
        #images
        wword1.image.setPixmap(QPixmap(r"E:\graduation project\application\images\????????.png"))
        wword1.image.setScaledContents(True)
        wword2.image.setPixmap(QPixmap(r"E:\graduation project\application\images\??????.jfif"))
        wword2.image.setScaledContents(True)
        wword3.image.setPixmap(QPixmap(r"E:\graduation project\application\images\????????.jfif"))
        wword3.image.setScaledContents(True)
        wword4.image.setPixmap(QPixmap(r"E:\graduation project\application\images\????????.jfif"))
        wword4.image.setScaledContents(True)
        wword5.image.setPixmap(QPixmap(r"E:\graduation project\application\images\????????.jfif"))
        wword5.image.setScaledContents(True)
        wword6.image.setPixmap(QPixmap(r"E:\graduation project\application\images\??????????.jfif"))
        wword6.image.setScaledContents(True)
       
        #audios 
        wword1.wordsound.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\????????.mp3")))
        wword2.wordsound.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\??????.mp3")))
        wword3.wordsound.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\????????.mp3")))
        wword4.wordsound.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\????????.mp3")))
        wword5.wordsound.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\????????.mp3")))
        wword6.wordsound.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\??????????.mp3")))
        #ex
        wex1=ex()
        wex2=ex_2()
        wex3=ex()
        cong=congrat()
        wex1.wordname.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:26pt; color:#ffffff;\"> /w/ </span></p></body></html>")
        wex1.soundname.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:26pt; color:#ffffff;\"> sound /w/ </span></p></body></html>")
        wex2.wordname.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:26pt; color:#ffffff;\"> /w/ </span></p></body></html>")
        wex2.soundname.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:26pt; color:#ffffff;\"> sound /w/ </span></p></body></html>")
        wex3.wordname.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:26pt; color:#ffffff;\"> /w/ </span></p></body></html>")
        wex3.soundname.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:26pt; color:#ffffff;\"> sound /w/ </span></p></body></html>")
        wex1.B1.setText("??????")
        wex1.B2.setText("??????")
        wex1.wordsoundb1.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\??????.mp3")))
        wex1.wordsoundb2.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\??????.m4a")))
        wex2.B1.setText("??????????")
        wex2.B2.setText("??????????")
        wex2.wordsoundb1.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\??????????.mp3")))
        wex2.wordsoundb2.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\??????????.mp3")))
        wex3.B1.setText("??????")
        wex3.B2.setText("??????")
        wex3.wordsoundb1.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\??????.mp3")))
        wex3.wordsoundb2.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\??????.mp3")))
        #images
        wex1.label_5.setPixmap(QPixmap(r"E:\graduation project\application\images\??????.jfif"))
        wex1.label_5.setScaledContents(True)
        wex1.label_4.setPixmap(QPixmap(r"E:\graduation project\application\images\??????.JPG"))
        wex1.label_4.setScaledContents(True)

        wex2.label_5.setPixmap(QPixmap(r"E:\graduation project\application\images\??????????.jfif"))
        wex2.label_5.setScaledContents(True)
        wex2.label_4.setPixmap(QPixmap(r"E:\graduation project\application\images\??????????.jfif"))
        wex2.label_4.setScaledContents(True)

        wex3.label_5.setPixmap(QPixmap(r"E:\graduation project\application\images\??????.png"))
        wex3.label_5.setScaledContents(True)
        wex3.label_4.setPixmap(QPixmap(r"E:\graduation project\application\images\??????.jpg"))
        wex3.label_4.setScaledContents(True)

        widgets_to_add = [w, wword1, wword2, wword3, wword4, wword5, wword6, wex1, wex2, wex3, cong]

        #widgets arrangment 
        if first_element_index is None:
            
            for x in widgets_to_add: 
                my_add_widget(w=widget, w_widget_stack=widget_stack, w_to_add=x)

        else:
            for i,x in enumerate(widgets_to_add): 
                my_add_widget(w=widget, w_widget_stack=widget_stack, w_to_add=x, index_to_insert_at= first_element_index +i )

    
        widget.setCurrentWidget(widgets_to_add[0])
    def j(self):
        global widget_stack
        global widget

        if len(widget_stack) >0:
            first_element_index = get_index_of_widget(w=widget, w_widget_to_get_index_for=widget_stack[0])
        else:
            first_element_index = None

        len_widget_stack = len(widget_stack)
        for i in range(len_widget_stack):
            widget, widget_stack = remove_last_widget(w=widget, w_widget_stack=widget_stack)

        j=soundform()
        j.label_2.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\soundvideo\j.mp4")))


        #instances
        jword1=wordform()
        jword2=wordform()
        jword3=wordform()
        jword4=wordform()
        jword5=wordform()
        #jword6=wordform()
        #jword7=wordform()
        #words
        jword1.wordlable.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\">    <span style=\" font-size:20pt; color:#ee5445;\">????</span><span style=\" font-size:20pt; color:#000000;\">??????</span>   <span style=\" font-size:20pt; color:#000000;\">    Yacht </span>     </p><p align=\"center\"><br/></p>  </body></html>",None))
        jword2.wordlable.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\">    <span style=\" font-size:20pt; color:#ee5445;\">????</span><span style=\" font-size:20pt; color:#000000;\">??????</span>   <span style=\" font-size:20pt; color:#000000;\">    Day </span>     </p><p align=\"center\"><br/></p>  </body></html>",None))
        jword3.wordlable.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\">    <span style=\" font-size:20pt; color:#ee5445;\">????</span><span style=\" font-size:20pt; color:#000000;\">????????</span>   <span style=\" font-size:20pt; color:#000000;\">    Right </span>     </p><p align=\"center\"><br/></p>  </body></html>",None))
        jword4.wordlable.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\">   <span style=\" font-size:20pt; color:#000000;\">????????</span><span style=\" font-size:20pt; color:#ee5445;\">??????</span><span style=\" font-size:20pt; color:#000000;\">????</span>         <span style=\" font-size:20pt; color:#000000;\">   Umbrella  </span>       </p><p align=\"center\"><br/></p>   </body></html>",None))
        jword5.wordlable.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\">   <span style=\" font-size:20pt; color:#000000;\">??????</span><span style=\" font-size:20pt; color:#ee5445;\">??????</span><span style=\" font-size:20pt; color:#000000;\">????</span>      <span style=\" font-size:20pt; color:#000000;\">   Legal will </span>       </p><p align=\"center\"><br/></p>   </body></html>",None))
        #jword6.wordlable.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\">    <span style=\" font-size:20pt; color:#ee5445;\">????</span><span style=\" font-size:20pt; color:#000000;\">??</span> <span style=\" font-size:20pt; color:#ee5445;\">??</span>  <span style=\" font-size:20pt; color:#000000;\">    Door </span>     </p><p align=\"center\"><br/></p>  </body></html>",None))
        #jword7.wordlable.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; color:#000000;\">??</span><span style=\" font-size:20pt; color:#ee5445;\">??</span><span style=\" font-size:20pt; color:#000000;\">   Dad </span></p><p align=\"center\"><br/></p></body></html>",None))
        
        #images
        jword1.image.setPixmap(QPixmap(r"E:\graduation project\application\images\??????.jfif"))
        jword1.image.setScaledContents(True)
        jword2.image.setPixmap(QPixmap(r"E:\graduation project\application\images\??????.jfif"))
        jword2.image.setScaledContents(True)
        jword3.image.setPixmap(QPixmap(r"E:\graduation project\application\images\????????.jfif"))
        jword3.image.setScaledContents(True)
        jword4.image.setPixmap(QPixmap(r"E:\graduation project\application\images\??????????.jfif"))
        jword4.image.setScaledContents(True)
        jword5.image.setPixmap(QPixmap(r"E:\graduation project\application\images\????????.jfif"))
        jword5.image.setScaledContents(True)
        #jword6.image.setPixmap(QPixmap(r"E:\graduation project\application\images\????????.jfif"))
        #jword6.image.setScaledContents(True)
        #jword7.image.setPixmap(QPixmap(r"E:\graduation project\application\images\????.jfif"))
        #jword7.image.setScaledContents(True)
        #audios 
        jword1.wordsound.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\??????.mp3")))
        jword2.wordsound.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\??????.mp3")))
        jword3.wordsound.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\????????.mp3")))
        jword4.wordsound.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\??????????.mp3")))
        jword5.wordsound.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\????????.mp3")))
        #jword6.wordsound.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\????????.mp3")))
        #jword7.wordsound.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\????.mp3")))

        #ex
        jex1=ex_2()
        jex2=ex()
        #jex3=ex()
        cong=congrat()
        jex1.wordname.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:26pt; color:#ffffff;\">/j/</span></p></body></html>")
        jex1.soundname.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:26pt; color:#ffffff;\">sound /j/ </span></p></body></html>")
        jex2.wordname.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:26pt; color:#ffffff;\">/j/</span></p></body></html>")
        jex2.soundname.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:26pt; color:#ffffff;\">sound /j/ </span></p></body></html>")
        #jex3.wordname.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:26pt; color:#ffffff;\">/j/</span></p></body></html>")
        #jex3.soundname.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:26pt; color:#ffffff;\">sound /j/</span></p></body></html>")
        jex1.B1.setText("??????")
        jex1.B2.setText("??????")
        jex1.wordsoundb1.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\??????.mp3")))
        jex1.wordsoundb2.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\??????.mp3")))
        jex2.B1.setText("??????")
        jex2.B2.setText("??????")
        jex2.wordsoundb1.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\??????.mp3")))
        jex2.wordsoundb2.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\??????.mp3")))
        #jex3.B1.setText("????????")
        #jex3.B2.setText("????????")
        #jex3.wordsoundb1.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\????????.mp3")))
        #jex3.wordsoundb2.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\????????.mp3")))
        #images
        jex1.label_5.setPixmap(QPixmap(r"E:\graduation project\application\images\??????.jfif"))
        jex1.label_5.setScaledContents(True)
        jex1.label_4.setPixmap(QPixmap(r"E:\graduation project\application\images\??????.jfif"))
        jex1.label_4.setScaledContents(True)

        jex2.label_5.setPixmap(QPixmap(r"E:\graduation project\application\images\??????.jfif"))
        jex2.label_5.setScaledContents(True)
        jex2.label_4.setPixmap(QPixmap(r"E:\graduation project\application\images\??????.png"))
        jex2.label_4.setScaledContents(True)

        #jex3.label_5.setPixmap(QPixmap(r"E:\graduation project\application\images\????????.jfif"))
        #jex3.label_5.setScaledContents(True)
        #jex3.label_4.setPixmap(QPixmap(r"E:\graduation project\application\images\????????.jpg"))
        #jex3.label_4.setScaledContents(True)

        widgets_to_add = [j, jword1, jword2, jword3, jword4, jword5, jex1, jex2, cong]

        #widgets arrangment 
        if first_element_index is None:
            
            for x in widgets_to_add: 
                my_add_widget(w=widget, w_widget_stack=widget_stack, w_to_add=x)

        else:
            for i,x in enumerate(widgets_to_add): 
                my_add_widget(w=widget, w_widget_stack=widget_stack, w_to_add=x, index_to_insert_at= first_element_index +i )

    
        widget.setCurrentWidget(widgets_to_add[0])
#=======================================================================================================================================================================
###Friends 
    def b(self):
        global widget_stack
        global widget

        if len(widget_stack) >0:
            first_element_index = get_index_of_widget(w=widget, w_widget_to_get_index_for=widget_stack[0])
        else:
            first_element_index = None

        len_widget_stack = len(widget_stack)
        for i in range(len_widget_stack):
            widget, widget_stack = remove_last_widget(w=widget, w_widget_stack=widget_stack)

        b=soundform()
        b.label_2.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\soundvideo\b.mp4")))


        #instances
        bword1=wordform()
        bword2=wordform()
        bword3=wordform()
        bword4=wordform()
        bword5=wordform()
        bword6=wordform()
        bword7=wordform()
        #words
        bword1.wordlable.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\">    <span style=\" font-size:20pt; color:#ee5445;\">????</span><span style=\" font-size:20pt; color:#000000;\">????</span>   <span style=\" font-size:20pt; color:#000000;\">    Girl </span>     </p><p align=\"center\"><br/></p>  </body></html>",None))
        bword2.wordlable.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\">    <span style=\" font-size:20pt; color:#ee5445;\">????</span><span style=\" font-size:20pt; color:#000000;\">??????????</span>   <span style=\" font-size:20pt; color:#000000;\">    Orange </span>     </p><p align=\"center\"><br/></p>  </body></html>",None))
        bword3.wordlable.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\">    <span style=\" font-size:20pt; color:#ee5445;\">????</span><span style=\" font-size:20pt; color:#000000;\">??????</span>   <span style=\" font-size:20pt; color:#000000;\">    Skin</span>     </p><p align=\"center\"><br/></p>  </body></html>",None))
        bword4.wordlable.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\">   <span style=\" font-size:20pt; color:#000000;\">????</span><span style=\" font-size:20pt; color:#ee5445;\">??????</span><span style=\" font-size:20pt; color:#000000;\">??</span>         <span style=\" font-size:20pt; color:#000000;\">   Rope </span>       </p><p align=\"center\"><br/></p>   </body></html>",None))
        bword5.wordlable.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\">   <span style=\" font-size:20pt; color:#000000;\">????</span><span style=\" font-size:20pt; color:#ee5445;\">??????</span><span style=\" font-size:20pt; color:#000000;\">????</span>         <span style=\" font-size:20pt; color:#000000;\">   Doctor </span>       </p><p align=\"center\"><br/></p>   </body></html>",None))
        bword6.wordlable.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\">    <span style=\" font-size:20pt; color:#ee5445;\">????</span><span style=\" font-size:20pt; color:#000000;\">??</span> <span style=\" font-size:20pt; color:#ee5445;\">??</span>  <span style=\" font-size:20pt; color:#000000;\">    Door </span>     </p><p align=\"center\"><br/></p>  </body></html>",None))
        bword7.wordlable.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; color:#000000;\">??</span><span style=\" font-size:20pt; color:#ee5445;\">??</span><span style=\" font-size:20pt; color:#000000;\">   Father </span></p><p align=\"center\"><br/></p></body></html>",None))
        
        #images
        bword1.image.setPixmap(QPixmap(r"E:\graduation project\application\images\??????.png"))
        bword1.image.setScaledContents(True)
        bword2.image.setPixmap(QPixmap(r"E:\graduation project\application\images\????????????.jfif"))
        bword2.image.setScaledContents(True)
        bword3.image.setPixmap(QPixmap(r"E:\graduation project\application\images\????????.jfif"))
        bword3.image.setScaledContents(True)
        bword4.image.setPixmap(QPixmap(r"E:\graduation project\application\images\??????.jfif"))
        bword4.image.setScaledContents(True)
        bword6.image.setPixmap(QPixmap(r"E:\graduation project\application\images\??????.jfif"))
        bword6.image.setScaledContents(True)
        bword5.image.setPixmap(QPixmap(r"E:\graduation project\application\images\????????.jfif"))
        bword5.image.setScaledContents(True)
        bword7.image.setPixmap(QPixmap(r"E:\graduation project\application\images\????.jfif"))
        bword7.image.setScaledContents(True)
        #audios 
        bword1.wordsound.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\??????.mp3")))
        bword2.wordsound.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\????????????.mp3")))
        bword3.wordsound.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\????????.mp3")))
        bword4.wordsound.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\??????.mp3")))
        bword6.wordsound.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\??????.mp3")))
        bword5.wordsound.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\????????.mp3")))
        bword7.wordsound.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\????.mp3")))

        #ex
        bex1=ex()
        bex2=ex_2()
        bex3=ex()
        cong=congrat()
        bex1.wordname.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:26pt; color:#ffffff;\">  /b/ </span></p></body></html>")
        bex1.soundname.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:26pt; color:#ffffff;\"> Sound /b/ </span></p></body></html>")
        bex2.wordname.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:26pt; color:#ffffff;\"> /b/ </span></p></body></html>")
        bex2.soundname.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:26pt; color:#ffffff;\"> Sound /b/ </span></p></body></html>")
        bex3.wordname.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:26pt; color:#ffffff;\"> /b/ </span></p></body></html>")
        bex3.soundname.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:26pt; color:#ffffff;\"> Sound /b/ </span></p></body></html>")
        bex1.B1.setText("??????")
        bex1.B2.setText("??????")
        bex1.wordsoundb1.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\??????.mp3")))
        bex1.wordsoundb2.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\??????.mp3")))
        bex2.B1.setText("??????")
        bex2.B2.setText("??????")
        bex2.wordsoundb1.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\??????.mp3")))
        bex2.wordsoundb2.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\??????.mp3")))
        bex3.B1.setText("????????")
        bex3.B2.setText("????????")
        bex3.wordsoundb1.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\????????.mp3")))
        bex3.wordsoundb2.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\????????.mp3")))

        #images
        bex1.label_5.setPixmap(QPixmap(r"E:\graduation project\application\images\??????.png"))
        bex1.label_5.setScaledContents(True)
        bex1.label_4.setPixmap(QPixmap(r"E:\graduation project\application\images\??????.jfif"))
        bex1.label_4.setScaledContents(True)

        bex2.label_5.setPixmap(QPixmap(r"E:\graduation project\application\images\??????.JPG"))
        bex2.label_5.setScaledContents(True)
        bex2.label_4.setPixmap(QPixmap(r"E:\graduation project\application\images\??????.jfif"))
        bex2.label_4.setScaledContents(True)

        bex3.label_5.setPixmap(QPixmap(r"E:\graduation project\application\images\????????.jfif"))
        bex3.label_5.setScaledContents(True)
        bex3.label_4.setPixmap(QPixmap(r"E:\graduation project\application\images\????????.jpg"))
        bex3.label_4.setScaledContents(True)

        widgets_to_add = [b, bword1, bword2, bword3, bword4, bword5, bword6, bword7, bex1, bex2, bex3, cong]

        #widgets arrangment 
        if first_element_index is None:
            
            for x in widgets_to_add: 
                my_add_widget(w=widget, w_widget_stack=widget_stack, w_to_add=x)

        else:
            for i,x in enumerate(widgets_to_add): 
                my_add_widget(w=widget, w_widget_stack=widget_stack, w_to_add=x, index_to_insert_at= first_element_index +i )

    
        widget.setCurrentWidget(widgets_to_add[0])
    def d(self):
        global widget_stack
        global widget

        if len(widget_stack) >0:
            first_element_index = get_index_of_widget(w=widget, w_widget_to_get_index_for=widget_stack[0])
        else:
            first_element_index = None

        len_widget_stack = len(widget_stack)
        for i in range(len_widget_stack):
            widget, widget_stack = remove_last_widget(w=widget, w_widget_stack=widget_stack)

        d=soundform()
        d.label_2.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\soundvideo\d.mp4")))
        #instances
        dword1=wordform()
        dword2=wordform()
        dword3=wordform()
        dword4=wordform()
        dword5=wordform()
        dword6=wordform()
        dword7=wordform()
        dword8=wordform()
        #words
        dword1.wordlable.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\">    <span style=\" font-size:20pt; color:#ee5445;\">??</span><span style=\" font-size:20pt; color:#000000;\">????????</span>   <span style=\" font-size:20pt; color:#000000;\">  Cupbord </span>     </p><p align=\"center\"><br/></p>  </body></html>",None))
        dword2.wordlable.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\">    <span style=\" font-size:20pt; color:#ee5445;\">??</span><span style=\" font-size:20pt; color:#000000;\">????</span>   <span style=\" font-size:20pt; color:#000000;\">    Religion </span>     </p><p align=\"center\"><br/></p>  </body></html>",None))
        dword3.wordlable.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\">    <span style=\" font-size:20pt; color:#ee5445;\">??</span><span style=\" font-size:20pt; color:#000000;\">??????</span>   <span style=\" font-size:20pt; color:#000000;\">    Invitation </span>     </p><p align=\"center\"><br/></p>  </body></html>",None))
        dword4.wordlable.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\">   <span style=\" font-size:20pt; color:#000000;\">????</span><span style=\" font-size:20pt; color:#ee5445;\">??</span><span style=\" font-size:20pt; color:#000000;\">??</span>         <span style=\" font-size:20pt; color:#000000;\">   Lie </span>       </p><p align=\"center\"><br/></p>   </body></html>",None))
        dword5.wordlable.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; color:#000000;\">??????</span><span style=\" font-size:20pt; color:#ee5445;\">??</span><span style=\" font-size:20pt; color:#000000;\">   Column </span></p><p align=\"center\"><br/></p></body></html>",None))
        dword6.wordlable.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; color:#000000;\">??????</span><span style=\" font-size:20pt; color:#ee5445;\">??</span><span style=\" font-size:20pt; color:#000000;\">   Feast </span></p><p align=\"center\"><br/></p></body></html>",None))
        dword7.wordlable.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; color:#000000;\">????</span><span style=\" font-size:20pt; color:#ee5445;\">??</span> <span style=\" font-size:20pt; color:#000000;\">???? </span><span style=\" font-size:20pt; color:#000000;\">   Justice </span></p><p align=\"center\"><br/></p></body></html>",None))
        dword8.wordlable.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; color:#000000;\">????</span><span style=\" font-size:20pt; color:#ee5445;\">??</span><span style=\" font-size:20pt; color:#000000;\">   Column </span></p><p align=\"center\"><br/></p></body></html>",None))

        #images
        dword1.image.setPixmap(QPixmap(r"E:\graduation project\application\images\??????????.jfif"))
        dword1.image.setScaledContents(True)
        dword2.image.setPixmap(QPixmap(r"E:\graduation project\application\images\??????.jpg"))
        dword2.image.setScaledContents(True)
        dword3.image.setPixmap(QPixmap(r"E:\graduation project\application\images\????????.jfif"))
        dword3.image.setScaledContents(True)
        dword4.image.setPixmap(QPixmap(r"E:\graduation project\application\images\??????.png"))
        dword4.image.setScaledContents(True)
        dword5.image.setPixmap(QPixmap(r"E:\graduation project\application\images\????????.jpg"))
        dword5.image.setScaledContents(True)
        dword6.image.setPixmap(QPixmap(r"E:\graduation project\application\images\??????.jfif"))
        dword6.image.setScaledContents(True)
        dword7.image.setPixmap(QPixmap(r"E:\graduation project\application\images\??????.jfif"))
        dword7.image.setScaledContents(True)
        dword8.image.setPixmap(QPixmap(r"E:\graduation project\application\images\????.png"))
        dword8.image.setScaledContents(True)

        #audios 
        dword1.wordsound.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\??????????.mp3")))
        dword2.wordsound.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\??????.mp3")))
        dword3.wordsound.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\????????.mp3")))
        dword4.wordsound.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\??????.mp3")))
        dword5.wordsound.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\????????.mp3")))
        dword6.wordsound.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\??????.mp3")))
        dword7.wordsound.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\??????.mp3")))
        dword8.wordsound.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\????.mp3")))

        #ex
        dex1=ex_2()
        dex2=ex()
        dex3=ex_2()
        cong=congrat()
        dex1.wordname.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:26pt; color:#ffffff;\"> /d/</span></p></body></html>")
        dex1.soundname.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:26pt; color:#ffffff;\">Sound  /d/</span></p></body></html>")
        dex2.wordname.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:26pt; color:#ffffff;\"> /d/</span></p></body></html>")
        dex2.soundname.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:26pt; color:#ffffff;\">Sound  /d/</span></p></body></html>")
        dex3.wordname.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:26pt; color:#ffffff;\"> /d/</span></p></body></html>")
        dex3.soundname.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:26pt; color:#ffffff;\">Sound  /d/</span></p></body></html>")
        dex1.B1.setText("??????")
        dex1.B2.setText("??????")
        dex1.wordsoundb1.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\??????.mp3")))
        dex1.wordsoundb2.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\??????.mp3")))
        dex2.B1.setText("??????")
        dex2.B2.setText("??????")
        dex2.wordsoundb1.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\??????.mp3")))
        dex2.wordsoundb2.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\??????.mp3")))
        dex3.B1.setText("????????")
        dex3.B2.setText("????????")
        dex3.wordsoundb1.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\????????.mp3")))
        dex3.wordsoundb2.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\????????.mp3")))

        #images
        dex1.label_5.setPixmap(QPixmap(r"E:\graduation project\application\images\??????.png"))
        dex1.label_5.setScaledContents(True)
        dex1.label_4.setPixmap(QPixmap(r"E:\graduation project\application\images\??????.jfif"))
        dex1.label_4.setScaledContents(True)

        dex2.label_4.setPixmap(QPixmap(r"E:\graduation project\application\images\??????.jfif"))
        dex2.label_4.setScaledContents(True)
        dex2.label_5.setPixmap(QPixmap(r"E:\graduation project\application\images\??????.jpg"))
        dex2.label_5.setScaledContents(True)

        dex3.label_5.setPixmap(QPixmap(r"E:\graduation project\application\images\????????.jpg"))
        dex3.label_5.setScaledContents(True)
        dex3.label_4.setPixmap(QPixmap(r"E:\graduation project\application\images\????????.jfif"))
        dex3.label_4.setScaledContents(True)

        widgets_to_add = [d, dword1, dword2, dword3, dword4, dword5, dword6, dword7, dword8, dex1, dex2, dex3, cong]

        #widgets arrangment 
        if first_element_index is None:
            
            for x in widgets_to_add: 
                my_add_widget(w=widget, w_widget_stack=widget_stack, w_to_add=x)

        else:
            for i,x in enumerate(widgets_to_add): 
                my_add_widget(w=widget, w_widget_stack=widget_stack, w_to_add=x, index_to_insert_at= first_element_index +i )

    
        widget.setCurrentWidget(widgets_to_add[0])    
    def ch(self):
        global widget_stack
        global widget

        if len(widget_stack) >0:
            first_element_index = get_index_of_widget(w=widget, w_widget_to_get_index_for=widget_stack[0])
        else:
            first_element_index = None

        len_widget_stack = len(widget_stack)
        for i in range(len_widget_stack):
            widget, widget_stack = remove_last_widget(w=widget, w_widget_stack=widget_stack)

        ch=soundform()
        ch.label_2.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\soundvideo\ch.mp4")))
        #instances
        chword1=wordform()
        chword2=wordform()
        chword3=wordform()
        chword4=wordform()
        chword5=wordform()
        chword6=wordform()
        chword7=wordform()
        #words
        chword1.wordlable.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\">    <span style=\" font-size:20pt; color:#ee5445;\">????</span><span style=\" font-size:20pt; color:#000000;\">????</span>   <span style=\" font-size:20pt; color:#000000;\">    Sun </span>     </p><p align=\"center\"><br/></p>  </body></html>",None))
        chword2.wordlable.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\">    <span style=\" font-size:20pt; color:#ee5445;\">????</span><span style=\" font-size:20pt; color:#000000;\">????????</span>   <span style=\" font-size:20pt; color:#000000;\">    Soup </span>     </p><p align=\"center\"><br/></p>  </body></html>",None))
        chword3.wordlable.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\">    <span style=\" font-size:20pt; color:#ee5445;\">????</span><span style=\" font-size:20pt; color:#000000;\">????</span>   <span style=\" font-size:20pt; color:#000000;\">    oldman </span>     </p><p align=\"center\"><br/></p>  </body></html>",None))
        chword4.wordlable.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\">   <span style=\" font-size:20pt; color:#000000;\">????</span><span style=\" font-size:20pt; color:#ee5445;\">??????</span><span style=\" font-size:20pt; color:#000000;\">??</span>         <span style=\" font-size:20pt; color:#000000;\">   comb </span>       </p><p align=\"center\"><br/></p>   </body></html>",None))
        chword5.wordlable.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\">   <span style=\" font-size:20pt; color:#000000;\">????????</span><span style=\" font-size:20pt; color:#ee5445;\">??</span>         <span style=\" font-size:20pt; color:#000000;\">   Bread </span>       </p><p align=\"center\"><br/></p>   </body></html>",None))
        chword6.wordlable.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\">    <span style=\" font-size:20pt; color:#ee5445;\">????</span><span style=\" font-size:20pt; color:#000000;\">??</span> <span style=\" font-size:20pt; color:#ee5445;\">??</span>  <span style=\" font-size:20pt; color:#000000;\">    Gauze </span>     </p><p align=\"center\"><br/></p>  </body></html>",None))
        chword7.wordlable.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; color:#000000;\">??????</span><span style=\" font-size:20pt; color:#ee5445;\">??</span><span style=\" font-size:20pt; color:#000000;\">   Army </span></p><p align=\"center\"><br/></p></body></html>",None))
        
        #images
        chword1.image.setPixmap(QPixmap(r"E:\graduation project\application\images\??????.jfif"))
        chword1.image.setScaledContents(True)
        chword2.image.setPixmap(QPixmap(r"E:\graduation project\application\images\??????????.jfif"))
        chword2.image.setScaledContents(True)
        chword3.image.setPixmap(QPixmap(r"E:\graduation project\application\images\??????.jfif"))
        chword3.image.setScaledContents(True)
        chword4.image.setPixmap(QPixmap(r"E:\graduation project\application\images\??????.jfif"))
        chword4.image.setScaledContents(True)
        chword5.image.setPixmap(QPixmap(r"E:\graduation project\application\images\??????.jfif"))
        chword5.image.setScaledContents(True)
        chword6.image.setPixmap(QPixmap(r"E:\graduation project\application\images\??????.jpg"))
        chword6.image.setScaledContents(True)
        chword7.image.setPixmap(QPixmap(r"E:\graduation project\application\images\??????.jfif"))
        chword7.image.setScaledContents(True)
        #audios 
        chword1.wordsound.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\??????.mp3")))
        chword2.wordsound.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\??????????.mp3")))
        chword3.wordsound.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\??????.mp3")))
        chword4.wordsound.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\??????.mp3")))
        chword5.wordsound.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\??????.mp3")))
        chword6.wordsound.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\??????.mp3")))
        chword7.wordsound.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\??????.mp3")))

        #ex
        chex1=ex()
        chex2=ex_2()
        chex3=ex()
        cong=congrat()
        chex1.wordname.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:26pt; color:#ffffff;\"> /??/ </span></p></body></html>")
        chex1.soundname.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:26pt; color:#ffffff;\"> Sound /??/ </span></p></body></html>")
        chex2.wordname.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:26pt; color:#ffffff;\"> /??/ </span></p></body></html>")
        chex2.soundname.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:26pt; color:#ffffff;\"> Sound /??/ </span></p></body></html>")
        chex3.wordname.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:26pt; color:#ffffff;\"> /??/ </span></p></body></html>")
        chex3.soundname.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:26pt; color:#ffffff;\"> Sound /??/ </span></p></body></html>")
        chex1.B1.setText("??????")
        chex1.B2.setText("??????")
        chex1.wordsoundb1.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\??????.mp3")))
        chex1.wordsoundb2.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\??????.mp3")))
        chex2.B1.setText("????????")
        chex2.B2.setText("??????")
        chex2.wordsoundb1.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\????????.mp3")))
        chex2.wordsoundb2.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\??????.mp3")))
        chex3.B1.setText("??????????")
        chex3.B2.setText("????????")
        chex3.wordsoundb1.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\??????????.mp3")))
        chex3.wordsoundb2.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\????????.mp3")))

        #images
        chex1.label_5.setPixmap(QPixmap(r"E:\graduation project\application\images\??????.jfif"))
        chex1.label_5.setScaledContents(True)
        chex1.label_4.setPixmap(QPixmap(r"E:\graduation project\application\images\??????.jfif"))
        chex1.label_4.setScaledContents(True)

        chex2.label_5.setPixmap(QPixmap(r"E:\graduation project\application\images\????????.JPG"))
        chex2.label_5.setScaledContents(True)
        chex2.label_4.setPixmap(QPixmap(r"E:\graduation project\application\images\??????.jfif"))
        chex2.label_4.setScaledContents(True)

        chex3.label_5.setPixmap(QPixmap(r"E:\graduation project\application\images\??????????.jfif"))
        chex3.label_5.setScaledContents(True)
        chex3.label_4.setPixmap(QPixmap(r"E:\graduation project\application\images\??????????.png"))
        chex3.label_4.setScaledContents(True)

        widgets_to_add = [ch, chword1, chword2, chword3, chword4, chword5, chword6, chword7, chex1, chex2, chex3, cong]

        #widgets arrangment 
        if first_element_index is None:
            
            for x in widgets_to_add: 
                my_add_widget(w=widget, w_widget_stack=widget_stack, w_to_add=x)

        else:
            for i,x in enumerate(widgets_to_add): 
                my_add_widget(w=widget, w_widget_stack=widget_stack, w_to_add=x, index_to_insert_at= first_element_index +i )

    
        widget.setCurrentWidget(widgets_to_add[0])    
    def z(self):
        global widget_stack
        global widget

        if len(widget_stack) >0:
            first_element_index = get_index_of_widget(w=widget, w_widget_to_get_index_for=widget_stack[0])
        else:
            first_element_index = None

        len_widget_stack = len(widget_stack)
        for i in range(len_widget_stack):
            widget, widget_stack = remove_last_widget(w=widget, w_widget_stack=widget_stack)

        z=soundform()
        z.label_2.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\soundvideo\z(2).mp4")))


        #instances
        zword1=wordform()
        zword2=wordform()
        zword3=wordform()
        zword4=wordform()
        zword5=wordform()
        zword6=wordform()
        zword7=wordform()
        #words
        zword1.wordlable.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\">    <span style=\" font-size:20pt; color:#ee5445;\">??</span><span style=\" font-size:20pt; color:#000000;\">????</span>   <span style=\" font-size:20pt; color:#000000;\">    Oil </span>     </p><p align=\"center\"><br/></p>  </body></html>",None))
        zword2.wordlable.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\">    <span style=\" font-size:20pt; color:#ee5445;\">??</span><span style=\" font-size:20pt; color:#000000;\">??????</span>   <span style=\" font-size:20pt; color:#000000;\">    Decoration </span>     </p><p align=\"center\"><br/></p>  </body></html>",None))
        zword3.wordlable.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\">    <span style=\" font-size:20pt; color:#ee5445;\">??</span><span style=\" font-size:20pt; color:#000000;\">??????</span>   <span style=\" font-size:20pt; color:#000000;\">    Customer </span>     </p><p align=\"center\"><br/></p>  </body></html>",None))
        zword4.wordlable.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\">   <span style=\" font-size:20pt; color:#000000;\">??</span><span style=\" font-size:20pt; color:#ee5445;\">??</span><span style=\" font-size:20pt; color:#000000;\">??</span>         <span style=\" font-size:20pt; color:#000000;\">   weight </span>       </p><p align=\"center\"><br/></p>   </body></html>",None))
        zword5.wordlable.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\">   <span style=\" font-size:20pt; color:#000000;\">??</span><span style=\" font-size:20pt; color:#ee5445;\">??</span>    <span style=\" font-size:20pt; color:#000000;\">   Rice </span>       </p><p align=\"center\"><br/></p>   </body></html>",None))
        zword6.wordlable.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\">  <span style=\" font-size:20pt; color:#000000;\">????</span><span style=\" font-size:20pt; color:#ee5445;\">??</span> <span style=\" font-size:20pt; color:#000000;\">    Banana </span>     </p><p align=\"center\"><br/></p>  </body></html>",None))
        zword7.wordlable.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; color:#000000;\">????</span><span style=\" font-size:20pt; color:#ee5445;\">??</span><span style=\" font-size:20pt; color:#000000;\">   Gas </span></p><p align=\"center\"><br/></p></body></html>",None))
        
        #images
        zword1.image.setPixmap(QPixmap(r"E:\graduation project\application\images\??????.jfif"))
        zword1.image.setScaledContents(True)
        zword2.image.setPixmap(QPixmap(r"E:\graduation project\application\images\????????.jfif"))
        zword2.image.setScaledContents(True)
        zword3.image.setPixmap(QPixmap(r"E:\graduation project\application\images\????????.jfif"))
        zword3.image.setScaledContents(True)
        zword4.image.setPixmap(QPixmap(r"E:\graduation project\application\images\??????.jfif"))
        zword4.image.setScaledContents(True)
        zword5.image.setPixmap(QPixmap(r"E:\graduation project\application\images\????.jfif"))
        zword5.image.setScaledContents(True)
        zword6.image.setPixmap(QPixmap(r"E:\graduation project\application\images\??????.jfif"))
        zword6.image.setScaledContents(True)
        zword7.image.setPixmap(QPixmap(r"E:\graduation project\application\images\??????.jfif"))
        zword7.image.setScaledContents(True)
        #audios 
        zword1.wordsound.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\??????.mp3")))
        zword2.wordsound.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\????????.mp3")))
        zword3.wordsound.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\????????.mp3")))
        zword4.wordsound.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\??????.mp3")))
        zword5.wordsound.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\????.mp3")))
        zword6.wordsound.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\??????.mp3")))
        zword7.wordsound.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\??????.mp3")))

        #ex
        zex1=ex()
        zex2=ex_2()
        zex3=ex()
        cong=congrat()
        zex1.wordname.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:26pt; color:#ffffff;\">/z/</span></p></body></html>")
        zex1.soundname.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:26pt; color:#ffffff;\"> Sound /z/ </span></p></body></html>")
        zex2.wordname.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:26pt; color:#ffffff;\"> /z/ </span></p></body></html>")
        zex2.soundname.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:26pt; color:#ffffff;\"> Sound /z/ </span></p></body></html>")
        zex3.wordname.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:26pt; color:#ffffff;\"> /z/ </span></p></body></html>")
        zex3.soundname.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:26pt; color:#ffffff;\"> Sound /z/ </span></p></body></html>")
        zex1.B2.setText("??????")
        zex1.B1.setText("??????")
        zex1.wordsoundb2.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\??????.mp3")))
        zex1.wordsoundb1.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\??????.mp3")))
        zex2.B1.setText("????????")
        zex2.B2.setText("??????")
        zex2.wordsoundb1.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\????????.mp3")))
        zex2.wordsoundb2.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\??????.mp3")))
        zex3.B1.setText("??????")
        zex3.B2.setText("??????")
        zex3.wordsoundb1.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\??????.mp3")))
        zex3.wordsoundb2.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\??????.mp3")))

        #images
        zex1.label_5.setPixmap(QPixmap(r"E:\graduation project\application\images\??????.png"))
        zex1.label_5.setScaledContents(True)
        zex1.label_4.setPixmap(QPixmap(r"E:\graduation project\application\images\??????.jfif"))
        zex1.label_4.setScaledContents(True)

        zex2.label_5.setPixmap(QPixmap(r"E:\graduation project\application\images\????????.jpg"))
        zex2.label_5.setScaledContents(True)
        zex2.label_4.setPixmap(QPixmap(r"E:\graduation project\application\images\??????.jfif"))
        zex2.label_4.setScaledContents(True)

        zex3.label_5.setPixmap(QPixmap(r"E:\graduation project\application\images\??????.jfif"))
        zex3.label_5.setScaledContents(True)
        zex3.label_4.setPixmap(QPixmap(r"E:\graduation project\application\images\??????.png"))
        zex3.label_4.setScaledContents(True)

        widgets_to_add = [z, zword1, zword2, zword3, zword4, zword5, zword6, zword7, zex1, zex2, zex3, cong]

        #widgets arrangment 
        if first_element_index is None:
            
            for x in widgets_to_add: 
                my_add_widget(w=widget, w_widget_stack=widget_stack, w_to_add=x)

        else:
            for i,x in enumerate(widgets_to_add): 
                my_add_widget(w=widget, w_widget_stack=widget_stack, w_to_add=x, index_to_insert_at= first_element_index +i )

    
        widget.setCurrentWidget(widgets_to_add[0])
    def s(self):
        global widget_stack
        global widget

        if len(widget_stack) >0:
            first_element_index = get_index_of_widget(w=widget, w_widget_to_get_index_for=widget_stack[0])
        else:
            first_element_index = None

        len_widget_stack = len(widget_stack)
        for i in range(len_widget_stack):
            widget, widget_stack = remove_last_widget(w=widget, w_widget_stack=widget_stack)

        s=soundform()
        s.label_2.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\soundvideo\s.mp4")))


        #instances
        sword1=wordform()
        sword2=wordform()
        sword3=wordform()
        sword4=wordform()
        sword5=wordform()
        sword6=wordform()
        sword7=wordform()
        sword8=wordform()
        sword9=wordform()

        #words
        sword1.wordlable.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\">    <span style=\" font-size:20pt; color:#ee5445;\">????</span><span style=\" font-size:20pt; color:#000000;\">??</span>   <span style=\" font-size:20pt; color:#000000;\">    Secret </span>     </p><p align=\"center\"><br/></p>  </body></html>",None))
        sword2.wordlable.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\">  <span style=\" font-size:20pt; color:#000000;\">??????</span><span style=\" font-size:20pt; color:#ee5445;\">??????</span><span style=\" font-size:20pt; color:#000000;\">????</span>   <span style=\" font-size:20pt; color:#000000;\">    Anise </span>     </p><p align=\"center\"><br/></p>  </body></html>",None))
        sword3.wordlable.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\">    <span style=\" font-size:20pt; color:#ee5445;\">????</span><span style=\" font-size:20pt; color:#000000;\">????</span>   <span style=\" font-size:20pt; color:#000000;\">    Year  </span> </p><p align=\"center\"><br/></p>  </body></html>",None))
        sword4.wordlable.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\">   <span style=\" font-size:20pt; color:#000000;\">????</span><span style=\" font-size:20pt; color:#ee5445;\">??????</span><span style=\" font-size:20pt; color:#000000;\">??</span>     <span style=\" font-size:20pt; color:#000000;\">   Musk </span>       </p><p align=\"center\"><br/></p>   </body></html>",None))
        sword5.wordlable.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\">   <span style=\" font-size:20pt; color:#000000;\">????????</span><span style=\" font-size:20pt; color:#ee5445;\">??</span>         <span style=\" font-size:20pt; color:#000000;\">   Teacher </span>       </p><p align=\"center\"><br/></p>   </body></html>",None))
        sword6.wordlable.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\">  <span style=\" font-size:20pt; color:#000000;\">??????</span><span style=\" font-size:20pt; color:#ee5445;\">??</span>  <span style=\" font-size:20pt; color:#000000;\">    Money </span>     </p><p align=\"center\"><br/></p>  </body></html>",None))
        sword7.wordlable.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; color:#000000;\">????</span><span style=\" font-size:20pt; color:#ee5445;\">??</span><span style=\" font-size:20pt; color:#000000;\">   People </span></p><p align=\"center\"><br/></p></body></html>",None))
        sword8.wordlable.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; color:#000000;\">??</span><span style=\" font-size:20pt; color:#ee5445;\">????</span><span style=\" font-size:20pt; color:#000000;\">????</span><span style=\" font-size:20pt; color:#000000;\">   Draw </span></p><p align=\"center\"><br/></p></body></html>",None))
        sword9.wordlable.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; color:#000000;\">??</span><span style=\" font-size:20pt; color:#ee5445;\">????</span><span style=\" font-size:20pt; color:#000000;\">???? </span><span style=\" font-size:20pt; color:#000000;\">   Name </span></p><p align=\"center\"><br/></p></body></html>",None))

        #images
        sword1.image.setPixmap(QPixmap(r"E:\graduation project\application\images\????.jfif"))
        sword1.image.setScaledContents(True)
        sword2.image.setPixmap(QPixmap(r"E:\graduation project\application\images\??????????.jfif"))
        sword2.image.setScaledContents(True)
        sword3.image.setPixmap(QPixmap(r"E:\graduation project\application\images\??????.jfif"))
        sword3.image.setScaledContents(True)
        sword4.image.setPixmap(QPixmap(r"E:\graduation project\application\images\??????.jfif"))
        sword4.image.setScaledContents(True)
        sword5.image.setPixmap(QPixmap(r"E:\graduation project\application\images\????????.jfif"))
        sword5.image.setScaledContents(True)
        sword6.image.setPixmap(QPixmap(r"E:\graduation project\application\images\????????.jfif"))
        sword6.image.setScaledContents(True)
        sword7.image.setPixmap(QPixmap(r"E:\graduation project\application\images\??????.jfif"))
        sword7.image.setScaledContents(True)
        sword8.image.setPixmap(QPixmap(r"E:\graduation project\application\images\??????.jfif"))
        sword8.image.setScaledContents(True)
        sword9.image.setPixmap(QPixmap(r"E:\graduation project\application\images\??????.jfif"))
        sword9.image.setScaledContents(True)
        #audios 
        sword1.wordsound.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\????.mp3")))
        sword2.wordsound.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\??????????.mp3")))
        sword3.wordsound.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\??????.mp3")))
        sword4.wordsound.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\??????.mp3")))
        sword5.wordsound.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\????????.mp3")))
        sword6.wordsound.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\????????.mp3")))
        sword7.wordsound.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\??????.mp3")))
        sword8.wordsound.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\??????.mp3")))
        sword9.wordsound.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\??????.mp3")))

        #ex
        sex1=ex()
        sex2=ex_2()
        sex3=ex()
        cong=congrat()
        sex1.wordname.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:26pt; color:#ffffff;\"> /s/ </span></p></body></html>")
        sex1.soundname.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:26pt; color:#ffffff;\"> Sound /s/ </span></p></body></html>")
        sex2.wordname.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:26pt; color:#ffffff;\"> /s/ </span></p></body></html>")
        sex2.soundname.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:26pt; color:#ffffff;\"> Sound /s/ </span></p></body></html>")
        sex3.wordname.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:26pt; color:#ffffff;\"> /s/ </span></p></body></html>")
        sex3.soundname.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:26pt; color:#ffffff;\"> Sound /s/ </span></p></body></html>")
        sex1.B1.setText("????")
        sex1.B2.setText("??????")
        sex1.wordsoundb1.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\????.mp3")))
        sex1.wordsoundb2.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\??????.mp3")))
        sex2.B1.setText("??????")
        sex2.B2.setText("??????")
        sex2.wordsoundb1.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\??????.mp3")))
        sex2.wordsoundb2.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\??????.mp3")))
        sex3.B1.setText("??????")
        sex3.B2.setText("??????")
        sex3.wordsoundb1.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\??????.mp3")))
        sex3.wordsoundb2.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\??????.mp3")))
        #images
        sex1.label_5.setPixmap(QPixmap(r"E:\graduation project\application\images\????.jfif"))
        sex1.label_5.setScaledContents(True)
        sex1.label_4.setPixmap(QPixmap(r"E:\graduation project\application\images\??????.JPG"))
        sex1.label_4.setScaledContents(True)

        sex2.label_5.setPixmap(QPixmap(r"E:\graduation project\application\images\??????.jfif"))
        sex2.label_5.setScaledContents(True)
        sex2.label_4.setPixmap(QPixmap(r"E:\graduation project\application\images\??????.jfif"))
        sex2.label_4.setScaledContents(True)

        sex3.label_5.setPixmap(QPixmap(r"E:\graduation project\application\images\??????.jpg"))
        sex3.label_5.setScaledContents(True)
        sex3.label_4.setPixmap(QPixmap(r"E:\graduation project\application\images\??????.jpg"))
        sex3.label_4.setScaledContents(True)

        widgets_to_add = [s, sword1, sword2, sword3, sword4, sword5, sword6, sword7, sword8, sword9, sex1, sex2, sex3, cong]

        #widgets arrangment 
        if first_element_index is None:
            
            for x in widgets_to_add: 
                my_add_widget(w=widget, w_widget_stack=widget_stack, w_to_add=x)

        else:
            for i,x in enumerate(widgets_to_add): 
                my_add_widget(w=widget, w_widget_stack=widget_stack, w_to_add=x, index_to_insert_at= first_element_index +i )

    
        widget.setCurrentWidget(widgets_to_add[0])
#=======================================================================================================================================================================
###family 
    def m(self):
        global widget_stack
        global widget

        if len(widget_stack) >0:
            first_element_index = get_index_of_widget(w=widget, w_widget_to_get_index_for=widget_stack[0])
        else:
            first_element_index = None

        len_widget_stack = len(widget_stack)
        for i in range(len_widget_stack):
            widget, widget_stack = remove_last_widget(w=widget, w_widget_stack=widget_stack)

        m=soundform()
        m.label_2.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\soundvideo\m.mp4")))
        #instances
        mword1=wordform()
        mword2=wordform()
        mword3=wordform()
        mword4=wordform()
        mword5=wordform()
        mword6=wordform()
        mword7=wordform()
        mword8=wordform()
        mword9=wordform()
        #words
        mword1.wordlable.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\">    <span style=\" font-size:20pt; color:#ee5445;\">????</span><span style=\" font-size:20pt; color:#000000;\">????????</span>   <span style=\" font-size:20pt; color:#000000;\">    Fan </span>     </p><p align=\"center\"><br/></p>  </body></html>",None))
        mword2.wordlable.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\">    <span style=\" font-size:20pt; color:#ee5445;\">????</span><span style=\" font-size:20pt; color:#000000;\">????????</span>   <span style=\" font-size:20pt; color:#000000;\">    Mirror </span>     </p><p align=\"center\"><br/></p>  </body></html>",None))
        mword3.wordlable.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\">   <span style=\" font-size:20pt; color:#000000;\">????</span><span style=\" font-size:20pt; color:#ee5445;\">??????</span><span style=\" font-size:20pt; color:#000000;\">??</span>         <span style=\" font-size:20pt; color:#000000;\">    Chickpeas </span>       </p><p align=\"center\"><br/></p>   </body></html>",None))
        mword4.wordlable.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\">   <span style=\" font-size:20pt; color:#000000;\">??????</span><span style=\" font-size:20pt; color:#ee5445;\">??</span>   <span style=\" font-size:20pt; color:#000000;\">   Stairs </span>       </p><p align=\"center\"><br/></p>   </body></html>",None))
        mword5.wordlable.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\">    <span style=\" font-size:20pt; color:#000000;\">??????</span><span style=\" font-size:20pt; color:#ee5445;\">??</span>  <span style=\" font-size:20pt; color:#000000;\">    Pen </span>     </p><p align=\"center\"><br/></p>  </body></html>",None))
        mword6.wordlable.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; color:#000000;\">??????</span><span style=\" font-size:20pt; color:#ee5445;\">??</span><span style=\" font-size:20pt; color:#000000;\">   Dream </span></p><p align=\"center\"><br/></p></body></html>",None))
        mword7.wordlable.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\">   <span style=\" font-size:20pt; color:#000000;\">????</span><span style=\" font-size:20pt; color:#ee5445;\">??????</span><span style=\" font-size:20pt; color:#000000;\">??</span>         <span style=\" font-size:20pt; color:#000000;\">    Chickpeas </span>       </p><p align=\"center\"><br/></p>   </body></html>",None))
        mword8.wordlable.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\">   <span style=\" font-size:20pt; color:#000000;\">????</span><span style=\" font-size:20pt; color:#ee5445;\">??????</span><span style=\" font-size:20pt; color:#000000;\">??</span>         <span style=\" font-size:20pt; color:#000000;\">    Chickpeas </span>       </p><p align=\"center\"><br/></p>   </body></html>",None))
        mword9.wordlable.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\">   <span style=\" font-size:20pt; color:#000000;\">??</span><span style=\" font-size:20pt; color:#ee5445;\">????</span><span style=\" font-size:20pt; color:#000000;\">??</span>         <span style=\" font-size:20pt; color:#000000;\">    Chickpeas </span>       </p><p align=\"center\"><br/></p>   </body></html>",None))

        #images
        mword1.image.setPixmap(QPixmap(r"E:\graduation project\application\images\??????????.jfif"))
        mword1.image.setScaledContents(True)
        mword2.image.setPixmap(QPixmap(r"E:\graduation project\application\images\??????????.jfif"))
        mword2.image.setScaledContents(True)
        mword3.image.setPixmap(QPixmap(r"E:\graduation project\application\images\??????.jfif"))
        mword3.image.setScaledContents(True)
        mword4.image.setPixmap(QPixmap(r"E:\graduation project\application\images\??????.jfif"))
        mword4.image.setScaledContents(True)
        mword5.image.setPixmap(QPixmap(r"E:\graduation project\application\images\??????.jfif"))
        mword5.image.setScaledContents(True)
        mword6.image.setPixmap(QPixmap(r"E:\graduation project\application\images\??????.jfif"))
        mword6.image.setScaledContents(True)
        mword7.image.setPixmap(QPixmap(r"E:\graduation project\application\images\??????.jfif"))
        mword7.image.setScaledContents(True)
        mword8.image.setPixmap(QPixmap(r"E:\graduation project\application\images\??????.jfif"))
        mword8.image.setScaledContents(True)
        mword9.image.setPixmap(QPixmap(r"E:\graduation project\application\images\??????.jfif"))
        mword9.image.setScaledContents(True)

        #audios 
        mword1.wordsound.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\??????????.mp3")))
        mword2.wordsound.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\??????????.mp3")))
        mword3.wordsound.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\??????.mp3")))
        mword4.wordsound.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\??????.mp3")))
        mword5.wordsound.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\??????.mp3")))
        mword6.wordsound.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\??????.mp3")))
        mword7.wordsound.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\??????.mp3")))
        mword8.wordsound.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\??????.mp3")))
        mword9.wordsound.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\??????.mp3")))
        #ex
        mex1=ex()
        mex2=ex_2()
        mex3=ex()
        cong=congrat()
        mex1.wordname.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:26pt; color:#ffffff;\"> /m/ </span></p></body></html>")
        mex1.soundname.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:26pt; color:#ffffff;\"> Sound /m/ </span></p></body></html>")
        mex2.wordname.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:26pt; color:#ffffff;\"> /m/ </span></p></body></html>")
        mex2.soundname.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:26pt; color:#ffffff;\"> Sound /m/ </span></p></body></html>")
        mex3.wordname.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:26pt; color:#ffffff;\"> /m/ </span></p></body></html>")
        mex3.soundname.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:26pt; color:#ffffff;\"> Sound /m/ </span></p></body></html>")
        mex1.B1.setText("??????")
        mex1.B2.setText("??????")
        mex1.wordsoundb1.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\??????.mp3")))
        mex1.wordsoundb2.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\??????.mp3")))
        mex2.B1.setText("??????")
        mex2.B2.setText("??????")
        mex2.wordsoundb1.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\??????.mp3")))
        mex2.wordsoundb2.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\??????.mp3")))
        mex3.B1.setText("??????????")
        mex3.B2.setText("????????")
        mex3.wordsoundb1.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\??????????.mp3")))
        mex3.wordsoundb2.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\????????.mp3")))
        #images
        mex1.label_5.setPixmap(QPixmap(r"E:\graduation project\application\images\??????.jfif"))
        mex1.label_5.setScaledContents(True)
        mex1.label_4.setPixmap(QPixmap(r"E:\graduation project\application\images\??????.jfif"))
        mex1.label_4.setScaledContents(True)

        mex2.label_5.setPixmap(QPixmap(r"E:\graduation project\application\images\??????.jfif"))
        mex2.label_5.setScaledContents(True)
        mex2.label_4.setPixmap(QPixmap(r"E:\graduation project\application\images\??????.jfif"))
        mex2.label_4.setScaledContents(True)

        mex3.label_5.setPixmap(QPixmap(r"E:\graduation project\application\images\??????????.jfif"))
        mex3.label_5.setScaledContents(True)
        mex3.label_4.setPixmap(QPixmap(r"E:\graduation project\application\images\????????.jpg"))
        mex3.label_4.setScaledContents(True)

        widgets_to_add = [m, mword1, mword2, mword3, mword4, mword5, mword6, mword7, mword8, mword9, mex1, mex2, mex3, cong]

        #widgets arrangment 
        if first_element_index is None:
            
            for x in widgets_to_add: 
                my_add_widget(w=widget, w_widget_stack=widget_stack, w_to_add=x)

        else:
            for i,x in enumerate(widgets_to_add): 
                my_add_widget(w=widget, w_widget_stack=widget_stack, w_to_add=x, index_to_insert_at= first_element_index +i )

    
        widget.setCurrentWidget(widgets_to_add[0])
    def n(self):
        global widget_stack
        global widget

        if len(widget_stack) >0:
            first_element_index = get_index_of_widget(w=widget, w_widget_to_get_index_for=widget_stack[0])
        else:
            first_element_index = None

        len_widget_stack = len(widget_stack)
        for i in range(len_widget_stack):
            widget, widget_stack = remove_last_widget(w=widget, w_widget_stack=widget_stack)

        n=soundform()
        n.label_2.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\soundvideo\n.mp4")))


        #instances
        nword1=wordform()
        nword2=wordform()
        nword3=wordform()
        nword4=wordform()
        nword5=wordform()
        nword6=wordform()
        nword7=wordform()
        
        #words
        nword1.wordlable.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\">    <span style=\" font-size:20pt; color:#ee5445;\">????</span><span style=\" font-size:20pt; color:#000000;\">????</span>   <span style=\" font-size:20pt; color:#000000;\">    SLeep </span>     </p><p align=\"center\"><br/></p>  </body></html>",None))
        nword2.wordlable.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\">    <span style=\" font-size:20pt; color:#ee5445;\">????</span><span style=\" font-size:20pt; color:#000000;\">????</span>   <span style=\" font-size:20pt; color:#000000;\">    Nile  </span>     </p><p align=\"center\"><br/></p>  </body></html>",None))
        nword3.wordlable.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\">    <span style=\" font-size:20pt; color:#ee5445;\">????</span><span style=\" font-size:20pt; color:#000000;\">??????</span>   <span style=\" font-size:20pt; color:#000000;\">    Ant</span>     </p><p align=\"center\"><br/></p>  </body></html>",None))
        nword4.wordlable.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\">   <span style=\" font-size:20pt; color:#000000;\">????</span><span style=\" font-size:20pt; color:#ee5445;\">??</span>      <span style=\" font-size:20pt; color:#000000;\">   Color </span>       </p><p align=\"center\"><br/></p>   </body></html>",None))
        nword5.wordlable.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\">   <span style=\" font-size:20pt; color:#000000;\">????</span><span style=\" font-size:20pt; color:#ee5445;\">????</span><span style=\" font-size:20pt; color:#000000;\">????</span><span style=\" font-size:20pt; color:#ee5445;\">??</span>    <span style=\" font-size:20pt; color:#000000;\">   Teeth </span>       </p><p align=\"center\"><br/></p>   </body></html>",None))
        nword6.wordlable.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\">   <span style=\" font-size:20pt; color:#000000;\">??????</span><span style=\" font-size:20pt; color:#ee5445;\">????</span>  <span style=\" font-size:20pt; color:#000000;\">    Fig </span>     </p><p align=\"center\"><br/></p>  </body></html>",None))
        nword7.wordlable.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\">    <span style=\" font-size:20pt; color:#ee5445;\">????</span><span style=\" font-size:20pt; color:#000000;\">????</span>   <span style=\" font-size:20pt; color:#000000;\">    SLeep </span>     </p><p align=\"center\"><br/></p>  </body></html>",None))

        #images
        nword1.image.setPixmap(QPixmap(r"E:\graduation project\application\images\??????.jfif"))
        nword1.image.setScaledContents(True)
        nword2.image.setPixmap(QPixmap(r"E:\graduation project\application\images\??????.jfif"))
        nword2.image.setScaledContents(True)
        nword3.image.setPixmap(QPixmap(r"E:\graduation project\application\images\????????.jfif"))
        nword3.image.setScaledContents(True)
        nword4.image.setPixmap(QPixmap(r"E:\graduation project\application\images\??????.jfif"))
        nword4.image.setScaledContents(True)
        nword5.image.setPixmap(QPixmap(r"E:\graduation project\application\images\????????.jfif"))
        nword5.image.setScaledContents(True)
        nword6.image.setPixmap(QPixmap(r"E:\graduation project\application\images\??????.jfif"))
        nword6.image.setScaledContents(True)
        nword7.image.setPixmap(QPixmap(r"E:\graduation project\application\images\??????.jfif"))
        nword7.image.setScaledContents(True)
        #audios 
        nword1.wordsound.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\??????.mp3")))
        nword2.wordsound.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\??????.mp3")))
        nword3.wordsound.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\????????.mp3")))
        nword4.wordsound.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\??????.mp3")))
        nword5.wordsound.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\????????.mp3")))
        nword6.wordsound.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\??????.mp3")))
        nword7.wordsound.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\??????.mp3")))

        #ex
        nex1=ex_2()
        nex2=ex()
        nex3=ex_2()
        cong=congrat()
        nex1.wordname.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:26pt; color:#ffffff;\"> /n/ </span></p></body></html>")
        nex1.soundname.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:26pt; color:#ffffff;\"> Sound /n/  </span></p></body></html>")
        nex2.wordname.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:26pt; color:#ffffff;\"> /n/  </span></p></body></html>")
        nex2.soundname.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:26pt; color:#ffffff;\"> Sound /n/ </span></p></body></html>")
        nex3.wordname.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:26pt; color:#ffffff;\"> /n/ </span></p></body></html>")
        nex3.soundname.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:26pt; color:#ffffff;\"> Sound /n/ </span></p></body></html>")
        nex1.B1.setText("??????")
        nex1.B2.setText("??????")
        nex1.wordsoundb1.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\??????.mp3")))
        nex1.wordsoundb2.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\??????.mp3")))
        nex2.B1.setText("??????")
        nex2.B2.setText("??????")
        nex2.wordsoundb1.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\??????.mp3")))
        nex2.wordsoundb2.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\??????.mp3")))
        nex3.B1.setText("????????")
        nex3.B2.setText("????????")
        nex3.wordsoundb1.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\????????.mp3")))
        nex3.wordsoundb2.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\????????.mp3")))
        #images
        nex1.label_5.setPixmap(QPixmap(r"E:\graduation project\application\images\??????.jfif"))
        nex1.label_5.setScaledContents(True)
        nex1.label_4.setPixmap(QPixmap(r"E:\graduation project\application\images\??????.JPG"))
        nex1.label_4.setScaledContents(True)

        nex2.label_5.setPixmap(QPixmap(r"E:\graduation project\application\images\??????.jfif"))
        nex2.label_5.setScaledContents(True)
        nex2.label_4.setPixmap(QPixmap(r"E:\graduation project\application\images\??????.jfif"))
        nex2.label_4.setScaledContents(True)

        nex3.label_5.setPixmap(QPixmap(r"E:\graduation project\application\images\????????.jfif"))
        nex3.label_5.setScaledContents(True)
        nex3.label_4.setPixmap(QPixmap(r"E:\graduation project\application\images\????????.jfif"))
        nex3.label_4.setScaledContents(True)

        widgets_to_add = [n, nword1, nword2, nword3, nword4, nword5, nword6, nword7, nex1, nex2, nex3, cong]

        #widgets arrangment 
        if first_element_index is None:
            
            for x in widgets_to_add: 
                my_add_widget(w=widget, w_widget_stack=widget_stack, w_to_add=x)

        else:
            for i,x in enumerate(widgets_to_add): 
                my_add_widget(w=widget, w_widget_stack=widget_stack, w_to_add=x, index_to_insert_at= first_element_index +i )

    
        widget.setCurrentWidget(widgets_to_add[0])
    def f(self):
        global widget_stack
        global widget

        if len(widget_stack) >0:
            first_element_index = get_index_of_widget(w=widget, w_widget_to_get_index_for=widget_stack[0])
        else:
            first_element_index = None

        len_widget_stack = len(widget_stack)
        for i in range(len_widget_stack):
            widget, widget_stack = remove_last_widget(w=widget, w_widget_stack=widget_stack)

        f=soundform()
        f.label_2.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\soundvideo\f.mp4")))


        #instances
        fword1=wordform()
        fword2=wordform()
        fword3=wordform()
        fword4=wordform()
        fword5=wordform()
        fword6=wordform()
        fword7=wordform()
        #words
        fword1.wordlable.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\">    <span style=\" font-size:20pt; color:#ee5445;\">????</span><span style=\" font-size:20pt; color:#000000;\">????</span>   <span style=\" font-size:20pt; color:#000000;\">    Oven </span>     </p><p align=\"center\"><br/></p>  </body></html>",None))
        fword2.wordlable.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\">    <span style=\" font-size:20pt; color:#ee5445;\">????</span><span style=\" font-size:20pt; color:#000000;\">????</span>   <span style=\" font-size:20pt; color:#000000;\">    Dawn </span>     </p><p align=\"center\"><br/></p>  </body></html>",None))
        fword3.wordlable.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\">    <span style=\" font-size:20pt; color:#ee5445;\">????</span><span style=\" font-size:20pt; color:#000000;\">????</span>   <span style=\" font-size:20pt; color:#000000;\">    Elephant </span>     </p><p align=\"center\"><br/></p>  </body></html>",None))
        fword4.wordlable.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\">   <span style=\" font-size:20pt; color:#000000;\">????</span><span style=\" font-size:20pt; color:#ee5445;\">??????</span><span style=\" font-size:20pt; color:#000000;\">??</span>         <span style=\" font-size:20pt; color:#000000;\">   a lock </span>       </p><p align=\"center\"><br/></p>   </body></html>",None))
        fword5.wordlable.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\">   <span style=\" font-size:20pt; color:#000000;\">??</span><span style=\" font-size:20pt; color:#ee5445;\">??</span>         <span style=\" font-size:20pt; color:#000000;\">   Rack </span>       </p><p align=\"center\"><br/></p>   </body></html>",None))
        fword6.wordlable.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\">   <span style=\" font-size:20pt; color:#000000;\">????????</span><span style=\" font-size:20pt; color:#ee5445;\">??</span>  <span style=\" font-size:20pt; color:#000000;\">    Sidewalk </span>     </p><p align=\"center\"><br/></p>  </body></html>",None))
        fword7.wordlable.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; color:#000000;\">????</span><span style=\" font-size:20pt; color:#ee5445;\">??????</span><span style=\" font-size:20pt; color:#000000;\">    ???? </span><span style=\" font-size:20pt; color:#000000;\">   Party </span></p><p align=\"center\"><br/></p></body></html>",None))
        
        #images
        fword1.image.setPixmap(QPixmap(r"E:\graduation project\application\images\??????.jfif"))
        fword1.image.setScaledContents(True)
        fword2.image.setPixmap(QPixmap(r"E:\graduation project\application\images\??????.jfif"))
        fword2.image.setScaledContents(True)
        fword3.image.setPixmap(QPixmap(r"E:\graduation project\application\images\??????.jfif"))
        fword3.image.setScaledContents(True)
        fword4.image.setPixmap(QPixmap(r"E:\graduation project\application\images\??????.jfif"))
        fword4.image.setScaledContents(True)
        fword5.image.setPixmap(QPixmap(r"E:\graduation project\application\images\????.jfif"))
        fword5.image.setScaledContents(True)
        fword6.image.setPixmap(QPixmap(r"E:\graduation project\application\images\????????.jfif"))
        fword6.image.setScaledContents(True)
        fword7.image.setPixmap(QPixmap(r"E:\graduation project\application\images\????????.jfif"))
        fword7.image.setScaledContents(True)
        #audios 
        fword1.wordsound.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\??????.mp3")))
        fword2.wordsound.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\??????.mp3")))
        fword3.wordsound.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\??????.mp3")))
        fword4.wordsound.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\??????.mp3")))
        fword5.wordsound.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\????.mp3")))
        fword6.wordsound.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\????????.mp3")))
        fword7.wordsound.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\????????.mp3")))

        #ex
        fex1=ex_2()
        fex2=ex()
        fex3=ex_2()
        cong=congrat()
        fex1.wordname.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:26pt; color:#ffffff;\"> /f/ </span></p></body></html>")
        fex1.soundname.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:26pt; color:#ffffff;\"> Sound /f/  /span></p></body></html>")
        fex2.wordname.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:26pt; color:#ffffff;\"> /f/ </span></p></body></html>")
        fex2.soundname.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:26pt; color:#ffffff;\"> Sound /f/ </span></p></body></html>")
        fex3.wordname.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:26pt; color:#ffffff;\"> /f/ </span></p></body></html>")
        fex3.soundname.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:26pt; color:#ffffff;\"> Sound /f/ </span></p></body></html>")
        fex1.B1.setText("??????")
        fex1.B2.setText("??????")
        fex1.wordsoundb1.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\??????.mp3")))
        fex1.wordsoundb2.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\??????.mp3")))
        fex2.B1.setText("????????")
        fex2.B2.setText("??????????")
        fex2.wordsoundb1.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\????????.mp3")))
        fex2.wordsoundb2.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\??????????.mp3")))
        fex3.B1.setText("??????")
        fex3.B2.setText("??????")
        fex3.wordsoundb1.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\??????.mp3")))
        fex3.wordsoundb2.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\??????.mp3")))
        #images
        fex1.label_5.setPixmap(QPixmap(r"E:\graduation project\application\images\??????.JPG"))
        fex1.label_5.setScaledContents(True)
        fex1.label_4.setPixmap(QPixmap(r"E:\graduation project\application\images\??????.jfif"))
        fex1.label_4.setScaledContents(True)

        fex2.label_5.setPixmap(QPixmap(r"E:\graduation project\application\images\????????.jfif"))
        fex2.label_5.setScaledContents(True)
        fex2.label_4.setPixmap(QPixmap(r"E:\graduation project\application\images\??????????.jpg"))
        fex2.label_4.setScaledContents(True)
        fex3.label_5.setPixmap(QPixmap(r"E:\graduation project\application\images\??????.jpg"))
        fex3.label_5.setScaledContents(True)
        fex3.label_4.setPixmap(QPixmap(r"E:\graduation project\application\images\??????.jfif"))
        fex3.label_4.setScaledContents(True)

        widgets_to_add = [f, fword1, fword2, fword3, fword4, fword5, fword6, fword7, fex1, fex2, fex3, cong]

        #widgets arrangment 
        if first_element_index is None:
            for x in widgets_to_add: 
                my_add_widget(w=widget, w_widget_stack=widget_stack, w_to_add=x)

        else:
            for i,x in enumerate(widgets_to_add): 
                my_add_widget(w=widget, w_widget_stack=widget_stack, w_to_add=x, index_to_insert_at= first_element_index +i )

    
        widget.setCurrentWidget(widgets_to_add[0])
    def t(self):
        global widget_stack
        global widget

        if len(widget_stack) >0:
            first_element_index = get_index_of_widget(w=widget, w_widget_to_get_index_for=widget_stack[0])
        else:
            first_element_index = None

        len_widget_stack = len(widget_stack)
        for i in range(len_widget_stack):
            widget, widget_stack = remove_last_widget(w=widget, w_widget_stack=widget_stack)

        t=soundform()
        t.label_2.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\soundvideo\t.mp4")))


        #instances
        tword1=wordform()
        tword2=wordform()
        tword3=wordform()
        tword4=wordform()
        tword5=wordform()
        tword6=wordform()
        #tword7=wordform()
        #words
        tword1.wordlable.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\">    <span style=\" font-size:20pt; color:#ee5445;\">????</span><span style=\" font-size:20pt; color:#000000;\">??????</span>   <span style=\" font-size:20pt; color:#000000;\">    Apple </span>     </p><p align=\"center\"><br/></p>  </body></html>",None))
        tword2.wordlable.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\">    <span style=\" font-size:20pt; color:#ee5445;\">????</span><span style=\" font-size:20pt; color:#000000;\">??????????</span>   <span style=\" font-size:20pt; color:#000000;\">    Telephone </span>     </p><p align=\"center\"><br/></p>  </body></html>",None))
        tword3.wordlable.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\">    <span style=\" font-size:20pt; color:#ee5445;\">????</span><span style=\" font-size:20pt; color:#000000;\">????????</span>   <span style=\" font-size:20pt; color:#000000;\">    Training </span>     </p><p align=\"center\"><br/></p>  </body></html>",None))
        tword4.wordlable.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\">   <span style=\" font-size:20pt; color:#000000;\">????</span><span style=\" font-size:20pt; color:#ee5445;\">????</span><span style=\" font-size:20pt; color:#000000;\">??</span>    <span style=\" font-size:20pt; color:#000000;\">   Meter </span>       </p><p align=\"center\"><br/></p>   </body></html>",None))
        tword5.wordlable.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\">   <span style=\" font-size:20pt; color:#000000;\">????</span><span style=\" font-size:20pt; color:#ee5445;\">??</span>    <span style=\" font-size:20pt; color:#000000;\">   Sound </span>       </p><p align=\"center\"><br/></p>   </body></html>",None))
        tword6.wordlable.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\">   <span style=\" font-size:20pt; color:#000000;\">??????</span><span style=\" font-size:20pt; color:#ee5445;\">??</span>  <span style=\" font-size:20pt; color:#000000;\">    Time </span>     </p><p align=\"center\"><br/></p>  </body></html>",None))
        #tword7.wordlable.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\">   <span style=\" font-size:20pt; color:#000000;\">??</span><span style=\" font-size:20pt; color:#ee5445;\">??</span><span style=\" font-size:20pt; color:#000000;\">   Dad </span></p><p align=\"center\"><br/></p></body></html>",None))
        
        #images
        tword1.image.setPixmap(QPixmap(r"E:\graduation project\application\images\????????.jfif"))
        tword1.image.setScaledContents(True)
        tword2.image.setPixmap(QPixmap(r"E:\graduation project\application\images\????????????.jfif"))
        tword2.image.setScaledContents(True)
        tword3.image.setPixmap(QPixmap(r"E:\graduation project\application\images\??????????.jfif"))
        tword3.image.setScaledContents(True)
        tword4.image.setPixmap(QPixmap(r"E:\graduation project\application\images\??????.jfif"))
        tword4.image.setScaledContents(True)
        tword5.image.setPixmap(QPixmap(r"E:\graduation project\application\images\??????.png"))
        tword5.image.setScaledContents(True)
        tword6.image.setPixmap(QPixmap(r"E:\graduation project\application\images\??????.png"))
        tword6.image.setScaledContents(True)
        #tword7.image.setPixmap(QPixmap(r"E:\graduation project\application\images\????.jfif"))
        #tword7.image.setScaledContents(True)
        #audios 
        tword1.wordsound.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\????????.mp3")))
        tword2.wordsound.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\????????????.mp3")))
        tword3.wordsound.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\??????????.mp3")))
        tword4.wordsound.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\??????.mp3")))
        tword5.wordsound.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\??????.mp3")))
        tword6.wordsound.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\??????.mp3")))
        #tword7.wordsound.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\????.mp3")))

        #ex
        tex1=ex_2()
        tex2=ex_2()
        tex3=ex()
        cong=congrat()
        tex1.wordname.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:26pt; color:#ffffff;\"> /t/ </span></p></body></html>")
        tex1.soundname.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:26pt; color:#ffffff;\"> Sound /t/ </span></p></body></html>")
        tex2.wordname.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:26pt; color:#ffffff;\"> /t/ </span></p></body></html>")
        tex2.soundname.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:26pt; color:#ffffff;\"> Sound /t/  </span></p></body></html>")
        tex3.wordname.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:26pt; color:#ffffff;\"> /t/ </span></p></body></html>")
        tex3.soundname.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:26pt; color:#ffffff;\">  Sound /t/ </span></p></body></html>")
        tex1.B1.setText("??????")
        tex1.B2.setText("??????")
        tex1.wordsoundb1.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\??????.mp3")))
        tex1.wordsoundb2.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\??????.mp3")))
        tex2.B1.setText("????????")
        tex2.B2.setText("??????????")
        tex2.wordsoundb1.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\????????.mp3")))
        tex2.wordsoundb2.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\??????????.mp3")))
        tex3.B1.setText("??????")
        tex3.B2.setText("????????")
        tex3.wordsoundb1.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\??????.mp3")))
        tex3.wordsoundb2.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\????????.mp3")))
        #images
        tex1.label_5.setPixmap(QPixmap(r"E:\graduation project\application\images\??????.png"))
        tex1.label_5.setScaledContents(True)
        tex1.label_4.setPixmap(QPixmap(r"E:\graduation project\application\images\??????.jfif"))
        tex1.label_4.setScaledContents(True)

        tex2.label_5.setPixmap(QPixmap(r"E:\graduation project\application\images\????????.JPG"))
        tex2.label_5.setScaledContents(True)
        tex2.label_4.setPixmap(QPixmap(r"E:\graduation project\application\images\??????????.jfif"))
        tex2.label_4.setScaledContents(True)

        tex3.label_5.setPixmap(QPixmap(r"E:\graduation project\application\images\??????.png"))
        tex3.label_5.setScaledContents(True)
        tex3.label_4.setPixmap(QPixmap(r"E:\graduation project\application\images\????????.jpg"))
        tex3.label_4.setScaledContents(True)

        widgets_to_add = [t, tword1, tword2, tword3, tword4, tword5, tword6, tex1, tex2, tex3, cong]

        #widgets arrangment 
        if first_element_index is None:
            
            for x in widgets_to_add: 
                my_add_widget(w=widget, w_widget_stack=widget_stack, w_to_add=x)

        else:
            for i,x in enumerate(widgets_to_add): 
                my_add_widget(w=widget, w_widget_stack=widget_stack, w_to_add=x, index_to_insert_at= first_element_index +i )

    
        widget.setCurrentWidget(widgets_to_add[0])
    def k(self):
        global widget_stack
        global widget

        if len(widget_stack) >0:
            first_element_index = get_index_of_widget(w=widget, w_widget_to_get_index_for=widget_stack[0])
        else:
            first_element_index = None

        len_widget_stack = len(widget_stack)
        for i in range(len_widget_stack):
            widget, widget_stack = remove_last_widget(w=widget, w_widget_stack=widget_stack)

        k=soundform()
        k.label_2.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\soundvideo\k.mp4")))


        #instances
        kword1=wordform()
        kword2=wordform()
        kword3=wordform()
        kword4=wordform()
        kword5=wordform()
        kword6=wordform()
        kword7=wordform()
        #words
        kword1.wordlable.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\">    <span style=\" font-size:20pt; color:#ee5445;\">????</span><span style=\" font-size:20pt; color:#000000;\">??????????</span>   <span style=\" font-size:20pt; color:#000000;\">    Electricity </span>     </p><p align=\"center\"><br/></p>  </body></html>",None))
        kword2.wordlable.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\">    <span style=\" font-size:20pt; color:#ee5445;\">????</span><span style=\" font-size:20pt; color:#000000;\">????????</span>   <span style=\" font-size:20pt; color:#000000;\">    Bridge </span>     </p><p align=\"center\"><br/></p>  </body></html>",None))
        kword3.wordlable.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\">    <span style=\" font-size:20pt; color:#ee5445;\">????</span><span style=\" font-size:20pt; color:#000000;\">????</span>   <span style=\" font-size:20pt; color:#000000;\">    Bag </span>     </p><p align=\"center\"><br/></p>  </body></html>",None))
        kword4.wordlable.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\">   <span style=\" font-size:20pt; color:#ee5445;\">????</span><span style=\" font-size:20pt; color:#000000;\">????</span><span style=\" font-size:20pt; color:#ee5445;\">??</span>  <span style=\" font-size:20pt; color:#000000;\">   Eid cake  </span>       </p><p align=\"center\"><br/></p>   </body></html>",None))
        kword5.wordlable.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\">   <span style=\" font-size:20pt; color:#000000;\">??????</span><span style=\" font-size:20pt; color:#ee5445;\">??</span>     <span style=\" font-size:20pt; color:#000000;\">   Fish </span>       </p><p align=\"center\"><br/></p>   </body></html>",None))
        kword6.wordlable.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\">   <span style=\" font-size:20pt; color:#000000;\">??????</span><span style=\" font-size:20pt; color:#ee5445;\">??</span>  <span style=\" font-size:20pt; color:#000000;\">    Window </span>     </p><p align=\"center\"><br/></p>  </body></html>",None))
        kword7.wordlable.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; color:#000000;\">??</span><span style=\" font-size:20pt; color:#ee5445;\">????</span><span style=\" font-size:20pt; color:#000000;\">???? </span><span style=\" font-size:20pt; color:#000000;\">   Food </span></p><p align=\"center\"><br/></p></body></html>",None))
        
        #images
        kword1.image.setPixmap(QPixmap(r"E:\graduation project\application\images\????????????.jfif"))
        kword1.image.setScaledContents(True)
        kword2.image.setPixmap(QPixmap(r"E:\graduation project\application\images\??????????.jfif"))
        kword2.image.setScaledContents(True)
        kword3.image.setPixmap(QPixmap(r"E:\graduation project\application\images\??????.jfif"))
        kword3.image.setScaledContents(True)
        kword4.image.setPixmap(QPixmap(r"E:\graduation project\application\images\??????.jfif"))
        kword4.image.setScaledContents(True)
        kword5.image.setPixmap(QPixmap(r"E:\graduation project\application\images\??????.jfif"))
        kword5.image.setScaledContents(True)
        kword6.image.setPixmap(QPixmap(r"E:\graduation project\application\images\????????.jfif"))
        kword6.image.setScaledContents(True)
        kword7.image.setPixmap(QPixmap(r"E:\graduation project\application\images\??????.jpg"))
        kword7.image.setScaledContents(True)
        #audios 
        kword1.wordsound.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\????????????.mp3")))
        kword2.wordsound.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\??????????.mp3")))
        kword3.wordsound.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\??????.mp3")))
        kword4.wordsound.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\??????.mp3")))
        kword5.wordsound.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\??????.mp3")))
        kword6.wordsound.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\????????.mp3")))
        kword7.wordsound.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\??????.mp3")))

        #ex
        kex1=ex_2()
        kex2=ex()
        kex3=ex()
        cong=congrat()
        kex1.wordname.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:26pt; color:#ffffff;\"> /k/ </span></p></body></html>")
        kex1.soundname.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:26pt; color:#ffffff;\"> Sound /k/ </span></p></body></html>")
        kex2.wordname.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:26pt; color:#ffffff;\"> /k/ </span></p></body></html>")
        kex2.soundname.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:26pt; color:#ffffff;\"> Sound /k/ </span></p></body></html>")
        kex3.wordname.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:26pt; color:#ffffff;\"> /k/ </span></p></body></html>")
        kex3.soundname.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:26pt; color:#ffffff;\"> Sound /k/ </span></p></body></html>")
        kex1.B1.setText("??????????")
        kex1.B2.setText("??????")
        kex1.wordsoundb1.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\??????????.mp3")))
        kex1.wordsoundb2.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\??????.mp3")))
        kex2.B1.setText("??????????")
        kex2.B2.setText("??????????")
        kex2.wordsoundb1.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\??????????.mp3")))
        kex2.wordsoundb2.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\??????????.mp3")))
        kex3.B1.setText("????????")
        kex3.B2.setText("??????")
        kex3.wordsoundb1.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\????????.mp3")))
        kex3.wordsoundb2.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\??????.mp3")))
        #images
        kex1.label_5.setPixmap(QPixmap(r"E:\graduation project\application\images\??????????.jpg"))
        kex1.label_5.setScaledContents(True)
        kex1.label_4.setPixmap(QPixmap(r"E:\graduation project\application\images\??????.jfif"))
        kex1.label_4.setScaledContents(True)

        kex2.label_5.setPixmap(QPixmap(r"E:\graduation project\application\images\??????????.jfif"))
        kex2.label_5.setScaledContents(True)
        kex2.label_4.setPixmap(QPixmap(r"E:\graduation project\application\images\??????????.jpg"))
        kex2.label_4.setScaledContents(True)

        kex3.label_5.setPixmap(QPixmap(r"E:\graduation project\application\images\????????.jfif"))
        kex3.label_5.setScaledContents(True)
        kex3.label_4.setPixmap(QPixmap(r"E:\graduation project\application\images\??????.jpg"))
        kex3.label_4.setScaledContents(True)

        widgets_to_add = [k, kword1, kword2, kword3, kword4, kword5, kword6, kword7, kex1, kex2, kex3, cong]

        #widgets arrangment 
        if first_element_index is None:
            
            for x in widgets_to_add: 
                my_add_widget(w=widget, w_widget_stack=widget_stack, w_to_add=x)

        else:
            for i,x in enumerate(widgets_to_add): 
                my_add_widget(w=widget, w_widget_stack=widget_stack, w_to_add=x, index_to_insert_at= first_element_index +i )

    
        widget.setCurrentWidget(widgets_to_add[0])   
    def x(self):
        global widget_stack
        global widget

        if len(widget_stack) >0:
            first_element_index = get_index_of_widget(w=widget, w_widget_to_get_index_for=widget_stack[0])
        else:
            first_element_index = None

        len_widget_stack = len(widget_stack)
        for i in range(len_widget_stack):
            widget, widget_stack = remove_last_widget(w=widget, w_widget_stack=widget_stack)

        x=soundform()
        x.label_2.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\soundvideo\L.mp4")))


        #instances
        xword1=wordform()
        xword2=wordform()
        xword3=wordform()
        xword4=wordform()
        xword5=wordform()
        xword6=wordform()
        xword7=wordform()
        xword8=wordform()
        #words
        xword1.wordlable.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\">    <span style=\" font-size:20pt; color:#ee5445;\">????</span><span style=\" font-size:20pt; color:#000000;\">????</span>   <span style=\" font-size:20pt; color:#000000;\">    Uncle </span>     </p><p align=\"center\"><br/></p>  </body></html>",None))
        xword2.wordlable.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\">    <span style=\" font-size:20pt; color:#ee5445;\">????</span><span style=\" font-size:20pt; color:#000000;\">????</span>   <span style=\" font-size:20pt; color:#000000;\">    Good </span>     </p><p align=\"center\"><br/></p>  </body></html>",None))
        xword3.wordlable.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\">    <span style=\" font-size:20pt; color:#ee5445;\">????</span><span style=\" font-size:20pt; color:#000000;\">??????</span>   <span style=\" font-size:20pt; color:#000000;\">    Exist </span>     </p><p align=\"center\"><br/></p>  </body></html>",None))
        xword4.wordlable.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\">   <span style=\" font-size:20pt; color:#000000;\">??</span><span style=\" font-size:20pt; color:#ee5445;\">????</span><span style=\" font-size:20pt; color:#000000;\">????????</span>         <span style=\" font-size:20pt; color:#000000;\">   Exam </span>       </p><p align=\"center\"><br/></p>   </body></html>",None))
        xword5.wordlable.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\">   <span style=\" font-size:20pt; color:#000000;\">??</span><span style=\" font-size:20pt; color:#ee5445;\">??</span>    <span style=\" font-size:20pt; color:#000000;\">   Brother </span>       </p><p align=\"center\"><br/></p>   </body></html>",None))
        xword6.wordlable.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\">    <span style=\" font-size:20pt; color:#000000;\">????</span><span style=\" font-size:20pt; color:#ee5445;\">??</span>   <span style=\" font-size:20pt; color:#000000;\">    Brain </span>     </p><p align=\"center\"><br/></p>  </body></html>",None))
        xword7.wordlable.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; color:#000000;\">????</span><span style=\" font-size:20pt; color:#ee5445;\">??????</span><span style=\" font-size:20pt; color:#000000;\">????</span> <span style=\" font-size:20pt; color:#000000;\">   Avarice </span></p><p align=\"center\"><br/></p></body></html>",None))
        xword8.wordlable.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; color:#000000;\">????</span><span style=\" font-size:20pt; color:#ee5445;\">??????</span><span style=\" font-size:20pt; color:#000000;\">????</span> <span style=\" font-size:20pt; color:#000000;\">   Hot </span></p><p align=\"center\"><br/></p></body></html>",None))

        #images
        xword1.image.setPixmap(QPixmap(r"E:\graduation project\application\images\??????.jfif"))
        xword1.image.setScaledContents(True)
        xword2.image.setPixmap(QPixmap(r"E:\graduation project\application\images\??????.png"))
        xword2.image.setScaledContents(True)
        xword3.image.setPixmap(QPixmap(r"E:\graduation project\application\images\????????.jfif"))
        xword3.image.setScaledContents(True)
        xword5.image.setPixmap(QPixmap(r"E:\graduation project\application\images\????.jfif"))
        xword5.image.setScaledContents(True)
        xword4.image.setPixmap(QPixmap(r"E:\graduation project\application\images\????????????.jfif"))
        xword4.image.setScaledContents(True)
        xword6.image.setPixmap(QPixmap(r"E:\graduation project\application\images\????.jfif"))
        xword6.image.setScaledContents(True)
        xword7.image.setPixmap(QPixmap(r"E:\graduation project\application\images\??????.jfif"))
        xword7.image.setScaledContents(True)
        xword8.image.setPixmap(QPixmap(r"E:\graduation project\application\images\??????.png"))
        xword8.image.setScaledContents(True)
        #audios 
        xword1.wordsound.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\??????.mp3")))
        xword2.wordsound.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\??????.mp3")))
        xword3.wordsound.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\????????.mp3")))
        xword4.wordsound.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\????.mp3")))
        xword5.wordsound.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\????????????.mp3")))
        xword6.wordsound.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\????.mp3")))
        xword7.wordsound.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\??????.mp3")))
        xword8.wordsound.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\??????.mp3")))


        #ex
        xex1=ex_2()
        xex2=ex()
        xex3=ex_2()
        cong=congrat()
        xex1.wordname.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:26pt; color:#ffffff;\"> /x/ </span></p></body></html>")
        xex1.soundname.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:26pt; color:#ffffff;\"> Sound /x/ </span></p></body></html>")
        xex2.wordname.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:26pt; color:#ffffff;\"> /x/</span></p></body></html>")
        xex2.soundname.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:26pt; color:#ffffff;\"> Sound /x/ </span></p></body></html>")
        xex3.wordname.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:26pt; color:#ffffff;\"> /x/ </span></p></body></html>")
        xex3.soundname.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:26pt; color:#ffffff;\"> Sound /x/ </span></p></body></html>")
        xex1.B1.setText("????????")
        xex1.B2.setText("????????")
        xex1.wordsoundb1.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\????????.mp3")))
        xex1.wordsoundb2.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\????????.mp3")))
        xex2.B1.setText("??????")
        xex2.B2.setText("??????")
        xex2.wordsoundb1.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\??????.mp3")))
        xex2.wordsoundb2.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\??????.mp3")))
        xex3.B1.setText("????????")
        xex3.B2.setText("????????")
        xex3.wordsoundb1.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\????????.mp3")))
        xex3.wordsoundb2.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\????????.mp3")))
        #images
        xex1.label_5.setPixmap(QPixmap(r"E:\graduation project\application\images\????????.jpg"))
        xex1.label_5.setScaledContents(True)
        xex1.label_4.setPixmap(QPixmap(r"E:\graduation project\application\images\????????.jfif"))
        xex1.label_4.setScaledContents(True)

        xex2.label_5.setPixmap(QPixmap(r"E:\graduation project\application\images\??????.jfif"))
        xex2.label_5.setScaledContents(True)
        xex2.label_4.setPixmap(QPixmap(r"E:\graduation project\application\images\??????.jfif"))
        xex2.label_4.setScaledContents(True)

        xex3.label_5.setPixmap(QPixmap(r"E:\graduation project\application\images\????????.jpg"))
        xex3.label_5.setScaledContents(True)
        xex3.label_4.setPixmap(QPixmap(r"E:\graduation project\application\images\????????.jfif"))
        xex3.label_4.setScaledContents(True)

        widgets_to_add = [x, xword1, xword2, xword3, xword4, xword5, xword6,xword7, xword8, xex1, xex2, xex3, cong]

        #widgets arrangment 
        if first_element_index is None:
            
            for x in widgets_to_add: 
                my_add_widget(w=widget, w_widget_stack=widget_stack, w_to_add=x)

        else:
            for i,x in enumerate(widgets_to_add): 
                my_add_widget(w=widget, w_widget_stack=widget_stack, w_to_add=x, index_to_insert_at= first_element_index +i )

    
        widget.setCurrentWidget(widgets_to_add[0])
    def l(self):
        global widget_stack
        global widget

        if len(widget_stack) >0:
            first_element_index = get_index_of_widget(w=widget, w_widget_to_get_index_for=widget_stack[0])
        else:
            first_element_index = None

        len_widget_stack = len(widget_stack)
        for i in range(len_widget_stack):
            widget, widget_stack = remove_last_widget(w=widget, w_widget_stack=widget_stack)

        L=soundform()
        L.label_2.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\soundvideo\L.mp4")))


        #instances
        Lword1=wordform()
        Lword2=wordform()
        Lword3=wordform()
        Lword4=wordform()
        Lword5=wordform()
        Lword6=wordform()
        Lword7=wordform()
        Lword8=wordform()
        #words
        Lword1.wordlable.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\">  <span style=\" font-size:20pt; color:#000000;\">??????</span><span style=\" font-size:20pt; color:#ee5445;\">??????</span><span style=\" font-size:20pt; color:#000000;\">????</span>   <span style=\" font-size:20pt; color:#000000;\">    Eduction  </span>     </p><p align=\"center\"><br/></p>  </body></html>",None))
        Lword2.wordlable.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\">    <span style=\" font-size:20pt; color:#ee5445;\">????</span><span style=\" font-size:20pt; color:#000000;\">????</span>   <span style=\" font-size:20pt; color:#000000;\">    Blame </span>     </p><p align=\"center\"><br/></p>  </body></html>",None))
        Lword3.wordlable.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\">    <span style=\" font-size:20pt; color:#ee5445;\">????</span><span style=\" font-size:20pt; color:#000000;\">??????</span>   <span style=\" font-size:20pt; color:#000000;\">    Lamp</span>     </p><p align=\"center\"><br/></p>  </body></html>",None))
        Lword4.wordlable.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\">   <span style=\" font-size:20pt; color:#000000;\">??????????</span><span style=\" font-size:20pt; color:#ee5445;\">??</span>         <span style=\" font-size:20pt; color:#000000;\">   Future </span>       </p><p align=\"center\"><br/></p>   </body></html>",None))
        Lword5.wordlable.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\">   <span style=\" font-size:20pt; color:#000000;\">????????</span><span style=\" font-size:20pt; color:#ee5445;\">??</span>         <span style=\" font-size:20pt; color:#000000;\">   pretty </span>       </p><p align=\"center\"><br/></p>   </body></html>",None))
        Lword6.wordlable.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\">    <span style=\" font-size:20pt; color:#000000;\">??????</span><span style=\" font-size:20pt; color:#ee5445;\">????</span>  <span style=\" font-size:20pt; color:#000000;\">    Onion </span>     </p><p align=\"center\"><br/></p>  </body></html>",None))
        Lword7.wordlable.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; color:#000000;\">????</span><span style=\" font-size:20pt; color:#ee5445;\">??????</span><span style=\" font-size:20pt; color:#000000;\">????</span> <span style=\" font-size:20pt; color:#000000;\">   Avarice </span></p><p align=\"center\"><br/></p></body></html>",None))
        Lword8.wordlable.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; color:#000000;\">????</span><span style=\" font-size:20pt; color:#ee5445;\">??????</span><span style=\" font-size:20pt; color:#000000;\">??????</span> <span style=\" font-size:20pt; color:#000000;\">   Avarice </span></p><p align=\"center\"><br/></p></body></html>",None))

        #images
        Lword1.image.setPixmap(QPixmap(r"E:\graduation project\application\images\??????????.jfif"))
        Lword1.image.setScaledContents(True)
        Lword2.image.setPixmap(QPixmap(r"E:\graduation project\application\images\??????.jfif"))
        Lword2.image.setScaledContents(True)
        Lword3.image.setPixmap(QPixmap(r"E:\graduation project\application\images\????????.jfif"))
        Lword3.image.setScaledContents(True)
        Lword4.image.setPixmap(QPixmap(r"E:\graduation project\application\images\????????????.jfif"))
        Lword4.image.setScaledContents(True)
        Lword5.image.setPixmap(QPixmap(r"E:\graduation project\application\images\????????.jfif"))
        Lword5.image.setScaledContents(True)
        Lword6.image.setPixmap(QPixmap(r"E:\graduation project\application\images\??????.jfif"))
        Lword6.image.setScaledContents(True)
        Lword7.image.setPixmap(QPixmap(r"E:\graduation project\application\images\??????.jpg"))
        Lword7.image.setScaledContents(True)
        Lword8.image.setPixmap(QPixmap(r"E:\graduation project\application\images\????????.jpg"))
        Lword8.image.setScaledContents(True)
        #audios 
        Lword1.wordsound.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\??????????.mp3")))
        Lword2.wordsound.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\??????.mp3")))
        Lword3.wordsound.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\????????.mp3")))
        Lword4.wordsound.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\????????????.mp3")))
        Lword5.wordsound.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\????????.mp3")))
        Lword6.wordsound.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\??????.mp3")))
        Lword7.wordsound.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\??????.mp3")))
        Lword8.wordsound.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\????????.mp3")))

        #ex
        Lex1=ex_2()
        Lex2=ex_2()
        Lex3=ex()
        cong=congrat()
        Lex1.wordname.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:26pt; color:#ffffff;\"> /l/ </span></p></body></html>")
        Lex1.soundname.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:26pt; color:#ffffff;\"> Sound /l/ </span></p></body></html>")
        Lex2.wordname.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:26pt; color:#ffffff;\"> /l/ </span></p></body></html>")
        Lex2.soundname.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:26pt; color:#ffffff;\"> Sound /l/ </span></p></body></html>")
        Lex3.wordname.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:26pt; color:#ffffff;\"> /l/ </span></p></body></html>")
        Lex3.soundname.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:26pt; color:#ffffff;\"> Sound /l/ </span></p></body></html>")
        Lex1.B1.setText("??????")
        Lex1.B2.setText("??????")
        Lex1.wordsoundb1.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\??????.mp3")))
        Lex1.wordsoundb2.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\??????.mp3")))
        Lex2.B1.setText("??????")
        Lex2.B2.setText("??????")
        Lex2.wordsoundb1.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\??????.mp3")))
        Lex2.wordsoundb2.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\??????.mp3")))
        Lex3.B1.setText("??????")
        Lex3.B2.setText("????????")
        Lex3.wordsoundb1.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\??????.mp3")))
        Lex3.wordsoundb2.setMedia(QMediaContent(QUrl.fromLocalFile(r"E:\graduation project\application\recorded words\????????.mp3")))
        #images
        Lex1.label_5.setPixmap(QPixmap(r"E:\graduation project\application\images\??????.jfif"))
        Lex1.label_5.setScaledContents(True)
        Lex1.label_4.setPixmap(QPixmap(r"E:\graduation project\application\images\??????.jfif"))
        Lex1.label_4.setScaledContents(True)

        Lex2.label_5.setPixmap(QPixmap(r"E:\graduation project\application\images\??????.jpg"))
        Lex2.label_5.setScaledContents(True)
        Lex2.label_4.setPixmap(QPixmap(r"E:\graduation project\application\images\??????.jfif"))
        Lex2.label_4.setScaledContents(True)

        Lex3.label_5.setPixmap(QPixmap(r"E:\graduation project\application\images\??????.JPG"))
        Lex3.label_5.setScaledContents(True)
        Lex3.label_4.setPixmap(QPixmap(r"E:\graduation project\application\images\????????.jpg"))
        Lex3.label_4.setScaledContents(True)

        widgets_to_add = [L, Lword1, Lword2, Lword3, Lword4, Lword5, Lword6, Lword7, Lword8, Lex1, Lex2, Lex3, cong]

        #widgets arrangment 
        if first_element_index is None:
            
            for x in widgets_to_add: 
                my_add_widget(w=widget, w_widget_stack=widget_stack, w_to_add=x)

        else:
            for i,x in enumerate(widgets_to_add): 
                my_add_widget(w=widget, w_widget_stack=widget_stack, w_to_add=x, index_to_insert_at= first_element_index +i )

        widget.setCurrentWidget(widgets_to_add[0])
#========================================================================================================================================================================
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1097, 731)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.friendslevel = QtWidgets.QPushButton(self.centralwidget)
        self.friendslevel.setGeometry(QtCore.QRect(460, 570, 221, 41))
        self.friendslevel.setStyleSheet("font: 16pt \"Permanent Marker\";\n"
    "color: rgb(255, 255, 255);\n"
    "border-radius: 10px 10px 20px 20px;\n"
    "background-color: rgb(238, 238, 0);\n"
    "opacity: 1;")
        self.friendslevel.setObjectName("friendslevel")
        self.enemieslevel = QtWidgets.QPushButton(self.centralwidget)
        self.enemieslevel.setGeometry(QtCore.QRect(110, 570, 221, 41))
        self.enemieslevel.setStyleSheet("background: rgb(0, 195, 122);\n"
    "font: 16pt \"Permanent Marker\";\n"
    "color: rgb(255, 255, 255);\n"
    "border-radius: 10px 10px 20px 20px;\n"
    "opacity: 1;")
        self.enemieslevel.setObjectName("enemieslevel")
        self.hi = QtWidgets.QLabel(self.centralwidget)
        self.hi.setGeometry(QtCore.QRect(260, 40, 631, 61))
        self.hi.setStyleSheet("border-radius: 25px 25px 35px 35px;\n"
    "font: 20pt \"MS Shell Dlg 2\";\n"
    "background-color: rgb(248, 248, 248);")
        self.hi.setObjectName("hi")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(480, 160, 181, 41))
        self.label_4.setStyleSheet("font: 18pt \"MS Shell Dlg 2\";")
        self.label_4.setObjectName("label_4")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(800, 270, 241, 281))
        self.label_6.setStyleSheet("border-radius: 25px 25px 35px 35px;\n"
    "font: 20pt \"MS Shell Dlg 2\";\n"
    "background-color: rgb(255, 255, 255);")
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap("F:\\Ghada\\4thYear\\GradProject/application/images/family.png"))
        self.label_6.setScaledContents(True)
        self.label_6.setObjectName("label_6")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(100, 270, 241, 281))
        self.label_2.setStyleSheet("border-radius: 25px 25px 35px 35px;\n"
    "font: 20pt \"MS Shell Dlg 2\";\n"
    "background-color: rgb(255, 255, 255);")
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("F:\\Ghada\\4thYear\\GradProject/application/images/lion-dance.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(450, 270, 241, 281))
        self.label_3.setStyleSheet("border-radius: 25px 25px 35px 35px;\n"
    "font: 20pt \"MS Shell Dlg 2\";\n"
    "background-color: rgb(255, 255, 255);")
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("F:\\Ghada\\4thYear\\GradProject/application/images/deal.png"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.familylevel = QtWidgets.QPushButton(self.centralwidget)
        self.familylevel.setGeometry(QtCore.QRect(810, 570, 221, 41))
        self.familylevel.setStyleSheet("font: 16pt \"Permanent Marker\";\n"
    "background-color: rgb(66, 33, 255);\n"
    "color: rgb(255, 255, 255);\n"
    "border-radius: 10px 10px 20px 20px;\n"
    "opacity: 1;")
        self.familylevel.setObjectName("familylevel")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1097, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.enemieslevel.clicked.connect(self.Enemies)
        self.friendslevel.clicked.connect(self.Friends)
        self.familylevel.clicked.connect(self.Family)

   

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.friendslevel.setText(_translate("MainWindow", "friends level"))
        self.enemieslevel.setText(_translate("MainWindow", "enemies level"))
        self.hi.setText(_translate("MainWindow", "     Hi, "))
        self.label_4.setText(_translate("MainWindow", "Choose level"))
        self.familylevel.setText(_translate("MainWindow", "family level"))
class soundform(QDialog):
    def __init__(self):
        super(soundform,self).__init__()
        loadUi(r"E:\graduation project\application\SoundForm.ui",self)

        #create media player object
        self.label_2 = QMediaPlayer(None, QMediaPlayer.VideoSurface)
        #self.player = QtMultimedia.QMediaPlayer()

        

        #create videowidget object
        videowidget = QVideoWidget()
        self.label_2.setVideoOutput(videowidget)
        self.vboxLayout.addWidget(videowidget)
    
        #clicked
        self.gtexercices.clicked.connect(self.gonext)
        self.backbutton.clicked.connect(self.back)
        self.playBtn.clicked.connect(self.play_video)
    #    self.soundBtn.clicked.connect(self.playsound)        
    def gonext(self):
        #wordform1=wordform()
        #widget.addWidget(wordform1)
        widget.setCurrentIndex(widget.currentIndex()+1)
    def back(self):
        form=soundform()
        widget.addWidget(form)
        widget.setCurrentIndex(widget.currentIndex()-1)
    def play_video(self):
        self.label_2.play()

class wordform(QDialog):
    def __init__(self):
        super(wordform,self).__init__()
        loadUi(r"E:\graduation project\application\Wordsform.ui",self)
        self.NextButton.clicked.connect(self.gonext)  
        self.backbutton.clicked.connect(self.back)
        self.micButton.clicked.connect(self.ConvertAudio)
        self.Listenbtn.clicked.connect(self.play)

        self.wordsound=QtMultimedia.QMediaPlayer()
        
    def gonext(self):
        exform=ex()
        widget.addWidget(exform)
        widget.setCurrentIndex(widget.currentIndex()+1)
    def back(self):
        widget.setCurrentIndex(widget.currentIndex()-1)
    def ConvertAudio(self):
        import pyaudio
        import speech_recognition as sr
        r=sr.Recognizer()
        with sr.Microphone() as source:
                audio=r.listen(source)
                text=r.recognize_google(audio,language="ar-EG")
                word=self.wordlable.text()
                if text in word:
                    self.msgRecbox.setText( "              BRAVO      " )
                    self.msgRecbox.setStyleSheet("background-color: rgb(15, 212, 48);\n"
                    "font: 75 18pt \"MS Shell Dlg 2\";\n"
                    "border-radius: 40px 40px 50px 50px;\n"
                    "opacity: 1;")
                elif "????????" in text or "??????"  in text or "????????" in text: #qaf errors
                    self.msgRecbox.setText( "               BRAVO      " )
                    self.msgRecbox.setStyleSheet("background-color: rgb(15, 212, 48);\n"
                    "font: 75 18pt \"MS Shell Dlg 2\";\n"
                    "border-radius: 40px 40px 50px 50px;\n"
                    "opacity: 1;")
                elif "??????"  in text or "????????" in text or "????????????"in text or "????????" in text: #glottal and 3ain errors 
                    self.msgRecbox.setText( "               BRAVO      " )
                    self.msgRecbox.setStyleSheet("background-color: rgb(15, 212, 48);\n"
                    "font: 75 18pt \"MS Shell Dlg 2\";\n"
                    "border-radius: 40px 40px 50px 50px;\n"
                    "opacity: 1;")
                elif text=="????????":
                    self.msgRecbox.setText( "               BRAVO      " )
                    self.msgRecbox.setStyleSheet("background-color: rgb(15, 212, 48);\n"
                    "font: 75 18pt \"MS Shell Dlg 2\";\n"
                    "border-radius: 40px 40px 50px 50px;\n"
                    "opacity: 1;")
                elif text=="????????"  or text == "??????" or text=="????????": #gain and Saad
                    self.msgRecbox.setText( "               BRAVO      " )
                    self.msgRecbox.setStyleSheet("background-color: rgb(15, 212, 48);\n"
                    "font: 75 18pt \"MS Shell Dlg 2\";\n"
                    "border-radius: 40px 40px 50px 50px;\n"
                    "opacity: 1;")
                else:
                    self.msgRecbox.setText("         Try again       ")
                    self.msgRecbox.setStyleSheet("background-color: rgb(255, 42, 0);\n"
                    "font: 75 18pt \"MS Shell Dlg 2\";\n"
                    "border-radius: 40px 40px 50px 50px;\n"
                    "opacity: 1;")
     
    def play(self,filename):
        self.wordsound.play()
class ex (QDialog):
    def __init__(self):
        super(ex,self).__init__()
        loadUi(r"E:\graduation project\application\exerciseButtonOne.ui",self)
        self.nextbutton.clicked.connect(self.gonext)
        #self.backbutton.clicked.connect(self.back)
        self.wordsoundb1=QtMultimedia.QMediaPlayer()
        self.B1.clicked.connect(self.ButtonOne)
        self.B2.clicked.connect(self.ButtonTwo)
        self.wordsoundb2=QtMultimedia.QMediaPlayer()
        self.SB1.clicked.connect(self.play)
        self.SB2.clicked.connect(self.play2)
    def ButtonOne(self):
        self.label_2.setText("                     Well Done!    ")
        self.label_2.setStyleSheet("border-radius: 20px 20px 35px 35px;\n"
                "background-color: rgb(15, 212, 48);\n"
                    "font: 75 18pt \"MS Shell Dlg 2\";\n"
                    "opacity: 1;")

    def ButtonTwo(self):
        self.label_2.setText("                     Try Again!    ")
        self.label_2.setStyleSheet("border-radius: 20px 20px 35px 35px;\n"
        "background-color: rgb(255, 42, 0);\n" "font: 75 18pt \"MS Shell Dlg 2\";\n" "opacity: 1;")

    def play(self,filename):
            self.wordsoundb1.play()

    def play2(self,filename):
            self.wordsoundb2.play()
    def gonext(self):
    #    exform_2=ex_2()
    #    widget.addWidget(exform_2)
        widget.setCurrentIndex(widget.currentIndex()+1)
    #def back(self):
    #    exform=ex()
    #    widget.addWidget(exform)
    #    widget.setCurrentIndex(widget.currentIndex()-1)

class ex_2 (QDialog):
    def __init__(self):
        super(ex_2,self).__init__()
        loadUi(r"E:\graduation project\application\exerciseButtonTwo.ui",self)
        self.nextbutton.clicked.connect(self.gonext)
        #self.backbutton.clicked.connect(self.back)
        self.B1.clicked.connect(self.ButtonOne)
        self.B2.clicked.connect(self.ButtonTwo)
        self.wordsoundb1=QtMultimedia.QMediaPlayer()
        self.wordsoundb2=QtMultimedia.QMediaPlayer()

        self.SB1.clicked.connect(self.play)
        self.SB2.clicked.connect(self.play2)

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
    def play(self,filename):
        self.wordsoundb1.play()
    
    def play2(self,filename):
        self.wordsoundb2.play()
    def gonext(self):
    #    cong=congrat()
    #    widget.addWidget(cong)
        widget.setCurrentIndex(widget.currentIndex()+1)
    #def back(self):
    #    exform_2=ex_2()
    #    widget.addWidget(exform_2)
    #    widget.setCurrentIndex(widget.currentIndex()-1)

class congrat(QDialog):
    def __init__(self):
        super(congrat,self).__init__()
        loadUi(r"E:\graduation project\application\congratulations.ui",self)
        self.backhome.clicked.connect(self.home)
    def home(self):
        global enemies 
        global friends
        widget.setCurrentIndex(1)

app=QApplication(sys.argv)
widget=QtWidgets.QStackedWidget()
widget_stack = []

def my_add_widget(w:QtWidgets.QStackedWidget, w_to_add, w_widget_stack, index_to_insert_at:int=None):

    if index_to_insert_at is not None:#list maliana 
        w.insertWidget(index_to_insert_at, w_to_add)  # just like the normal addWidget.. nothing new
    else:
        w.addWidget(w_to_add)

    w_widget_stack.append(w_to_add)  # global variable to keep track of the stack widgets

    return w, w_widget_stack

def remove_last_widget(w, w_widget_stack):
    w_to_remove = w_widget_stack[-1] # ?????? ???? ?????? ???????????? 
    w.removeWidget(w_to_remove)
    del w_widget_stack[-1]

    return w, w_widget_stack

def get_index_of_widget(w, w_widget_to_get_index_for):
    return w.indexOf(w_widget_to_get_index_for)

def remove():
    for i in reversed(range(widget).count()-2):
            widget(i).widget().setParent(None)
            print("d")
#instances 
log=log()
#Adding Widgets for the QStackWidget
widget.addWidget(log)
#fixed size
widget.setFixedHeight(800)
widget.setFixedWidth(1280)
#show 
widget.setWindowTitle("????????")
widget.setWindowIcon(QIcon(r"E:\graduation project\application\images\??.JPG"))
widget.show()
app.exec_()