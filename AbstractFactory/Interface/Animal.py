from abc import ABCMeta, abstractmethod

class AbstractAnimal:
    __metaclass__ = ABCMeta

    @abstractmethod
    def show(self):
        pass