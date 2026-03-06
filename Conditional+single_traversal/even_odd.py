# Count how many numbers are even and how many are odd

arr = [2, 5, 6, 8, 23, 1, 49, 98, 34, 87, 52] 

even = 0
odd = 0

for n in arr:
    if n % 2 == 0:
        even += 1
    else:
        odd += 1

print(f"Even num = {even}\nOdd num = {odd}")


