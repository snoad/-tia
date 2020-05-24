from PyQt5.QtWidgets import (QMessageBox,QApplication, QWidget, QToolTip, QPushButton,
                             QDesktopWidget, QMainWindow, QAction, qApp, QToolBar, QVBoxLayout,
                             QComboBox,QLabel,QLineEdit,QGridLayout,QMenuBar,QMenu,QStatusBar,
                             QTextEdit,QDialog,QFrame,QProgressBar
                             )
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtGui import QIcon,QFont,QPixmap,QPalette
from PyQt5.QtCore import QCoreApplication, Qt,QBasicTimer, QPoint
from functools import partial
import sys
import winsound
import os

class cssden(QMainWindow):
    def __init__(self):
        super().__init__()


        self.mwidget = QMainWindow(self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)


        #size
        self.setFixedSize(260, 180)
        self.center()


        #label
        self.lbl = QLabel(self)
        self.lbl.setPixmap(QPixmap("s111.png"))
        self.lbl.setGeometry(0,0,260,190)
        self.oldPos = self.pos()
		#button
        self.but1=QPushButton(self)
        self.but1.setGeometry(0,0,90,85)
        self.but2=QPushButton(self)
        self.but2.setGeometry(85,0,90,85)
        self.but3=QPushButton(self)
        self.but3.setGeometry(170,0,90,85)
        self.but4=QPushButton(self)
        self.but4.setGeometry(0,85,90,85)
        self.but5=QPushButton(self)
        self.but5.setGeometry(85,85,90,85)
        self.but6=QPushButton(self)
        self.but6.setGeometry(170,85,90,85)
        op1 = QtWidgets.QGraphicsOpacityEffect()  
        op1.setOpacity(0)#透明度 
        op2 = QtWidgets.QGraphicsOpacityEffect()  
        op2.setOpacity(0)#透明度 
        op3 = QtWidgets.QGraphicsOpacityEffect()  
        op3.setOpacity(0)#透明度         
        op4 = QtWidgets.QGraphicsOpacityEffect()  
        op4.setOpacity(0)#透明度         
        op5 = QtWidgets.QGraphicsOpacityEffect()  
        op5.setOpacity(0)#透明度         
        op6 = QtWidgets.QGraphicsOpacityEffect()  
        op6.setOpacity(0)#透明度         

        self.but1.setGraphicsEffect(op1)
        self.but2.setGraphicsEffect(op2) 
        self.but3.setGraphicsEffect(op3) 
        self.but4.setGraphicsEffect(op4) 
        self.but5.setGraphicsEffect(op5) 
        self.but6.setGraphicsEffect(op6) 
        self.but1.setAutoFillBackground(True)
        self.but2.setAutoFillBackground(True)
        self.but3.setAutoFillBackground(True)
        self.but4.setAutoFillBackground(True)
        self.but5.setAutoFillBackground(True)
        self.but6.setAutoFillBackground(True)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        
        self.show()

        
    #center
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def mousePressEvent(self, event):
        self.oldPos = event.globalPos()

    def mouseMoveEvent(self, event):
        delta = QPoint (event.globalPos() - self.oldPos)
        #print(delta)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = event.globalPos()

def covent1(ui):
    
    QApplication.processEvents()
    winsound.PlaySound("mp3\铷啊.wav",flags=1)
def covent2(ui):
    
    QApplication.processEvents()
    winsound.PlaySound("mp3\笨蛋(1).wav",flags=1)
def covent3(ui):
    
    QApplication.processEvents()
    winsound.PlaySound("mp3\奶酥.wav",flags=1)
def covent4(ui):
    
    QApplication.processEvents()
    winsound.PlaySound("mp3\搞死你.wav",flags=1)
def covent5(ui):
    
    QApplication.processEvents()
    winsound.PlaySound("mp3\被射死啦.wav",flags=1)

def covent6(ui):
    
    QApplication.processEvents()
    winsound.PlaySound("mp3\啊~.wav",flags=1)
"""     self.but1.setGraphicsEffect(op)  
        self.but2.setGraphicsEffect(op)  
        self.but3.setGraphicsEffect(op)  
        self.but4.setGraphicsEffect(op)  
        self.but5.setGraphicsEffect(op)  
        self.but6.setGraphicsEffect(op)  
        self.but1.setAutoFillBackground(True)"""

if __name__=="__main__":
    app = QApplication(sys.argv)
    
    app.setStyleSheet("QLabel{background: WA_TranslucentBackground;}")
    app.setStyleSheet("QPushButton{background: transparent;}")
    app.setStyleSheet("QMainWindow{background: #FFFFFF;}")

    
    ex = cssden()
    ex.setWindowOpacity(1);
    ex.but1.clicked.connect(partial(covent1,ex))
    ex.but2.clicked.connect(partial(covent2,ex))
    ex.but3.clicked.connect(partial(covent3,ex))
    ex.but4.clicked.connect(partial(covent4,ex))
    ex.but5.clicked.connect(partial(covent5,ex))
    ex.but6.clicked.connect(partial(covent6,ex))
    sys.exit(app.exec_())
