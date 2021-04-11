# -*- coding: utf-8 -*-
import sys
#the setting of UI of the main dialog
from UiSet import Ui_Dialog
import cv2 as cv
import numpy as np
import requests
from PyQt5 import QtCore
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QApplication, QDialog, QFileDialog, QGridLayout, QLabel, QPushButton, QGroupBox

#The global variable. An id corresponds to a web link. 
idd = '0'
#the main dialog
class MainDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
    
    #Classification query
    def queryArticle(self):
        Category = self.ui.comboBox1.currentText()
        Type = self.ui.comboBox2.currentText()
        #Find by option
        if Category == 'Girl':
            CategoryCode = 'Girl'
            TypeCode = 'Girl'
        else:
            CategoryCode = self.get_CategoryCode(Category)
            TypeCode = self.get_TypeCode(Type)
        #Corresponding API 
        self.r = requests.get("https://gank.io/api/v2/data/category/{}/type/{}/page/1/count/10".format(CategoryCode,TypeCode))
        if self.r.json().get('status') == 100:
            l = len(self.r.json()['data'])
            #Output after successful query
            if l >=3:
                Msg2 = 'title:{}\ndata:{}\nauthor:{}\ndescribe:{}'.format(
                    self.r.json()['data'][0]['title'],
                    self.r.json()['data'][0]['createdAt'],
                    self.r.json()['data'][0]['author'],
                    self.r.json()['data'][0]['title']
                )
                Msg3 = 'title:{}\ndata:{}\nauthor:{}\ndescribe:{}'.format(
                    self.r.json()['data'][1]['title'],
                    self.r.json()['data'][1]['createdAt'],
                    self.r.json()['data'][1]['author'],
                    self.r.json()['data'][1]['desc']
                )
                Msg4 = 'title:{}\ndata:{}\nauthor:{}\ndescribe:{}'.format(
                    self.r.json()['data'][2]['title'],
                    self.r.json()['data'][2]['createdAt'],
                    self.r.json()['data'][2]['author'],
                    self.r.json()['data'][2]['title']
                )
            else:
                Msg2 = 'No Data'
                Msg3 = 'No Data'
                Msg4 = 'No Data'
        else:
            Msg2 = 'Query failed, please try later!'
            Msg3 = 'Query failed, please try later!'
            Msg4 = 'Query failed, please try later!'
        self.ui.textEdit2.setText(Msg2)
        self.ui.textEdit3.setText(Msg3)
        self.ui.textEdit4.setText(Msg4)
    
    #Option converted to api code (Category Code)
    def get_CategoryCode(self, Category):
        CategoryDict = {"Article": "Article",
                    "Skill": "GanHuo",
                    "Girl": "Girl"}  
        return CategoryDict.get(Category)
    #Option converted to api code (Type Code)
    def get_TypeCode(self, Type):
        CategoryDict = {"Android": "Android",
                    "iOS": "iOS",
                    "Flutter": "Flutter",
                    "Frontend":"frontend",
                    "app":"app"}
        return CategoryDict.get(Type)
    #Clear the search box 
    def clearText(self):
        self.ui.textEdit.clear()
    #serch the text of the search box
    def searchText(self):
        item = self.ui.textEdit.text()
        self.r = requests.get("https://gank.io/api/v2/search/{}/category/All/type/All/page/1/count/10".format(item))
        if self.r.json().get('status') == 100:
            #Output after successful query
            l = len(self.r.json()['data'])
            if l >=3:
                Msg2 = 'title:{}\ndata:{}\nauthor:{}\ndescribe:{}'.format(
                    self.r.json()['data'][0]['title'],
                    self.r.json()['data'][0]['createdAt'],
                    self.r.json()['data'][0]['author'],
                    self.r.json()['data'][0]['title']
                )
                Msg3 = 'title:{}\ndata:{}\nauthor:{}\ndescribe:{}'.format(
                    self.r.json()['data'][1]['title'],
                    self.r.json()['data'][1]['createdAt'],
                    self.r.json()['data'][1]['author'],
                    self.r.json()['data'][1]['desc']
                )
                Msg4 = 'title:{}\ndata:{}\nauthor:{}\ndescribe:{}'.format(
                    self.r.json()['data'][2]['title'],
                    self.r.json()['data'][2]['createdAt'],
                    self.r.json()['data'][2]['author'],
                    self.r.json()['data'][2]['title']
                )
            else:
                Msg2 = 'No Data'
                Msg3 = 'No Data'
                Msg4 = 'No Data'
        else:
            Msg2 = 'Query failed, please try later!'
            Msg3 = 'Query failed, please try later!'
            Msg4 = 'Query failed, please try later!'
        self.ui.textEdit2.setText(Msg2)
        self.ui.textEdit3.setText(Msg3)
        self.ui.textEdit4.setText(Msg4)
    #Corresponds to the first detail button 
    def detialText1(self):
        global idd
        idd = self.r.json()['data'][0]['_id']
        if self.r.json()['data'][0]['category'] == 'Girl':
            self.child_win = NewWinGirl()
            self.child_win.show()
            self.child_win.exec_()
        else:
            self.child_win = NewWin()
            self.child_win.show()
            self.child_win.exec_()
    #Corresponds to the second detail button 
    def detialText2(self):
        global idd
        idd = self.r.json()['data'][1]['_id']
        if self.r.json()['data'][1]['category'] == 'Girl':
            self.child_win = NewWinGirl()
            self.child_win.show()
            self.child_win.exec_()
        else:
            self.child_win = NewWin()
            self.child_win.show()
            self.child_win.exec_()
    #Corresponds to the third detail button 
    def detialText3(self):
        global idd
        idd = self.r.json()['data'][2]['_id']
        if self.r.json()['data'][2]['category'] == 'Girl':
            self.child_win = NewWinGirl()
            self.child_win.show()
            self.child_win.exec_()
        else:
            self.child_win = NewWin()
            self.child_win.show()
            self.child_win.exec_()
