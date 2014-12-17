from random import randint

won = False
guesses = 10

screen = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
def display_screen():
    for i in range(len(screen)):
        print screen[i]
display_screen()

# shipx needs to be 1 behind what it should be.
#shipx = 0
shipx = randint(0, 4)
# shipy needs to be negative
#shipy = -1
shipy = randint(1, 5) * -1

while not won and guesses > 0:
    print " You have " + str(guesses) + " guesses left!"
    posx = int(raw_input("X?")) - 1
    posy = int(raw_input("Y?")) * -1

    if posx == shipx and posy == shipy:
        screen[posy][posx] = "H"
        display_screen()
        print "You sunk my battleship, you win!"
        won = True
    else:
        screen[posy][posx] = "M"
        display_screen()
        guesses -= 1

raw_input("PRESS ENTER TO EXIT")