

def main ( n ) :

	n = int( n )

	print( count( n ) )



def count ( n ) :

	grid = gengrid( n )

	return recurse( () , set( [ ( 0 , 0 ) ] ) , set( ) , grid , n )

def gengrid ( n ) :

	grid = []

	for i in range( n ) : grid.append( [None] * n )

	for i in range( n ) :
		for j in range( n ) :

			grid[i][j] = i * j + i + j

	return grid

def successors ( x , y , n ) :

	for i in range( x , n ) :

		for j in range( y , n ) :

			if i == x and j == y : continue

			yield ( i , j )


def decrement ( grid , x , y , n ) :

	for i , j in successors( x , y , n ) : grid[i][j] -= 1

def increment ( grid , x , y , n ) :

	for i , j in successors( x , y , n ) : grid[i][j] += 1

def recurse( prefix , positions , states , grid , n ) :

	if prefix in states : return 0

	if not positions : return 1

	states.add( prefix )

	total = 0

	for x , y in positions :

		decrement( grid , x , y , n )

		newpositions = positions.copy( )

		newpositions.remove( ( x , y ) )

		if x + 1 < n and grid[x+1][y] == 0 : newpositions.add( ( x + 1 , y ) )

		if y + 1 < n and grid[x][y+1] == 0 : newpositions.add( ( x , y + 1 ) )

		newprefix = prefix + ( ( x , y ) , )

		total += recurse( newprefix , newpositions , states , grid , n )

		increment( grid , x , y , n )

	return total


def view ( grid , n ) :

	width = str( len( str( n * n - 1 ) ) + 1 )

	fmt = ( '{:' + width + '}' ) * n

	for line in grid :

		print( fmt.format( *line ) )


if __name__ == '__main__' :

	import sys

	main( *sys.argv[1:] )
