
class Reader(object):

  def __init__(self, fileName):

    self.file = open(fileName, 'r')
    self.fileLines = self.file.readlines()
    self.file.close()
    self.years = self.getYears()
    self.fileLines = self.fileLines[5:]

    print(self.fileLines)

  def getYears(self):
    # self.years = self.fileLines[4].split("[")
    # self.years = self.years[2][:-2]
    # self.years = self.years.split("=").pop(1).split("-")
    return self.fileLines[4].split("[")[2][:-2].split("=").pop(1).split("-")

R = Reader("Version1/cru-ts-2-10.1991-2000-cutdown.pre")