#python includes for order

#from inventory import *
#from food import *
from order_error import *
#
#If you can avoid it, dont read this code or you might actually die 
#
#
#
#Attributes:
#items[] - contains dict of key values pairs, where key 
#   is the name plus an identifier e.g "pM-beef patty" (pM= paddy Main) and key is the class instance of the food item
# To print item without identifier, use item[3:]
#status - satus of order 'Processing', 'Preparing', 'Complete'
#Methods:
#
#****add_item(self,inventory,name,quantity,size=None) ****
#- adds a class instance of inv item to order,
#
#****_check_inputs(self, inventory, food, quantity) ****
#- used by add_item to verify inputs are valid
#
#****_get_sides(self, name, food, quantity, size)****
#- copies sides object with given quantity, 
#
#****_get_main(self, name, food, quantity, size)****
# - copies main object with given quantity, 
# - returns dict of size == 1
#****_get_sides(self, name, food, quantity, size)****
#- copies main object with given quantity,
#- returns dict of size ==1
#
#****confirm_order(self, inventory)****
# - decrements values in inventory
#
#****remove_item(self, item, quantity, size = None)****
# - removes item from order, or decrements its quantity
#
#****remove_all(self)**** 
# - removes all items in order
#
#****get_price_total(self)****
# - returns total price of order
#
#****get_price_main(self)****
# - returns price for main
#
#****get_price_sides(self)****
# - returns price computed for all sides and their sizes
#
#****get_price_drinks(self)**** 
# - returns price computed for all drinks in order 
#
#****change_status(self)****
#
#@property
#****status(self) ****
#
#****get_price(self)**** # Dosen't exist
#
#**** __str__(self)****
#

