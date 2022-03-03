# base 2
class job():

    # deklarasi atribut privat
    __NIP = ""
    __nameCompany = ""
    __positionJob = ""

    # membuat constructor
    def __init__(self):
        self.__NIP = ""
        self.__nameCompany = ""
        self.__positionJob = ""

    # get set atribut NIP
    def setNIP(self, NIP):
        self.__NIP = NIP

    def getNIP(self):
        return self.__NIP

    # get set atribut nameCompany
    def setCompany(self, nameCompany):
        self.__nameCompany = nameCompany

    def getCompany(self):
        return self.__nameCompany

    # get set atribut positionJob
    def setPos(self, positionJob):
        self.__positionJob = positionJob

    def getPos(self):
        return self.__positionJob

    # print class
    def printJob(self):
        print("NIP          : " + str(self.getNIP()))
        print("Company Name : " + str(self.getCompany()))
        print("Job Position : " + str(self.getPos()))
        print("==================================")
