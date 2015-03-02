from functools import reduce
from determinant import det
from matrix import mat , show , subscripts
from combinatorics import C
from information import partial , comparator


def mohanty ( compare , Mo , m , n ) :

	"""

		>>> compare = comparator( [ ] )
		>>> Mo = mat( 0 , 0 )
		>>> mohanty( compare , Mo , 0 , 0 )
		>>> abs( det( Mo , 0 ) )
		1

		>>> compare = comparator( [ [ ] , [ ] , [ ] ] )
		>>> Mo = mat( 3 , 3 )
		>>> mohanty( compare , Mo , 3 , 0 )
		>>> abs( det( Mo , 3 ) )
		1

		>>> compare = comparator( [ [ -1 ] ] )
		>>> Mo = mat( 1 , 1 )
		>>> mohanty( compare , Mo , 1 , 1 )
		>>> abs( det( Mo , 1 ) )
		1

		>>> compare = comparator( [ [ 1 ] ] )
		>>> Mo = mat( 1 , 1 )
		>>> mohanty( compare , Mo , 1 , 1 )
		>>> abs( det( Mo , 1 ) )
		1

		>>> compare = comparator( [ [ 0 ] ] )
		>>> Mo = mat( 1 , 1 )
		>>> mohanty( compare , Mo , 1 , 1 )
		>>> abs( det( Mo , 1 ) )
		2

		>>> compare = comparator( [ [ 0 , 0 ] , [ 0 , 0 ] ] )
		>>> Mo = mat( 2 , 2 )
		>>> mohanty( compare , Mo , 2 , 2 )
		>>> abs( det( Mo , 2 ) )
		6

		>>> compare = comparator( [ [ 0 , 0 ] , [ 0 , 0 ] ] )
		>>> Mo = mat( 2 , 2 )
		>>> mohanty( compare , Mo , 2 , 2 )
		>>> abs( det( Mo , 2 ) )
		6

		>>> compare = comparator( [ [ 1 , 0 ] , [ 1 , 0 ] ] )
		>>> Mo = mat( 2 , 2 )
		>>> mohanty( compare , Mo , 2 , 2 )
		>>> abs( det( Mo , 2 ) )
		3

		>>> compare = comparator( [ [ -1 , -1 ] , [ -1 , -1 ] ] )
		>>> Mo = mat( 2 , 2 )
		>>> mohanty( compare , Mo , 2 , 2 )
		>>> abs( det( Mo , 2 ) )
		1

		>>> compare = comparator( [ [ -1 , -1 ] , [ 0 , 0 ] ] )
		>>> Mo = mat( 2 , 2 )
		>>> mohanty( compare , Mo , 2 , 2 )
		>>> abs( det( Mo , 2 ) )
		3

		>>> compare = comparator( [ [ 1 , 1 ] , [ 1 , 1 ] ] )
		>>> Mo = mat( 2 , 2 )
		>>> mohanty( compare , Mo , 2 , 2 )
		>>> abs( det( Mo , 2 ) )
		1

		>>> compare = comparator( [ [ 0 , -1 ] , [ 1 , 0 ] ] )
		>>> Mo = mat( 2 , 2 )
		>>> mohanty( compare , Mo , 2 , 2 )
		>>> abs( det( Mo , 2 ) )
		4

		>>> compare = comparator( [ [ 0 , -1 ] , [ 1 , 1 ] ] )
		>>> Mo = mat( 2 , 2 )
		>>> mohanty( compare , Mo , 2 , 2 )
		>>> abs( det( Mo , 2 ) )
		2

		>>> compare = comparator( [ [ -1 , -1 ] , [ 1 , 0 ] ] )
		>>> Mo = mat( 2 , 2 )
		>>> mohanty( compare , Mo , 2 , 2 )
		>>> abs( det( Mo , 2 ) )
		2

	"""

	for i , j in subscripts( 0 , m , 0 , m ) :

		b = reduce( min , ( t + 1 for t in range( n ) if compare( i , t ) < 0 ) , n + 1 )
		a = reduce( max , ( t + 1 for t in range( n ) if compare( j , t ) > 0 ) , 0 )

		Mo[i][j] = C( b - a , j - i + 1 )


def main ( m , n ) :

	m , n = max( m , n ) , min( m , n )

	M = partial( m , n )

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
