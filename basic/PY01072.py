n,k = map(int,input().split())
a = list(map(int,input().split()))
a=sorted(set(a))
n=len(a)

v=[]

def Try(i) :
    if len(v) == k:
        print(*v)
        return 
    for j in range(i,n):
        v.append(a[j])
        Try(j+1)
        v.pop()

Try(0)