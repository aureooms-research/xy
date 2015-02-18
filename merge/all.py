import math

def count ( n , k ) :

	return ( n**2 ) * ( 2**k - 1 ) / ( 2**k )

def all ( n , i , j ) :

	return sum( count( n , k ) for k in range( i , j ) )

def main ( n ) :

	M = int( math.log( n , 2 ) )
	N = 2 * M

	a = all( n , 1 , M + 1 )
	b = all( n , M + 1 , N + 1 )
	c = a + b

	f = 2 * ( n**2 ) * math.log( n , 2 )
	g = 1 - n**2 + n**2 * math.log( n**2 , 2 )

	print( "%d - %d = %d" % ( c , g , c - g ) )
	print( "%d - %d = %d" % ( f , c , f - c ) )
	print( "%d - %d = %d" % ( b , a , b - a ) )

if __name__ == "__main__" :

	import sys

	main( *map( int , sys.argv[1:] ) )
