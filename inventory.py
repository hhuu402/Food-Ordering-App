#== Python Libraries ==#
from food import *
import pickle   # Because we need pickles in our restaurant
#==== Library Header ====================================================
# Constructor << "f_name" >> - Reads & Writes inv from f_name(string)
#
# Part of Food.py
# self.inv["item"] - prints size + identifier e.g. "3 pc", "5x 900ml"
#              - See Possible Servings for more in Food Class
# self.inv["item"].amount - alias to get_stock() | DON'T modify object
# self.inv["item"].type - alias to get_type() | DON'T modify this
# self.inv["item"].get(num) - copies class with num item, 
#                           - if num not specified, copies exact class.
# for prices, see food.py
#
# Part of Class
# self.size - return the amount of unique items inside this inventory
# set(str item,int qty) - sets X from inv    | only   positives
# add(str item,int qty) - adds X from inv    | allows negatives 
# sub(str item,int qty) - subs X from inv    | allows negatives
# bool delete_item(str item) - dels X from inv | return (if work) ? 1 : 0
# add_item(str Name, Food class) | return False if item already in inv
# get_list() - returns list of all food items
# get_type() - returns type of food ("main", "sides", "drinks")
# get_stock(item) - returns # of items in stock or false if not found
# [IMPORTANT] free() - Saves inventory into file and closes file
# __str__ - Prints list in table format from in type then lexicon order.
#==== Function throws =================================================== 
# ValueError    | if item stock falls below zero
#   add_inventory
#   sub_inventory
#   set_inventory    
#========================================================================
    ### [Instance Creation] ###
