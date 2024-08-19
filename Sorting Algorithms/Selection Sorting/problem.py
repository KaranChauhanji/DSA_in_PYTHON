# Sort this list in ascending order with selection sorting -->

arr = [88,100,75,89,20,15]

n = len(arr)

for i in range(n):
    min_index = i
    for j in range(i+1,n):
        if arr[j] < arr[min_index]:
            min_index = j
    if min_index != i:
        arr[i], arr[min_index] = arr[min_index], arr[i]
        
print(arr)