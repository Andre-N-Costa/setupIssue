import os
import pickle
import sys
from PySide6.QtWidgets import QApplication
from widget import Widget

issue_list = list()

"""
Main file of the app

Before running the app, it's loaded all the issue objects that
we have saved.
"""

os.chdir(r"C:\Users\andre.costa\Desktop\random code\IssueAuto")
try:
    with open('issuesfile.pkl', 'rb') as inp:
        print("Loading data...")
        issue_list = pickle.load(inp)
except:
    pass
print("Done")

app = QApplication(sys.argv)

widget = Widget(issue_list)
widget.resize(500, 50)
widget.setStyleSheet("""
    font-size: 15px;
""")
widget.show()

app.exec()