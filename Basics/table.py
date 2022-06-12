#n = int(input('Enter the table numbers you want:'))
column = [1,2,3,4,5]
row = [1,2,3,4,5]

for i in column :
    for n in row:
        if n < column[-1]:
            print(f"{n} X {i} = {i*n}",end = "\t")
        elif n == column[-1]:
            print(f"{n} X {i} = {i*n}",end = "\n")


