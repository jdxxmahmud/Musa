def max_sum(lst, k = 3):
    
    max_sum = -99999
    current_sum = 0
    
    for i in range(len(lst)):
        current_sum += lst[i]
        
        if i >= k - 1:
            if max_sum < current_sum:
                max_sum = current_sum
            current_sum -= lst[i - (k - 1)]
            
    return max_sum


lst = [1, 2, 3, 6, 7, 8, 1, 2, 9, 6, 2, 10, 5, 0, 1, 3, 9, 8, 1]
print(max_sum(lst, 4))