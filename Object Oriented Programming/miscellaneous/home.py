class House:
    def __init__(self, windows_, rooms_, doors_, secretRoom_ ) :

        #Attributes - Public 
        self.windows = windows_
        self.rooms = rooms_
        self.doors = doors_

        #Attributes - Private 
        self.__secretRoom = secretRoom_

    #Getter - Methods 
    def get_windows(self):
        return self.windows

    def get_rooms(self):
        return self.rooms

    def get_doors(self):
        return self.doors

    def get_secretRoom(self):
        return self.__secretRoom

    #Setter - Methods
    def set_windows(self, windows_):
        self.windows = windows_

    def set_rooms(self, rooms_):
        self.rooms = rooms_

    def set_doors(self, doors_):
        self.doors = doors_

    def set_secretRoom(self, secretRoom_):
        self.__secretRoom = secretRoom_



home = House(9, 5, 12, True)

print(home.windows)
print(home.rooms)
print(home.doors)
print(home.get_secretRoom())

