# Taking out k length of substrings with sliding Windows -->

arr = [1,2,3,4,5,6]
n = len(arr)
k = 3

for i in range(n - k + 1):
    print(arr[i:i+k])
