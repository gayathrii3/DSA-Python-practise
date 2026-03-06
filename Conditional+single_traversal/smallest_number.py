# Find the smallest number in a list of numbers

arr = [10, 25, 3, 47, 5, 62, 7, 81, 9, 10]

smallest = arr[0]

for num in arr:
    if num < smallest:
        smallest = num

print(f"{smallest} is the smallest number")