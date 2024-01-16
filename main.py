import os
from tkinter import ttk
from tkinter import *
import tkinter as tk
import pickle

from buttonFuncs import createButton, addButton, openButton, save, delete

issues = list()
os.chdir(r"C:\Users\andre.costa\Desktop\random code\IssueAuto")
try:
    with open('issuesfile.pkl', 'rb') as inp:
        print("Loading...")
        issues = pickle.load(inp)
except:
    pass
print("Done")
print(issues)

root = Tk()

root.title("Issue Setup")
root.geometry("800x400")

content = ttk.Frame(root, padding=(3, 3, 12, 12))
content.pack(fill="none", expand=True)

label = Label(content, text="Issue number: ", font="Verdana 10")
label.grid(row=0, column=0, padx=5, pady=5)

text = Text(content, height=2, width=10)
text.insert('1.0', '1000')
text.grid(row=0, column=1, padx=5, pady=5)

label2 = Label(content, text="Issue number: ", font="Verdana 10")
label.grid(row=0, column=0, padx=5, pady=5)

notes = IntVar()
c1 = Checkbutton(content, text='Notes', variable=notes, onvalue=0, offvalue=1)
c1.grid(row=0, column=2, padx=5, pady=5)

Button(content, height=2, width=40, text="Add Comment to Issue",
       command=lambda: addButton(issues, text.get("1.0", "end-1c"))).grid(row=3, column=0, padx=5, pady=5)

Button(content, height=2, width=40, text="Create Issue",
       command=lambda: createButton(issues, text.get("1.0", "end-1c"))).grid(row=2, column=0, padx=5, pady=5)

Button(content, height=2, width=40, text="Delete Issue",
       command=lambda: delete(issues, text.get("1.0", "end-1c"))).grid(row=2, column=1, padx=5, pady=5)

Button(content, height=2, width=40, text="Save and Close",
       command=lambda: save(issues, root)).grid(row=4, column=0, columnspan=2, padx=5, pady=5)

Button(content, height=2, width=40, text="Open Issue Notes",
       command=lambda: openButton(issues, text.get("1.0", "end-1c"))).grid(row=3, column=1, padx=5, pady=5)

root.mainloop()
