# 1. Each player takes a turn in, throwing 3 darts.
# 2. To decide who starts, each player throws one dart at the bullseye - the one closest begins the game. (If you prefer, toss a coin.)
# 3. When it's your turn, throw one dart at a time, each dart score will tally to the total of all three darts thrown in that turn.  
# 4. But any dart that misses, bounces off or falls from the board, earns no score. If a dart sticks in another dart, it counts as a throw and gets no score.
from random import choice

dart_board = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,"B"]
multiplier = [1,2,3]
start_point = 501
player_trow = 0
player_current_score = start_point

pin_landed_value = choice(dart_board)
multiplier_value = choice(multiplier)
print(pin_landed_value)
print(multiplier_value)
player_current_score = player_current_score - pin_landed_value*multiplier_value
print(player_current_score)
return player_current_score
    
print(throw_pin())

