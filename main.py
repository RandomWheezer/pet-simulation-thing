

class Pet:
    def __init__(self, name,  hunger, happiness, energy):
    
        self.hunger = hunger
        self.happiness = happiness
        self.energy = energy

    hunger = 0
    happiness = 10
    energy = 10


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
        if hunger<6 and happiness<4:
            hunger = hunger+3
            happiness = happiness-3
            print("time has passed.")
        else:
            print("Your pet needs more care before passing more time.")

    print("Handle your own virtual pet!")
    name = str(input("What will your pet name be?"))
    if name:
        print(f"Your pet's name is {name}.")
    else:
        print("ERROR, please rerun.")


    while True:
        print("Choose an option \n feed \n play \n rest \n status (check on your pet)\n Update (pass time)")
        option_input = input("Enter an option: ")


        if option_input == "feed":
            if hunger == 10:
                print("Your pet is full")
                
            elif hunger < 5:
                hunger += 5
                print("Your pet is fed")
            else:
                hunger += 1
                print("Your pet is fed")
        elif option_input == "play":
            play()
        elif option_input == "rest":
            rest()
        elif option_input == "status":
            status()
        elif option_input == "update":
            update()