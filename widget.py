import os
import pickle
import shutil

from PySide6.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QHBoxLayout, QVBoxLayout, QMessageBox

from IssueClass import Issue
from issueWindow import IssueWindow


class Widget(QWidget):

    """
    A class, that using Qt, represents the main GUI window of the app

    Attributes
    ----------
    issue_list : Issue[]
        The list of all the issue objects saved in the machine
    setWindowTitle : str
        The title of the window
    line_edit : QLineEdit
        The text box where the issue number is written

    Methods
    -------
    createIssue()
        Creates an Issue object with the number written in line_edit and saves the changes in issue_list
    openIssue()
        Creates a new GUI window for the managing of the Issue whose number is written on line_edit
    deleteIssue()
        Deletes all the traces of the Issue whose number is written on line_edit
    warningPrompt()
        Creates a warning as a popup message to make sure the user wants to delete an Issue
    errorNonExistentPrompt()
        Creates a error prompt to let the user know that the Issue they're trying to use doesn't exist
    """

    def __init__(self, issue_list):
        """
        In this constructor are created all the widgets of the window, including buttons
        labels and the whole layout

        Parameters
        ----------
        issue_list: Issue[]
                list with all the issues saved until now
        """

        super().__init__()

        self.issue_list = issue_list

        self.setWindowTitle("Issue Menu")

        # User input for the Issue Number
        label = QLabel("Issue Number : ")
        self.line_edit = QLineEdit()
        self.info = QLabel("")
        self.info.setProperty("type",1)

        # Buttons creation and connection to methods on click
        buttonC = QPushButton("Create")
        buttonC.clicked.connect(self.createIssue)

        buttonO = QPushButton("Open")
        buttonO.clicked.connect(self.openIssue)

        buttonD = QPushButton("Delete")
        buttonD.clicked.connect(self.warningPrompt)

        # Building the layout
        number_layout = QHBoxLayout()
        number_layout.addWidget(label)
        number_layout.addWidget(self.line_edit)

        buttons_layout = QHBoxLayout()
        buttons_layout.addWidget(buttonC)
        buttons_layout.addWidget(buttonO)
        buttons_layout.addWidget(buttonD)

        menu_layout = QVBoxLayout()
        menu_layout.addLayout(number_layout)
        menu_layout.addLayout(buttons_layout)
        menu_layout.addWidget(self.info)

        self.setLayout(menu_layout)

    def save(self):
        os.chdir(r"C:\Users\andre.costa\Desktop\random code\IssueAuto")
        with open('issuesfile.pkl', 'wb') as outp:
            pickle.dump(self.issue_list, outp, pickle.HIGHEST_PROTOCOL)
        print("Saved!")
        self.info.setText("Saved!")
    def createIssue(self):
        """
        It's created an Issue object, stored that object in issues_list and saved all the
        issues of issue_list outside the app in a file named issuesfile.pkl
        """
        issue = Issue(self.line_edit.text())
        self.issue_list.append(issue)

        # Test if the issue was created successfully
        if issue.number != -1:
            self.save()
            self.info.setText(f"Issue {self.line_edit.text()} Created")
        else:
            self.info.setText(f"Issue {self.line_edit.text()} Not Created")
        print(f"Issue {self.line_edit.text()} Created")

    def openIssue(self):
        """
        After making sure that an issue with the number provided exists,
        it's created and shown a new window IssueWindow, used to manage the issue at hand.
        """
        found = False
        for i in self.issue_list:
            if i.number == self.line_edit.text():
                found = True
                self.issuewindow = IssueWindow(self.issue_list, i)
                self.issuewindow.resize(750, 500)
                self.issuewindow.show()
                print(f"Issue {self.line_edit.text()} Opened")
                self.info.setText(f"Issue {self.line_edit.text()} Opened")

        if not(found):
            self.errorNonExistentPrompt()

    def deleteIssue(self):
        """
        Goes to the path where the files of the Issue are located, deletes them, removes the issue from
        issue_list and then saves the changes in a file
        """
        os.chdir(r"C:\Users\andre.costa\Desktop\Farmatodo\Issues")
        for i in self.issue_list:
            if i.number == self.line_edit.text():
                self.issue_list.remove(i)
                shutil.rmtree(i.path)
                self.save()
                print("Deleted Issue " + self.line_edit.text())
                self.info.setText("Deleted Issue " + self.line_edit.text())
                return
        self.errorNonExistentPrompt()

    def warningPrompt(self):
        """
        Creates a prompt message with 2 buttons where the user
        chooses to go ahead and delete an Issue or cancel the action
        """

        ret = QMessageBox.warning(self, "!",f"Are you sure you want to delete Issue {self.line_edit.text()}?"
                                  ,QMessageBox.Yes | QMessageBox.Cancel)

        if ret == QMessageBox.Yes:
            self.deleteIssue()
        else:
            print("Operation Canceled")
            return

    def errorNonExistentPrompt(self):
        """
        Creates a prompt message just to let the user know
        that the Issue they're trying to manage doesn't exist
        """
        ret = QMessageBox.critical(self,"!!!",f"Issue {self.line_edit.text()} doesn't exist", QMessageBox.Ok)

        if ret == QMessageBox.Ok:
            return
