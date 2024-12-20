import time

class VirtualPet:
    def __init__(self, name):
        self.name = name
        self.hunger = 50  # Hunger level: 0 (full) to 100 (starving)
        self.happiness = 50  # Happiness level: 0 (sad) to 100 (very happy)
        self.energy = 50  # Energy level: 0 (tired) to 100 (energetic)

    def feed(self):
        if self.hunger > 0:
            self.hunger -= 10
            self.happiness += 5
            print(f"You fed {self.name}. Hunger decreased, happiness increased!")
        else:
            print(f"{self.name} is not hungry right now.")

    def play(self):
        if self.energy > 10:
            self.happiness += 10
            self.energy -= 10
            print(f"You played with {self.name}. Happiness increased, but energy decreased.")
        else:
            print(f"{self.name} is too tired to play. Let them rest.")

    def rest(self):
        self.energy += 20
        self.hunger += 10
        print(f"{self.name} took a nap. Energy increased, but hunger increased.")

    def check_status(self):
        print(f"\nStatus of {self.name}:\nHunger: {self.hunger}\nHappiness: {self.happiness}\nEnergy: {self.energy}\n")

    def update(self):
        # Simulates time passing
        self.hunger += 5
        self.happiness -= 5
        self.energy -= 5

        if self.hunger > 100:
            print(f"Oh no! {self.name} is starving!")
            self.happiness -= 10

        if self.happiness < 0:
            print(f"{self.name} is very unhappy. Spend some time with them!")

        if self.energy < 0:
            print(f"{self.name} is exhausted. Let them rest.")

# Main game loop
def main():
    name = input("What would you like to name your pet? ")
    pet = VirtualPet(name)

    print(f"\nWelcome to the Virtual Pet Game! Meet {name}.\n")

    while True:
        pet.check_status()
        print("What would you like to do?")
        print("1. Feed")
        print("2. Play")
        print("3. Rest")
        print("4. Quit")

        choice = input("Enter your choice (1-4): ")
        if choice == "1":
            pet.feed()
        elif choice == "2":
            pet.play()
        elif choice == "3":
            pet.rest()
        elif choice == "4":
            print(f"Goodbye! Take care of {name}!")
            break
        else:
            print("Invalid choice. Please select 1, 2, 3, or 4.")

        pet.update()
        time.sleep(1)

if __name__ == "__main__":
    main()
