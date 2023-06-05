class Student:

    def __init__(self, name_, group_, section_, marks_,studentID_):

        #Attibutes - Public
        self.name = name_
        self.group = group_
        self.section = section_
        
        #Attributes - Private
        self.__studentID = studentID_
        self.__marks = marks_

    #Getter Method
    def get_studentID(self):
        return self.__studentID 

    def get_marks(self):
        return self.__marks
    
    #Setter Method
    def set_studentID(self, studentID_):
        self.__studentID = studentID_

    def set_marks(self, marks_):
        self.__marks = marks_

    


# for i in class8:

#     print(i.name, end = ", ")
#     #print(i.group, end = ", ")
    
#     print(i.section)


# def printer(arr):
#     for i in range(0, len(arr)):

#         print(arr[i].name, end = ", ")
#         print(arr[i].get_studentID(), end = ", ")
#         print(arr[i].section, end = ", ")
#         print(arr[i].get_marks())
        
# def update_studentID(arr):

#     for i in range(0, len(arr)):
#         class8[i].set_studentID(i + 1)

# # def increase_mark(class8):

# #     for i in range(0, len(class8)):
# #         if class8[i].section == "B":
# #             class8[i].set_marks(class8[i].get_marks() + 3)

# def increase_marks(arr, section, num, increase):

#     operation = 0
#     if increase == True:
#         operation = 1
#     else:
#         operation = -1 

#     for i in range(0, len(arr)):
        
#         if arr[i].section == section:
#             arr[i].set_marks(arr[i].get_marks() + (operation * num))


# for i in range(len(class8)):

#     for j in range(0, len(class8) - i - 1):

#         if class8[j].get_marks() < class8[j + 1].get_marks():

#             temp = class8[j]

#             class8[j] =  class8[j + 1]

#             class8[j + 1] = temp

# # update_studentID(class8)
# # printer(class8)
# # print()
# # increase_marks(class8,"B", 3, True)
# # printer(class8)