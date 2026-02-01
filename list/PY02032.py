tmp = input()
s = set()
a=[]
for i in range(0,len(tmp)-1,2) :
    s.add(int(tmp[i]+tmp[i+1]))
for c in s:
    a.append(c)
a.sort()
for c in a : print(c,end=" ")