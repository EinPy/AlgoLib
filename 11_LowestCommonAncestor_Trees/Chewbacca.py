i=lambda:map(int,input().split())
n,k,q=i()
while q:
	q-=1;x,y=i();x-=1;y-=1;d=0
	while x!=y:
		if x>y:x=(x-1)//k
		else:y=(y-1)//k
		d+=1
	print(d)