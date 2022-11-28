def player1_choice():
    checker = True
    while checker:
        chosen_symbol = input('Pick a symbol [ X / O ]: ').upper()
    
        if chosen_symbol == 'X' or chosen_symbol == 'O':
            checker = False
            return chosen_symbol
        else:
            chosen_symbol = input('Oops. Invalid input: ')

def cells_to_fill():
    cells = '|[ ]|[ ]|[ ]|\n|[ ]|[ ]|[ ]|\n|[ ]|[ ]|[ ]|'
    cells_list = cells.split('|')
    print(''.join(cells_list))
    return cells_list

def replace(cells_list,desired_symbol):
    checker = True
    
    while checker:
        
        position = int(input('Choose a num \n|[1]|[2]|[3]|\n|[5]|[6]|[7]|\n|[9]|[10]|[11]|\n: '))
        if position in range(1,12) and position != 4 and position != 8 and cells_list[position] == '[ ]':
            cells_list[position] = f'[{desired_symbol}]'
            checker = False
        else:
            print('Oops. Invalid input')
    
    print(''.join(cells_list))