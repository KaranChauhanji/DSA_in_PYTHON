# Sort this list in ascending order with bubble sorting -->

arr = [88,100,75,89,20,15]

n = len(arr)

for i in range(n):
    isSwap = False
    for j in range(n-1-i):
        if arr[j+1] < arr[j]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
            isSwap = True
            
    if not isSwap:
        break
    
print(arr)