class Order():
    def __init__(self):
        self._items = {}
        self._status = 'Processing'
        self._ID = -1
        self._meal = ''
        self._meal_counter = 0
        self._errors = {}             

    def set_meal(self, meal):
        self._meal = meal
        return 
    
    def is_meal(self):
        self._counter = 1
        return   

    def get_meal(self):
        return self._meal  
    #adds item to order if all fields are valid
    def add_item(self, inventory, name, quantity, size=None):
        quantity = str(quantity)
        if not quantity.isdigit():
            self._errors[name] = 'Invalid quantity given'
            return
        try:
            self._check_inputs(inventory, name, quantity)
        except OrderError as e:
            self._append_error(name, e)
            return False
        else:    
            quantity = int(quantity)
            food_item = inventory.inv[name].get()
            if food_item.type[-4:] == 'main':
                try:
                    food_dict = self._get_main(name, food_item, quantity, size)
                except OrderError as e:
                    self._append_error(name, e)
                    return False
                else:
                    for key, value in food_dict.items():
                        if key in self._items.keys():
                            try:
                                food_temp = inventory.inv[key[3:]].get(value.amount+self._items[key].amount)
                                self._check_food_sub(key, food_temp, inventory)
                                if not self._dict_empty():                                
                                    self._items.pop(key)
                                self._items[key] = food_temp
                            except OrderError as e:
                                self._append_error(name, e)
                                return False
                        else:
                            try: 
                                self._check_food_sub(key, value, inventory)
                                self._items[key] = value
                                
                            except OrderError as e:
                                self._append_error(name, e)
                                return False
            elif food_item.type == 'sides':
                try:
                    food_dict = self._get_sides(name, food_item, quantity, size)
                except OrderError as e:
                    self._append_error(name, e)
                    return False
                else:

                    for key, value in food_dict.items():
                        if key in self._items.keys():

                            try:
                                food_temp = inventory.inv[key[3:]].get(value.amount+self._items[key].amount)
                                self._check_food_sub(key, food_temp, inventory)
                                if not self._dict_empty():
                                    self._items.pop(key)

                                self._items[key] = food_temp
                            except OrderError as e:
                                self._append_error(name, e)
                                return False
                        else:
                            
                            try:
                                self._check_food_sub(key, value, inventory)
                                self._items[key] = value
                            except OrderError as e:
                                self._append_error(name, e)
                                return False
            elif food_item.type == 'drinks':
 
                try:
                    food_dict = self._get_drinks(name, food_item, quantity, size)
                except OrderError as e:
                    self._append_error(name, e)
                    return False
                else:
                    for key, value in food_dict.items():
                        if key in self._items.keys():
                            try:
                                food_temp = inventory.inv[key[3:]].get(value.amount+self._items[key].amount)
                                self._check_food_sub(key, food_temp, inventory)
                                if not self._dict_empty():
                                    self._items.pop(key)
                                self._items[key] = food_temp
                            except OrderError as e:
                                self._append_error(name, e)
                                return False
                        else:
                            try:
                                self._check_food_sub(key, value, inventory)
                                self._items[key] = value
                            except OrderError as e:
                                self._append_error(name, e)
                                return False
        return
        
  
    def type(self):
        return '<Class \'Order\'>'
        
    def items(self):
        return dict(self._items)
    #checks to validate user input, if not valid --> dont add item
    #also checks to see if order is for a burger or wrap
    def _check_inputs(self, inventory, food, quantity):
        quantity = int(quantity)
        if food not in inventory.get_list():
            raise OrderError(food,'Item does not exist in inventory')
        if quantity <= 0:
            raise OrderError(food,'Must input a valid quantity to order')
        bun_counter = 0 # 3
        wrap_counter = 0 # 1
        patty_counter = 0 #2
        food_item = inventory.inv[food].get()
        for item_name in self._items.keys():
            if self._items[item_name].class_type() == 'Buns':
                bun_counter += int(self._items[item_name].amount)
            if self._items[item_name].class_type() == 'Paddies':
                patty_counter += int(self._items[item_name].amount)
            if self._items[item_name].class_type() == 'Wraps':
                wrap_counter += int(self._items[item_name].amount)
        if food_item.class_type() == 'Wraps':
            if quantity + wrap_counter > 1:
                raise OrderError(food, 'Quantity is greater than 1 allowable')
        if food_item.class_type() == 'Buns':
            if quantity + bun_counter > 3:
                raise OrderError(food, 'Quantity is greater than 3 allowable')
        if food_item.class_type() == 'Paddies':
            if quantity + int(patty_counter) > 2:
                raise OrderError(food, 'Quantity is greater than 2 allowable')
        for item_name in self._items.keys():
            if food_item.class_type() == 'Buns' or food_item.class_type() == 'Patties':
                if self._items[item_name].class_type() == 'Wraps':
                    raise OrderError(food,'Order is for a '
                    'gourmet wrap. To make a wrap, remove buns from order')
            elif food_item.class_type() == 'Wraps':
                if self._items[item_name].class_type() == 'Buns':
                    raise OrderError(food,'Order is for a '
                    'gourmet burger. To make a burger, remove wraps from order')
            
        return True
        
    def _get_main(self, name, food, quantity, size):
        temp_dict = {}
        if size != None:
            raise OrderError(name,'Mains do not accept a size')
        else:
            if food.class_type() == "Wraps":
                temp_dict['wM-'+name] = food.get(quantity)
            if food.class_type() == "Paddies":
                if quantity <= 2:
                    temp_dict['pM-'+name] = food.get(quantity) 
                else:
                    raise OrderError(name, 'You can only have a maximum of 2 patties')
            elif food.class_type() == "Buns":
                if quantity <= 3:
                    temp_dict['bM-'+name] = food.get(quantity)
                else:
                    raise OrderError(name, 'You can only have a maximum of 3 buns')
            elif food.class_type() == "Servings":
                temp_dict['sM-'+name] = food.get(quantity)
        return temp_dict
    #private method for copying instance of sides class with a given
    #   quantity
    def _get_sides(self, name, food, quantity, size):
        temp_dict = {}
        if size == None:
            raise OrderError(name,'You must input a size for sides')
        elif size != 'small' and size != 'medium' and size != 'large':
            raise OrderError(name,'Must input valid size for sides')
        else:
            if food.class_type() == "Pieces":
                if size == 'small':
                    temp_dict['sS-'+name] = food.get(quantity*4)
                if size == 'medium':
                    temp_dict['mS-'+name] = food.get(quantity*6)
                if size == 'large':
                    temp_dict['lS-'+name] = food.get(quantity*15)
            elif food.class_type() == "Grams":
                if size == 'small':
                    temp_dict['sS-'+name] = food.get(quantity*75)
                if size == 'medium':
                    temp_dict['mS-'+name] = food.get(quantity*125)
                if size == 'large':
                    temp_dict['lS-'+name] = food.get(quantity*170)
        return temp_dict
   
    #private method for copying instance of drink class with a given
    #   quantity
    def _get_drinks(self, name, food, quantity, size):
        temp_dict = {}  
        if size == None:
            if food.class_type() == "Milliliters_Bottle":
                temp_dict['bD-'+name] = food.get(quantity)
            elif food.class_type() == "Milliliters_Can":
                temp_dict['cD-'+name] = food.get(quantity)
            else:
                raise OrderError(name,'Must specify a size for juice ')
        else:
            if food.class_type() == 'Milliliters':
                if size == 'small':
                    temp_dict['sD-'+name] = food.get(quantity*250)
                elif size == 'medium':
                    temp_dict['mD-'+name] = food.get(quantity*450)
                else:
                    raise OrderError(name,'Must input a valid serving size for juice')
            else:
                raise OrderError(name,'must input a valid size and quantity')
        
        return temp_dict     

    def edit_order(self, inventory, name, quantity, size, order):    # sizes are 'n', 's', 'm', 'l', name is food string
        for item in self._items:
            if item[3:] == name and int(quantity) == 0:
                if item[0] == 's' and size == 's':
                    self._items.pop(item)
                    self._dict_empty()
                    return True   
                if item[0] == 'm' and size == 'm':
                    self._items.pop(item)
                    self._dict_empty()
                    return True
                if item[0] == 'l' and size == 'l':
                    self._items.pop(item)
                    self._dict_empty()
                    return True
                self._items.pop(item)
                self._dict_empty()
                return True
        for item in self._items:
            if item[3:] == name:
                if size == 'n':
                    order.add_item(inventory, name, quantity)
                    errors = order.get_errors()
                    if errors:
                        error = errors[name]
                        self._errors['n-'+name]= error
                        return False
                    else:
                        self._items.pop(item)
                        self._dict_empty()
                        self.add_item(inventory, name, quantity)
                        return True

