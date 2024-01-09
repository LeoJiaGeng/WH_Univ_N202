# -*- coding: utf-8 -*-
"""
Created on Sun Apr  3 21:53:27 2022

@author: 41137
"""

import sys
from PyQt5.QtWidgets import QApplication, QFileDialog, QWidget
from PyQt5.QtCore import pyqtSlot, QCoreApplication, Qt, QDir, QThread, pyqtSignal
from ui_translation import Ui_Form
from translation import *

class QmyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.APPID = '20240109001936084'
        self.APPKEY = 'tpphd5ZQSEvFG4fpcHRc'

    @pyqtSlot()
    def on_btn_trans_clicked(self):
        input_text = self.ui.input_plainTextEdit.toPlainText()
        if (self.ui.button_to_zh.isChecked()):
            self.show_content(trans_Baidu_POST(input_text, self.APPID, self.APPKEY))
        else:
            self.show_content(trans_Baidu_GET(input_text, self.APPID, self.APPKEY))

    def get_content(self):
        return self.ui.input_plainTextEdit.toPlainText()

    def show_content(self, strCont):
        self.ui.output_plainTextEdit.appendPlainText(strCont)

    @pyqtSlot() 
    def on_btn_clear_clicked(self):
        self.ui.input_plainTextEdit.clear()
        self.ui.output_plainTextEdit.clear()


if __name__ == "__main__":
    QCoreApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    app = QApplication(sys.argv)
    myWidget = QmyApp()
    myWidget.show()
    sys.exit(app.exec())
        