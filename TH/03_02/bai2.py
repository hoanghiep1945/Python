import sys

def main():
    with open("BANTAU.INP", "r") as f:
        data = list(map(int, f.read().split()))
    if not data:
        return

    n, k = data[0], data[1]
    d = data[2:2 + n]

    pref = [0] * (n + 1)
    for i in range(1, n + 1):
        pref[i] = pref[i - 1] + d[i - 1]

    cost = [[0] * (n + 1) for _ in range(n + 1)]
    for l in range(1, n + 1):
        mx = 0
        for r in range(l, n + 1):
            if d[r - 1] > mx:
                mx = d[r - 1]
            seg_sum = pref[r] - pref[l - 1]
            cost[l][r] = (r - l + 1) * mx - seg_sum

    INF = 10**30
    max_seg = min(n, k + 1)

    dp_prev = [INF] * (n + 1)
    dp_prev[0] = 0

    ans = INF
    for seg in range(1, max_seg + 1):
        dp = [INF] * (n + 1)
        for i in range(1, n + 1):
            best = INF
            for j in range(1, i + 1):
                v = dp_prev[j - 1] + cost[j][i]
                if v < best:
                    best = v
            dp[i] = best

        if dp[n] < ans:
            ans = dp[n]
        dp_prev = dp

    with open("BANTAU.OUT", "w") as f:
        f.write(str(ans))


if __name__ == "__main__":
    main()