#adds all instances of food in order ot new order, so when adding a new item, it first checks if the old order can take a
# larger quantity of that order
        for item in self._items: 
            if item[3:] == name:
                if item[0] == 's' and item[0] != size:
                    order.add_item(inventory, name, self._items[item].s(), 'small')
                if item[0] == 'm' and item[0] != size:
                    order.add_item(inventory, name, self._items[item].m(), 'medium')
                if item[0] == 'l' and item[0] != size:
                    order.add_item(inventory, name, self._items[item].l(), 'large')

        for item in self._items:
            if item[3:] == name:
                if item[0] == 's' and size == 's':
                    order.add_item(inventory, name, quantity, 'small')
                    errors = order.get_errors()
                    if len(errors) != 0:
                        error = errors[name]
                        self._errors['s-'+name]= error
                        return False
                    else:
                        self._items.pop(item)
                        self._dict_empty()
                        self.add_item(inventory, name, quantity, 'small')
                        return True
                if item[0] == 'm' and size == 'm':
                    order.add_item(inventory, name, quantity, 'medium')
                    errors = order.get_errors()
                    if len(errors) != 0:
                        error = errors[name]
                        self._errors['m-'+name]=error
                        return False
                    else:
                        self._items.pop(item)
                        self._dict_empty()
                        self.add_item(inventory, name, quantity, 'medium')
                        return True
                if item[0] == 'l' and size == 'l':
                    order.add_item(inventory, name, quantity, 'large')
                    errors = order.get_errors()
                    if len(errors) != 0:
                        error = errors[name]
                        self._errors['l-'+name] = error
                        return False
                    else:
                        self._items.pop(item)
                        self._dict_empty()
                        self.add_item(inventory, name, quantity, 'large')
                        return True
        return False

    def _dict_empty(self):
        if not self._items:
            self._items = {}
            print('dict is empty')
            return True
        return False
    #checks to make sure food quantity is valid when adding item to order
    def _check_food_sub(self, name,  food, inventory):
        quantity = food.amount
        for food_tmp in self._items.keys():    
            if food_tmp[3:] == name[3:] and food_tmp != name:
                quantity += self._items[food_tmp].amount
        food_check = inventory.inv[name[3:]].get()
        if food_check.amount - quantity < 0:
                raise OrderError(name[3:],'Stock is too low to add items to order.'
                    'Current stock level is {}'.format(food_check))
    
    #confirm_order checks inventory and order and subs the inventory only
    #   if the quantity is valid
    def confirm_order(self, inventory):
        inv_list = inventory.get_list()
        for key, value in self._items.items():
            try:
                self._check_food_sub(key, self._items[key], inventory)
            except OrderError as e:
                self._errors[key[3:]] = e.message()
        if self._errors:
            return False
        else:
            for key, value in self._items.items():
                if key[3:] in inv_list:

                    try:
                        inventory.sub(key[3:], value.amount)
                    except ValueError as err:
                        self._errors[key[3:]] = ('Stock is too low to add {} of'
                                          '{}'.format(err.args[1], err.args[2]))

        return True

    def _append_error(self, food, error):
        self._errors[food] = error.message()

    def pop_errors(self):
        tmp = dict(self._errors)
        self.clear_errors()
        return tmp

    def get_errors(self):
        return self._errors

    def is_empty(self):
        if not self._items:
            return True
        return False 

    def get_amount(self, food, size=None): #sizes as 's', 'm', 'l'
        for item in self._items:
            if item[3:] == food:
                if size == None:
                    return self._items[item].amount
                if size == 's' and item[0] == 's': 
                    return self._items[item].s()
                if size == 'm' and item[0] == 'm':
                    return self._items[item].m()
                if size == 'l' and item[0] == 'l':
                    return self._items[item].l()
       
    def get_type(self, item):
        for food in self._items:
            if food[3:] == item:
                return self._items[food].type

    def get_items(self):
        dict_tmp = {}
        for food in self._items:    
            if food[3:] not in dict_tmp:
                dict_tmp[food[3:]] = []
            if food[1] == 'S':
                dict_tmp[food[3:]].append(food[0])
            if (food[1] == 'D') and (food[0] != 'b') and (food[0] != 'c'):
                dict_tmp[food[3:]].append(food[0])

        return dict_tmp
                
             
    #pop item out of dictionary, and add adjusted copy if its quantity >= 0
    def _pop_item(self, key, item, amount, size):
        food_dict = {}
        if item.type[-4:] == 'main':
            food_dict = self._get_main(key, item, amount, size) 
        elif item.type == 'sides':
            food_dict = self._get_sides(key, item, amount, size)
        elif item.type == 'drinks':
            food_dict = self._get_drinks(key, item, amount, size)
        for key_tmp, value_tmp in food_dict.items():
                if amount == int(0):
                    self._items.pop(key_tmp)
                else:
                    self._items.pop(key_tmp)
                    self._items[key_tmp] = value_tmp
                if self._items == None:
                    self._items = {}

    def is_valid(self):
        if len(self.get_errors()) > 0:
            return False
        return True 
    #remove_item function removes item according to input, if valid, removes item from order
    #'skip' method used only when using remove_all
    #remove_item calls _pop_item which duplicates object instance with adjusted quantity
    #   and adds it to self._items after removing the old dict pair, if quantity = 0, remove it completely     
    def remove_item(self, item, quantity, size = None):
        quantity = int(quantity)
        counter = 0 
        for key in list(self._items.keys()):
            if item == key[3:]:
                counter =  1
                if self._items[key].amount < quantity or quantity <= 0:
                    self._items[item]='Quantity must be <= order size'
                    return False
                elif self._items[key].type[-4:] == 'main':
                    if size == None:
                        self._pop_item(key[3:], self._items[key], (self._items[key].amount - quantity), size)  
                        break
                elif self._items[key].type == 'sides':
                    if self._items[key].class_type() == 'Grams':
                        if size == 'small' and key[:2] == 'sS':
                            self._pop_item(key[3:], self._items[key], 
                            (self._items[key].amount - (quantity*75))/75, size)
                            break  
                        elif size == 'medium' and key[:2] == 'mS':
                            self._pop_item(key[3:], self._items[key], 
                            (self._items[key].amount - (quantity*125))/125, size)
                            break      
                        elif size == 'large' and key[:2] == 'lS':                     
                            self._pop_item(key[3:], self._items[key], 
                            (self._items[key].amount - (quantity*170))/170, size)
                            break
                        else:
                            self._errors[item]='Invalid size given'
                    elif self._items[key].class_type() == 'Servings':
                        if size == 'small' and key[:2] == 'sS':
                            self._pop_item(key[3:], self._items[key], 
                            (self._items[key].amount - (quantity*4))/4, size)
                            break  
                        elif size == 'medium' and key[:2] == 'mS':
                            self._pop_item(key[3:], self._items[key], 
                            (self._items[key].amount - (quantity*6))/6, size)
                            break      
                        elif size == 'large' and key[:2] == 'lS':
                            self._pop_item(key[3:], self._items[key], 
                            (self._items[key].amount - (quantity*15))/15, size)
                            break
                        else:
                            self._errors[item] = 'Invalid item size'
                            return False
                elif self._items[key].type == 'drinks':
                    if size == 'small' and key[:2] == 'sD':
                        self._pop_item(key[3:], self._items[key], 
                        (self._items[key].amount - (quantity*250))/250, size)
                        break
                    elif size == 'medium' and key[:2] == 'mS':
                        self._pop_item(key[3:], self._items[key], 
                        (self._items[key].ramount - (quantity*450))/450, size)
                        break  
                    elif size == None:
                        if self._items[key].class_type() == 'Milliliters_Can':
                            self._pop_item(key[3:], self._items[key], 
                            (self._items[key].amount - quantity), size)
                        else:
                            self._pop_item(key[3:], self._items[key], 
                            (self._items[key].amount - quantity), size)

                    else:
                        self._errors[item]= 'Invalid item quantity'
                        return False
        if counter == 0:
            self._errors[item]= 'Item is not in order'
            return False                           
    #removes all items in self.items
    def remove_all(self):
        if self._items == None:
            print('Cannot empty an already empty list')
            return False
        else:
            for key in list(self._items.keys()):
                self._items.pop(key)
                self._dict_empty()
        return True

    #change status of order
    def change_status(self, status):
        self._status = status
        return self._status

    def remove_mains(self):
        for item in list(self._items.keys()):
            t = self._items[item].type
            if ((t == 'burger_main') or (t == 'wrap_main') or (t == 'main') or
                                                         (t == 'paddy_main')):
                self._items.pop(item)
                self._dict_empty()


    # get status of order
    @property
    def status(self):
        return self._status
        
    def get_ID(self):
        return self._ID
        
    def set_ID(self, ID):
        self._ID = ID
    
    def get_price_main(self):
        price = 0
        for key in self._items:
            if self._items[key].type[-4:] == 'main':
                price += self._items[key].price * self._items[key].amount   
        return price


    def get_price_drinks(self):
        price = 0
        for key in self._items:
            if self._items[key].type == 'drinks':
                if self._items[key].class_type() == "Milliliters_Can":
                    price += self._items[key].price * self._items[key].amount
                elif self._items[key].class_type() == "Milliliters_Bottle":
                    price += self._items[key].price * self._items[key].amount
                else: 
                    if key[:2] == 'sD':
                        price += self._items[key].p_s * self._items[key].amount/250
                    if key[:2] == 'mD':
                        price += self._items[key].p_m * self._items[key].amount/450
        return price
        
        
    def get_price_sides(self):
        price = 0
        for key in self._items:
            if self._items[key].class_type() == "Grams":
                if key[:2] == 'sS':
                    price += self._items[key].p_s * self._items[key].amount/75
                if key[:2] == 'mS':
                    price += self._items[key].p_m * self._items[key].amount/125
                if key[:2] == 'lS':
                    price += self._items[key].p_l * self._items[key].amount/170
            elif self._items[key].class_type() == "Pieces":
                if key[:2] == 'sS':
                    price += self._items[key].p_s * self._items[key].amount/4
                if key[:2] == 'mS':
                    price += self._items[key].p_m * self._items[key].amount/6
                if key[:2] == 'lS':
                    price += self._items[key].p_l * self._items[key].amount/15
        return price

    def get_price_total(self):
        price = 0
        if len(self._items) == 0:
            print("Order is empty!")
            return price
        else:
            for key in self._items:
                price += self.get_price_sides()
                price += self.get_price_main()
                price += self.get_price_drinks()
                if self._meal_counter == 1:
                    price -= 2
                return price

    #Should only be accessed by Queue *****
    def cancel_order(self, inv):
        inv_list = inv.get_list()
        for food_item in self._items.keys():
            if food_item[3:] in inv_list:
                inv.add(food_item[3:], self._items[food_item].amount)
        self.remove_all()
        print("Order cancelled")
        return

    def make_meal(self, inv):
        if self._meal == 'Tru-Blu':
            self.add_item(inv, 'beef patty', 1)
            self.add_item(inv, 'cheddar cheese', 1)
            self.add_item(inv, 'lettuce', 1)
            self.add_item(inv, 'avocado', 1)
            self.add_item(inv, 'sesame bun', 2)
            self.add_item(inv, 'tomato sauce', 1)
            self.add_item(inv, 'pineapple', 1)
            self.add_item(inv, 'onion', 1)
        elif self._meal == 'The Leftist':
            self.add_item(inv, 'muffin bun', 1)
            self.add_item(inv, 'vegetarian patty', 1)
            self.add_item(inv, 'lettuce', 1)
            self.add_item(inv, 'tomato sauce', 1)
            self.add_item(inv, 'pineapple', 2)          
        elif self._meal == 'The Rooster':
            self.add_item(inv, 'chicken patty', 1)
            self.add_item(inv, 'swiss cheese', 1)
            self.add_item(inv, 'sesame bun', 2)
            self.add_item(inv, 'onion', 1)
            self.add_item(inv, 'lettuce', 1)
            self.add_item(inv, 'tomato sauce', 1)
        elif self._meal == 'Julius':
            self.add_item(inv, 'chicken wrap', 1)
            self.add_item(inv, 'cheddar cheese', 1)
            self.add_item(inv, 'lettuce', 1)
            self.add_item(inv, 'tomato sauce', 1)
            self.add_item(inv, 'onion', 1)
        elif self._meal == 'The Sheep':
            self.add_item(inv, 'lamb wrap', 1)
            self.add_item(inv, 'swiss cheese', 1)
            self.add_item(inv, 'lettuce', 1)
            self.add_item(inv, 'avocado', 1)
            self.add_item(inv, 'tomato sauce', 1)
            self.add_item(inv, 'pineapple', 1)
            self.add_item(inv, 'onion', 1)
        elif self._meal == 'Cow-Ai':
            self.add_item(inv, 'beef wrap', 1)
            self.add_item(inv, 'cheddar cheese', 1)
            self.add_item(inv, 'lettuce', 1)
            self.add_item(inv, 'avocado', 1)
            self.add_item(inv, 'tomato sauce', 1)
            self.add_item(inv, 'onion', 1)
        return 

    def clear_errors(self):
        if len(self._errors)== 0:
            return False
        self._errors.clear()
        return True
    # returns a list of printed items in format {amount}x size/type item                          
    def __str__(self):
        if not self._items:
            return "Order is empty!"
        s = ''
        counter = 0
        for key in self._items:
            key_split = key.split('-')
            if self._items[key].class_type() == 'Buns' or self._items[key].class_type() == 'Wraps':
                if counter == 0:
                    s+= 'Main:\n'
                s += str(self._items[key]) + ' (' + key_split[1] + ')\n'
                counter = 1
        for key in self._items:
            key_split = key.split('-')
            if self._items[key].class_type() == 'Paddies':
                if counter == 0:
                    s += 'Main:\n'
                s += str(self._items[key]) + ' (' + key_split[1] + ')\n'
        for key in self._items:
            key_split = key.split('-')
            if self._items[key].class_type() == 'Servings':
                if counter == 0:
                    s += 'Main:\n'
                s += str(self._items[key]) + ' of ' + key_split[1] + '\n'
        counter = 0
        for key in self._items:
            key_split = key.split('-')
            if self._items[key].type == 'sides':
                if counter == 0:
                    s += "Sides:\n"
                if key_split[0] == 'sS':
                    s += str(self._items[key].small()) + ' ' + key[3:] + '\n'
                if key_split[0] == 'mS':
                    s += str(self._items[key].med()) + ' ' + key[3:] + '\n'
                if key_split[0] == 'lS':
                    s += str(self._items[key].large()) + ' ' + key[3:] + '\n'
                counter = 1
        counter = 0   
        for key in self._items:
            key_split = key.split('-')
            if self._items[key].type == 'drinks':
                if counter == 0:
                    s += "Drinks:\n"
                if key_split[0] == 'sD':
                    s += str(self._items[key].small()) + ' of ' + key[3:] + '\n'
                if key_split[0] == 'mD':
                    s += str(self._items[key].med()) + ' of ' + key[3:] + '\n'
                if key_split[0] == 'cD':
                    s += str(self._items[key]) + ' of ' + key[3:] + '\n' 
                if key_split[0] == 'bD':
                    s += str(self._items[key]) + ' of ' + key[3:] + '\n'
                counter = 1
        return s

# For general debugging #

'''
kitchen = Inventory(".db")
item_list = kitchen.get_list()
test_order = Order()


test_order.add_item(kitchen, 'beef patty', 2)
test_order.add_item(kitchen, 'mountain dew', 550)
test_order.add_item(kitchen, 'apple juice', 2, 'small')
test_order.add_item(kitchen, 'apple juice', 2, 'medium')
test_order.add_item(kitchen, 'pepsi', 2)
test_order.add_item(kitchen, 'fries', 2, 'large')
test_order.add_item(kitchen, 'fries', 2, 'medium')
#test_order.add_item(kitchen, 'mountain dew', -1)
print(test_order.get_errors())
test_order.clear_errors()
print(test_order.get_errors())
print(test_order)
print(test_order.get_items())


test_order.add_item(kitchen, 'muffin bun', 2)
test_order.add_item(kitchen, 'sesame bun', 1)
test_order.add_item(kitchen, 'mountain dew', 550)
test_order.add_item(kitchen, 'pepsi', 440)
'''
#print(test_order);
#print(test_order.get_price_total());

 
    

