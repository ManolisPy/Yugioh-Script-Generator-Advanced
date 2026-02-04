#-------------------------------------------------------------------------------
# ygoscr_script_creation

# The files are created here.
# Other modules handle the text-to-code convertion.
#-------------------------------------------------------------------------------

import re

from PyQt6.QtWidgets import QFileDialog, QMessageBox
from PyQt6.QtCore import QFileInfo

import ygoscr_script_form
import ygoscr_text_tokenization



def file_creation(self):

    # If there is a problem with the effect (invalid syntax, missing key words etc.),
    # the process will stop and the user will be informed.
    self.effect_error = False

    if self.coretext.toPlainText() == "":
        QMessageBox.critical(self, 'Missing text','Please write an effect.')
    else:
        ygoscr_text_tokenization.text_token_list(self, self.coretext.toPlainText())
        if self.effect_error == True:
            QMessageBox.critical(self, 'Error', self.effect_err_msg)
        else:

            self.effect_error = False
            tempname, _ = QFileDialog.getSaveFileName(
                self,'Save as', "custom_script", 'Lua Files (*.lua)'
            )
            if not tempname:
                return
            else:
                savedFile = QFileInfo(tempname)

            if savedFile:
                codenum = savedFile.baseName()

            ygoscr_script_form.script_formula(self)
            file = open(savedFile.absoluteFilePath(), 'w')
            file.write(self.card_form)

            file.close()

            QMessageBox.information(self, 'Success','Script creation completed!')