import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *

class Mainwindow(QMainWindow):
    def __init__(self):
        super(Mainwindow, self).__init__()
        self.browser=QWebEngineView()
        self.browser.setUrl(QUrl('https://duckduckgo.com'))
        self.setCentralWidget(self.browser)
        self.showMaximized()
        navbar=QToolBar()
        self.addToolBar(navbar)

        back_btn=QAction('back', self)
        back_btn.triggered.connect(self.browser.back)
        navbar.addAction(back_btn)

        forwardbtn=QAction('forward', self)
        forwardbtn.triggered.connect(self.browser.forward)
        navbar.addAction(forwardbtn)
        self.browser.font()

app=QApplication(sys.argv)
QApplication.setApplicationName('Akash Browser')
window=Mainwindow()
app.exec_()