from PySide6.QtCore import Qt
from PySide6.QtWidgets import QLabel, QMainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("VvE Toolkit")
        self.resize(1000, 700)

        label = QLabel("Welkom bij de VvE Appartementen Brouwershof Parkzijde Toolkit")
        label.setAlignment(Qt.AlignCenter)

        self.setCentralWidget(label)