import wikipedia


class TextExtractor:

    __numberOfObjects: int
    __csvObjects: [][]

    def __init__(self, pageTitle, pageId):
        self.__numberOfObjects = 0
        self.__csvObjects = [][]

    def getObject(self, position=pos):
        return self.__csvObjects[pos]
        
    def extract(self):
        page = wikipedia.page(title=self.__pageTitle, pageid=self.__pageId)
        f = open("./text/" + self.__pageTitle + ".txt", "w")
        f.write(page.content)
        f.close()

    def getText(self):
        # TODO use csv class to import csv and save asd self.__csvObjects[][]
        f = open("./text/" + self.__pageTitle + ".txt", "r")
        return f.read()
