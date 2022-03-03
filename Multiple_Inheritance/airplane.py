# import base
from vehicle import vehicle


# child_1
class airplane(vehicle):

    # deklarasi atribut privat
    __airplaneType = ""
    __airplaneAge = 0
    __wingSpan = 0
    __lengthBody = 0
    __tallHeight = 0
    __cabinWidth = 0

    # membuat constructor
    def __init__(self):
        self.__airplaneType = ""
        self.__airplaneAge = 0
        self.__wingSpan = 0
        self.__lengthBody = 0
        self.__tallHeight = 0
        self.__cabinWidth = 0

    # get set atribut airplaneType
    def setTypeAir(self, airplaneType):
        self.__airplaneType = airplaneType

    def getTypeAir(self):
        return self.__airplaneType

    # get set atribut airplaneAge
    def setAgeAir(self, airplaneAge):
        self.__airplaneAge = airplaneAge

    def getAgeAir(self):
        return self.__airplaneAge

    # get set atribut wingSpan
    def setWing(self, wingSpan):
        self.__wingSpan = wingSpan

    def getWing(self):
        return self.__wingSpan

    # get set atribut lenghtBody
    def setBody(self, lengthBody):
        self.__lengthBody = lengthBody

    def getBody(self):
        return self.__lengthBody

    # get set atribut tallHeight
    def setTall(self, tallHeight):
        self.__tallHeight = tallHeight

    def getTall(self):
        return self.__tallHeight

    # get set atribut cabinWidth
    def setCabin(self, cabinWidth):
        self.__cabinWidth = cabinWidth

    def getCabin(self):
        return self.__cabinWidth

    # fungsi call move
    def move(self):
        print("Airplane " + str(self.getTypeAir()) + " is flying.")

    # print airplane
    def printAirplane(self):
        print("Airplane Type    : " + str(self.getTypeAir()))
        print("Airplane Age     : " + str(self.getAgeAir()) + " years old")
        print("Wingspan         : " + str(self.getWing()) + " meters")
        print("Body Length      : " + str(self.getBody()) + " meters")
        print("Tall Height      : " + str(self.getTall()) + " meters")
        print("Cabin Width      : " + str(self.getCabin()) + " meters")
        self.move()
        print("==================================")
