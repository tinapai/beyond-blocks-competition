def sumofmultiples(n):
	total = 0
	i = n-1
	while i >= 0:
		if i%3 == 0 or i%5 == 0:
			total = total+i
		i = i-1
	return total
print(sumofmultiples(1000))