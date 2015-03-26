SIZE = 5

def input_hit(): 
    while True:
		hit = raw_input('please insert hit:')
		try:
			return split_hit(hit)
		except ValueError as e:
			print 'invalid input: %s' % str(e)


def split_hit(hit):
	if len(hit) != 2:
		raise ValueError('Hit must be of length 2')

	hit_y = hit[0]
	if not hit_y.isalpha():
		raise ValueError('Hit-x must be alphabetic')

	if ord(hit_y.lower()) - ord('a') >= SIZE:
		raise ValueError('Hit-x must be inside limits')

	try:
		hit_x = int(hit[1])
	except ValueError:
		raise ValueError('Hit-y must be a digit v2')

	if hit_x > SIZE or hit_x <= 0:
		raise ValueError('Hit-y must be inside limits')

	return hit_x, hit_y  


def translating_hits(n, hit_x, hit_y):
    x = n - hit_x
    y = ord(hit_y)- ord('a')  
    return (x, y)