class Herbivore:
    def eat_plants(self):
        print("Eats plants")




class Carnivore:
    def eat_meat(self):
        print("Eats meat")



class Omnivore:
    def eat_both(self):
        print("Eats plants and meat")


class Bear(Herbivore, Carnivore, Omnivore):
    def show(self):
        print("Bear")


b1 = Bear()



b1.show()
b1.eat_plants()
b1.eat_meat()
b1.eat_both()