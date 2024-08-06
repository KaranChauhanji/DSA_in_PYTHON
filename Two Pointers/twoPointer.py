# Q - Problem: Count Unique Pairs with Given Sum

# You are given a list of integers and a target sum. Your task is to count the number of unique pairs in the list that add up to the target sum. A pair is considered unique if it consists of two different elements, and the order of the elements in the pair does not matter (i.e., (a, b) is the same as (b, a)).



# Two pointers approach for this question

A = [1,2,3,4,5]
size = len(A)
x = 7

def checkPair(A,size,x):
    
    A.sort()
    count = 0 
    left = 0
    right  = size - 1
    
    while (left < right):
        current_sum = A[left] + A[right] 
        if(current_sum == x):
            count += 1
            left += 1
            right -= 1
        elif(current_sum < x):
            left += 1
        else:
            right -= 1
    return count 

    

result = checkPair(A,size,x)

print(result)



# TC = O(n log n)
# SP = O(1)