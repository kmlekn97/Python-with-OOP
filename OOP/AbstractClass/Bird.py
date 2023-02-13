from Animal import Animal
from abc import ABC,abstractmethod
class Bird(Animal):
    def __init__(self):
        print("Bird")

    def walk(self):
        print("Kuş yürüyor")

    def run(self):
        print("kuş koşuyor")

