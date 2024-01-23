import webbrowser

from PySide6.QtCore import QTimer
from PySide6.QtWidgets import QWidget, QLabel, QPushButton, QHBoxLayout, QVBoxLayout, QLineEdit, QPlainTextEdit
from datetime import datetime


class IssueWindow(QWidget):
    """
        A class, that using Qt, represents the GUI window to manage an Issue

        Attributes
        ----------
        issue : Issue
            The issue that's being managed
        issue_list : Issue[]
            The list of all the issue objects saved in the machine
        setWindowTitle : str
            The title of the window
        note_text_edit : QPlainTextEdit
            The text box where all the notes of the Issue at hand are written

        Methods
        -------
        back()
            Closes this window and consequently goes back to the main window
        open()
            Opens the Issue notes ouside of the app in the OS predefined .txt app
        add()
            Adds to the notes another template for a new instance of notes in the same Issue
        save()
            Saves the text inside note_text_edit to a .txt file
        """

    def __init__(self, issue_list, issue):
        """
            In this constructor are created all the widgets of the window, including buttons,
            labels, etc. and the whole layout

            Parameters
            ----------
            issue_list: Issue[]
                    List with all the issues saved until now
            issue: Issue
                    Issue that's being managed
            """
        super().__init__()

        self.issue = issue

        self.issue_list = issue_list

        self.setWindowTitle("Issue " + str(issue.number))

        notes = ""

        # Retrieving the text in the Issue notes
        with open(self.issue.path + '\\' + "Notes.txt", 'r', encoding="utf8") as f:
            for line in f:
                notes = notes + line
        f.close()

        # Creating the text box for the notes and populating it
        self.note_text_edit = QPlainTextEdit()
        self.note_text_edit.setPlainText(notes)

        #Label that stays in the bottom of the window and gives information about the user actions

        self.info = QLabel("")
        self.info.setProperty("type",1)
        self.timer = QTimer()
        self.timer.timeout.connect(self.cleanLabel)

        # Buttons creation and connection to methods on click
        buttonS = QPushButton("Back")
        buttonS.clicked.connect(self.back)
        buttonE = QPushButton("Open file")
        buttonE.clicked.connect(self.open)
        buttonA = QPushButton("Add Comment")
        buttonA.clicked.connect(self.add)
        buttonR = QPushButton("Save")
        buttonR.clicked.connect(self.save)

        # Building the layout
        buttons_layout = QHBoxLayout()
        buttons_layout.addWidget(buttonS)
        buttons_layout.addWidget(buttonE)
        buttons_layout.addWidget(buttonA)

        issue_layout = QVBoxLayout()
        issue_layout.addLayout(buttons_layout)
        issue_layout.addWidget(buttonR)
        issue_layout.addWidget(self.note_text_edit)
        issue_layout.addWidget(self.info)

        self.setLayout(issue_layout)

    def cleanLabel(self):
        self.info.setText("")
        self.timer.stop()

    def back(self):
        """
        Closes the current window
        """
        self.close()

    def open(self):
        """
        Opens the .txt file that contains the notes of the Issue
        """
        print("Opening Notes...")
        webbrowser.open(self.issue.path + '\\' + "Notes.txt")
        print("Done")

    def add(self):
        """
        Adds note_text_edit a new preset of notes
        """
        print("Adding Comment...")
        now = datetime.now()
        self.note_text_edit.appendPlainText(
            "%%%%%%%%%%%%%%%%%%%%% ISSUE " + self.issue.number + " NOTES %%%%%%%%%%%%%%%%%%%%% " + "\n\n--------PROBLEM DESCRIPTION:\n\n--------OBSERVATIONS:\n\n--------POSSIBLE SOLUTION:\n\n" + "%%%%%%%%%%%%%%%%%% CREATED: " + str(
                now)[:19] + " %%%%%%%%%%%%%%%%%%\n\n")
        self.info.setText("Added comment!")
        self.timer.start(5000)

    def save(self):
        """
        Saves the text in note_text_edit in a .txt file
        """
        with open(self.issue.path + '\\' + "Notes.txt", 'w', encoding="utf8") as f:
            f.write(self.note_text_edit.toPlainText())
        f.close()

        print("Saved!")
        self.info.setText("Saved!")
        self.timer.start(5000)

    """ Function that finds the text selected whats selected
    def handleSelectionChanged(self):
        cursor = self.edit.textCursor()
        print("Selection start: %d end: %d" %
              (cursor.selectionStart(), cursor.selectionEnd()))
    """