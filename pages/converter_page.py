from PySide6.QtCore import Qt
from PySide6.QtWidgets import QLabel

from pages.base_page import BasePage


class ConverterPage(BasePage):
    """Pagina voor het converteren van PDF-bestanden."""

    def __init__(self):
        super().__init__()

        titel = QLabel("PDF Converter")
        titel.setStyleSheet("""
            font-size:24px;
            font-weight:bold;
        """)

        tekst = QLabel("Sleep hier uw PDF-bestanden")
        tekst.setAlignment(Qt.AlignmentFlag.AlignCenter)
        tekst.setStyleSheet("""
            font-size:18px;
            color:#666666;
        """)

        self.layout.addWidget(titel)
        self.layout.addStretch()
        self.layout.addWidget(tekst)
        self.layout.addStretch()