import sys

from PyQt5.QtWidgets import QApplication, QDialog
from dosya import Ui_Form

app = QApplication(sys.argv)
window = QDialog()
ui = Ui_Form()
ui.setupUi(window)
window.show()
sys.exit(app.exec_())