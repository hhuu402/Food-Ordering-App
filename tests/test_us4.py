import sys
import os
sys.path.append('../')
import pytest
from staff import *
from inventory import *
from order import *
from queue_file import *
from food import F_S
from call_error import CallError

#TEST FOR USERSTORIES 4
class Test_US4():
    inventory = 'Inventory(.db)'

    def setup_method(self):
        ...
   
    #4.1: Check Staff Login
    #this tests for login attempts
    def test_bad_password(self):   
        staff = Staff()
        bad_pass1 = '234'
        bad_pass2 = ''
        bad_pass3 = 'hello'
        bad_pass4 = 12

        assert(staff.login(bad_pass1) == False)
        assert(staff.login(bad_pass2) == False)
        assert(staff.login(bad_pass3) == False)
        assert(staff.login(bad_pass4) == False)

    def test_good_password(self):
        staff = Staff()
        good_pass = '123'

        assert(staff.login(good_pass) == True)

    #4.2: Check Log
    #staff needs to be able to see a list of orders
    def test_staff_check_order(self):
        staff = Staff()
        q = Queue()

        order1 = Order()
        assert(q.add_order(order1) == 1)
        assert(staff.view_size(q) == 1)

        order2 = Order()
        assert(q.add_order(order2) == 2)
        assert(staff.view_size(q) == 2)

        order3 = Order()
        assert(q.add_order(order3) == 3)
        assert(staff.view_size(q) == 3)

    #4.3: edit log
    #this tests to ensure order progress is updated
    def test_change_status(self):
        q = Queue()

        order1 = Order()
        assert(q.add_order(order1) == 1)

        order2 = Order()
        assert(q.add_order(order2) == 2)

        order3 = Order()
        assert(q.add_order(order3) == 3)

        order = q.get_order(int(1))
        assert(order.status == 'Processing')
        order = q.get_order(int(2))
        assert(order.status == 'Processing')
        order = q.get_order(int(3))
        assert(order.status == 'Processing')

        q.change_status(int(1))
        order = q.get_order(int(1))
        assert(order.status == 'Preparing')

        q.change_status(int(2))
        order = q.get_order(int(2))
        assert(order.status == 'Preparing')

        q.change_status(int(3))
        order = q.get_order(int(3))
        assert(order.status == 'Preparing')
        
        q.change_status(int(1))
        order = q.get_order(int(1))
        assert(order.status == 'Complete')

        q.change_status(int(2))
        order = q.get_order(int(2))
        assert(order.status == 'Complete')

        q.change_status(int(3))
        order = q.get_order(int(3))
        assert(order.status == 'Complete')