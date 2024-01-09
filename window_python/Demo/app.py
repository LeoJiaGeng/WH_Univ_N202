
import sys

from PyQt5.QtWidgets import  QApplication
from PyQt5.QtCore import QCoreApplication, Qt
from appMain import QmyApp
    
if __name__ == "__main__":
    QCoreApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    app = QApplication(sys.argv)
    mainform = QmyApp()
    mainform.show()
    sys.exit(app.exec())
