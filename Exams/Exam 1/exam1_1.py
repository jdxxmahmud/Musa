# Problem 1

for i in (1, 2, 3):
    print(i)

'''
Output:
=======================
1
2
3
========================
'''

# Problem 2

for i in (2, 3, 4):
    print("i")

'''
Output:
=======================
2
3
4
========================
'''

# Problem 3

for i in range(10):
    if(i % 2 != 0):
        print("Hello", i)

'''
Output:
=======================
Hello1
Hello3
Hello5
Hello7
Hello9
========================
'''

# Problem 4
num1 = 7
num2 = 10
for i in range(5):
    num2 = num2+10
    print(num2)
    print(num1)

'''
Output:
=======================
20
7
30
7
40
7
50
7
60
7
========================
'''

# Problem 5
a = 7
b = 5

while(a < 9):
    print(a+b)
    a += 1

'''
Output:
=======================
12
13
========================
'''


# Problem 6
L = [13 , 12 , 21 , 16 , 35 , 7, 4]
s = 5
s1 = 3
for i in L:
     if (i % 4 == 0):
          s = s + i
          continue
     if (i % 7 == 0):
          s1 = s1 + i
print(s , end=" ")
print(s1)

'''
Output:
=======================
25 63
========================
'''

# Problem 7

s1 = "ilovepython"
c = 0
for x in s1:
    if(x != "l"):
        c = c+1
print(c)

'''
Output:
=======================
10
========================
'''

#Marks - 64.3%
#Grade-  C