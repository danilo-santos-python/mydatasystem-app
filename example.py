from PyQt6.QtWidgets import QApplication, QLabel, QWidget, QGridLayout, \
     QLineEdit, QPushButton

import sys
from datetime import datetime


class AgeCalculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Age Calculator")
        grid = QGridLayout()

        # Create widgets
        name_label = QLabel("Nome:")
        self.name_line_edit = QLineEdit()

        date_birth_label = QLabel("Date of Birth DD/MM/YYYY:")
        self.date_birth_line_edit = QLineEdit()

        calculate_button = QPushButton("Calculate Age")
        calculate_button.clicked.connect(self.calculate_age)
        self.output_label = QLabel("")

        # Add widgets to grid
        grid.addWidget(name_label, 0, 0)
        grid.addWidget(self.name_line_edit, 0, 1)
        grid.addWidget(date_birth_label, 1, 0)
        grid.addWidget(self.date_birth_line_edit, 1, 1)
        grid.addWidget(calculate_button, 2, 0, 1, 2)
        grid.addWidget(self.output_label, 3, 0, 1, 2)

        self.setLayout(grid)

    def calculate_age(self):
        try:
            birth_date = datetime.strptime(self.date_birth_line_edit.text(), "%d/%m/%Y").date()
            today = datetime.today().date()
            age = today.year - birth_date.year
            # Ajustar caso ainda não tenha feito aniversário este ano
            if (today.month, today.day) < (birth_date.month, birth_date.day):
                age -= 1
            self.output_label.setText(f"{self.name_line_edit.text()} is {age} years old.")
        except ValueError:
            self.output_label.setText("Invalid date format. Use DD/MM/YYYY.")


app = QApplication(sys.argv)
age_calculator = AgeCalculator()
age_calculator.show()
sys.exit(app.exec())