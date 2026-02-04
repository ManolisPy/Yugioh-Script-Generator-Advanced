#-------------------------------------------------------------------------------
# ygoscr_core_widgets

# The menu bar and all the required widgets.
#-------------------------------------------------------------------------------

from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import (QTextEdit, QPushButton, QLabel, QComboBox,
                            QWidget, QVBoxLayout, QTextBrowser, QGridLayout)
from PyQt6.QtCore import Qt



def initialize_methods(self):

    core_menubar(self)
    core_note(self)
    core_demo_text(self)
    core_card_type(self)
    core_card_st_type(self)
    core_effect_text(self)
    core_button_script(self)
    about_window(self)
    help_window(self)
    widget_group_1(self)


def core_menubar(self):

    actioncoreabt = QAction('&About', self)
    actioncoreabt.triggered.connect(lambda: self.aboutwnd.show())

    actioncoreexit = QAction('&Exit', self)
    actioncoreexit.setShortcut('Alt+F4')
    actioncoreexit.triggered.connect(self.close)

    actioncorehelp = QAction('&How to write a card effect', self)
    actioncorehelp.triggered.connect(lambda: self.helpwnd.show())
    #actioncorehelp.setEnabled(False)

    coremenu = self.menuBar()
    menufile = coremenu.addMenu('&Menu')
    menufile.addAction(actioncoreabt)
    menufile.addAction(actioncoreexit)

    corehelp = self.menuBar()
    helpfile = corehelp.addMenu('&Help')
    helpfile.addAction(actioncorehelp)


def core_note(self):

    self.corenote = QLabel(
        'This is a mini version of a project in mind.'
        '\n\nThe program generates script files by reading text.'
        '\nIt revolves around one platform about a specific game, '
        '\nso a few words/terminologies may look weird if you are unfamiliar.'
        '\nSimply choose from the options below and click "Create script".'
        '\nYour option will appear in the text box as if you wrote it manually.'
        '\n\nMore information in Menu/About.',
        self)
    self.corenote.setAlignment(Qt.AlignmentFlag.AlignHCenter)


def core_demo_text(self):

    self.demotext = QComboBox(self)
    self.demotext.setMaximumWidth(300)
    self.demotext.addItem('Select effect')
    self.demotext.addItem(
        'Destroy all monsters on the field.'
        )
    self.demotext.addItem(
        'Destroy all spells and traps on the field.'
        )


def core_card_type(self):

    self.corecardtype = QComboBox(self)
    self.corecardtype.setMaximumWidth(100)
    self.corecardtype.addItem('Type of card')
    self.corecardtype.addItem('Monster')
    self.corecardtype.addItem('Spell')
    self.corecardtype.addItem('Trap')
    #self.corecardtype.model().item(1).setEnabled(False)


def core_card_st_type(self):

    self.corecardsttype = QComboBox(self)
    self.corecardsttype.setMaximumWidth(130)
    self.corecardsttype.addItem('Type of Spell/Trap')
    self.corecardsttype.addItem('Normal')
    self.corecardsttype.addItem('Continuous')
    self.corecardsttype.setEnabled(False)
    #self.corecardsttype.model().item(2).setEnabled(False)


def core_effect_text(self):

    self.coretext = QTextEdit(self)
    self.coretext.setFixedSize(400, 200)
    #self.coretext.setReadOnly(True)
    #self.coretext.setText(self.corecombo.currentText())


def core_button_script(self):

    self.corebtn = QPushButton('Create script', self)
    self.corebtn.setMaximumSize(100, 50)


