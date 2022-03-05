# bitwise &
print(2 & 1, 234 & 1, 500 & 1) #even: returns 0s
print(3&1, 9&1, 325 & 1) #odd: returns 1s

def isEven(n): # of course you could just use the modulus statment
	#however, it is slightly faster with very large numbers
	if n&1 == 0:
		return True
	else: return False

n = 32
print(n >> 2) #returns 8
m = 300
print(m >> 3)
# x >> z = x // 2**z
m = 400
print(m << 4)
#m << 4 = m * (2**4) = m * 16

def mulPow2(x, y):
	return x << y:

def divPow2(x, y):
	return x >> y


