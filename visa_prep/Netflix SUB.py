A, B, C, X = map(int, input().split())
print("YES" if (A + B >= X or A + C >= X or B + C >= X)else "NO")
