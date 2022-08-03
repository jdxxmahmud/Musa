class identity:
    name = 'Musa'#why is this called an object
    age = 16
    gender = "Male"
    occupation = "Professional Racist"

print(identity.name)
print(identity.age)
print(identity.occupation)
print(identity.gender)

class Person:
    def __init__(self, name, age):
        #attributes
         self.name = name
         self.age = age

#print(Person("Musa", 16))

p1 = Person("musa", 16)
p2 = Person("Sudad", 18)
p3 = Person('ayan', 12)

ask = input('')

if ask == 'age':
    print(p1.age)
    #print(p1) - eta kono kichu dai na keno 
else:
    print(p1.name)

class My_Class:
    def __init__(self, age):
        self.age = age
        def next_age(self):
            return print(age+1)

    


