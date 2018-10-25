from random import randint

#  available weapons => stored in an array
#  choices numbers 0, 1, 2
choices = ["Rock", "Paper", "Scissors"]
player = False

# making the computer pick one item at random
computer = choices[randint(0,2)]

# user choice
while player is False:
    player = input("Rock, Paper or Scissors?")
    print("Player chooses:", player)
# showing the computers choice in the terminal window
    print("Computer Chooses:", computer)


# check for equal values
    if (player == computer):
        print("It's a tie!")

# paper beats rock
    elif (player == "Rock"):
        if (computer == "Paper"):
            # computer wins
            print("Computer Wins. You Lose!", computer, "covers", player)
        else:
            print("You Win! Computer Loses!", player, "covers", computer)

# scissors cuts paper
    elif (player == "Paper"):
        if (computer == "Scissors"):
            # computer wins
            print("Computer Wins. You Lose!", computer, "cuts", player)
        else:
            print("You Win! Computer Loses!", player, "cuts", computer)

# rock smashes scissors
    elif (player == "Scissors"):
        if (computer == "Rock"):
            # computer wins
            print("Computer Wins. You Lose!", computer, "smashes", player)
        else:
            print("You Win! Computer Loses!", player, "smashes", computer)

# to quit
    elif player == "Quit":
        exit()

# final else
    else:
        print("Please select a valid option")

    player = False
    computer = choices[randint(0,2)]