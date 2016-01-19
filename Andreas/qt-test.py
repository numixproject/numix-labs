from PyQt5 import *
from PyQt5.Qt import *
from PyQt5.QtWidgets import *
import sys

class MyMainWindow(QMainWindow):

    def __init__(self, parent=None):

        super(MyMainWindow, self).__init__(parent)
        self.form_widget = FormWidget(self) 
        self.setCentralWidget(self.form_widget) 

class FormWidget(QWidget):
    def __init__(self, parent):        
        super(FormWidget, self).__init__(parent)
        self.layout = QHBoxLayout(self)
        sizes=[16,22,24,32,48,64,96,128,256]
        icon = QIcon.fromTheme('distribute-horizontal-right')
        print(icon.availableSizes())
        for i, size in enumerate(sizes):
            label = QLabel()
            label.setPixmap(icon.pixmap(size))
            self.layout.addWidget(label)
        self.setLayout(self.layout)

app = QApplication([])
foo = MyMainWindow()
foo.show()
sys.exit(app.exec_())
