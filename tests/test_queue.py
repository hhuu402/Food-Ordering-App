import sys
import os
sys.path.append('../')
from inventory import Inventory
from food import F_S
from order import Order
import pytest
from queue_file import Queue
from call_error import CallError

class Test_Order():
    def setup_method(self):
        if os.path.exists('.inv_test_dinerdash'):
            os.remove('.inv_test_dinerdash')
        self.inv = Inventory('.inv_test_dinerdash')

    def test_queue_empty(self):
        queue = Queue()
        assert(queue.get_size() == 0)


    def test_add_order(self):
        queue = Queue()
        order1 = Order()
        order2 = Order()
        queue.add_order(order1)
        queue.add_order(order2)
        print(queue.get_size())
        assert(queue.get_size() == 2)
 
    def test_remove_order(self):
        queue = Queue()
        order1 = Order()
        order2 = Order()
        order4 = Order()
        queue.add_order(order1)
        assert(queue.get_size() == 1)
        queue.remove_order(order1)
        assert(queue.get_size() == 0)
        queue.add_order(order2)
        queue.add_order(order1)
        assert(queue.get_size() == 2)
        queue.remove_order(order2)
        queue.remove_order(order1)
        assert(queue.get_size() == 0)

        
        #fail cases

        with pytest.raises(CallError) as e:
            queue.remove_order(order4)




    def test_change_status(self):
        order1 = Order()
        queue = Queue()
        queue.add_order(order1)
        assert(queue.get_status(1) == 'Processing')
        queue.change_status(1)
        assert(queue.get_status(1) == 'Preparing')
        queue.change_status(1)
        assert(queue.get_status(1) == 'Complete')
        with pytest.raises(CallError) as e:
            queue.change_status(-1)
            
	
    def test_view_current_orders(self):
        order1 = Order()
        q = Queue()
        assert(q.view_current_orders() == False)
        order2 = Order()
        order3 = Order()
        order4 = Order()
        q.add_order(order1)
        q.add_order(order2)
        q.add_order(order3)
        q.add_order(order4)
        assert(q.view_current_orders() != False)
        #please add to this: I don't have updated version

    def test_get_order_history(self):
        order1 = Order()
        q = Queue()
        assert(q.view_completed_orders() == False)
        q.add_order(order1)
        q.change_status(1)
        q.change_status(1)
    
        assert(q.view_completed_orders() != False)

