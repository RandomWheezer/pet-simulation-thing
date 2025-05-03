

class Pet:
    def __init__(self, name, hunger, happiness, energy):
        self.name = name
        self.hunger = hunger
        self.happiness = happiness
        self.energy = energy





while True:
    print("Handle your own virtual pet")
    pet_name =  input("What will your pet name will be? ")
    name = Pet(name=pet_name)
    if name:
        print(f"Your pet name is {name}")
    else:
        print("ERR: Please redo the prompt")
        break
    print("Choose an option of your pet \n feed [ feed your pet]\n play [play with your pet]\n rest [rest your pet]\n status [show the status of your pet]\n ")
    option_input = input("Enter an option: ")

    

