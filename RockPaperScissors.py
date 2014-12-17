from random import randint

gameloop = True

def choose():
    rndm = randint(0,3)
    if rndm == 1:
        return 'rock'
    elif rndm == 2:
        return 'paper'
    else:
        return 'scissors'

def check(uc, cc):
    if uc == cc:
        print "You tied."
    elif uc == "rock" and cc == "scissors":
        print "Rock crushes Scissors, you win!"
    elif uc == "paper" and cc == "rock":
        print "Paper covers Rock, you win!"
    elif uc == "scissors" == cc == "paper":
        print "Scissors cut Paper, you win!"
    else:
        print "Your opponent has defeated you!"

def again():
    print "Would you like to play again? y/n"
    again = raw_input("> ")
    nagain = again.lower()

    if nagain == "y":
        gameloop = True
    else:
        gameloop = False

while gameloop:
    print "What do you choose? \nRock\nPaper\nScissors"
    user_choice = raw_input("CHOICE: ")

    nuser = user_choice.lower()
    computer_choice = choose()

    check(nuser, computer_choice)

    gameloop = again()