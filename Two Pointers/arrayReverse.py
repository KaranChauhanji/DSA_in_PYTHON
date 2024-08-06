# Reverse the array -->

arr = [1,2,3,4,5]
size = len(arr)


# 1. Brute Force method : 

# new_arr = []

# for i in range(size-1, -1 , -1):
#      new_arr.append(arr[i])
     
# print(new_arr)

# TC = O(size)
# SC = O(size)


# 2. Two Pointers approach :

left = 0
right = size - 1

while left < right :
    arr[left], arr[right] = arr[right], arr[left]
    left += 1
    right -= 1
    
print(arr)

# TC = O(size)
# SC = O(1)
