# Find the largest number in a list of numbers

arr = [10, 25, 3, 47, 5, 62, 7, 81, 9, 10]

# largest = arr[0] #assume first number as the largest
# for num in arr:
#     if num > largest:
#         largest = num

# print(f"{largest} is the larget number")

# --------------------------------------------------------

largest = arr[0]
smallest = arr[0]

for n in arr:
    if n > largest:
        largest = n
    else:
        smallest = n

print(f"Largest = {largest}, Smallest = {smallest}")