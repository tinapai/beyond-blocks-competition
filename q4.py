def palindrome(x):
	num = str(x)
	if len(num)==2 and num[0] == num[1]:
		return True
	if len(num)<2:
		return True
	if num[0] == num[len(num)-1]:
		return palindrome(num[1:len(num)-2])
	else:
		return False
def largest(y):
	factor1 = 999
	factor2 = 999
	while factor1 > 1:
		if palindrome(factor1*factor2):
			return factor1*factor2
		if factor1 >= factor2:
			factor1 = factor1-1
		else:
			factor2 = factor2-1
print(largest(y))