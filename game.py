from player_choice import *
import os

def clear():
    os.system('cls')

def tic_tac_toe():
    lst = [0,1,2,3,4,5,6,7,8,9]
    celll = cells_to_fill(lst)
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
        
        clear()

        if player_switch == 1:
            
            replace(celll,symbol1)
            counter +=1
            player_switch += 1
        elif player_switch == 2:
            
            replace(celll,symbol2)
            counter +=1
            player_switch -=1
        
        if celll[1] == celll[2] and celll [2] == celll[3] and (celll[1] == 'X' or celll[1] == 'O'):
            print(f'{celll[1]} is a winner')
            checker = False
        
        elif celll[4] == celll[5] and celll [6] == celll[5] and (celll[5] == 'X' or celll[5] == 'O'):
            print(f'{celll[5]} is a winner')
            checker = False
        
        elif celll[7] == celll[8] and celll [8] == celll[9] and (celll[9] == 'X' or celll[9] == 'O'):
            print(f'{celll[9]} is a winner')
            checker = False
    
        elif celll[1] == celll[4] and celll [4] == celll[7] and (celll[1] == 'X' or celll[1] == 'O'):
            print(f'{celll[1]} is a winner')
            checker = False
        
        elif celll[2] == celll[5] and celll [5] == celll[8] and (celll[2] == 'X' or celll[2] == 'O'):
            print(f'{celll[2]} is a winner')
            checker = False
    
        elif celll[3] == celll[6] and celll [6] == celll[9] and (celll[3] == 'X' or celll[3] == 'O'):
            print(f'{celll[6]} is a winner')
            checker = False
        
        elif celll[1] == celll[5] and celll [5] == celll[9] and (celll[1] == 'X' or celll[1] == 'O'):
            print(f'{celll[5]} is a winner')
            checker = False
    
        elif celll[3] == celll[5] and celll [5] == celll[7] and (celll[3] == 'X' or celll[3] == 'O'):
            print(f'{celll[5]} is a winner')
            checker = False
    
        if counter == 9:
            print("It's a tie!")
            checker = False
    return 'done'