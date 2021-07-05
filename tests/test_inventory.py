import sys
import os
sys.path.append('../')
from inventory import Inventory
from food import F_S
class Test_Inventory():
    def setup_method(self):
        if os.path.exists('.inv_test_dinerdash'):
            os.remove('.inv_test_dinerdash')
        self.inv = Inventory('.inv_test_dinerdash')
    #  No need to test self[item].amount & self[item].amount & self[Item]
    #  Since they are calling functions from the Food Class      
    #  Which has been tested already in test_food.py


    ## Test Case
    # delete known item         1.1  | X
    # delete non-existant item  1.2  | X
    # add non-existant item     1.3  | X
    # add known item            1.4  | X
    # get list                  1.5  | X
    # get size                  1.6  | X
    # get price                 1.7  | X

    def test_list_delete_add_size_price(self):
        list = self.inv.get_list()
        assert(self.inv.size > 0)
        # If all items are deleted, then we know 1.1 and 1.5 works
        for i in list:
            print(i)
            self.inv.delete_item(i)
        assert(self.inv.size == 0)
        # testing 1.2
        assert(self.inv.delete_item("eofkeofke") == False)

        # testing 1.3
        self.inv.add_item("Apples", F_S(1))
        assert(self.inv.inv["Apples"].amount == 0)
        self.inv.add_item("Banana", F_S(1))
        self.inv.add_item("Oranges", F_S(1))

        # testing 1.4
        assert(self.inv.add_item("Apples", F_S(1)) == False)

        # testing 1.7
        assert(self.inv.inv["Apples"].price == 1)

        # testing 1.6 (tested lines 26,32 as well)
        assert(self.inv.size == 3)
        self.inv.free()
    ## Test cases
    # adding number                 2.1 | X
    # subtracting number            2.2 | X
    # adding to make item < 0       2.3 | X (Should give ValueError)
    # subtacting to make item < 0   2.4 | X (Should give ValueError)
    # setting > 0                   2.5 | X
    # setting < 0                   2.6 | X (Should give ValueError)
    # get_stock                     2.7 | X
    def test_add_sub_set_stock(self):
        # testing 2.6
        self.inv.add_item("Apples", F_S(1))
        self.inv.set("Apples", 1)
        assert(self.inv.get_stock("Apples") == 1)
        # testing 2.1
        self.inv.add("Apples", 10)
        assert(self.inv.get_stock("Apples") == 11)
        # testing 2.2
        self.inv.sub("Apples", 5)
        assert(self.inv.get_stock("Apples") == 6)
        # testing 2.3
        try:
            self.inv.add("Apples", -10)
        except ValueError:
            assert(self.inv.get_stock("Apples") == 6)
        else:
            assert(False)
        # testing 2.4
        try:
            self.inv.sub("Apples", 10)
        except ValueError:
            assert(self.inv.get_stock("Apples") == 6)
        else:
            assert(False) 
          # testing 2.5
        try:
            self.inv.set("Apples", -10)
        except ValueError:
            assert(self.inv.get_stock("Apples") == 6)
        else:
            assert(False)
        self.inv.free()     
    
    # testing free
    def test_free(self):
        self.inv.add_item("Apples", F_S(1))
        self.inv.free()
        self.inv = Inventory('.inv_test_dinerdash')
        assert("Apples" in self.inv.inv)
        self.inv.free()



