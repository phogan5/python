class character:
    def __init__(self, name, hp, acc, inventory, exp):
        self.name = name
        self.hp = hp
        self.acc = acc
        self.inventory = inventory
        self.exp = exp






class Rouge(character):
    def __init__(self):
        super().__init__(name=input("What is your characters name?"), hp = 75, acc = 90, inventory={"Iron Dagger"}, exp = 0)

    prof = "Rouge"
    maxhp = 100
    level = 1

class Knight(character):
    def __init__(self):
        super().__init__(name=input("What is your characters name?"), hp = 125, acc = 85, inventory={"Steel Sword"}, exp = 0)
    
    prof = "Knight"
    maxhp = 125
    level = 1

class Sorcerer(character):
    def __init__(self):
        super().__init__(name=input("What is your characters name?"), hp = 100, acc = 80, inventory={"Oak Wood Staff"}, exp = 0)

    prof = "Sorcerer"
    maxhp = 100
    level = 1

def chooseclass():
    print("Which class will you play as?\n")
    print ('Press R for Rouge: A stealthy swordsman, skirting the line between good and evil.')
    print ('Press K for Knight: A battle-hardened warrior fighting for the honor of the throne.')
    print ('Press S for Sorcerer: A mysterious spellcaster who uses the power of magic to defeat her foes.')
pclass = input(">>>")

##if prof == "R":
    #prof = Rouge()
##elif prof == "K":
    #prof = Knight()
##elif prof == "S":
    #prof = Sorcerer()







chooseclass()