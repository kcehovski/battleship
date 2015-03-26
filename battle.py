
def count_ships_lenght(real_board):
    a = 0
    for x in real_board:
        for y in x:
            if y == 'X':
                a +=1
    return a


def count_hits(hit_board):
    a = 0
    for x in hit_board:
        for y in x:
            if y == 'X':
                a += 1
    return a


def checking_and_filing(real_board, hit_board, hit_x, hit_y, board_length):
    x, y = hits.translating_hits(board_length, hit_x, hit_y)
    if real_board[x][y] == '-':
        hit_board[x][y] = '0'
    else:
        hit_board[x][y] = 'X'


def is_all_ship_coordinates_hit(hit_board, one_ship):  
    for i in one_ship:
        x = i[0]
        y = i[1]
        if hit_board[x][y] != 'X':
            return False
    return True


def count_ship_sank(hit_board, ship_coordinates):
    sank_ships = 0
    for i in ship_coordinates:
        if is_all_ship_coordinates_hit(hit_board, i):
            sank_ships += 1
    return sank_ships


def is_everything_hit(all):
    for v in all.values():
        if count_hits(v['hit_board']) == count_ships_lenght(v['real_board']):
            return True
    return False


def battle(all, board_length):
    while not is_everything_hit(all):      
        for key, value in all.items():
            print "Player %r: " %key
            pprint(value['hit_board'])
            hit_x, hit_y = hits.input_hit()
            checking_and_filing(value['real_board'], value['hit_board'], hit_x, hit_y, board_length)
            pprint(value['hit_board'])
            sank_ships = count_ship_sank(value['hit_board'], value['ship_coordinates'])
            print "%r from 5 have been sank" % sank_ships
            time.sleep(3)