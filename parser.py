import pprint
from collections import OrderedDict


class Parser:
    def __init__(self, path):
        self.data = {}
        self.number = -1
        self.path = path
        self.parseData()

    def parseData(self):
        # read file and format lines for comfort
        def getLines():
            # Read from file
            f = open(self.path, "r")
            lines = f.readlines()
            f.close()

            # Format lines before returning
            lineNum = -1+1  # idk why I put -1 here before
            for line in lines:
                # clean line from white space in the beginning and comments
                line = line.split("//")[0].strip()
                lines[lineNum] = line
                lineNum += 1
            # remove all empty lines
            empties = True
            while (empties):
                try:
                    lines.remove('')
                except:
                    empties = False

            return lines

        # recursively traverse text data and insert into dictionary
        def handleData(subDict, key = ''):
            # uses local lines variable
            self.number += 1
            if self.number >= len(lines):
                return
            line = lines[self.number]
            if line.find(":") > -1:
                split = line.split(":")
                Lline = split[0].rstrip()
                Rline = split[1].rstrip().lstrip()
                subDict[Lline] = Rline  # add key value pairs to data dict
                handleData(subDict)
                return
            if line.find("{") > -1:
                split = line.split("{")
                key = split[0].rstrip()
                subDict[key] = {}
                handleData(subDict[key])
                handleData(subDict)
            if self.number >= len(lines) or lines[self.number].find("}") > -1:
                return

        lines = getLines()
        handleData(self.data)
        # pprint.pprint(self.data)
        return self.data

    def getData(self):
        return self.data


# # Running flow - create Parser object, pass the path. Run getData()
# file_path = "./Intel/flow.tessent_meta"  # for test purposes
#
# test = Parser(file_path)
# finalData = test.getData()
#
# pprint.pprint((finalData))
