from abc import ABC, abstractmethod
from math import pi

class Switchable(ABC):

    @abstractmethod
    def turn_of(self):
        pass

    @abstractmethod
    def turn_on(self):
        pass

class Light(Switchable):
    is_on = False

    def turn_on(self):
        self.is_on = True

    def turn_of(self):
        self.is_on = False