from matrix import mat , show , subscripts
from information import partial , comparator


def grid ( m , n ) :

	e = mat( m + 1 , n + 1 )

	for i in range ( m + 1 ) : e[i][0] = 1
	for j in range ( n + 1 ) : e[0][j] = 1

	return e

def linial ( compare , e , i , j ) :

	"""

		>>> compare = comparator( [ [ 0 , 0 ] , [ 0 , 0 ] ] )
		>>> e = grid( 2 , 2 )
		>>> linial( compare , e , 2 , 2 )
		6

		>>> compare = comparator( [ [ 1 , 0 ] , [ 1 , 0 ] ] )
		>>> e = grid( 2 , 2 )
		>>> linial( compare , e , 2 , 2 )
		3

		>>> compare = comparator( [ [ -1 , -1 ] , [ -1 , -1 ] ] )
		>>> e = grid( 2 , 2 )
		>>> linial( compare , e , 2 , 2 )
		1

		>>> compare = comparator( [ [ -1 , -1 ] , [ 0 , 0 ] ] )
		>>> e = grid( 2 , 2 )
		>>> linial( compare , e , 2 , 2 )
		3

		>>> compare = comparator( [ [ 1 , 1 ] , [ 1 , 1 ] ] )
		>>> e = grid( 2 , 2 )
		>>> linial( compare , e , 2 , 2 )
		1

		>>> compare = comparator( [ [ 0 , -1 ] , [ 1 , 0 ] ] )
		>>> e = grid( 2 , 2 )
		>>> linial( compare , e , 2 , 2 )
		4

		>>> compare = comparator( [ [ 0 , -1 ] , [ 1 , 1 ] ] )
		>>> e = grid( 2 , 2 )
		>>> linial( compare , e , 2 , 2 )
		2

		>>> compare = comparator( [ [ -1 , -1 ] , [ 1 , 0 ] ] )
		>>> e = grid( 2 , 2 )
		>>> linial( compare , e , 2 , 2 )
		2

	"""

	if e[i][j] is None :

		result = compare( i - 1 , j - 1 )

		if result > 0 :

			e[i][j] = linial( compare , e , i - 1 , j )

		elif result < 0 :

			e[i][j] = linial( compare , e , i , j - 1 )

		else :

			e[i][j] = linial( compare , e , i - 1 , j ) + linial( compare , e , i , j - 1 )


	return e[i][j]


def main ( m , n ) :

	M = partial( m , n )

	compare = comparator( M )

	e = grid( m , n )

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
