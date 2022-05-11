'''
It takes a l, and a key. 
Returns the position of the key in the list,
    * if the key is present in the list
    * else return -1 
'''


from pickletools import int4


def linearSearch(my_list: int, key: int):

    len_list = len(my_list)

    for i in range(len_list):
        if my_list[i] == key:
            return i

    # The following will run if the key is not in the list
    return -1


def main():
    # my_list = map(int, input("Enter list").split(" "))
    # key = int(input("Enter key: "))

    my_list = [10, 20, 30, 12, 6, 50, -2, 79]
    key = 7

    ans = linearSearch(my_list, key)

    print(f"Correct, position is {ans}" if ans == 4 else "Wrong")


main()
