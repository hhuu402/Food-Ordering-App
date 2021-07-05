import sys
import os
sys.path.append('../')
from inventory import Inventory
from food import F_S
from order import *
import pytest
class Test_Order():
    def setup_method(self):
        if os.path.exists('.inv_test_dinerdash'):
            os.remove('.inv_test_dinerdash')
        self.inv = Inventory('.inv_test_dinerdash')
        for x in self.inv.get_list():
            self.inv.add(x, 500)

    #As a customer I would like to be able to customise my burger/wrap
    #so I can eat a meal which suits my tastes
    def test1_1(self):
        order = Order()        

        order.add_item(self.inv, 'onion', 1)
        order.add_item(self.inv, 'lettuce', 1)
        order.add_item(self.inv, 'beef patty', 1)
        order.add_item(self.inv, 'muffin bun', 1) 
        assert(len(order.items()) == 4) 
        order.add_item(self.inv, 'beef wrap', 1)
        assert(len(order.get_errors()) == 1)
        assert(len(order.items()) == 4)

    #As a customer I would like to order sides in sizes 's','m','l'
    def test1_2(self):
        order = Order()        
 
        order.add_item(self.inv, 'fries', 1, 'small')
        order.add_item(self.inv, 'fries', 1, 'medium')
        order.add_item(self.inv, 'fries', 1, 'large')

        assert(len(order.get_items())== 1)
        order.add_item(self.inv, 'fries', 500, 'large')
        order.add_item(self.inv, 'fries', 500, 'medium')
        order.add_item(self.inv, 'fries', 500, 'small')
        assert(len(order.get_errors())== 1)
     
    #As a customer I would like to order drinks, either in cans, bottles or 
    # as sizes 'small' 'medium'  
    def test1_3(self):
        order = Order()        
        order.add_item(self.inv, 'pepsi', 1)
        order.add_item(self.inv, 'mountain dew', 1)
        order.add_item(self.inv, 'orange juice', 1, 'small')
        order.add_item(self.inv, 'apple juice', 1, 'medium')
        order.add_item(self.inv, 'orange juice', 1, 'large')
        assert(len(order.get_items())== 4)
        order.add_item(self.inv, 'apple juice', 500, 'medium')
        order.add_item(self.inv, 'pepsi', 500, 'medium')
        order.add_item(self.inv, 'mountain dew', 500)
        assert(len(order.get_errors())== 3)
    

