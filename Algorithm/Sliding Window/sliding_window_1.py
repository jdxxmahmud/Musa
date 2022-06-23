def max_sum(lst, k=3):

    length = len(lst)
    max_sum = -99999

    for i in range(length - k):

        current_sum = 0

        for j in range(i, i + k):  # Getting the sum of the window
            current_sum += lst[j]

        if max_sum < current_sum:
            indexes = []
            max_sum = current_sum
            for j in range(i, i + k):
                indexes.append(j)

    return max_sum, indexes


lst = [1, 2, 3, 6, 7, 8, 1, 2, 9, 6, 2, 10, 5, 0, 1, 3, 9, 8, 1]
print(max_sum(lst, 4))
