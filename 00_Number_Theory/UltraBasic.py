#SUM OF NATURAL NUMBER
'''
Sum of natural numbers up to n where t is testcases 
and n is numbers.
'''

# time complexity O(1)
t = int(input)
while t:
	t -= 1
	n = int(input())
	return (n * (n+1)) // 2


'''
This way is a lot more efficient that adding all the number
together in lets say a for loop with efficiency O(n)
'''

# GCD (greatest common divisor) and LCM (lowest ommon multiple)
# O(log(min(a,b)))
#product = lcm * gcd

def gcd(a, b):
	if a == 0:
		return b
	return gcd(b%a, a)

def lcm(a, b):
	product = a*b
	#highest common factor == greatest common divisor
	hcf = gcd(a, b)
	return product // hcf

t = int(input())
while t:
	t -= 1
	n, j = list(map(int,input().split()))
	print(f'gcd = {gcd(n)} and lcm = {lcm(n)}')
