import sys
import time
from pprint import pprint
from random import randint

from battleship import battle
from battleship import hits
from battleship import creating_board
from battleship import boards

SIZE = 5
    
def main():
    ships = [5, 4]
    all_in_one = {}
    
    for i in range(1, 3):
        if i == 1:
            print "Player %r create board for your enemy." %(i+1)
        else:
            print "Player %r create board for your enemy." %(i-1)
        
        d = {}
        a, b = creating_board.creating_board_for_enemy(ships)
        c = boards.creating_empty_board(SIZE)
        d['real_board'] = a
        d['ship_coordinates'] = b
        d['hit_board'] = c
        all_in_one[i] = d
    
    #pprint(all_in_one)
    # a = real_board, b = ship_coordinates, c = hit_board
    print "Welcome to the battleship. You have five ships to sink."
    battle.battle(all_in_one, SIZE)
    print "Well done. All ships have been sank."

    
if __name__ == '__main__':
    main()