

from sympy import false, im, true
from window import Ui_MainWindow
from PySide6.QtWidgets import QApplication,QMainWindow,QLabel
from PySide6.QtCore import QObject, QThread,Signal
from PySide6.QtGui import QImage,QPixmap

import cv2 as cv


class cam_thread(QThread):

   

  
   
    set_address = "agfsa"
    pic = Signal(QImage)

    def run(self,lock):

        cap = cv.VideoCapture(0)
        while(lock):
            
            _,frame = cap.read()
            if(_):
                frame = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
                height, width, channel = frame.shape
                bytesPerLine = 3 * width
                qImg = QImage(frame.data, width, height, bytesPerLine, QImage.Format_RGB888)

                self.pic.emit(qImg)
                

    









class main_window(QMainWindow):

    def __init__(self) -> None:
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.lock = false

        self.t_thread = cam_thread()
        
        self.t_thread.pic.connect(self.image_updator)
        self.ui.pushButton.clicked.connect(self.str_btn_pressed)
    
    def image_updator(self,img):
        app.processEvents()
        self.ui.label.setPixmap(QPixmap.fromImage(img))
        print("setted")
        

    def str_btn_pressed(self):
        if(self.lock):
            self.lock = false

        else:
            self.lock = true
            self.t_thread.run(self.lock)

if __name__ == "__main__":
    import sys
    app = QApplication()
    
    window = main_window()
    window.show()
    sys.exit(app.exec())