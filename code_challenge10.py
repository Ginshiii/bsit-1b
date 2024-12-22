
n = 10

# First part: Increasing stars
for i in range(2, n + 2, 2):
    print(" " * (n - (i // 2)) + "*" * i)
for i in range(n, 0, -2):
    print(" " * (n -(i // 2)) + "^" * i)