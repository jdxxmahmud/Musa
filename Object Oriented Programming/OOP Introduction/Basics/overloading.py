class box:
    def __init__(self, name: str):
        self._name = name
        self._area = 0

    def findArea(length = None, breadth = None ):
        if length != None and breadth != None:
            return length * breadth
        elif length != None:
            return length **2
        else:
            return 'Give measurements'


Garden = box

print(Garden.findArea())


