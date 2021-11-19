'''input
1
50
'''
"""
SEIVE of Eratosthenes THEOREM
Genererat all prime numbers up to N with TC O(n*log(log(n)))

#basic:
for each in number from 1 to N: # T.C O(N)
	traverse and check if number is prime ----> in O(root(N))
		print if number is prime # T.C O(1) constant

total T.C = O(N*root(N)) 

A better approach is to as you go mark number you know are not primes.
i.e. After visiting a prime p, you know that all numbers that are
>= p^2 and divisible by p are not prime
"""

from math import sqrt

def generate_primes(n):
	primes = [True]*(n+1)
	primes[0], primes[1] = False, False
	for p in range(2, int(sqrt(n)) + 1):
		if primes[p]:
			for i in range(p*p, n+1, p):
				primes[i] = False

	out = []
	for i, n in enumerate(primes):
			if n:
				out.append(i)
	return out


t = int(input())
while t:
	n = int(input())
	print(generate_primes(n))
	t -= 1
