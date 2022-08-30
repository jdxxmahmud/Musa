#conditions
#if num is smaller than 256 = 0 
#if num is equal to 256 = 1 
#if num is greater than 256 -> int(num) = greater than 1


num  = input('')

if float(num) == 256.0:
    new_num = 1

elif float(num) < 256:
    new_num = 0

else:
    new_num = int(float(num) / 256)



print(float(num) - (new_num * 256))