# main.py

import sys
from pathlib import Path

from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QToolBar,
    QToolButton,
    QMenu
)
from PyQt6.QtGui import QDesktopServices
from PyQt6.QtCore import Qt, QUrl

# 👇 import the other window
from settings_window import SettingsWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Launcher")
        self.resize(900, 500)

        # Keep a reference so it doesn't get garbage-collected
        self.settings_window = None

        toolbar = QToolBar()
        toolbar.setMovable(False)
        toolbar.setToolButtonStyle(
            Qt.ToolButtonStyle.ToolButtonTextBesideIcon
        )
        self.addToolBar(toolbar)

        instance_btn = QToolButton()
        instance_btn.setText("Add Instance")

        toolbar.addWidget(instance_btn)

        # Settings button
        settings_btn = QToolButton()
        settings_btn.setText("Settings")

        # When clicked → open settings window
        settings_btn.clicked.connect(self.open_settings)

        toolbar.addWidget(settings_btn)

    def open_settings(self):
        # Create window if it doesn't exist
        if self.settings_window is None:
            self.settings_window = SettingsWindow()

        self.settings_window.show()
        self.settings_window.raise_()
        self.settings_window.activateWindow()


app = QApplication(sys.argv)
app.setStyleSheet("""
QToolBar {
    spacing: 6px;
    background: #1e1e1e;
}

QToolButton {
    min-width: 100px;
    min-height: 30px;
    padding: 4px 10px;
    font-size: 10pt;
    color: white;
}

QToolButton:hover {
    background: #2a2a2a;
}

QToolButton:pressed {
    background: #333333;
}
""")


window = MainWindow()
window.show()
sys.exit(app.exec())
