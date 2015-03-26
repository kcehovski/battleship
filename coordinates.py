SIZE = 5

def input_coordinates(): 
    while True:
        coordinates = raw_input('Please insert first coordinate:')
        direction = raw_input('Insert direction of the ship. Right or down?')
        try:
            return split_coordinates(coordinates, direction)
        except ValueError as e:
            print 'invalid input: %s' % str(e)


def split_coordinates(coord, direc):
    coord_z = direc.lower()
    coord_y = coord[0].lower()
    if len(coord) != 2:
		raise ValueError('Coordinate must be of length 2')
    
    if not coord_y.isalpha():
		raise ValueError('Coordinate-x must be alphabetic')
    
    if ord(coord_y.lower()) - ord('a') >= SIZE:
		raise ValueError('Coordinate-x must be inside limits')
    
    try:
		coord_x = int(coord[1])
    except ValueError:
		raise ValueError('Coordinate-y must be a digit v2')
    
    if coord_x > SIZE or coord_x <= 0:
		raise ValueError('Coordinate-y must be inside limits')
    
    if not (coord_z == 'right' or coord_z == 'down'): 
        raise ValueError('Direction must be right or down')
    
    coord_x, coord_y, coord_z = translating_coordinates(SIZE, coord_x, coord_y, coord_z)    
    return coord_x, coord_y, coord_z


def translating_coordinates(n, hit_x, hit_y, hit_z):
    x = n - hit_x
    y = ord(hit_y)- ord('a') 
    if hit_z == 'right':
        z = 0
    else:
        z = 1
    return (x, y, z)