from abc import ABCMeta, abstractmethod

class Plant:
    __metaclass__ = ABCMeta

    @abstractmethod
    def show(self):
        pass