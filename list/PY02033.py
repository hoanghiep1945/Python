tmp = input()
a=[]
d=[0]*1001
for i in range(0,len(tmp)-1,2) :
    if d[int(tmp[i]+tmp[i+1])] == 0:
        a.append(int(tmp[i]+tmp[i+1]))
        d[int(tmp[i]+tmp[i+1])] += 1
for c in a:
    print(c,end=" ")