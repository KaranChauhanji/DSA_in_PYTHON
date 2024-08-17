arr = [6,2,4,7,1,2]
n = len(arr)
k = 3


# Take out the sum of the fixed size (k) sliding windows -->

# sum_ = 0

# for i in range(n - k + 1):
#     sum_ = sum(arr[i:i+k])
#     print(sum_)
    

# Take out the maximum sum of the fixed size (k) sliding windows -->

max_sum = float('-inf')

for i in range(n - k + 1):
    current_sum = sum(arr[i:i+k])
    max_sum = max(current_sum, max_sum)
    
print(max_sum)
