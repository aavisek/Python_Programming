array=[39,56,87,90,21,45,67,12,34,78]
length = len(array)
for i in range(length):
    print("Position:", i, "Value:", array[i])
# This code traverses through the array and prints each element one by one.

# sum of all elements in the array
total_sum = 0
for i in range(length):
    total_sum += array[i]
print("Total Sum:", total_sum)