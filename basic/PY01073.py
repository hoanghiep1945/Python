# s = input()

# v=[]
# use = [False]*len(s)

# def Try():
#     if len(v) == len(s):
#         print("".join(v))
#         return 
#     for i in range(len(s)):
#         if not use[i] : 
#             use[i]  = True
#             v.append(s[i])
#             Try()
#             v.pop()
#             use[i] = False
# Try()

from itertools import permutations
s = input()
for c in permutations(s):
    print("".join(c))