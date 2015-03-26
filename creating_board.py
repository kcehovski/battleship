from pprint import pprint

from battleship import coordinates
from battleship import boards

SIZE = 5
MAX_USER_ATTEMPTS = 100


def check_input_coordinates(ship, current_board):
    count = 0
    print "This is the ship of %r places." %ship
    coord_x, coord_y, coord_z = coordinates.input_coordinates()
    while True:
        if not(boards.is_valid(coord_x, coord_y, coord_z, ship, current_board)):
            print 'Invalid input.'
            print "This is the ship of %r places." %ship
            coord_x, coord_y, coord_z = coordinates.input_coordinates()
            count += 1
            if count > MAX_USER_ATTEMPTS:
                print "Error: Unable to create a board."
                sys.exit(1)
            
        else:
            return coord_x, coord_y, coord_z
    

def creating_board_for_enemy(ships):
    d = []
    a = boards.creating_empty_board(SIZE)
    pprint(a)
    for i in ships:        
        coord_x, coord_y, coord_z = check_input_coordinates(i, a)
        a, c = boards.put_ship_in_place(a, coord_x, coord_y, coord_z, i)
        d.append(c)
        print 'Ship added.'
        pprint(a)        
    return a, d
    
