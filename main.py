

class Pet:
    def __init__(self, name, hunger, happiness, energy):
        self.name = name
        self.hunger = hunger
        self.happiness = happiness
        self.energy = energy

    hunger = 10
    happiness = 10
    energy = 10

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