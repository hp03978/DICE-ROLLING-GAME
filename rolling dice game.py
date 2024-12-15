import random

def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value,max_value)

    return roll

players = int(input("enter the number of players(2 - 4): "))
if  players >=2 and players <= 4:
    print("okay, ready to go!")

else:
    print("Must be between 2 - 4")

max_score = 50
players_score = [0 for i in range(players)]

while max(players_score) < max_score:
    for player_index in range(players):
     print("\nplayer number", player_index + 1, "turn has just started\n")
     print("you total score is:", players_score[player_index] , "\n")
     current_score = 0

    while True:
     should_roll = (input("would you like to roll?(y)"))

     if should_roll.lower() != "y":
      break

     value = roll()
     if value == 1:
        print("you rolled a 1!, turn done")
        break
     else:
        current_score += value
        print("you rolled a :", value)

     print("your score is:", current_score)
    players_score[player_index] += current_score
    print("your total score is:", players_score[player_index])

max_score = max(players_score)
winning_index = players_score.index(max_score)
print("player number", winning_index , "is the winner with a score of:", max_score)
