#Sum square difference

import math

def sum_square_diff(n):
	sum_squares = n * (n+1)*(2* n + 1)/6
	sum_till_n = n*(n+1)/2
	diff = math.pow(sum_till_n, 2) - sum_squares
	return int(diff) 


print sum_square_diff(100)