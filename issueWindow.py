import os
import webbrowser

from PySide6.QtCore import QTimer, QRect
from PySide6.QtGui import QTextCursor
from PySide6.QtWidgets import QWidget, QLabel, QPushButton, QHBoxLayout, QVBoxLayout, QLineEdit, QPlainTextEdit, \
    QComboBox
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

        # Retrieving the name of all the files in the issue folder
        filesname = []

        for path in os.listdir(self.issue.path):
            if os.path.isfile(os.path.join(self.issue.path, path)):
                filesname.append(path)

        # Creating the text box for the notes and populating it
        self.note_text_edit = QPlainTextEdit()
        self.note_text_edit.setPlainText(notes)

        self.filelabel = QLabel("Folder files")

        #Label that stays in the bottom of the window and gives information about the user actions
        self.info = QLabel("")
        self.info.setProperty("type",1)
        self.timer = QTimer()
        self.timer.timeout.connect(self.cleanLabel)

        # Buttons creation and connection to methods on click
        buttonB = QPushButton("Back")
        buttonB.clicked.connect(self.back)
        buttonE = QPushButton("Open folder")
        buttonE.clicked.connect(self.open)
        buttonA = QPushButton("Add Comment")
        buttonA.clicked.connect(self.add)
        buttonS = QPushButton("Save")
        buttonS.clicked.connect(self.save)

        # Building the layout
        buttons_layout = QHBoxLayout()
        buttons_layout.addWidget(buttonB)
        buttons_layout.addWidget(buttonE)
        buttons_layout.addWidget(buttonA)

        files_layout = QVBoxLayout()

        files_layout.addStretch()

        files_layout.addWidget(self.filelabel)

        for file in filesname:
            button = QPushButton(file, self)
            button.setProperty("type", 1)
            button.clicked.connect(self.openfiles)
            files_layout.addWidget(button)

        files_layout.addStretch()

        actionsNtext_layout = QVBoxLayout()
        actionsNtext_layout.addLayout(buttons_layout)
        actionsNtext_layout.addWidget(buttonS)
        actionsNtext_layout.addWidget(self.note_text_edit)
        actionsNtext_layout.addWidget(self.info)

        full_layout = QHBoxLayout()
        full_layout.addLayout(files_layout)
        full_layout.addLayout(actionsNtext_layout)

        self.setLayout(full_layout)

    def openfiles(self):
        sender = self.sender()
        webbrowser.open(self.issue.path + r'\\' + sender.text())

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
        print("Opening Folder...")
        webbrowser.open(self.issue.path)
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