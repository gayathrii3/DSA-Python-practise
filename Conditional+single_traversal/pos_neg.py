# Count how many numbers are positive, negative, and zero

arr = [0, 25.0, -3, 47, 0.95, -62, 7, 81, -9, 0]

positive = 0
negative = 0
zeros = 0

for n in arr:
    if n > 0:
        positive += 1
    elif n < 0:
        negative += 1
    else:
        zeros += 1

print(f"pos = {positive}\nneg = {negative}\nzeros = {zeros}")
