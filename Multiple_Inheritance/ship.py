# import base
from vehicle import vehicle


# child_2
class ship(vehicle):

    # deklarasi atribut privat
    __shipType = ""
    __shipAge = 0
    __manufactureCountry = ""

    # membuat constructor
    def __init__(self):
        self.__shipType = ""
        self.__shipAge = 0
        self.__manufactureCountry = 0

    # get set atribut shipType
    def setTypeShip(self, shipType):
        self.__shipType = shipType

    def getTypeShip(self):
        return self.__shipType

    # get set atribut shipAge
    def setAgeShip(self, shipAge):
        self.__shipAge = shipAge

    def getAgeShip(self):
        return self.__shipAge

    # get set atribut manufacture country
    def setManu(self, manufactureCountry):
        self.__manufactureCountry = manufactureCountry

    def getManu(self):
        return self.__manufactureCountry

    # fungsi call move
    def move(self):
        print("Ship " + str(self.getTypeShip()) + " is sailed.")

    # print ship
    def printShip(self):
        print("Ship Type        : " + str(self.getTypeShip()))
        print("Ship Age         : " + str(self.getAgeShip()) + "years old")
        print("Manufacturer     : " + str(self.getManu()))
        self.move()
        print("==================================")
