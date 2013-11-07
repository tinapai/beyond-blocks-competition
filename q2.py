def evenfib (n):
	fib = 1
	fib2 = 2
	total = 0
	while fib < n:
		if fib%2 == 0:
			total = total + fib
		if fib2%2 == 0:
			total = total + fib2
		fib = fib + fib2
		fib2 = fib2 + fib
	return total
print(evenfib(4000000))