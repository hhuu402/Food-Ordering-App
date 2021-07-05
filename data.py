from inventory import *
from order import *
from queue_file import *
from staff import *

# -- Global Variables Only --
# This file will only contain variables that will be used across
# multiple html pages.

# HOME PAGE
q = Queue()
staff = Staff()
inventory = Inventory('.db')
sides_sizes = ['small','medium','large']
drink_sizes = ['small','medium']

temp_orders = []
# Dictionary in format...
# name : func in routes.py
nav_start =  {
    "home": 'home',
    "check order": 'check_id' #replace when possible
}
nav_end = {
    "staff": 'staff_login' #replace when possible
}
