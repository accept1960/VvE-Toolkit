from PySide6.QtWidgets import (
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
)

from gui.header import Header
from gui.sidebar import Sidebar
from gui.workspace import Workspace


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("VvE Toolkit")
        self.resize(1300, 800)

        central = QWidget()

        root = QVBoxLayout()
        root.setContentsMargins(0, 0, 0, 0)
        root.setSpacing(0)

        root.addWidget(Header())

        content = QHBoxLayout()
        content.setContentsMargins(0, 0, 0, 0)

        content.addWidget(Sidebar())
        content.addWidget(Workspace(), 1)

        root.addLayout(content)

        central.setLayout(root)

        self.setCentralWidget(central)