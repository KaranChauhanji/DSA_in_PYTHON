# Q - You are given a list of integers and a target sum. Your task is to write a Python function that counts the number of unique pairs of elements in the list whose sum equals the target sum. The function should implement a brute force approach to solve this problem.

# Function Signature:

# Define a function named checkPair that takes three arguments:
# A (a list of integers)
# size (an integer representing the size of the list)
# x (an integer representing the target sum)
# The function should return an integer representing the number of unique pairs in the list whose sum equals x.



# Brute Force Approach for this question

A = [1,2,3,4,5]
size = len(A)
x = 7

def checkPair(A, size, x):
    
    count =0
    
    for i in range(size - 1):
        for j in range(i+1, size):
            if(A[i] + A[j] == x):
                count += 1
                
    return count




print(checkPair(A,size,x))



# TC = O(n**2)
# SC = O(1)