# (default) Use Inventory(".db") when initialising an Inventory class.
class Inventory:
    ## [Inventory Properties] ##
    @property
    def size(self):
        return len(self.inv)
    ## [Constructor] ##
    def __init__(self, f_name):
        try:
            self._f_name = f_name
            self._inv_file = open(f_name, mode='rb')
            self.inv = pickle.load(self._inv_file) 
          #  if type(self.inv) is not list:
          #      print("Not List");
          #      raise IOError
        except IOError:
            print("[warning] Could not find file {}".format(f_name))
            print("[warning] Creating file {}...".format(f_name))
            print("[warning] Using factory settings..")
            self.inv = {
                "avocado": F_S(1, 50),
                "bacon": F_S(2, 50),
                "beetroot": F_S(0.5, 50),
                "barbeque sauce": F_S(0.5, 50),
                "beef patty": F_P(8, 50),
                "cheddar cheese": F_S(0.5, 50),
                "chicken patty": F_P(7, 50),
                "chicken wrap": F_W(7, 50),
                "lamb wrap": F_W(9, 50),
                "beef wrap": F_W(8, 50),
                "lettuce": F_S(0.5, 50),
                "pineapple": F_S(1, 50),
                "muffin bun": F_B(2, 50),
                "sesame bun": F_B(3, 50),
                "swiss cheese": F_S(0.5, 50),
                "tomato sauce": F_S(0.5, 50),
                "vegetarian patty": F_P(6, 50), 
                "fries": F_G(2.5,3.5,4, 5000),
                "chicken nuggets": F_Pc(2,2.5,4, 50),
                "apple juice": F_Ml(2,3, 5000),
                "mountain dew": F_Ml_B(3, 50),
                "onion": F_S(0.5, 50),
                "orange juice": F_Ml(2,3, 5000),
                "pepsi": F_Ml_C(2, 50),
                "sundae": F_Ml(2,3, 5000),
            }
            try:
                self._inv_file = open(f_name, mode='wb')
            except IOError:
                print("[Error] File Creation Failed. No files created")
            else:
                pickle.dump(self.inv,self._inv_file)
                self._inv_file.close()
                self._inv_file = open(f_name, mode='r+b')
    ## [Methods] ##
    def add(self, item, quantity):
        if self.inv[item].amount + quantity < 0:
            err = 'Quantity passed made stock negative!'
            raise ValueError(err, item, quantity, self.inv[item].amount)
        else:
            self.inv[item].add(quantity)
            self._inv_file.close()
            self._inv_file = open(self._f_name, mode='wb')
            pickle.dump(self.inv,self._inv_file)
            self._inv_file.close()
            self._inv_file = open(self._f_name, mode='r+b')       
    def sub(self, item, quantity):
        if self.inv[item].amount - quantity < 0:
            err = 'Quantity passed made stock negative!'
            raise ValueError(err, item, quantity, self.inv[item].amount)
        else:
            self.inv[item].add(-quantity)
    def set(self, item, quantity): # needs testing to see if new
        if quantity < 0:
            err = 'Quantity passed made stock negative!'
            raise ValueError(err, item, quantity, self.inv[item].amount)
        self.inv[item].set(quantity)
        self._inv_file.close()
        self._inv_file = open(self._f_name, mode='wb')        
        pickle.dump(self.inv,self._inv_file)
        self._inv_file.close()
        self._inv_file = open(self._f_name, mode='r+b')
    def delete_item(self, item):
        try:
            del self.inv[item]
        except KeyError:
            return False
        return True
    def add_item(self, name,item):
        if name in self.inv:
            return False
        self.inv[name] = item
    def get_list(self):
        list = []
        for key in self.inv:
            list.append(key)
        return list
    def get_stock(self, item):
        if (item in self.inv):
            return self.inv[item].amount
        return False
    def get_type(self, item):
        return self.inv[item]
    def free(self):
        try:
            self._inv_file.close()
            self._inv_file = open(self._f_name, mode='wb')        
            pickle.dump(self.inv,self._inv_file)
            self._inv_file.close()
        except pickle.PickleError:
            print("Cannot save file if class has not been initalised!")
        except IOError:
            print("Cannot close file if file has not been initailised!")

    def __str__(self):
        l0 = [] #master
        l1 = [] #main
        l1_b = [] #main_burger
        l1_w = [] #main_wrap
        l2 = [] #sides
        l3 = [] #drinks
        s = ""
        for i in self.inv:
            if self.inv[i].type == "main":
                l1.append([i, self.inv[i].__str__(), self.inv[i].type])
            elif self.inv[i].type == "burger_main":
                l1_b.append([i, self.inv[i].__str__(), self.inv[i].type])
            elif self.inv[i].type == "wrap_main":
                l1_w.append([i, self.inv[i].__str__(), self.inv[i].type])
            elif self.inv[i].type == "sides":
                l2.append([i, self.inv[i].__str__(), self.inv[i].type])
            elif self.inv[i].type == "drinks":
                l3.append([i, self.inv[i].__str__(), self.inv[i].type])
        l1.sort(key=lambda l:l[0])
        l1_w.sort(key=lambda l:l[0])
        l1_b.sort(key=lambda l:l[0])
        l2.sort(key=lambda l:l[0])
        l3.sort(key=lambda l:l[0])
        l0 = l1_b + l1_w + l1 + l2 + l3
        l1 = []
        l2 = []
        l3 = []
        for i in range(len(l0)):
         #   print("{}".format(l0[i][0]))
            if self.inv[l0[i][0]].amount == 0:
                l0[i][1] = l0[i][1] + " [EMPTY]"  
                print("{}".format( l0[i][1]))
            elif self.inv[l0[i][0]].amount <= 20:
                l0[i][1] = l0[i][1] + " [LOW]"
                l0[i][0] = "!! " +l0[i][0] + " !!"  
            elif self.inv[l0[i][0]].class_type() == 'Milliliters' and self.inv[l0[i][0]].amount <= 500:
                l0[i][1] = l0[i][1] + " [LOW]" 
                l0[i][0] = "!! " +l0[i][0] + " !!"   
            elif self.inv[l0[i][0]].class_type() == 'Grams' and self.inv[l0[i][0]].amount <= 500:
                l0[i][1] = l0[i][1] + " [LOW]"
                l0[i][0] = "!! " +l0[i][0] + " !!"  
        for i in range(len(l0)):
            l1.append(l0[i][0])
            l2.append(l0[i][1])
            l3.append(l0[i][2])     
        le1 = max(len(max(l1, key=len)), 4)+2
        le2 = max(len(max(l2, key=len)),3)+2
        le3 = max(len(max(l3, key=len)),4)+2
        s += "+{:-^{a}}+{:-^{b}}+{:-^{c}}+\n".format("","","",
                                                     a=le1,b=le2,c=le3)
        s += "|{:^{a}}|{:^{b}}|{:^{c}}|\n".format("Name","Qty","Type",
                                                  a=le1,b=le2,c=le3)
        s +="+{:-^{a}}+{:-^{b}}+{:-^{c}}+\n".format("","","",
                                                    a=le1,b=le2,c=le3)
        for i in range(len(l1)):
            s += "|{:<{a}}|{:<{b}}|{:<{c}}|\n".format(l1[i],l2[i],l3[i], 
                                                      a=le1,b=le2,c=le3)
        s +="+{:-^{a}}+{:-^{b}}+{:-^{c}}+\n".format("","","",
                                                    a=le1,b=le2,c=le3)
        return s


