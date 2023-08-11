lst = [1, 2, 48, 65, 32, 128, 99, 10]

def bubbleSort(array):

    for i in range(len(array)):

        for j in range(0, len(array) - i - 1):

            if array[j] < array[j + 1]:

                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp

    return array 


list2 = [1, 9, 2, 8, 3, 7, 4, 6, 10, 0, 5, 5]

for i in range(len(list2)):
    for j in range(len(list2) - i - 1):
        if list2[j] < list2[j+1]:
            temporary = list2[j] 
            list2[j] = list2[j + 1]
            list2[j + 1] = temporary

print(list2)



print(bubbleSort(lst))


