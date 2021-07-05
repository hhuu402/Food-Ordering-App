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

#TEST FOR USERSTORIES 3

class Test_US3():

    def setup_method(self):
        ...
   
    #3.1: Check Order
    #this checks for the associated order when given an order id
    def test_order_bad_id(self):
        q = Queue()
        assert(q.get_order(int(1)) == False)
        assert(q.get_order(int(3)) == False)

    def test_orders_real_id(self):
        q = Queue()
        order1 = Order()
        assert(q.add_order(order1) == 1)

        order2 = Order()
        assert(q.add_order(order2) == 2)

        order3 = Order()
        assert(q.add_order(order3) == 3)

    def test_removed_orders_real_id(self):
        q = Queue()
        order1 = Order()
        assert(q.add_order(order1) == 1)

        order2 = Order()
        assert(q.add_order(order2) == 2)

        order3 = Order()
        assert(q.add_order(order3) == 3)

        assert(q.remove_order(order1) == True)
        assert(q.remove_order(order2) == True)
        assert(q.remove_order(order3) == True)

    def test_get_initial_status(self):
        q = Queue()

        order1 = Order()
        assert(q.add_order(order1) == 1)

        order2 = Order()
        assert(q.add_order(order2) == 2)

        order3 = Order()
        assert(q.add_order(order3) == 3)

        assert(order1.status == 'Processing')
        assert(order2.status == 'Processing')
        assert(order3.status == 'Processing')

    def test_get_updated_status(self):
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