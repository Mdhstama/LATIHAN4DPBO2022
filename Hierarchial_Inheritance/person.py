# base 1
class person():

    # deklarasi atribut privat
    __NIK = ""
    __name = ""
    __gender = ""

    # membuat constructor
    def __init__(self):
        self.__NIK = ""
        self.__name = ""
        self.__gender = ""

    # get set atribut NIK
    def setNIK(self, NIK):
        self.__NIK = NIK

    def getNIK(self):
        return self.__NIK

    # get set atribut name
    def setName(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    # get set atribut gender
    def setGen(self, gender):
        self.__gender = gender

    def getGen(self):
        return self.__gender

    # fungsi call sleep
    def sleepy(self):
        print(str(self.getName()) + " is sleep.")

    # print class
    def printPerson(self):
        print("NIK          : " + str(self.getNIK()))
        print("Name         : " + str(self.getName()))
        print("Gender       : " + str(self.getGen()))
        self.sleepy()
        print("==================================")
