from player_choice import *

def tic_tac_toe():
    game_cells = '|[ ]|[ ]|[ ]|\n|[ ]|[ ]|[ ]|\n|[ ]|[ ]|[ ]|'
    celll = cells_to_fill()
    symbol1 = player1_choice()
    symbol2 = ''
    if symbol1 == 'X':
        symbol2 = 'O'
    else:
        symbol2 = 'X'
    player_switch = 1
    checker = True
    counter = 0
    while checker:
    
        if player_switch == 1:
            
            replace(celll,symbol1)
            counter +=1
            player_switch += 1
        elif player_switch == 2:
            
            replace(celll,symbol2)
            counter +=1
            player_switch -=1
        
        if celll[1] == celll[2] and celll [2] == celll[3] and (celll[1] == '[X]' or celll[1] == '[O]'):
            print(f'{celll[1]} is a winner')
            checker = False
        
        elif celll[5] == celll[6] and celll [6] == celll[7] and (celll[5] == '[X]' or celll[5] == '[O]'):
            print(f'{celll[5]} is a winner')
            checker = False
        
        elif celll[9] == celll[10] and celll [10] == celll[11] and (celll[9] == '[X]' or celll[9] == '[O]'):
            print(f'{celll[9]} is a winner')
            checker = False
    
        elif celll[1] == celll[5] and celll [5] == celll[9] and (celll[1] == '[X]' or celll[1] == '[O]'):
            print(f'{celll[1]} is a winner')
            checker = False
        
        elif celll[2] == celll[6] and celll [6] == celll[10] and (celll[2] == '[X]' or celll[2] == '[O]'):
            print(f'{celll[2]} is a winner')
            checker = False
    
        elif celll[3] == celll[7] and celll [7] == celll[11] and (celll[3] == '[X]' or celll[3] == '[O]'):
            print(f'{celll[5]} is a winner')
            checker = False
        
        elif celll[1] == celll[6] and celll [6] == celll[11] and (celll[1] == '[X]' or celll[1] == '[O]'):
            print(f'{celll[11]} is a winner')
            checker = False
    
        elif celll[3] == celll[6] and celll [6] == celll[9] and (celll[3] == '[X]' or celll[3] == '[O]'):
            print(f'{celll[3]} is a winner')
            checker = False
    
        if counter == 9:
            print("It's a tie!")
            checker = False
    return 'done'