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

    def test_order_is_empty(self):
        list = self.inv.get_list()
        assert(self.inv.size > 0)
        
        print(list)
        order = Order()
        assert(str(order) == 'Order is empty!')


    def test_order_add_valid_wrap(self):
        for x in self.inv.get_list():
            self.inv.add(x, 500)
        order = Order()
        order.add_item(self.inv, 'chicken wrap', 1)
        order.add_item(self.inv, 'tomato sauce', 3)
        items = order.items()
        items_list = [] 
        for key in items.keys():
            items_list.append(key[3:])
        assert('chicken wrap' in items_list)
        assert('tomato sauce' in items_list)
 
        assert(len(order.items()) == 2)
        
    def test_order_add_valid_burger(self):	
        for x in self.inv.get_list():
            self.inv.add(x, 500)
        order = Order()
        order.add_item(self.inv, 'chicken patty', 1)
        order.add_item(self.inv, 'muffin bun', 2)
        assert(len(order.items()) == 2)
        items = order.items()
        items_list = [] 
        for key in items.keys():
            items_list.append(key[3:])
        assert('chicken patty' in items_list)
        assert('muffin bun' in items_list)
      
    def test_order_add_valid_sides(self):	
        for x in self.inv.get_list():
            self.inv.add(x, 500)
        order = Order()

        order.add_item(self.inv, 'chicken nuggets', 1, 'large')
        order.add_item(self.inv, 'fries', 2, 'small')
        assert(len(order.items()) == 2)
        items = order.items()
        items_list = [] 
        for key in items.keys():
            items_list.append(key[3:])
        assert('chicken nuggets' in items_list)
        assert('fries' in items_list)
        
    def test_order_add_valid_drinks(self):	
        for x in self.inv.get_list():
            self.inv.add(x, 500)
        order = Order()

        order.add_item(self.inv, 'pepsi', 2)
        order.add_item(self.inv, 'mountain dew', 2)
        order.add_item(self.inv, 'apple juice', 1, 'small')
        assert(len(order.items()) == 3)
        items = order.items()
        items_list = [] 
        for key in items.keys():
            items_list.append(key[3:])
        assert('pepsi' in items_list)
        assert('apple juice' in items_list)
        assert('mountain dew' in items_list)
        
    def test_order_add_invalid_item(self):	
        for x in self.inv.get_list():
            self.inv.add(x, 500)
        order = Order()
        order.add_item(self.inv, 'bepis', 3)
        order.add_item(self.inv, 'conk', 2)
 
        assert(len(order.items()) == 0)
        
    def test_order_add_invalid_size_type(self):	
        for x in self.inv.get_list():
            self.inv.add(x, 500)
        order = Order()

        order.add_item(self.inv, 'pepsi', 2, 'small')
        order.add_item(self.inv, 'mountain dew', 2, 'large')
        #order.add_item(self.inv, 'apple juice', 1, 'large')
        order.add_item(self.inv, 'fries', 1, 'very large')
        order.add_item(self.inv, 'fries', 1)
        print(self.inv)
        print(order)
        assert(len(order.items()) == 0)
        
    def test_order_add_item_low_stock(self):	
        for x in self.inv.get_list():
            self.inv.add(x, 400)
        order = Order()
        print(self.inv)
        order.add_item(self.inv, 'pepsi', 550)
        order.add_item(self.inv, 'mountain dew', 550)
        assert(len(order.items()) == 0)      
 
    def test_order_add_invalid_item_amount(self):	
        for x in self.inv.get_list():
            self.inv.add(x, 400)
        order = Order()
        print(self.inv)
        order.add_item(self.inv, 'mountain dew', -1)
        order.add_item(self.inv, 'apple juice', -1, 'large')
        order. add_item(self.inv, 'chicken nuggets', -5, 'small')
        assert(len(order.items()) == 0)   

    def test_order_remove_all(self):
        for x in self.inv.get_list():
            self.inv.add(x, 400)
        order = Order()
        order.add_item(self.inv, 'cheddar cheese', 2)
        order.add_item(self.inv, 'beef patty', 2)
        order.add_item(self.inv, 'pepsi', 2)
        order.add_item(self.inv, 'fries', 2, 'small')
        order.add_item(self.inv, 'apple juice', 2, 'small')
        order.remove_all()
        assert(len(order.items()) == False) 

        
    def test_order_price_main(self):	
        for x in self.inv.get_list():
            self.inv.add(x, 400)
        price = 0
        order = Order()
        order.add_item(self.inv, 'cheddar cheese', 5)
        price += self.inv.inv['cheddar cheese'].get().price*5
        assert(order.get_price_total() == price)
        order.add_item(self.inv, 'sesame bun' ,2)
        price += self.inv.inv['sesame bun'].get().price*2
        assert(order.get_price_total() == price)
        order.add_item(self.inv, 'beef patty', 2)
        price += self.inv.inv['beef patty'].get().price*2     
        assert(order.get_price_total() == price) 
    
    def test_order_price_sides(self):	
        for x in self.inv.get_list():
            self.inv.add(x, 400)
        price = 0
        order = Order()
        order.add_item(self.inv, 'fries', 1, 'small')
        price += self.inv.inv['fries'].get().p_s*1
        assert(order.get_price_total() == price)
        order.add_item(self.inv, 'fries', 1, 'medium')
        price += self.inv.inv['fries'].get().p_m*1
        assert(order.get_price_total() == price)
        order.add_item(self.inv, 'fries', 1, 'large')
        price += self.inv.inv['fries'].get().p_l*1
        assert(order.get_price_total() == price)
        
        order.add_item(self.inv, 'chicken nuggets', 1, 'small')
        price += self.inv.inv['chicken nuggets'].get().p_s*1
        assert(order.get_price_total() == price)
        order.add_item(self.inv, 'chicken nuggets', 1, 'medium')
        price += self.inv.inv['chicken nuggets'].get().p_m*1
        assert(order.get_price_total() == price)
        order.add_item(self.inv, 'chicken nuggets', 1, 'large')
        price += self.inv.inv['chicken nuggets'].get().p_l*1
        assert(order.get_price_total() == price)
        
     
    def test_order_price_sides(self):	
        for x in self.inv.get_list():
            self.inv.add(x, 400)
        price = 0
        order = Order()
        order.add_item(self.inv, 'pepsi', 1)
        price += self.inv.inv['pepsi'].get().price*1
        assert(order.get_price_total() == price)
        order.add_item(self.inv, 'mountain dew', 1)
        price += self.inv.inv['mountain dew'].get().price*1
        assert(order.get_price_total() == price)
        order.add_item(self.inv, 'apple juice', 1, 'small')
        price += self.inv.inv['apple juice'].get().p_s*1
        assert(order.get_price_total() == price)
        order.add_item(self.inv, 'apple juice', 1, 'medium')
        price += self.inv.inv['apple juice'].get().p_m*1
        assert(order.get_price_total() == price)
        
    def test_remove_valid_item_partially(self):
        for x in self.inv.get_list():
            self.inv.add(x, 400)
        order = Order()    
        order.add_item(self.inv, 'apple juice', 2, 'small')
        order.remove_item('apple juice', 1, 'small')
        order.add_item(self.inv, 'beef patty', 2)
        order.remove_item('beef patty', 1)
        order.add_item(self.inv, 'fries', 2, 'large')
        order.remove_item('fries', 1, 'large')
        order.add_item(self.inv, 'pepsi', 2)
        order.remove_item('pepsi', 1)
        order.add_item(self.inv, 'mountain dew', 2)
        order.remove_item('mountain dew', 1)
        order.add_item(self.inv, 'lettuce', 2)
        order.remove_item('lettuce', 1)
        for key, value in order.items().items():
            if key[3:] == 'apple juice':
                assert(value.amount == 250)
            elif key[3:] == 'beef patty':
                assert(value.amount == 1)
            elif key[3:] == 'fries':
                assert(value.amount == 170)
            elif key[3:] == 'pepsi':
                assert(value.amount == 1)
            elif key[3:] == 'mountain dew':
                assert(value.amount == 1)
            elif key[3:] == 'lettuce':
                assert(value.amount == 1)
        
        assert(len(order.items())== 6)
        
    def test_remove_valid_item_completely(self):
        for x in self.inv.get_list():
            self.inv.add(x, 400)
        order = Order()    
        order.add_item(self.inv, 'apple juice', 1, 'small')
        order.remove_item('apple juice', 1, 'small')
        order.add_item(self.inv, 'beef patty', 1)
        order.remove_item('beef patty', 1)
        order.add_item(self.inv, 'fries', 1, 'large')
        order.remove_item('fries', 1, 'large')
        order.add_item(self.inv, 'pepsi', 2)
        order.remove_item('pepsi', 2)
        order.add_item(self.inv, 'mountain dew', 2)
        order.remove_item('mountain dew', 2)
        order.add_item(self.inv, 'lettuce', 1)
        order.remove_item('lettuce', 1)
        assert(len(order.items()) == 0)

       
    def test_remove_invalid_item(self):
        for x in self.inv.get_list():
            self.inv.add(x, 400)
        order = Order()    
        order.add_item(self.inv, 'apple juice', 1, 'small')
        order.add_item(self.inv, 'beef patty', 1)
        order.add_item(self.inv, 'fries', 1, 'large')
        order.add_item(self.inv, 'pepsi', 2)
        order.add_item(self.inv, 'mountain dew', 2)
        order.add_item(self.inv, 'lettuce', 1)

        order.remove_item('apple juicey', 1, 'small')
        order.remove_item('beef patties', 1)
        order.remove_item('fries!', 1, 'large')
        order.remove_item('bepis', 2)
        order.remove_item('mountain dews', 2)
        order.remove_item('lettuces :)', 1)
        assert(len(order.get_errors()) == 6)
        assert(len(order.items())==  6)       



'''       
    def test_order_add_invalid_amount(self):	
        for x in self.inv.get_list():
            item = self.inv.inv[x].get()
            print('-----')
            print(x)
            print(item)
            if item.class_type() == 'Grams':
                print(item.p_l)
                print(item.p_m)
                print(item.p_s)
            elif item.class_type() == "Milliliters":
                print(item.p_m)
                print(item.p_s)
            elif item.class_type() == 'Pieces':
                print(item.p_l)
                print(item.p_m)
                print(item.p_s)
            else:
                print(item.price)
            print('-----\n') 
        assert(False)
'''
       
