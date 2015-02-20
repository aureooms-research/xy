import math , functools

def mergesort ( whole , half ) :

	count = 0

	left = 0
	center = half * 2
	right = 0

	while half < whole :

		if left == 0 :
			j = whole
			i = left = j % center

		else :
			if right == 0 :
				count += left + half - 1
				left += half
				i = left
				right = ( whole - left ) % center
				j = whole - right

			else :
				count += left + right - 1
				i = left
				left += right
				j = whole - right
				right = ( whole - left ) % center
				j -= right


		k = i
		while k < j :
			count += center - 1
			k += center

		half <<= 1
		center <<= 1


	return count

def iterative ( n ) :

	return mergesort( n , 1 )

@functools.lru_cache ( maxsize = None )
def recursive ( n ) :

	return 0 if n < 2 else n - 1 + recursive(n//2) + recursive((n+1)//2)

def summation ( n ) :

	return sum( math.ceil(math.log(i,2)) for i in range(1,n+1) )

def nlogn ( n ) :

	return 0 if n < 2 else n * math.log( n , 2 )

def lognf0 ( n ) :

	return math.log(math.sqrt(2*math.pi*n),2) + n * math.log( n / math.e , 2 )

def lognf1 ( n ) :

	return sum( math.log(i,2) for i in range(1,n+1) )

def lognf2 ( n ) :

	return math.log(math.factorial(n),2)


def main ( begin , end  , step ) :

	for n in range( begin , end + 1 , step ) :

		print( n , mergesort( n ** 2 , n ) / lognf0( n ** 2 ) )

if __name__ == "__main__" :

	import sys

	main( *map( int , sys.argv[1:] ) )
