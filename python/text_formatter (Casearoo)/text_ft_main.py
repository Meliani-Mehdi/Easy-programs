# This Python file uses the following encoding: utf-8
import sys
from casey import Casey as cs

from PySide6.QtWidgets import QApplication, QWidget

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_text_ft_main

class text_ft_main(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_text_ft_main()
        self.ui.setupUi(self)

        self.ui.sentenceCase.clicked.connect(lambda: self.useFunk(cs.sentenceCase))
        self.ui.altCase.clicked.connect(lambda: self.useFunk(cs.altCase))
        self.ui.upperCase.clicked.connect(lambda: self.useFunk(cs.upperCase))
        self.ui.lowerCase.clicked.connect(lambda: self.useFunk(cs.lowerCase))
        self.ui.titleCase.clicked.connect(lambda: self.useFunk(cs.titleCase))
        self.ui.inverseCase.clicked.connect(lambda: self.useFunk(cs.inverseCase))
        self.ui.reverseCase.clicked.connect(lambda: self.useFunk(cs.reverseCase))
        self.ui.capitalizedCase.clicked.connect(lambda: self.useFunk(cs.capitalizedCase))

    def useFunk(self, funk):
        text = self.ui.main_text.toPlainText()
        self.ui.formatter_holder.setDisabled(True)
        self.ui.main_text.setText(funk(cs, text))
        self.ui.formatter_holder.setDisabled(False)
    


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = text_ft_main()
    widget.show()
    sys.exit(app.exec())
