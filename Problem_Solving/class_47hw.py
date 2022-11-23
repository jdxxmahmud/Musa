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
    range_lst = {
        '0 to 10' : 0,
        '11 to 20' : 0,
        '21 to 30' : 0,
        '31 to 40' : 0, 
        '41 to 50' : 0,
        '51 to 60' : 0, 
        '61 to 70' : 0,
        '71 to 80' : 0, 
        '81 to 90' : 0, 
        '91 to 100': 0 
    }
    for j in arr:
        if j <= 50:
            if j <= 10:
                range_lst['0 to 10'] += 1
                continue
            elif j <= 20 and j >= 11:
                range_lst['11 to 20'] += 1
                continue
            elif j <= 30 and j >= 21:
                range_lst['21 to 30'] += 1
                continue
            elif j <= 40 and j >= 31:
                range_lst['31 to 40'] += 1
                continue
            else:
                range_lst['41 to 50'] += 1
        else:
            if j <= 60:
                range_lst['51 to 60'] += 1
                continue
            if j <= 70 and j >= 61:
                range_lst['61 to 70'] += 1
                continue
            if j <= 80 and j >= 71:
                range_lst['71 to 80'] += 1
                continue
            if j <= 90 and j >= 81:
                range_lst['81 to 90'] += 1
                continue
            else:
                range_lst['91 to 100'] += 1

    return range_lst


lst = [91, 93, 85, 83, 71, 77, 54, 51, 60, 69, 42, 48, 39, 33, 27, 
28, 19, 15, 10, 5, 8]

print(rangeMaker(lst))