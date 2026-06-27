from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QLabel,
    QPushButton,
    QVBoxLayout,
    QWidget,
)


class Sidebar(QWidget):
    """Linker navigatiebalk."""

    def __init__(self):
        super().__init__()

        self.setFixedWidth(220)

        layout = QVBoxLayout()

        title = QLabel("VvE Toolkit")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        #layout.addWidget(title)

        menu_items = [
            "Dashboard",
            "Converter",
            "Analyse",
            "Historie",
            "Instellingen",
        ]

        for item in menu_items:
            knop = QPushButton(item)
            layout.addWidget(knop)

        layout.addStretch()

        self.setLayout(layout)