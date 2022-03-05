'''input
5 6
html text/html
htm text/html
png image/png
svg image/svg+xml
txt text/plain
index.html
this.file.has.lots.of.dots.txt
nodotsatall
virus.exe
dont.let.the.png.fool.you
case.matters.TXT
'''

# Sample solution to: https://www.codechef.com/COOK09/problems/MIME2
# A problem from codechef that screams for hashTable

N, Q = list(map(int, input().split()))

media = {}
for i in range(N):
	ext, name = input().split()
	media[ext] = name
#print(media)

for i in range(Q):
	file = input()
	if '.' in file:
		parts = file.split('.')
#		print(parts)
#		print(f'last part: {parts[-1]}')
		noDigEnd = ''.join(i for i in parts[-1] if not i.isdigit())
		if noDigEnd in media:
			print( media[noDigEnd])
		else:
			print( 'unknown')
	else:
#		print ('no dot')
		print ('unknown')