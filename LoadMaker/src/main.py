# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtGui import QIcon
# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_Widget

class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setApplicationName("Load Maker")
    app.setStyleSheet("""QTextEdit { 	font: 20px verdana;
    background-color: white;
    color: black; }
    """)
    widget = Widget()
    widget.setWindowTitle("Load Maker")
#    CNU = QIcon(":/style/cnu")
#    app.setWindowIcon(CNU)
#    widget.setWindowIcon(CNU)
    widget.show()
    sys.exit(app.exec())

