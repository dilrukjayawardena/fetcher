import json
class FileHandler:
    def __init__(self,fileName):
        self.fileName=fileName
    # write to json file
    def writeToFile(self,data):
        f=open(self.fileName, 'w')
        f.write(json.dumps(data))
        f.close()
