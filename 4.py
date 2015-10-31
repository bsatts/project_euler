# Find the largest palindrome which is product of 2 3-digit numbers
# TODO - can improve by checking if either of the two products is factor of 11
import signal, sys, traceback

def handler(signum, frame):
	print "Exceeded 1 minute"
	raise Exception("out of time")

signal.signal(signal.SIGALRM, handler)
signal.alarm(60)


def check_palindrome(num):
	"""
	Checks if a number is a palindrome
	"""
	num_str = str(num)
	is_pal = True
	for i in range(0, len(num_str)/2):
		if num_str[i] != num_str[len(num_str) - 1 - i]:
			is_pal = False
			break 
	return is_pal

start = 999
max_pal = 0

for i in xrange(0, 898):
	for j in xrange(i, 898):
		prod = (start - i)*(start - j)
		if prod < max_pal:
			break
		if check_palindrome(prod):
			if max_pal < prod:
				max_pal = prod 
print max_pal

