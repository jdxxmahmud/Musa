import os
import sys
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from manager import Manager
from datetime import datetime

def createManager():
    manager = Manager(1, "Superman", 2000000)

    # print(manager.position)
    manager.printFullDetails()

if __name__ == "__main__":
    createManager()
