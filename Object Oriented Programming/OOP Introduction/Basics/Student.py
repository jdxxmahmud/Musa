class Student:
    def __init__(self, id: int, name: str, age: int) -> None:
        self.__id = id
        self.__name = name 
        self.__age = age

    def getId(self):
        return self.__id

    def getName(self):
        return self.__name

    # Complete the getters and setters 
    
