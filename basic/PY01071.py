s = input()
ok = 1
if not s.lower().endswith(".py"): 
    print("no")
    ok = 0
for i in s :
    if not (i.isalpha() or i in "._") and ok == 1: 
        print("no")
        ok = 0
        break
if(ok == 1) : print("yes")