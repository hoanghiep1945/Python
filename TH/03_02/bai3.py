import sys

class DSU:
    def __init__(self, n, area):
        self.p = list(range(n))
        self.sz = [1] * n
        self.area = area[:]

    def find(self, x):
        while self.p[x] != x:
            self.p[x] = self.p[self.p[x]]
            x = self.p[x]
        return x

    def union(self, a, b):
        ra = self.find(a)
        rb = self.find(b)
        if ra == rb:
            return
        if self.sz[ra] < self.sz[rb]:
            ra, rb = rb, ra
        self.p[rb] = ra
        self.sz[ra] += self.sz[rb]
        self.area[ra] += self.area[rb]


def merge_touch(listA, listB, dsu):
    i = 0
    j = 0
    na = len(listA)
    nb = len(listB)
    while i < na and j < nb:
        a_s, a_e, a_id = listA[i]
        b_s, b_e, b_id = listB[j]

        if a_e < b_s:
            i += 1
        elif b_e < a_s:
            j += 1
        else:
            dsu.union(a_id, b_id)
            if a_e < b_e:
                i += 1
            else:
                j += 1


def main():
    with open("LATGACH.INP", "r") as f:
        data = list(map(int, f.read().split()))
    if not data:
        return

    n = data[0]
    vals = data[1:]

    x1 = [0] * n
    y1 = [0] * n
    x2 = [0] * n
    y2 = [0] * n
    area = [0] * n

    for i in range(n):
        X, Y, D, C = vals[4 * i:4 * i + 4]
        x1[i] = X
        y1[i] = Y
        x2[i] = X + D
        y2[i] = Y + C
        area[i] = D * C

    dsu = DSU(n, area)

    left_edges = {}
    right_edges = {}

    bot_edges = {}
    top_edges = {}

    for i in range(n):
        lx = x1[i]
        rx = x2[i]
        by = y1[i]
        ty = y2[i]

        left_edges.setdefault(lx, []).append((y1[i], y2[i], i))
        right_edges.setdefault(rx, []).append((y1[i], y2[i], i))

        bot_edges.setdefault(by, []).append((x1[i], x2[i], i))
        top_edges.setdefault(ty, []).append((x1[i], x2[i], i))

    for x in right_edges:
        if x not in left_edges:
            continue
        A = right_edges[x]
        B = left_edges[x]
        A.sort()
        B.sort()
        merge_touch(A, B, dsu)

    for y in top_edges:
        if y not in bot_edges:
            continue
        A = top_edges[y]
        B = bot_edges[y]
        A.sort()
        B.sort()
        merge_touch(A, B, dsu)

    ans = 0
    for i in range(n):
        if dsu.find(i) == i:
            if dsu.area[i] > ans:
                ans = dsu.area[i]

    with open("LATGACH.OUT", "w") as f:
        f.write(str(ans))


if __name__ == "__main__":
    main()