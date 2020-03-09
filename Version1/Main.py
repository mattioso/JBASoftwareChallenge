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

filePath = ""
databasePath = ""

Reader("cru-ts-2-10.1991-2000-cutdown-modified.pre", "Database.csv")

