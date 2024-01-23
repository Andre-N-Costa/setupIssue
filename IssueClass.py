import os
import webbrowser
from datetime import datetime
from tkinter import messagebox


class Issue:
    """
    The class that represents Issues

    Attributes
    ----------
    number : int
        The number of the Issue
    path : str
        The path where the issue is stored with its notes

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

    def __init__(self, number):
        try:
            self.number = number
            self.path = r"C:\Users\andre.costa\Desktop\Farmatodo\Issues" + '\\' + number
            os.chdir(r"C:\Users\andre.costa\Desktop\Farmatodo\Issues")
            os.mkdir(number)
            self.addNotes()
            print("Created Issue " + number)
        except:
            self.number = -1
            messagebox.showwarning("!PROBLEM!", "Not possible to create Issue " + number)

    def addNotes(self):
        os.chdir(self.path)
        now = datetime.now()
        file = open('Notes.txt', 'a')
        file.write(
            "%%%%%%%%%%%%%%%%%%%%% ISSUE " + self.issue.number + " NOTES %%%%%%%%%%%%%%%%%%%%% " + "\n\n--------PROBLEM DESCRIPTION:\n\n--------OBSERVATIONS:\n\n--------POSSIBLE SOLUTION:\n\n" + "%%%%%%%%%%%%%%%%%% CREATED: " + str(
                now)[:19] + " %%%%%%%%%%%%%%%%%%\n\n")
        file.close()
