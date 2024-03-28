# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui for project.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QLCDNumber, QLabel,
    QProgressBar, QPushButton, QSizePolicy, QTextEdit,QMainWindow,
    QWidget)
import pytesseract


class Ui_application(QMainWindow):
    def setupUi(self, application):
        if not application.objectName():
            application.setObjectName(u"application")
        application.resize(724, 645)
        self.label = QLabel(application)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(60, 15, 671, 31))
        font = QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label_2 = QLabel(application)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 360, 81, 31))
        self.label_2.setFont(font)
        self.label_3 = QLabel(application)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 400, 81, 31))
        self.label_3.setFont(font)
        self.label_4 = QLabel(application)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(20, 440, 81, 31))
        self.label_4.setFont(font)
        self.textEdit = QTextEdit(application)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(170, 360, 241, 31))
        self.textEdit_2 = QTextEdit(application)
        self.textEdit_2.setObjectName(u"textEdit_2")
        self.textEdit_2.setGeometry(QRect(170, 440, 241, 31))
        self.textEdit_3 = QTextEdit(application)
        self.textEdit_3.setObjectName(u"textEdit_3")
        self.textEdit_3.setGeometry(QRect(170, 400, 241, 31))
        self.label_5 = QLabel(application)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(430, 80, 121, 31))
        self.label_5.setFont(font)
        self.lcdNumber = QLCDNumber(application)
        self.lcdNumber.setObjectName(u"lcdNumber")
        self.lcdNumber.setGeometry(QRect(590, 80, 111, 31))
        self.label_7 = QLabel(application)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(430, 160, 151, 31))
        self.label_7.setFont(font)
        self.lcdNumber_2 = QLCDNumber(application)
        self.lcdNumber_2.setObjectName(u"lcdNumber_2")
        self.lcdNumber_2.setGeometry(QRect(590, 160, 111, 31))
        self.label_6 = QLabel(application)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(20, 480, 151, 31))
        self.label_6.setFont(font)
        self.textEdit_4 = QTextEdit(application)
        self.textEdit_4.setObjectName(u"textEdit_4")
        self.textEdit_4.setGeometry(QRect(170, 480, 241, 31))
        self.progressBar = QProgressBar(application)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(430, 230, 271, 51))
        self.progressBar.setValue(24)
        self.pushButton = QPushButton(application)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(140, 550, 93, 28))
        self.pushButton.setFont(font)
        self.label_8 = QLabel(application)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(30, 70, 381, 211))
        self.label_9 = QLabel(application)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(446, 346, 251, 261))

        self.retranslateUi(application)

        QMetaObject.connectSlotsByName(application)
    # setupUi

    def retranslateUi(self, application):
        application.setWindowTitle("")
        self.label.setText(QCoreApplication.translate("application", u"Application creation for quality control and component counting in FMCG sectors", None))
        self.label_2.setText(QCoreApplication.translate("application", u"Batch No", None))
        self.label_3.setText(QCoreApplication.translate("application", u"Used Date", None))
        self.label_4.setText(QCoreApplication.translate("application", u"MRP", None))
        self.label_5.setText(QCoreApplication.translate("application", u"Component No", None))
        self.label_7.setText(QCoreApplication.translate("application", u"confidence score", None))
        self.label_6.setText(QCoreApplication.translate("application", u"Components/batch", None))
        self.pushButton.setText(QCoreApplication.translate("application", u"OK", None))
        self.label_8.setText(QCoreApplication.translate("application",  None))
        self.label_9.setText(QCoreApplication.translate("application",  None))
    # retranslateUi

import cv2 as cv
import threading


import sys
from threading import Thread

from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import Signal,QThread
from PySide6.QtGui import QImage,QPixmap

from cv2 import VideoCapture , cvtColor, COLOR_BGR2GRAY , equalizeHist

import numpy as np


# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py


thread_run = False

class VideoThread(QThread):
    change_pixmap_signal = Signal(QImage)
    pic_text = Signal(str)

    def run(self):
        global thread_run
        # Video capture from webcam
        cap = cv.VideoCapture(0)

        while thread_run:
            ret, frame = cap.read()
            if ret:
                
        #        self.ui.label_9.setText(pytesseract.image_to_string(img_rgb))
               
                # Convert OpenCV BGR image to RGB
                rgb_image = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
                
                h, w, ch = rgb_image.shape
                bytes_per_line = ch * w
                # Convert RGB image to QImage
                qt_image = QImage(rgb_image.data, w, h, bytes_per_line, QImage.Format_RGB888)
                # Emit signal with the converted image
                self.change_pixmap_signal.emit(qt_image)
            else:
                print("Error: Couldn't read frame.")
                break

        # Release the VideoCapture object
        cap.release()  
        self.pic_text.emit(pytesseract.image_to_string(rgb_image)) 

        #self.cam_reeder()

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_application()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.train)
        self.worker = VideoThread()
        self.worker.change_pixmap_signal.connect(self.update_video_frame)
        self.worker.pic_text.connect(self.display_text)


    def display_text(self,txt):
        self.ui.label_9.setText(txt)
    
    def update_video_frame(self, image):
        app.processEvents()
        self.ui.label_8.setPixmap(QPixmap.fromImage(image))
#         qimage = image

# # Convert QImage to numpy array
#         # width = qimage.width()
#         # height = qimage.height()
#         #bytes_per_line = qimage.bytesPerLine()
#         arr = np.frombuffer(qimage.constBits(), dtype=np.uint8).reshape(640, 480, 3)

# # Copy image data into numpy array

#         img_rgb = cv.cvtColor(arr, cv.COLOR_BGR2RGB)
#         self.ui.label_9.setText(pytesseract.image_to_string(img_rgb))

    def train(self):
        print("pressed")
        global thread_run
        if(self.worker.isRunning()):
            thread_run = False
            

            
        else:
            thread_run = True 
            self.worker.start()
            #self.worker.run()
            
        
        #self.template_handler = template_handler(VideoCapture(0))
        # t_handler = Thread(target=self.template_handler.main)
        # t_handler.setDaemon(True)
        # if not thread_run:
        #     thread_run = True
        #     t_handler.start()
        #     self.ui.pushButton_3.setText("Stop")
        #     print("this thread is started ")

        # else :
        #     thread_run = False
        #     self.ui.pushButton_3.setText("Start")
        #     print("this thread is stoped ")


        
if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
    