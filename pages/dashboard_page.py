from PySide6.QtWidgets import QLabel

from pages.base_page import BasePage


class DashboardPage(BasePage):

    def __init__(self):
        super().__init__()

        titel = QLabel("Dashboard")
        titel.setStyleSheet("""
            font-size:24px;
            font-weight:bold;
        """)

        tekst = QLabel("Welkom bij de VvE Toolkit")

        self.layout.addWidget(titel)
        self.layout.addWidget(tekst)
        self.layout.addStretch()