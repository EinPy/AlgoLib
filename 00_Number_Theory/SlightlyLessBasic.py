'''input
6
2
3
54
8
24
19
'''
from math import sqrt
"""
SLIGHTLY LESS BASIC

example: 
24 has the divisors [1,2,3,4,6,8,12,24]
Finding all the divisors
"""
def fun1(n):
	#Inefficient O(n)
	div1 = []
	for i in range(1, n+1):
		if n%i==0:
			div1.append(i)
	return div1

def fun2(n):
	#more efficient O(sqrt(n))
	div2 = set()
	for i in range(1, int(sqrt(n))+1): #range [1, root(n)]
		if n%i == 0:
			div2.add(i)
			div2.add(n//i)
	return div2

def runTestDivisors():
	t = int(input())
	while t:
		t -= 1

		n = int(input())
		div1 = fun1(n)
		div2 = fun2(n)
		# note that * is used to unpack things
		print(*div1)
		print(*div2)

#root(n) is an efficient program that will seldom 
#be a bottleneck for any program. 

"""
notes on print(*"name")
lets say we have arr = [1,2,3,4,6,8,12,24]
print(arr) yields: [1,2,3,4,6,8,12,24]
if we want it to look nice one can write
for i in arr:
	print(i, end =" ")
this gets us: 1 2 3 4 6 8 12 24
however the quickest way to unpack a list is with
print(*arr)
instantly yielding:1 2 3 4 6 8 12 24
"""

"""
PRIMALITY test
A prime number only has two factors
Two approaches, one O(n) and one O(root(n))
"""
def approach1(n):
# T.C O(n)
	divCnt = 0
	for i in range(1, n+1): #[1,n]
		if n%i == 0:
			divCnt +=1
	print(divCnt)
	if divCnt == 2:
		return True
	else:
		return False

def approach2(n):
	#T.C = O(root(n))
	if n == 0 or n == 1: #O(1)
		return False
	if n == 2 or n == 3: #O(1)
		return True
	if n%2 == 0 or n%3 == 0: #O(1)
		return False
	for i in range(5,int(sqrt(n))+1): # [1, root (n)]
		if n%i == 0 or n%(i+2) == 0:
			return False
	return True


t = int(input())
while t:
	n = int(input())
	print(approach1(n))
	print(approach2(n))

	t -= 1
