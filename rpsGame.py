import random, sys

"""This is a rock, paper, scissors game """
print('ROCK, PAPER, SCISSORS')
print('0 Wins, 0 Losses, 0 Ties')
wins = 0
losses = 0
ties = 0
# move = input("Enter your move: (r)ock (p)aper (s)cissors or (q)uit ")
rps_list = ["ROCK versus...", "PAPER versus...", "SCISSORS versus..."]
choice = random.choice(rps_list)
print(choice)

# Loop through the program
# while True:    
#     if move == "p":
#         print("PAPER")
#     elif move == "r":
#         print("ROCK")
#     elif move == "s":
#         print("SCISSORS")
#     else:
#         sys.exit()

    