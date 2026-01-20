_,_ = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
da = [0]*1001
db = [0]*1001
sa = set()
sb = set()
for c in a : 
    sa.add(c)
for c in b : 
    sb.add(c)
if sa==sb : print("YES")
else : print("NO")