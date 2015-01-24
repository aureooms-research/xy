
import math

def main ( n ) :

	n = int( n )

	print( count( n ) )



def count ( n ) :

	c = math.factorial( n * n )

	for k in range( 1 , 2 * n ) :

		c //= k ** ( n - abs( n - k ) )

	return c


if __name__ == '__main__' :

	import sys

	main( *sys.argv[1:] )
