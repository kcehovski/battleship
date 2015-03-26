from random import randint

SIZE = 5
RANDOM_MAX_ATTEMPTS = 1000

def creating_empty_board(n):
    a = []
    for x in range(0, n):
        b = []
        for y in range(0, n):
            b.append('-')
        a.append(b)    
    return a  


def check_board_limits(x, y, z, ship):
    if z == 0:
        return y+ship-1 <= SIZE-1
    else:
        return x+ ship - 1 <= SIZE-1


def check_overlap(x, y, z, ship, current_board):
    if z == 0:
        for i in range(0, ship):
            if current_board[x][y + i] == 'X': 
                return False
    else: 
        for i in range(0, ship):
            if current_board[x+i][y]== 'X':
                return False
    return True    


def is_valid(x,y,z, ship, current_board):
    return check_board_limits(x,y,z, ship) and check_overlap(x,y,z,ship, current_board)


def put_ship_in_place(b,x,y,z, ship):
    c = []
    if z == 0:
        j = ship
        for v in range(0, j):
            b[x][y + v] = 'X'
            c.append([x, y+v])
        return b, c
    else:
        j = ship
        for v in range(0, j):
            b[x+ v][y] = 'X'
            c.append([x+v, y])
        return b, c


def creating_board(ships):
    d = []
    a = creating_empty_board(SIZE)
    for i in ships:
        x = randint(0, SIZE-1)
        y = randint(0, SIZE-1)
        z = randint(0, 1)
        count = 0
        while not(is_valid(x,y,z, i, a)):
            x = randint(0, SIZE-1)
            y = randint(0, SIZE-1)
            z = randint(0, 1)
            count += 10 
            if count > MAX_ATTEMPTS:
                print "Error: Unable to create a board."
                sys.exit(1)
        a, c = put_ship_in_place(a,x,y,z, i)
        d.append(c)
    return a, d

