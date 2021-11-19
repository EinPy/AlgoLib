Sum of natural numbers up to n where t is testcases 
and n is numbers.

´´´
O(1)
t = int(input)
while t:
	t -= 1
	n = int(input())
	return (n * (n+1)) // 2

´´´

This way is a lot more efficient that adding all the number
together in lets say a for loop with efficiency O(n)