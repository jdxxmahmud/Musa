class Student:
    def __init__(self, id: int, name: str, age: int):
        
        #Private 
        self.__id = id
        self.__name = name 
        self.__age = age

    #Getter Methods - Private 

    def getId(self):
        return self.__id

    def getName(self):
        return self.__name
    
    def getAge(self):
        return self.__age

    #Setter Methods - Private 

    def setId(self, id):
        self.__id = id

    def setName(self, name):
        self.__name = name
    
    def setAge(self, age):
        self.__age = age

    
    
