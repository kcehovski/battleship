import sys
import time
from pprint import pprint
from random import randint

from battleship import battle
from battleship import boards
from battleship import hits

SIZE = 5

def read_board_from_file(name):
    a = open(name).readlines()
    board = []
    for x in a:
        x = x.strip().split()
        board.append(x)
    return board   

def main_simple():
    if len(sys.argv) != 2: 
        print "Usage: python battleship.py [input_file]"
        sys.exit(1)
        
    script, filename = sys.argv   
    board = read_board_from_file(filename)   
    board_length = len(board)
    n_s = count_ship_lenght(board) 
    empty_board = boards.creating_empty_board(board_length)
       
    battle(board, empty_board, board_length)

    
def main():
    if len(sys.argv)!=2:
        print "Usage: python battleship.py number of players"
        sys.exit(1)
    if 1> int(sys.argv[1]) or int(sys.argv[1]) > 5:
        print "Game can play 1 to 5 players."
        sys.exit(1)
        
    script, n = sys.argv
    number_of_players = int(n)
    
    ships = [5, 4, 3, 3, 2]
    all_in_one = {}
    
    print "Welcome to the battleship. You have five ships to sink."
    for i in range(1, number_of_players +1):
        d = {}
        a, b = boards.creating_board(ships)
        c = boards.creating_empty_board(SIZE)
        d['real_board'] = a
        d['ship_coordinates'] = b
        d['hit_board'] = c
        all_in_one[i] = d
    
    # a = real_board, b = ship_coordinates, c = hit_board
    
    battle.battle(all_in_one, SIZE)
    print "Well done. All ships have been sank."

    
if __name__ == '__main__':
    main()