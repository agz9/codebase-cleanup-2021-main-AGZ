
from random import choice

#
# USER SELECTION
#

VALID_OPTIONS = ["rock", "papers", "scissors"]

u = input("Please choose one of 'Rock', 'Paper', or 'Scissors': ").lower()

print("USER CHOICE:", u)
if u not in VALID_OPTIONS:
    print("OOPS, TRY AGAIN")
    exit()

#
# COMPUTER SELECTION
#

c = choice(VALID_OPTIONS)
print("COMPUTER CHOICE:", )

#
# DETERMINATION OF WINNER
#

if u == c:
    print("It's a tie!")
elif u == "rock":
    if c == "paper":
        print("The computer wins")
    elif c == "scissors":
        print("The user wins") 
elif u == "scissors":
    if c == "rock":
        print("The computer wins")
    elif c == "paper":
        print("The user wins")
elif u == "paper":
    if c == "rock":
        print("The computer wins")
    elif c == "scissors":
        print("The user wins") 
