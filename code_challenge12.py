n = 8
for i in range(2, n + 2, 2):
    print(" " * (n - (i // 2)) + "*" * i)
for _ in range(n):
    print(" " * ( n - 1) + "**")