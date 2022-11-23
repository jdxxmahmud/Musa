# 0 - 0 to 10 
# 1 - 11 to 20
# 2 - 21 to 30 
# 3 - 31 to 40 
# 4 - 41 to 50 
# 5 - 51 to 60 
# 6 - 61 to 70 
# 7 - 71 to 80 
# 8 - 81 to 90 
# 9 - 91 to 100
def rangeMaker (arr: int):
    range_lst = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for j in arr:
        if j <= 50:
            if j <= 10:
                range_lst[0] += 1
                continue
            elif j <= 20 and j >= 11:
                range_lst[1] += 1
                continue
            elif j <= 30 and j >= 21:
                range_lst[2] += 1
                continue
            elif j <= 40 and j >= 31:
                range_lst[3] += 1
                continue
            else:
                range_lst[4] += 1
        else:
            if j <= 60:
                range_lst[5] += 1
                continue
            if j <= 70 and j >= 61:
                range_lst[6] += 1
                continue
            if j <= 80 and j >= 71:
                range_lst[7] += 1
                continue
            if j <= 90 and j >= 81:
                range_lst[8] += 1
                continue
            else:
                range_lst[9] += 1
            
    return f'''0 to 10 = {range_lst[0]}\n11 to 20 = {range_lst[1]}\n21 to 30 = {range_lst[2]}\n31 to 40 = {range_lst[3]}\n41 to 50 = {range_lst[4]}
51 to 60 = {range_lst[5]}\n61 to 70 = {range_lst[6]}\n71 to 80 = {range_lst[7]}\n81 to 90 = {range_lst[8]}\n91 to 100 = {range_lst[9]}'''


lst = [91, 93, 85, 83, 71, 77, 54, 51, 60, 69, 42, 48, 39, 33, 27, 
28, 19, 15, 10, 5, 8]

print(rangeMaker(lst))

