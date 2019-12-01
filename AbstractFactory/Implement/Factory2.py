import Interface.AbstractFactory as abf
from Implement.cow import cow
import Implement.apple as apple

class Factory2(abf.AbstractFactory):
    def newAnimal(self):
        return cow()
    def newPlant(self):
        return apple.apple()