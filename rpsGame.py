import random, sys

"""This is a rock, paper, scissors game """
print('ROCK, PAPER, SCISSORS')
print('0 Wins, 0 Losses, 0 Ties')
wins = 0
losses = 0
ties = 0
rps_list = ["ROCK ", "PAPER", "SCISSORS"]


#Iterate through choice and move chosen by user
while True:
    move = input("Enter your move: (r)ock (p)aper (s)cissors or (q)uit ")
    choice = random.choice(rps_list)
    if move == "p":
        print("PAPER versus...", choice)
    elif move == "r":
        print("ROCK versus...", choice)
    elif move == "s":
        print("SCISSORS verus...", choice)
    else:
        sys.exit()
    
# Calculate and update the score board
    if (move == "r" and choice == "ROCK") or (move == "p" and choice == "PAPER") or (move == "s" and choice == "SCISSORS"):
        print("It's  a tie!")
        ties += 1
        print(f"{int(wins)} Wins, {int(losses)} Losses, {int(ties)} Ties")
    elif move == "p" and choice == "ROCK": 
        print("You win!")
        wins += 1
        print(f"{int(wins)} Wins, {int(losses)} Losses, {int(ties)} Ties")
    elif move == "r" and choice == "SCISSORS":
        print("You win!")
        wins += 1
        print(f"{int(wins)} Wins, {int(losses)} Losses, {int(ties)} Ties")
    elif move == "s" and choice == "PAPER":
        print("You win!")
        wins += 1
        print(f"{int(wins)} Wins, {int(losses)} Losses, {int(ties)} Ties")
    else:
        print("You lose")
        losses += 1
        print(f"{int(wins)} Wins, {int(losses)} Losses, {int(ties)} Ties")