# Find the smallest number evenly divisible by every number from 1 to 20
import math

# First find list of primes from 1 to 20
non_primes = set()
primes = []

for i in xrange(2, 20):
	if i in non_primes:
		continue

	for j in xrange(i*i, 20, i):
		non_primes.add(j)

	primes.append(i)

largest_multiple = []
for p in primes:
	max_exp = int(math.floor(math.log(20)/math.log(p)))
	largest_multiple.append(p**max_exp)

print reduce(lambda x,y: x*y, largest_multiple)