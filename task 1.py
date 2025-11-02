# Create an abstract class named Absclass with one abstract method named task and one regular method named print that takes a parameter x and prints it.
from abc import ABC, abstractmethod
class Absclass(ABC):
    # Regular method
    def  print(self,x):
        print("Past value is:",x)
    @abstractmethod
    def task(self):
        print("We are in Absclass task")
# Create a subclass of Absclass
class test_class(Absclass):
    def task(self):
        print("We are in test_class task")
#object of subclass
test_obj = test_class()
test_obj.task()
test_obj.print(100)