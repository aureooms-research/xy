import random

def comparator ( M ) :

	def compare ( i , j ) :

		return M[i-1][j-1]

	return compare

def mat ( m , n , v = None ) :

	return [ [ v ] * n for _ in range( m ) ]

def show ( matrix ) :

	width = max( len( str( item ) ) for row in matrix for item in row )

	for row in matrix :

		for item in row :

			print( ( "%" + str( width ) + "s" ) % str( item ) , end = " " )

		print( )

def linial ( compare , e , i , j ) :

	if e[i][j] is None :

		result = compare( i , j )

		if result > 0 :

			e[i][j] = linial( compare , e , i - 1 , j )

		elif result < 0 :

			e[i][j] = linial( compare , e , i , j - 1 )

		else :

			e[i][j] = linial( compare , e , i - 1 , j ) + linial( compare , e , i , j - 1 )


	return e[i][j]

def choose ( n , k ) :

	return random.sample( range( n ) , k )

def subscripts ( mi , mj , ni , nj ) :

	for i in range ( mi , mj ) :

		for j in range ( ni , nj ) :

			yield i , j

def main ( m , n ) :

	M = mat( m , n )

	# fill M
	# M[i][j] = -1 means ai < bj
	# M[i][j] =  1 means ai > bj
	# M[i][j] =  0 means ai and bj are incomparable

	positions = sorted( choose( m + n , m ) )

	for i , j in enumerate( positions ) :

		M[i][:j-i] = [ random.randint(  0 , 1 ) ] * ( j - i )
		M[i][j-i:] = [ random.randint( -1 , 0 ) ] * ( n - j + i )

	for i , j in subscripts ( 0 , m , 0 , n ) :

		if M[i][j] > 0 :

			for k , l in subscripts ( i , m , 0 , j + 1 ) :

				M[k][l] = M[i][j]

		elif M[i][j] < 0 :

			for k , l in subscripts ( 0 , i + 1 , j , n ) :

				M[k][l] = M[i][j]

	compare = comparator( M )

	e = mat( m + 1 , n + 1 )

	for i in range ( m + 1 ) : e[i][0] = 1
	for j in range ( n + 1 ) : e[0][j] = 1

	linial( compare , e , m , n )

	for i , j in subscripts ( 0 , m + 1 , 0 , n + 1 ) :

		if e[i][j] is None : e[i][j] = 0

	print( "partial information" )
	show( M )
	print( "count of linear extensions" )
	show( e )

	return e[m][n]

if __name__ == "__main__" :

	import sys

	print( main( *map( int , sys.argv[1:] ) ) )
