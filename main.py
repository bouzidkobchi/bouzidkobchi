import sys
import PyQt5
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.uic import *
from PyQt5 import uic
from tkinter import filedialog as fd
class UI(QMainWindow):
    def __init__(self):
        super(UI,self).__init__()
        uic.loadUi('app.ui',self)
        self.show()
        self.btn1 = self.findChild(QPushButton,'pushButton_14')
        self.btn1.clicked.connect(self.choose_a_color)
        self.btn2 = self.findChild(QPushButton,'pushButton_37')
        self.btn2.clicked.connect(self.choose_a_file)
    def choose_a_color(self):
        rgb = QColorDialog().getColor(title='choose a color here !')
        # print('you choose '+ str(rgb))
        self.bt = QPushButton('abdellah bechraire',self)
        self.bt.resize(80,80)
        self.bt.move(100,100)
        self.bt.setStyleSheet(f'background-color:red;')
        pass
    def choose_a_file(self):
        filename = fd.askopenfilename()
        print(f"the adress of choozen file is {filename}")
app = QApplication(sys.argv)
window = UI()
app.exec_()
