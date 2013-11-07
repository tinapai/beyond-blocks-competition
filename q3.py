def prime(n):
	i = round(n**.5)
	while i > 1:
		if n%i==0:
			return False
		i = i - 1
	return True
def largest_prime_factor(x):
	factor = x
	denom = 2
	if prime(x):
		return x
	while factor > 2:
		if x%denom == 0:
			factor = x/denom
			if prime(factor):
				return factor
		denom = denom + 1
print(largest_prime_factor(600851475143))