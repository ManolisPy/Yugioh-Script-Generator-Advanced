#-------------------------------------------------------------------------------
# ygoscr_core_window

# The main window is created and some of the necessary modules are initialized.
#-------------------------------------------------------------------------------

import sys

from PyQt6.QtWidgets import (QApplication, QWidget, QMainWindow, QVBoxLayout)
from PyQt6.QtCore import Qt

import ygoscr_core_widgets
import ygoscr_script_creation
import ygoscr_script_dictionaries



class CoreWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        ygoscr_core_widgets.initialize_methods(self)
        ygoscr_script_dictionaries.dictionaries(self)
        self.base_window()


    def base_window(self):

        self.setFixedSize(500, 600)
        self.setWindowTitle("Yugioh Script Generator Advanced - Minimal")

        scrnrescenter = self.screen().availableGeometry().center()
        corewingeo = self.frameGeometry()
        corewingeo.moveCenter(scrnrescenter)
        self.move(corewingeo.topLeft())

        self.core_layout()
        self.signals()


    def core_layout(self):

        corelayout = QVBoxLayout()
        corelayout.setAlignment(Qt.AlignmentFlag.AlignHCenter)

        corelayout.addWidget(self.corenote, alignment=Qt.AlignmentFlag.AlignTop)
        corelayout.addWidget(self.demotext,alignment=Qt.AlignmentFlag.AlignBottom|
                                                    Qt.AlignmentFlag.AlignHCenter)
        corelayout.addLayout(self.widget1layout)
        corelayout.addWidget(self.coretext, alignment=Qt.AlignmentFlag.AlignCenter)
        corelayout.addWidget(self.corebtn, alignment=Qt.AlignmentFlag.AlignHCenter)

        corewnd = QWidget()
        corewnd.setLayout(corelayout)
        self.setCentralWidget(corewnd)


    def signals(self):

        self.corebtn.clicked.connect(lambda: ygoscr_script_creation.file_creation(self))
        self.demotext.currentTextChanged.connect(lambda: self.combo_to_text())


    def combo_to_text(self):

        if self.demotext.currentText() != 'Select effect':
            self.coretext.setText(self.demotext.currentText())
        else:
            self.coretext.setText("")
        #self.demotext.model().item(0).setEnabled(False)



# The following lines can be included in a method and called from there.
ygoapp = QApplication([])
mainwnd = CoreWindow()
mainwnd.show()
ygoapp.exec()
