#import neceary packages
from abc import ABC, abstractmethod
# Create an abstract class named Animal with one abstract method named sound and one regular method named info that takes a parameter name and prints it.
class Animal(ABC):
#abstract method
    # Regular method
    def move(self):
        pass
#subclass of Animal
class Human(Animal):
    def move(self):
        print("I can walk")
class Snake(Animal):
    def move(self):
        print("I can crawl")
class Dog(Animal):
    def move(self):
        print("I can bark")
class Lion(Animal):
    def move(self):
        print("I can roar")
#driver code
R = Human()
R.move()
K = Snake()
K.move()
R = Dog()
R.move()
K = Lion()
K.move()