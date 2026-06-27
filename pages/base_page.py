from PySide6.QtWidgets import QWidget, QVBoxLayout


class BasePage(QWidget):
    """Basisklasse voor alle pagina's."""

    def __init__(self):
        super().__init__()

        self.layout = QVBoxLayout()
        self.layout.setContentsMargins(30, 30, 30, 30)
        self.layout.setSpacing(20)

        self.setLayout(self.layout)