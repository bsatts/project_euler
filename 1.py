#Find the sum of all the multiples of 3 or 5 below 999
n3 = 999/3
l3 = n3 * 3
n5 = (999-1)/5
l5 = n5 * 5
n15 = 999/15
l15 = (999/15) * 15

def am_sum(first, last, n):
	return n * (first + last)/2

answer = am_sum(3, l3, n3) + am_sum(5, l5, n5) - am_sum(15, l15, n15)
print answer