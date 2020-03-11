
from tkinter import *

class Reader(object):

  def __init__(self, fileName, databasePath):

    self.file = open(fileName, 'r')
    self.fileLines = self.file.readlines()
    self.file.close()
    self.years = self.getYears()
    self.fileLines = self.fileLines[5:]

    self.file = open(databasePath, "w")

    self.currentPos = []
    self.currentYear = int(self.years[0])
    self.prevLine = None
    self.currentLine = None

    self.file.write("Xref,Yref,Date,Value\n")

    for line in self.fileLines:
      if "Grid-ref=" in line:
        self.currentPos = list(filter(None, line.split(" ")[1:]))
        self.currentPos = [self.currentPos[0][:-1], self.currentPos[1].rstrip("\n")]
        self.currentYear = int(self.years[0])

      else:
        self.prevLine = self.currentLine
        self.currentLine = list(filter(None, line.split(" ")))
        try:
          self.currentLine[11] = self.currentLine[11].rstrip("\n")

        except:
          print("{}, {}".format(self.currentPos[0], self.currentPos[1]))

        for month in range(len(self.currentLine)):
          self.file.write("{},{},{}/1/{},{}\n".format(self.currentPos[0], self.currentPos[1], month+1, self.currentYear, self.currentLine[month]))

        self.currentYear += 1

    self.file.close()

  def getYears(self):
    return self.fileLines[4].split("[")[2][:-2].split("=").pop(1).split("-")

class InputWindow(object):

  def __init__(self):
    self.root = Tk()

    self.root.geometry("300x300")

    self.fileLocationLabel = Label(self.root, text="File Location")
    self.fileLocationEntry = Entry(self.root)

    self.fileLocationLabel.grid(row=0, column=0)
    self.fileLocationEntry.grid(row=0, column=1, ipadx=25, ipady=3, padx=3, pady=2)

    self.databaseLocationLabel = Label(self.root, text="Database Location")
    self.databaseLocationEntry = Entry(self.root)

    self.databaseLocationLabel.grid(row=1, column=0)
    self.databaseLocationEntry.grid(row=1, column=1, ipadx=25, ipady=3, padx=3, pady=2)

    self.submitButton = Button(self.root, text="Create Database", command=self.getData)
    self.submitButton.grid(row=3, ipadx=30, ipady=5, columnspan=2)

    self.warnings = StringVar()
    self.warnings.set(" ")
    self.warningsLabel = Label(self.root, textvariable=self.warnings)
    self.warningsLabel.grid(row=4, ipadx=30, ipady=5, columnspan=2)

  def update(self):
    mainloop()

  def getData(self):
    self.fileLocation = self.fileLocationEntry.get()
    self.databaseLocation = self.databaseLocationEntry.get()

    if self.checkFile(self.fileLocation):
      self.warnings.set("")
      self.r = Reader(self.fileLocation, self.databaseLocation)
      self.warnings.set("Completed")

    else:
      self.warnings.set("File location not found")

  def checkFile(self, fileLoc):
    try:
      file = open(fileLoc, 'r')
      return True
    except FileNotFoundError:
      return False

window = InputWindow()
window.update()

