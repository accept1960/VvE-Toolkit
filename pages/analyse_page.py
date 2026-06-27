from PySide6.QtWidgets import QLabel

from pages.base_page import BasePage


class AnalysePage(BasePage):

    def __init__(self):
        super().__init__()

        titel = QLabel("Analyse")

        titel.setStyleSheet("""
            font-size:24px;
            font-weight:bold;
        """)

        self.layout.addWidget(titel)
        self.layout.addStretch()