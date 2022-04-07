import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QIntValidator
from PyQt5.QtWidgets import QLabel, QWidget, QLineEdit
from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout
from PyQt5.QtWidgets import QPushButton, QGroupBox, QMessageBox
from PyQt5.QtCore import Qt, QMetaObject
import matplotlib.pyplot as plt
from torchvision.utils import make_grid
import cv2 as cv
import glob
import os
import numpy as np
import utils_Q5
import webbrowser
__appname__ = "cvdl Hw2 Q5_N76101012"

class MainWindow(object):

    def setupUI(self, MainScreen):
        MainScreen.setObjectName("MainScreen")
        MainScreen.resize(640,480)
        MainScreen.setWindowTitle(__appname__)


        
        grpQuestion5 = QGroupBox("5. Dog & Cate catgorization - RESNET 50")
        grpVerticleLayout = QVBoxLayout(grpQuestion5)

        self.btnShowStructure = QPushButton("5.1 Show model structure")
        self.btnDisplayTensorboard = QPushButton("5.2 Display tensorboard")

        grpTest = QGroupBox("5.3 Test")
        layoutMain = QVBoxLayout(grpTest)

        select_layout, self.edit_5_3 = self.CreateTexBox("Select image: ")
        layoutMain.addLayout(select_layout)
        self.btnPredict = QPushButton("5.3 Predict")
        layoutMain.addWidget(self.btnPredict)
        
        self.btnDisplayRandomEraserImg = QPushButton("5.4 Display Augumentation Random-Eraser images")

        grpVerticleLayout.addWidget(self.btnShowStructure)
        grpVerticleLayout.addWidget(self.btnDisplayTensorboard)
        
        grpVerticleLayout.addWidget(grpTest)
        grpVerticleLayout.addWidget(self.btnDisplayRandomEraserImg)
        self.centralwidget = QWidget(MainScreen)
        self.centralwidget.setObjectName("centralwidget")

        vLayout = QHBoxLayout()
        vLayout.addWidget(grpQuestion5)
        self.centralwidget.setLayout(vLayout)
        MainScreen.setCentralWidget(self.centralwidget)
        QMetaObject.connectSlotsByName(MainScreen)

    @staticmethod
    def CreateTexBox(title:str, unit = "", showUnit= False):
        hLayout = QHBoxLayout()
        title_label = QLabel(title)
        title_label.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        title_label.setFixedWidth(60)
        unit_label = QLabel(unit)
        unit_label.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        unit_label.setFixedWidth(30)
        editText = QLineEdit("1")
        editText.setFixedWidth(50)
        editText.setAlignment(Qt.AlignRight)
        editText.setValidator(QIntValidator())

        hLayout.addWidget(title_label, alignment=Qt.AlignLeft)
        hLayout.addWidget(editText)
        if showUnit:
            hLayout.addWidget(unit_label)
        return hLayout, editText

class MainScreen(QMainWindow, MainWindow):

    def __init__(self, parent = None):
        super(MainScreen, self).__init__(parent=parent)
        self.setupUI(self)
        self.initialValue()
        self.buildUi()

    def buildUi(self):
        self.btnShowStructure.clicked.connect(self.ShowModelStructure)
        self.btnDisplayTensorboard.clicked.connect(self.show_tensorboard)
        self.btnPredict.clicked.connect(self.test)
        self.btnDisplayRandomEraserImg.clicked.connect(self.show_augumentation)
    
    def initialValue(self):
        pass

    def errorMessage(self, title, message):
        return QMessageBox.critical(self, title, '<p><b>%s</b></p>%s' % (title, message))
    
    def status(self, message, delay=5000):
        self.statusBar().showMessage(message, delay)

    def ShowModelStructure(self):
        utils_Q5.ShowModelStructure()

    def show_tensorboard(self):
        webbrowser.open('http://localhost:6006/')

    def test(self):
        index = int(self.edit_5_3.text())
        utils_Q5.predict(index)
        

    def show_augumentation(self):
        
        # for images, labels in utils_Q5.train_data_loader:
            # fig, ax = plt.subplots(figsize = (50, 50))
            # ax.set_xticks([])
            # ax.set_yticks([])
            # ax.imshow(make_grid(images, 4).permute(1,2,0))
            # break
        utils_Q5.show_before_after('C:/Users/Hsin/Desktop/Hw2_CVDL_202112_NCKU-master/Data/compare.txt')
    



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainScreen()
    window.setGeometry(500, 150, 300, 300)
    window.show()
    sys.exit(app.exec_())