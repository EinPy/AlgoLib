# Sample solution to: https://www.codechef.com/COOK09/problems/MIME2
# A problem from codechef that screams for hashTable

N, Q = list(map(int, input().split()))

media = {}
for i in range(N):
	ext, name = input().split()

for i in range(Q):
	file = input()
	if . in file:
		parts = file.split(.)
		if parts[-1] in media:
			return media[parts[-1]]
		else:
			return 'unknown'
	else:
		return 'unknown'