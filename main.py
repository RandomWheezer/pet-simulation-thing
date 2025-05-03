

class Pet:
    def __init__(self, name, hunger, happiness, energy):
        self.name = name
        self.hunger = hunger
        self.happiness = happiness
        self.energy = energy

    hunger = 0
    happiness = 10
    energy = 10

    def feed(self, hunger):
        if hunger>0:
            print("You have fed your dog.")
            hunger = 10
        else:
            print("Your pet isn't hungry.")

    def play(self, happiness, energy, hunger):
        if happiness<10 and energy>1 and hunger>9:
            print("You played with your pet!")
            happiness = 10
            energy = energy-1
            hunger = hunger+2
        elif energy == 0:
            print("Your pet doesn't have energy to play.")
        elif hunger == 9:
            print("Your pet is too hungry to play.")
        else:
            print("Your pet is unable to play.")

    def rest(self, energy, hunger, happiness):
        if energy == 10 and hunger != 9 and happiness != 1:
            energy = 10
            hunger = hunger+1
            happiness = happiness-1
        else:
            print("unable to rest.")

    def status(self, energy, hunger, happiness, name):
        print(f"Name: {name}\n Hunger: {hunger}\n Happiness: {happiness}\n Energy: {energy}")

    def update(self, hunger, happiness):
        if hunger<7
            hunger = hunger+3
            happiness = happiness-3

    while True:
        print("Handle your own virtual pet!")
        name = str(input("What will your pet name be?"))
        if name:
            print(f"Your pet's name is {name}.")
        else:
            print("ERROR, please redo the prompt")
            break
        print("Choose an option \n feed \n play \n rest \n \n status (check on your pet)")
        option_input = input("Enter an option: ")

        if option_input == "feed":
            feed()
        