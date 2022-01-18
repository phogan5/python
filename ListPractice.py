from os import system, name
from random import seed 
from random import randint
#Clear screen function (unrelated to exercise)
def cls():
    _=system('cls')


#3.4
guestList = ['Mike Tyson', 'Albert Einstein', 'Stephan King', 'Kobe Bryant', 'John Adams']

for i in guestList:
    print ("Greetings " + i + "! You are graciously invited to this celebratory dinner. We hope you can attend!")


input("Press enter to continue to part 3.5")
cls()

#3.5
cantAttend = guestList.pop(3)
print(f"Uh Oh, it looks like {cantAttend.title()} can't attend :(")

print("It looks like Linus Torvalds can come instead!")
guestList.append('Linus Torvalds')
print("The new guest list looks like this:")
for i in guestList:
    print (i)

input("Press enter to continue to part 3.6")
cls()

#3.6
choicesLeft = 2
while choicesLeft > 0:
    choice = input(f'Good news! {choicesLeft} more people can attend, who should we invite next?\n')
    guestList.append(choice.title())
    choicesLeft = choicesLeft - 1

print ('Invitations will now go out for: ')
for i in guestList:
    print (i)

input("Press enter to continue to part 3.7")
cls()

print('Nevermind, it looks like two people will actually have to leave.\n To be fair lets pick random names from a hat.')
seed(1)
namecount = len(guestList)

choicesLeft = 2
while choicesLeft > 0:
    randvalue = randint(0, namecount)
    goinghome = guestList[randvalue]
    print(f'Looks like {goinghome} has to go home.\n')
    guestList.remove(goinghome)

    choicesLeft = choicesLeft - 1
    seed(5)


print ("This is the FINAL guest list:")
for i in guestList:
    print (i)


    



