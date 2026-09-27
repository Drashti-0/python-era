from abc import ABC

class animal(ABC):
    def make_sound():
        pass

class lion(animal):
    def make_sound(self):
        print(":roar!!!")
        
class cow(animal):
    def make_sound(self):
        print("Moo!!")
        
        
lion=lion()
lion.make_sound()

cow=cow()
cow.make_sound()