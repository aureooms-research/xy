
from matrix import mat , subscripts
from combinatorics import choose
from random import randint

def partial ( m , n ) :

	M = mat( m , n )

	# fill M
	# we assume that for all j > i --> ai < aj and bi < bj
	# M[i][j] = -1 means ai < bj
	# M[i][j] =  1 means ai > bj
	# M[i][j] =  0 means ai and bj are incomparable

	# generate random info

	positions = sorted( choose( m + n , m ) )

	for i , j in enumerate( positions ) :

		M[i][:j-i] = [ randint(  0 , 1 ) ] * ( j - i )
		M[i][j-i:] = [ randint( -1 , 0 ) ] * ( n - j + i )

	# fix transitivity

	for i , j in subscripts ( 0 , m , 0 , n ) :

		if M[i][j] > 0 :

			for k , l in subscripts ( i , m , 0 , j + 1 ) :

				M[k][l] = M[i][j]

		elif M[i][j] < 0 :

			for k , l in subscripts ( 0 , i + 1 , j , n ) :

				M[k][l] = M[i][j]

	return M


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

