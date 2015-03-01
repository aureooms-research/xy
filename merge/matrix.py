
def mat ( m , n , v = None ) :

	"""

		>>> mat( 0 , 3 , 1 )
		[]

		>>> mat( 5 , 0 , 1 )
		[[], [], [], [], []]

		>>> M = mat( 5 , 3 , 1 )
		>>> M
		[[1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1]]

		>>> M[1][2] = 2
		>>> M
		[[1, 1, 1], [1, 1, 2], [1, 1, 1], [1, 1, 1], [1, 1, 1]]

	"""

	return [ [ v ] * n for _ in range( m ) ]

def show ( matrix ) :

	"""

		>>> show( mat( 5 , 3 , 1 ) )
		1 1 1
		1 1 1
		1 1 1
		1 1 1
		1 1 1

		>>> M = mat( 2 , 3 , 12 )
		>>> M[0][1] = M[1][2] = 1
		>>> show( M )
		12  1 12
		12 12  1

	"""

	width = max( len( str( item ) ) for row in matrix for item in row )

	for row in matrix :

		fmt = " ".join( [ "%" + str( width ) + "s" ] * len( row ) )

		print( fmt % tuple( row ) )


def subscripts ( mi , mj , ni , nj ) :

	"""

		>>> list( subscripts( 1 , 3 , 2 , 5 ) )
		[(1, 2), (1, 3), (1, 4), (2, 2), (2, 3), (2, 4)]

	"""

	for i in range ( mi , mj ) :

		for j in range ( ni , nj ) :

			yield i , j

