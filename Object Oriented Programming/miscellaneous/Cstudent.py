class Student:

    def __init__(self, name_, group_, section_, marks_, studentID_):

        #Attributes - Public 
        self.name = name_
        self.group = group_
        self.section = section_

        #Attributes - Private 
        self.__studentID = studentID_
        self.__marks = marks_

    #Getter Methods 
    def get_studentID(self):
        return self.__studentID

    def get_marks(self):
        return self.__marks

    #Setter Method 

    def set_studentID(self, studentID):
        self.__studentID = studentID

    def set_marks(self, marks_):
        self.__marks = marks_

Musa = Student("Musa Sudad", "10", "A", 87, "202110A")

Tasnuba = Student("Tasnuba Tahiyat", "9", "B", 82, "20229B")

Mahtab = Student("Syed Mahtab", "5", "E", 68, "20165E")

Shikhi = Student("Shikhi Hussain", "7", "C", 96, "20207C")

Abdullah = Student("Abdullah Al Mamun", "6", "D", 73, "20106D")

Fahad = Student("Fahad Al Azad", "10", "B", 85, "201510B")

Nafees = Student("Nafees Abid", "8", "F", 88, "20198F")

class8 = [Musa, Tasnuba, Shikhi, Fahad, Nafees, Abdullah, Mahtab]

'''
for i in class8:

    print(i.name, end = ", ")
    print(i.group, end = ", ")
    print(i.section)
'''
def printer(arr):
    for i in range(0, len(arr)):

        print(arr[i].name, end = ", ")
        print(arr[i].get_studentID(), end = ", ")
        print(arr[i].section, end = ", ")
        print(arr[i].get_marks())

def update_studentID(arr):
    
    for i in range(0, len(arr)):
        class8[i].set_studentID(i + 1)

'''
def increase_mark(class8):

    for in range(0, len(class8)):
        if class8[i].section == "B":
            class8[i].set_marks(class8[i].get_marks() + 3)
'''

def increase_marks(arr, section, num, increase):

    operation = 0
    if increase == True:
        operation = 1
    else:
        operation = -1 

    for i in range(0, len(arr)):

        if arr[i].section  == section:
            arr[i].set_marks(arr[i].get_marks() + (operation * num))

for i in range(len(class8)):

    for j in range(0, len(class8) - i - 1):

        if class8[j].get_marks() < class8[j + 1].get_marks():
            temp = class8[j]

            class8[j] = class8[j + 1]

            class8[j + 1] = temp

update_studentID(class8)

printer(class8)

print()

increase_marks(class8, "B", 3, True)

printer(class8)

arr = [1,2,3,4]
key = 5
hi = len(arr) - 1 
lo = 0 