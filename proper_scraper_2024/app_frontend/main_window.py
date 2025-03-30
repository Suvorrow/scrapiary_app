from PySide6.QtWidgets import QMainWindow
from PySide6.QtCore import QSize


class MainWindow(QMainWindow):
    def __init__(self, app, parent=None):
        super().__init__(parent)

        self.app = app  # declare an app instance

        self.setWindowTitle("Scrapiary")

        # Size policy:
        self.setMaximumSize(QSize(832, 592))
        self.setMinimumSize(QSize(632, 448))
        self.resize(720, 512)