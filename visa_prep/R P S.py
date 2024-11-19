v, c = input().split()
print("NULL" if v == c else "Vignesh" if (v, c) in [("R", "S"), ("P", "R"), ("S", "P")] else "Charan")
