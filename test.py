import sys
from PySide6.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton


class ButtonHolder(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ButtonHolderApp")
        button = QPushButton("Press Me!")
        self.setCentralWidget(button)


app = QApplication(sys.argv)

window = ButtonHolder()
window.show()

sys.exit(app.exec())