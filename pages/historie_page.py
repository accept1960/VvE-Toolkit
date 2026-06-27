from PySide6.QtWidgets import QLabel

from pages.base_page import BasePage


class HistoriePage(BasePage):

    def __init__(self):
        super().__init__()

        titel = QLabel("Historie")

        titel.setStyleSheet("""
            font-size:24px;
            font-weight:bold;
        """)

        self.layout.addWidget(titel)
        self.layout.addStretch()