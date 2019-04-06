import sys
from PyQt5.QtWidgets import (QLineEdit, QSlider, QPushButton, QVBoxLayout, QApplication, QWidget)
from PyQt5.QtCore import Qt


class Window(QWidget):

    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        
        self.b1 = QPushButton('Clear')
        v_box = QVBoxLayout()
        v_box.addWidget(self.b1)
        self.setLayout(v_box)
        self.setWindowTitle('Demo')
        self.show()

  


app = QApplication(sys.argv)
a_window = Window()
sys.exit(app.exec_())