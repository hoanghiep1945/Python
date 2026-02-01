s = input()
a = list(map(int,input().split()))
a.sort()
print(max(a[len(a)-1]*a[len(a)-2]*a[len(a)-3],
          a[len(a)-1]*a[len(a)-2],
          a[0]*a[1]*a[len(a)-1]))