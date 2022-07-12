n = input("")
x = map(int, (input('')).split())

group_one = 0
group_two = 0
group_three = 0
group_four = 0

#Inputing number in variables 
for i in x:
    if i == 1:
        group_one += 1
    elif i == 2:
        group_two += 1
    elif i == 3:
        group_three += 1
    else:
        group_four += 1

num_taxi = group_four


if group_three >= group_one:
    num_taxi += group_three
    group_three = 0 
    group_one = 0

elif group_three < group_one:
    num_taxi += group_three
    group_one = group_one - group_three 
    group_three = 0

if group_two % 2 == 0 :
    num_taxi += group_two // 2
    group_two = 0
else:
    num_taxi += group_two // 2   
    group_two = 0
    if group_one <=2:
        num_taxi += 1
        group_one = 0
    elif group_one != 0:
        num_taxi += 1
        group_one -= 2
'''
if group_one <= 4 :
    num_taxi += 1 
else:
    if group_one % 4 == 0:
        num_taxi += group_one // 4
    else:
        num_taxi += group_one // 4 + 1
'''
if group_one >= 4:
    if group_one % 4 == 0:
        num_taxi += group_one // 4
        group_one = 0
    else:
        num_taxi += group_one // 4 + 1
elif group_one >= 1:
    num_taxi += 1
    group_one = 0

print(num_taxi)



