def player1_choice():
    checker = True
    while checker:
        chosen_symbol = input('Pick a symbol [ X / O ]: ').upper()
    
        if chosen_symbol == 'X' or chosen_symbol == 'O':
            checker = False
            return chosen_symbol
        else:
            chosen_symbol = input('Oops. Invalid input: ')

def cells_to_fill(cell_nums):
    
    print('[ '+ str(cell_nums[1])+ ' ]'+'[ '+ str(cell_nums[2])+ ' ]'+'[ '+ str(cell_nums[3])+ ' ]' + '\n'+'-'*15)
    print('[ '+ str(cell_nums[4])+ ' ]'+'[ '+ str(cell_nums[5])+ ' ]'+'[ '+ str(cell_nums[6])+ ' ]' + '\n'+'-'*15)
    print('[ '+ str(cell_nums[7])+ ' ]'+'[ '+ str(cell_nums[8])+ ' ]'+'[ '+ str(cell_nums[9])+ ' ]')

    print('Choose a num')
    # cells = '|[ ]|[ ]|[ ]|\n|[ ]|[ ]|[ ]|\n|[ ]|[ ]|[ ]|'
    # cells_list = cells.split('|')
    # print(''.join(cells_list))
    return cell_nums

def replace(cells_list,desired_symbol):
    checker = True
    cells_to_fill(cells_list)
    while checker:
        try:
            position = int(input(''))
            if position in range(1,10) and  cells_list[position] != 'X' and cells_list[position] != 'O' :
                cells_list[position] = desired_symbol
                checker = False
            else:
                print('Opps, the position is taken or then num is out of range')
            
                
        except: 
            print('Oops. Invalid input')
    
    