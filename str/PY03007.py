import sys
import re

s = re.split(r"[.?!]", sys.stdin.read().lower())

for c in s:
    c = c.strip()
    c=c.capitalize()
    print(re.sub(r"\s+", " ", c.strip()))