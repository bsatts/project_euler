# Find the largest prime factor of a number
import signal, sys, traceback
from math import sqrt

def handler(signum, frame):
	print "Exceeded 1 minute"
	raise Exception("out of time")

def largest_pf(num):
	"""
	Returns the largest prime factor of a number
	"""
	i = 2
	largest_div = 1
	max_factor = int(sqrt(num))
	while(num > i):
		if num % i == 0:
			num = num/i
			i = 2
			max_factor = int(sqrt(num))
		else:
			i += 1
	return i

signal.signal(signal.SIGALRM, handler)
signal.alarm(60)

try:
	num = 600851475143
	print largest_pf(num)
except:
	traceback.print_exc(file=sys.stdout)