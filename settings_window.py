# settings_window.py

from PyQt6.QtWidgets import QMainWindow, QLabel
from PyQt6.QtCore import Qt


class SettingsWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Settings")
        self.resize(400, 300)

        label = QLabel("Settings go here", self)
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setCentralWidget(label)
