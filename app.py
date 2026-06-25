import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel
from PySide6.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("VvE Toolkit")
        self.resize(900, 600)

        label = QLabel("Welkom bij de VvE Toolkit")
        label.setAlignment(Qt.AlignCenter)

        self.setCentralWidget(label)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

sys.exit(app.exec())