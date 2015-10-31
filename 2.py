# Find the sum of all even fibonacci numbers less than 4 million

f = [1, 1]

f_sum = 0

i = 3 # We're looking for the 3rd fib onwards 
while (f[1] < 4000000):
	f_n = f[0] + f[1]
	f[0], f[1] = f[1], f_n
	if ((i-3) % 3 == 0):
		f_sum += f_n
	i += 1
print f_sum
