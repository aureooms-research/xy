from random import randint , sample
from functools import reduce
from operator import mul

def gcd ( a , b ) :

	"""

		>>> gcd( 2 * 3 * 5 * 7 * 13 , 2 * 2 * 2 * 5 * 7 * 11 * 13 * 17 )
		910

	"""

	while True :

		if a == 0 : return b

		b %= a

		if b == 0 : return a

		a %= b

def prod ( iterable ) :

	"""

		>>> prod( [ 4 , 7 , 2 , -9 ] )
		-504

	"""

	p = 1

	for item in iterable : p *= item

	return p


def det ( A , n ) :

	"""

		Using Gaussian elimination and gcd. For integers only!

		>>> det( [ [ 4 , 1 ] , [ 1 , 2 ] ] , 2 )
		7

		>>> det( [ [ -2 , 2 , -3 ] , [ -1 , 1 , 3 ] , [ 2 , 0 , -1 ] ] , 3 )
		18

		>>> det( [ [ -1 , 1 , 3 ] , [ -2 , 2 , -3 ] , [ 2 , 0 , -1 ] ] , 3 )
		-18

	"""

	d = 1

	for i in range ( n - 1 ) :

		# find first non zero row

		if A[i][i] == 0 :

			j = i + 1

			while j < n :

				if A[j][i] != 0 : break

				j += 1

			if j == n : return 0

			# make it the ith row

			A[i] , A[j] = A[j] , A[i]

			d = -d

		for j in range ( i + 1 , n ) :

			a = A[i][i]
			b = A[j][i]

			c = gcd( a , b )

			a //= c
			b //= c

			# we want to cancel A[j][i]

			# assert  a * A[j][i] == b * A[i][i]

			A[j][i] = 0

			# so we multiply both rows so that
			#
			#     A[i][i] = A[j][i] = lcm( A[i][i] , A[j][i] )
			#
			# and we remove the ith row from the jth row

			for k in range ( i + 1 , n ) :

				A[j][k] = a * A[j][k] - b * A[i][k]

			d *= a

	return prod( A[i][i] for i in range( n ) ) // d


def comparator ( M ) :

	"""

		>>> M = mat( 3 , 2 )
		>>> compare = comparator( M )
		>>> for i , j in subscripts( 0 , 3 , 0 , 2 ) : M[i][j] = 2 * i + j
		>>> compare( 0 , 0 ) == M[0][0]
		True
		>>> compare( 0 , 1 ) == M[0][1]
		True
		>>> compare( 1 , 0 ) == M[1][0]
		True
		>>> compare( 1 , 1 ) == M[1][1]
		True
		>>> compare( 2 , 0 ) == M[2][0]
		True
		>>> compare( 2 , 1 ) == M[2][1]
		True

	"""

	def compare ( i , j ) :

		return M[i][j]

	return compare

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


def mohanty ( compare , Mo , m , n ) :

	for i , j in subscripts( 0 , m , 0 , m ) :

		b = reduce( min , ( t for t in range( n ) if compare( i , t ) < 0 ) , n  )
		a = reduce( max , ( t for t in range( n ) if compare( j , t ) > 0 ) , 0  )

		Mo[i][j] = C( b - a + 1 , j - i + 1 )


def C ( n , k ) :

	"""

		>>> C( 4 , 2 )
		6

		>>> C( 0 , 0 )
		1

		>>> C( -1 , 0 )
		0

	"""

	if n < 0 or k < 0 : return 0

	k = min( k , n - k )

	if k == 0 : return 1
	if k  < 0 : return 0

	numer = reduce( mul , range( n , n - k , -1 ) )
	denom = reduce( mul , range( 1 , k + 1 ) )

	return numer // denom

def choose ( n , k ) :

	"""

		>>> A = choose( 10 , 3 )
		>>> len( A )
		3

		>>> sorted( choose( 10 , 10 ) )
		[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

	"""

	return sample( range( n ) , k )

def subscripts ( mi , mj , ni , nj ) :

	"""

		>>> list( subscripts( 1 , 3 , 2 , 5 ) )
		[(1, 2), (1, 3), (1, 4), (2, 2), (2, 3), (2, 4)]

	"""

	for i in range ( mi , mj ) :

		for j in range ( ni , nj ) :

			yield i , j

def information ( m , n ) :

	M = mat( m , n )

	# fill M
	# M[i][j] = -1 means ai < bj
	# M[i][j] =  1 means ai > bj
	# M[i][j] =  0 means ai and bj are incomparable

	positions = sorted( choose( m + n , m ) )

	for i , j in enumerate( positions ) :

		M[i][:j-i] = [ randint(  0 , 1 ) ] * ( j - i )
		M[i][j-i:] = [ randint( -1 , 0 ) ] * ( n - j + i )

	for i , j in subscripts ( 0 , m , 0 , n ) :

		if M[i][j] > 0 :

			for k , l in subscripts ( i , m , 0 , j + 1 ) :

				M[k][l] = M[i][j]

		elif M[i][j] < 0 :

			for k , l in subscripts ( 0 , i + 1 , j , n ) :

				M[k][l] = M[i][j]

	return M


def main ( m , n ) :

	m , n = max( m , n ) , min( m , n )

	M = information( m , n )

	compare = comparator( M )

	Mo = mat( m , m )

	mohanty( compare , Mo , m , n )

	print( "partial information" )
	show( M )
	print( "mohanty matrix" )
	show( Mo )

	d = det( Mo , m )

	print( "after gaussian elimination" )
	show( Mo )

	return d


if __name__ == "__main__" :

	import sys

	print( main( *map( int , sys.argv[1:] ) ) )
