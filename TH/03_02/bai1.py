import sys

class BIT:
    def __init__(self, n):
        self.n = n
        self.bit = [0] * (n + 1)

    def add(self, i, v):
        n = self.n
        while i <= n:
            self.bit[i] += v
            i += i & -i

    def sum(self, i):
        s = 0
        while i > 0:
            s += self.bit[i]
            i -= i & -i
        return s


def main():
    with open("SAPXEP.INP", "r") as f:
        data = list(map(int, f.read().split()))
    if not data:
        return

    n = data[0]
    a = data[1:1 + n]

    pos = [0] * (n + 1)
    for i, v in enumerate(a, 1):
        pos[v] = i

    bit = BIT(n)
    for i in range(1, n + 1):
        bit.add(i, 1)

    out = []
    L, R = 1, n
    rem = n

    for step in range(1, n + 1):
        if step % 2 == 1:
            x = L
            cur_rank = bit.sum(pos[x])
            swaps = cur_rank - 1
            out.append(str(swaps))
            bit.add(pos[x], -1)
            L += 1
        else:
            x = R
            cur_rank = bit.sum(pos[x])
            swaps = rem - cur_rank
            out.append(str(swaps))
            bit.add(pos[x], -1)
            R -= 1

        rem -= 1

    with open("SAPXEP.OUT", "w") as f:
        f.write("\n".join(out))


if __name__ == "__main__":
    main()