import random, sys

"""This is a rock, paper, scissors game """
print('ROCK, PAPER, SCISSORS')
print('0 Wins, 0 Losses, 0 Ties')
wins = 0
losses = 0
ties = 0
move = input("Enter your move: (r)ock (p)aper (s)cissors or (q)uit ")
rps_list = ["ROCK versus...", "PAPER versus...", "SCISSORS versus..."]
choice = random.choice(rps_list)


#Iterate through choice and move chosen by user
if move == "p":
    print(choice, end='\n' "PAPER ")
elif move == "r":
    print(choice, end='\n' "ROCK ")
elif move == "s":
    print(choice, end='\n' "SCISSORS ")
else:
    sys.exit()
    
    