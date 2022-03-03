# base
class vehicle():

    # deklarasi atribut privat
    __fuelType = ""
    __maxPassengers = ""
    __codeID = ""

    # membuat constructor
    def __init__(self):
        self.__fuelType = ""
        self.__maxPassengers = ""
        self.__codeID = ""

    # get set atribut fuelType
    def setFuel(self, fuelType):
        self.__fuelType = fuelType

    def getFuel(self):
        return self.__fuelType

    # get set atribut maxPassengers
    def setMax(self, maxPassengers):
        self.__maxPassengers = maxPassengers

    def getMax(self):
        return self.__maxPassengers

    # print vehicle
    def printVehicle(self):
        print("Fuel Type        : " + str(self.getFuel()))
        print("Max Passengers   : " + str(self.getMax()) + " passengers")
        print("==================================\n")
