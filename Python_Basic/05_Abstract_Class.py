#Write a program using an abstract class.
from abc import ABC, abstractmethod
class family(ABC):
    @abstractmethod
    def greeting(self):
        pass

class dad(family):
    def greeting(self):
        return "hello dad!!"

class mom(family):
    def greeting(self):
        return "hello mom!!"

m=mom()
print(m.greeting())
d=dad()
print(d.greeting())
