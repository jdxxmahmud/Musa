import os
import sys
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from company import Company
from datetime import datetime


if __name__ == "__main__":
    pass
