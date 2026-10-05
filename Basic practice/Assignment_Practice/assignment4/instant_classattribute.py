class Player:
    player_count = 0

    def __init__(self, name, level):
        self.name = name
        self.level = level
        Player.player_count = Player.player_count + 1

    def display(self):
        print("Name:", self.name)
        print("Level:", self.level)


p1 = Player("Drashti", 10)
p2 = Player("Rahul", 20)
p3 = Player("Krisha", 15)

p1.display()
p2.display()
p3.display()

print("Total players:", Player.player_count)