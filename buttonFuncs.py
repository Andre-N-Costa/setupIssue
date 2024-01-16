import os
import pickle
import shutil

from IssueClass import Issue


def createButton(issues, number):
    issue = Issue(number)
    issues.append(issue)


def addButton(issues, number):
    for i in issues:
        if i.number == number:
            i.add2Notes()
            return
    print("Issue " + number + " doesn't exist")


def openButton(issues, number):
    os.chdir(r"C:\Users\andre.costa\Desktop\random code\IssueAuto")
    for i in issues:
        if i.number == number:
            i.openNotes()
            return
    print("Opened Issue " + number)


def save(issues, root):
    os.chdir(r"C:\Users\andre.costa\Desktop\random code\IssueAuto")
    with open('issuesfile.pkl', 'wb') as outp:
        pickle.dump(issues, outp, pickle.HIGHEST_PROTOCOL)
    root.destroy()


def delete(issues, number):
    os.chdir(r"C:\Users\andre.costa\Desktop\Farmatodo\Issues")
    for i in issues:
        if i.number == number:
            issues.remove(i)
            shutil.rmtree(i.path)
            print("Deleted Issue " + number)
            return
    print("Issue " + number + " doesn't exist")
