# Taking out all the substrings if size(k) is not fixed with sliding windows -->

arr = [1,2,3,4,5,6]
n = len(arr)

# for size in range(1, n+1):
#     for i in range(n - size + 1):
#         print(arr[i:i+size])


# Different approach :

# for i in range(n):
#     for j in range(i+1,n+1):
#         print(arr[i:j])
        
        
