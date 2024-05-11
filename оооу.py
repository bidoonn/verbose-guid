class Sword:
    def __init__(self, durability):
        self.durability = durability

    def use(self, player):
        if player.alive:
            self.durability -= 1
            if self.durability <= 0:
                print("The sword is broken!")
                player.die()
            else:
                print("The sword is used.")
        else:
            print("The game is over. Player is dead.")

    def repair(self, blacksmith):
        self.durability = blacksmith.repair(self)
        print("The sword is repaired.")


class Player:
    def __init__(self, name):
        self.name = name
        self.alive = True

    def use_sword(self, sword):
        sword.use(self)

    def die(self):
        print(f"{self.name} died.")
        self.alive = False


class Blacksmith:
    def repair(self, sword):
        print("Repairing the sword...")
        return sword.durability + 5  


sword = Sword(durability=10)
player = Player(name="John")
blacksmith = Blacksmith()

player.use_sword(sword)


for _ in range(10):
    player.use_sword(sword)


sword.repair(blacksmith)


player.use_sword(sword)
