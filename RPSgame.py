from random import randint

#  available weapons => stored in an array
choices = ["Rock", "Paper", "Scissors"]

# making the computer pick one item at random
computer_choice = choices[randint(0,2)]

# showing the computers choice in the terminal window
print("Computer Chooses:", computer_choice)
