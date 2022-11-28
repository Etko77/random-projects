from game import *

def play_replay_quit():
    game = tic_tac_toe()
    while game == 'done':
        play_again = input('Wanna play again? [Y/N]: ').upper()
        if play_again == 'Y':
            play_replay_quit()
        elif play_again == 'N':
            print('Thanks for playing')
            game = 'finito'
        else:
            print('Invalid input')

play_replay_quit()