def about_window(self):

    self.aboutwnd = QWidget()
    self.aboutwnd.setFixedSize(550, 450)
    self.aboutwnd.setWindowTitle('About')

    abttext = QTextBrowser()
    abttext.setHtml(
        '''<p align='center'>
        <span style='font-size:14pt'>About The Program</span>
        <br><br><br>
        <span style='font-size:10pt'>The program creates .lua files, based on
         a Yu-Gi-Oh! game emulator,
        <br>commonly known as EDOPro or YGOPro.
        <br>The idea is to \"read\" the text written in the box and create the desired file,
        <br>compared to choosing parts from a list of options like in my
        <br>original work here: <a href='https://github.com/ManolisPy/ScriptGeneratorYGO'>
        https://github.com/ManolisPy/ScriptGeneratorYGO</a>
        <br><br>Due to the game's nature, the program will never be truly complete.
        <br>Currently, it can create only two specific scripts.
        <br>For convenience and assuming lack of knowledge about the game,
        <br>you can choose one of the options from the drop-down menu.
        <br>You can write card effects manually if you want too. An error message
        <br>will pop up if the input is invalid or out of the program's capabilities.
        <br><br>The program uses NLTK to make the text easier to work on,
        <br>also a few custom methods that \"translate\" the text to code.
        <br>Not sure if it counts as using AI to \"do the job for me\" or if it\'s mostly
        <br>a fluttering term in this case.
        <br><br>Looking forward to feedback, questions, even ideas to work
         on it more efficiently!

        <br><br> e-mail: emmanouilgs@gmail.com
        <br>LinkedIn:
        <a href='https://www.linkedin.com/in/emmanouil-gkarmpos/'>
        https://www.linkedin.com/in/emmanouil-gkarmpos/</span>'''
        )
    abttext.setReadOnly(True)
    abttext.setOpenExternalLinks(True)

    abtlayout = QVBoxLayout()
    abtlayout.addWidget(abttext)
    self.aboutwnd.setLayout(abtlayout)


def help_window(self):

    self.helpwnd = QWidget()
    self.helpwnd.setFixedSize(650, 550)
    self.helpwnd.setWindowTitle('Help')

    abttext = QTextBrowser()
    abttext.setHtml(
        '''<p align='center'>
        <span style='font-size:12pt'>Writing Yu-Gi-Oh! Cards The Right Way</span></p>
        <br><br>
        <span style='font-size:10pt'>Konami, the founder of the card game,
        has established rules to writing card effects.
        The reason is to make clear how cards function, without causing misunderstandings.
        <br>I'll just mention a few things for now. There's also a TL;DR version at the end.
        <br><br>Generally, a card effect consists of up to four parts:
        <br>- activation condition (optional)
        <br>- cost to use (optional)
        <br>- application target (optional)
        <br>- action (mandatory)
        <br>In the action, there need to be at least 1 verb (action),
        the affected object (monster/spell/trap card)
        and often the object's location (on the field, in the hand etc.)
        <br>e.g. one effect could be "Destroy all monsters on the field."
        The only thing here is an action. "Destroy" is the verb that describes
        the action, "all monsters" are the affected objects and "on the field" is the location.
        <br><br>An alternative way to write the effect would be "Destroy all monster
        cards on the field".
        The program tries to simplify variations like this - in our case,
        treating "monster cards" as "monsters".
        However, writing something like "All monsters on the." or "Destroy all on
        the field." would raise an error. That's because key parts are missing from the effect.
        <p align='center'>___________________________________________</p>
        TL;DR
        <br>You can experiment by writing one of the two default effects in the
        program, in different ways, to see if errors will be raised or the file
        (script) will be created successfully. Try with small and sensible changes:
        add, remove, change or rearrange one or two words.
        Writing a completely wrong sentence will obviously not work.
        <br><br>NOTE: The options in the drop-down menu with "type of card" refer
        to the type of card that includes the effect.
        It has NOTHING to do with the effect itself.</span>'''
        )
    abttext.setReadOnly(True)
    abttext.setOpenExternalLinks(True)

    abtlayout = QVBoxLayout()
    abtlayout.addWidget(abttext)
    self.helpwnd.setLayout(abtlayout)


def widget_group_1(self):

    self.widget1layout = QGridLayout()
    self.widget1layout.setAlignment(Qt.AlignmentFlag.AlignTop|Qt.AlignmentFlag.AlignHCenter)
    self.widget1layout.addWidget(self.corecardtype, 0, 0)
    self.widget1layout.addWidget(self.corecardsttype, 0, 1)
