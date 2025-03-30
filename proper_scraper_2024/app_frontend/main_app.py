import sys

from PySide6.QtWidgets import QApplication
from main_window import MainWindow


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setApplicationName("Scrapiary")

    scrApp = MainWindow(app)

    scrApp.show()

    try:
        sys.exit(app.exec())
    except SystemExit:
        print('Closing Application')