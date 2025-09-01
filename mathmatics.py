print("a^2 + b^2 + c^2 = 2026　を満たす自然数の組 (a, b, c) を全て求めよ")

N = 44

for a in range(1, N + 1):
    for b in range(1, N + 1):
        for c in range(1, N + 1):
            i = a ** 2 + b ** 2 + c ** 2
            if i == 2026:
                print(a, b, c)