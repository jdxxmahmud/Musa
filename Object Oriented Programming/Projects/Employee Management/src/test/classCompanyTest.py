import os
import sys
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from company import Company
from datetime import datetime
from employee import Employee

companyOne = Company(datetime.date(2006, 3, 19), "Hexagon", "Uttara, Dhaka", "Technology", 156000000)

