from PySide6.QtCore import Qt
from PySide6.QtWidgets import QLabel, QVBoxLayout, QWidget


class Workspace(QWidget):
    """Centraal werkgebied."""

    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()

        title = QLabel("Sleep hier uw PDF-bestanden")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        title.setStyleSheet("""
            font-size:24px;
            color:#666666;
        """)

        layout.addStretch()
        layout.addWidget(title)
        layout.addStretch()

        self.setLayout(layout)