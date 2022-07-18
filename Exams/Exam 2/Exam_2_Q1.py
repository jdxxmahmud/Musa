# Exam: 2 Question 1

'''
You will be given a sorted array and a target value. 
You have to find the indexes of elements that sum to the target value. 
Return -1 if no such pair of elements are found.
Example:
Input: arr = [1, 2, 3, 4, 8, 12], target = 7
Output: [2, 3]

Note: It's confirmed that there will not be multiple answer. 
Repeatation of a element while summing to the target is not acceptable. 
For example: arr = [1, 2, 3, 4] and target: 6, you can not return [2, 2], since the element 3
will have to be used only once. Here the ans will be [1, 3]
Time: 30 minutes
'''


def targ_sum(arr, target):
    # Your code starts here
        for i in range(0,len(arr)-1):

            for n in range(i+1, len(arr)):
                if arr[i] + arr[n] == target:
                    return[i, n]
            
        return -1 
            
        


arr = [1, 2, 3, 4, 8, 12]
target = 7
print("Correct" if targ_sum(arr, target) == [2, 3] else "Incorrect")
print("Correct" if targ_sum([5, 4, 7, 1], 2) == -1 else "Incorrect")


'''
lo = 0
hi = len(arr) - 1

while arr[lo] + arr[hi] != target:
        


arr = [1, 2, 3, 4, 8, 12]
target = 7


'''