#Secondary window of girl
class NewWinGirl(QDialog):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        global idd
        #Output information 
        self.r = requests.get("https://gank.io/api/v2/post/{}".format(idd))
        self.resize(300,200)
        self.btnQuit = QPushButton('Quit', self)
        self.lb1 = QLabel("content:\n{}".format(self.r.json()['data']['content']))
        self.lb2 = QLabel("email:{}".format(self.r.json()['data']['email']))
        self.lb3 = QLabel(self)
        self.lb3.setText("<A href='{}'>The Url</a>".format(self.r.json()['data']['images'][0]))
        self.lb3.setOpenExternalLinks(True)
        self.lb4 = QLabel("author:{}".format(self.r.json()['data']['author']))
        #GUI layout 
        layout = QGridLayout(self)
        layout.addWidget(self.lb4, 1, 1, 1, 1)
        layout.addWidget(self.lb1, 2, 1, 1, 1)
        layout.addWidget(self.lb2, 3, 1, 1, 1)
        layout.addWidget(self.lb3, 4, 1, 1, 1)
        layout.addWidget(self.btnQuit, 5, 4, 1, 1)
        #Associate button and quit
        self.btnQuit.clicked.connect(self.close)
#Secondary window of article and skills
class NewWin(QDialog):
    def __init__(self):
        super().__init__()
        self.initUI()
    #Output information 
    def initUI(self):
        global idd
        self.r = requests.get("https://gank.io/api/v2/post/{}".format(idd))
        self.resize(300,400)
        self.btnQuit = QPushButton('Quit', self)
        self.lb = QLabel(self)
        self.lb.setText("<A href='{}'>The Url</a>".format(self.r.json()['data']['url']))
        self.lb.setOpenExternalLinks(True)
        self.lb1 = QLabel("title:{}".format(self.r.json()['data']['title']))
        self.lb2 = QLabel("author:{}".format(self.r.json()['data']['author']))
        self.lb3 = QLabel("author:{}".format(self.r.json()['data']['createdAt']))
        self.lb4 = QLabel("type:{}-{}".format(self.r.json()['data']['category'],self.r.json()['data']['type']))
        self.lb5 = QLabel("views:{};like Counts:{}".format(self.r.json()['data']['views'],self.r.json()['data']['likeCounts']))
        self.lb6 = QLabel("description:{}".format(self.r.json()['data']['desc']))
        #GUI layout
        layout = QGridLayout(self)
        layout.addWidget(self.lb1, 1, 1, 1, 1)
        layout.addWidget(self.lb2, 2, 1, 1, 1)
        layout.addWidget(self.lb3, 3, 1, 1, 1)
        layout.addWidget(self.lb4, 4, 1, 1, 1)
        layout.addWidget(self.lb5, 5, 1, 1, 1)
        layout.addWidget(self.lb6, 6, 1, 1, 1)
        layout.addWidget(self.lb, 7, 1, 1, 1)
        layout.addWidget(self.btnQuit, 8, 4, 1, 1)
        #Associate button and quit
        self.btnQuit.clicked.connect(self.close)

if __name__ == '__main__':
    myapp = QApplication(sys.argv)
    myDlg = MainDialog()
    myDlg.show()
    sys.exit(myapp.exec_())