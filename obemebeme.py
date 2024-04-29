import random

class Cat:
    def __init__(self, name):
        self.name = name
        self.hunger = 50
        self.energy = 50
        self.happiness = 50
        self.alive = True
        self.days_lived = 0

    def eat(self):
        print("Eat time")
        self.hunger -= 10
        self.energy += 5
        self.happiness += 2

    def sleep(self):
        print("good night")
        self.energy += 10
        self.hunger += 5

    def play(self):
        print("'lets play cuz i'm bored")
        self.energy -= 10
        self.hunger += 5
        self.happiness += 5

    def is_alive(self):
        if self.hunger <= 0 or self.energy <= 0:
            print("Your cat is too tired and hungry...")
            self.alive = False
        elif self.happiness <= 0:
            print("Your cat is sad and depressed...")
            self.alive = False

    def end_of_day(self):
        print(f"Hunger: {self.hunger}")
        print(f"Energy: {self.energy}")
        print(f"Happiness: {self.happiness}")

    def live(self, day):
        print(f"Day {day} of {self.name}'s life".center(50, "="))
        action = random.choice(["eat", "sleep", "play"])
        if action == "eat":
            self.eat()
        elif action == "sleep":
            self.sleep()
        elif action == "play":
            self.play()

        self.end_of_day()
        self.is_alive()
        self.days_lived += 1

obeme = Cat(name="Garfield")
for day in range(1, 366):
    if not obeme.alive:
        break
    obeme.live(day)

print(f"{obeme.name} lived {obeme.days_lived} days out of 365.")
