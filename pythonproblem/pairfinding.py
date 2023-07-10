'''
Suppose you have an undsorted array and you need to find a pair that's sums up to the specific given number 
Example 
[1,3,5,3,8,2,3,1,6,9,2,6,3,7] key = 10
output : 1 and 9 are a pair that adds up to 10
'''
def pairfinding(arr, key):
    for i in range(len(arr)-1, -1, -1):
        for j in range(0,i):
            if key - arr[i] == arr[j]:
                return f'after [ {i} , {j} ] {arr[i]} and {arr[j]} are a pair that adds up to {key}'

print(pairfinding([1,3,5,3,8,2,3,1,6,9,2,6,3,7], 11))

print(pairfinding([1, 2, 5, 8, 3], 11))