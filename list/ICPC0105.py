import re
for _ in range(int(input())) :
    nums = list(map(int, re.findall(r'\d+', input())))
    print(max(nums))