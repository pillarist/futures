import sys
import cv2
from PySide6.QtCore import Qt, QThread, Signal
from PySide6.QtGui import QImage, QPixmap
from PySide6.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget


class VideoThread(QThread):
    change_pixmap_signal = Signal(QImage)

    def run(self):
        # Video capture from webcam
        cap = cv2.VideoCapture(0)

        while True:
            ret, frame = cap.read()
            if ret:
                # Convert OpenCV BGR image to RGB
                rgb_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
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


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Live Video Display")
        self.resize(640, 480)

        self.video_label = QLabel(self)
        self.video_label.setAlignment(Qt.AlignCenter)

        self.text_label = QLabel("Press Start to show live video", self)
        self.text_label.setAlignment(Qt.AlignCenter)

        self.start_button = QPushButton("Start", self)
        self.start_button.clicked.connect(self.start_video)

        layout = QVBoxLayout()
        layout.addWidget(self.video_label)
        layout.addWidget(self.text_label)
        layout.addWidget(self.start_button)
        self.setLayout(layout)

        self.video_thread = VideoThread()
        self.video_thread.change_pixmap_signal.connect(self.update_video_frame)

    def start_video(self):
        self.start_button.setEnabled(False)
        self.text_label.setText("Live video is running...")
        self.video_thread.start()

    def update_video_frame(self, image):
        self.video_label.setPixmap(QPixmap.fromImage(image))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
