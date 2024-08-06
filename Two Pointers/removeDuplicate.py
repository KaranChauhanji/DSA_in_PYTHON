# Remove Duplicate from the list --> 


# Brute Force approach : 

# arr = [1,2,2,3,3,3,4,4,4,4]
# new_arr = []

# for i in arr: 
#     if i not in new_arr:
#         new_arr.append(i)
        
# print(new_arr)
        
        
        
# TC = O(n**2)
# SC = O(n)
        
        
        
        
# Two Pointers Approach : 

# same direction Two pointers -

arr = [1,2,2,3,3,3,4,4,4,4]

left = 0
right = 1

while right < len(arr):
    if (arr[left] == arr[right]):
        right += 1
    else:
        left += 1
        arr[left] = arr[right]
        right += 1
        
        
print(arr[:left + 1]) 

# TC = O(n)
# SP = O(1)