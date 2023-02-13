from abc import ABC,abstractmethod
class Animal(ABC):
    @abstractmethod
    def walk(self):
        pass

    @abstractmethod
    def run(self):
        pass