from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QLabel,
    QHBoxLayout,
    QWidget,
)


class Header(QWidget):
    """Header bovenaan de applicatie."""

    def __init__(self):
        super().__init__()

        self.setFixedHeight(60)

        layout = QHBoxLayout()
        layout.setContentsMargins(20, 10, 20, 10)

        title = QLabel("VvE Toolkit")
        title.setStyleSheet("""
            font-size:20px;
            font-weight:bold;
        """)

        version = QLabel("v0.2.0")
        version.setAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)

        layout.addWidget(title)
        layout.addStretch()
        layout.addWidget(version)

        self.setLayout(layout)