from PyQt5.QtWidgets import QApplication
import sys
from includes.gui import GraphVoyager

if __name__ == '__main__':
    app = QApplication(sys.argv)
    application_window = GraphVoyager()
    application_window.show()
    sys.exit(app.exec_())