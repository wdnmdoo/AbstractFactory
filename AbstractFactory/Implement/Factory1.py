import Interface.AbstractFactory as abf
from .hourse import hourse
from .banana import banana

class Factory1(abf.AbstractFactory):
    def newAnimal(self):
        return hourse()
    def newPlant(self):
        return banana()