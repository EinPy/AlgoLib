#iterative solution if n is greater than 2
def fibIt(n):
    one, two = 1, 1
    n = n-2
    for i in range(n):
        three = one + two
        one = two
        two = three
    print(three)
fibIt(7)


#solving the problem recursively
#non opimal implementation, but the simplest recursive implementation
#T.C O(N^2) S.C O(N)
def fibRec(n):
    fibRec.cnt += 1
    if n <= 2:
        return 1
    return fibRec(n-2) + fibRec(n-1)

fibRec.cnt = 0



#improved recursive solution with memoizatoin
#Using a dict for example, in large scale it will
#be more effective with array
def fibMem(n, memo = {}):
    fibMem.cnt += 1
    if n in memo:
        return memo[n]
    if n <= 2:
        return 1
    memo[n] = fibMem(n-1,memo) + fibMem(n-2,memo)
    return memo[n]
fibMem.cnt = 0


print(fibRec(30), fibRec.cnt)
print(fibMem(30), fibMem.cnt)
