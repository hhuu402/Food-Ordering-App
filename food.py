#== Python Libraries ==#
from abc import ABC, abstractmethod # So we can count the alphabet
#==== Food Class (ABSTRACT) =============================================
# CONSTRUCTOR << amount=0, item_type=DEFAULT_TYPE, size=DEFAULT_SIZE >>
# self.amount - amount of the item currently in stock
# self.sizes -  returns the # of sizes item holds. e.g. 2 for small,med
# self.type   - Categorised as ["main", "sides", "drinks"]
# self.price  - prints out _price, note: pcs, grams, ml have their own
# self.price = {} | throws ValueError if {} < 0, also note: ^
# self.class_type()- returns class name in string, basically str after #                    Food_ e.g. Pieces, Servings, Milliliters_Bottle
# set(num)    - sets amount of item | NO ERROR CHECKING
# add(num)    - adds num to item    | NO ERROR CHECKING
# __str__ = prints size + identifier e.g. "3 pc", "5x 900ml" 
#==== ABSTRACT TYPES ====================================================
# Class  | Class Full Name         |  __STR__              | DEFAULT_TYPE
#--------+-------------------------+-----------------------+-------------
# F_Pc   | Food_Pieces             |  "{}x pc/s"           | "sides"
# F_S    | Food_Servings           |  "{}x serving/s"      | "main"
# F_Ml_B | Food_Milliliters_Bottle |  "{}x bottle/s"       | "drinks"
# F_Ml_C | Food_Milliliters_Can    |  "{}x canned drink/s" | "drinks"
# F_Ml   | Food_Milliliters        |  "{}x ml/s"           | "drinks"
# F_B    | Food_Buns               |  "{}x bun/s"          | "burger_main"
# F_P    | Food_Paddies            |  "{}x padd[y/ies]"    | "burger_main"
# F_G    | Food_Grams              |  "{}x gram/s          | "sides"
# F_W    | Food_Wraps              |  "{}x wrap/s          | "wrap_main"
#==== Additional Functions ==============================================
# F_Ml   
#   small(): returns "{}x 250ml"  | {} = self._amount / 250
#   med(): returns "{}x 450ml"    | {} = self._amount / 450
#   self.p_s: returns _price of 1 small drink
#   self.p_m: returns _price of 1 med drink
# F_G  
#   small(): returns "{}x small"  | {} = self._amount / 75
#   med(): returns "{}x medium"   | {} = self._amount / 125
#   large(): returns "{}x large"  | {} = self._amount / 170
#   self.p_s: returns _price of 1 small size
#   self.p_m: returns _price of 1 med size
#   self.p_l: returns _price of 1 large size
# F_Pc
#   small(): returns "{} 4x"      | {} = self._amount / 4
#   med(): returns "{} 6x"        | {} = self._amount / 6
#   large() returns "{} 10x"      | {} = self._amount / 10
#   self.p_s: returns _price of 1 small pc size (4x)
#   self.p_m: returns _price of 1 med pc size (6x)
#   self.p_l: returns _price of 1 lrg pc size (15x)
#========================================================================
class Food(ABC):
    @abstractmethod
    def __init__(self, price, amount, item_type, sizes=1):
        self._price = price
        self._amount = amount
        self._type = item_type
        self.sizes = sizes
    def add(self, num):
        self._amount += num
    def set(self, num):
        self._amount = num
    @abstractmethod
    def class_type(self):
        pass
    @property
    def type(self):
        return self._type
    @property
    def amount(self):
        return self._amount
    @property
    def price(self):
        return self._price
    @price.setter
    def price(self, cost):
        if cost <= 0:
            raise ValueError("_price negative or 0!")
            self._price = 999999 # prevents accidents
        else:
            self._price = cost
    @property
    def sizes(self):
        return self._sizes
    @sizes.setter
    def sizes(self, size):
        if size <= 0:
            raise ValueError("ValueError", "There can't be < 1 size!")
        else:
            self._sizes = size

class F_Pc(Food):     #Pcs
    def __init__(self, p_s, p_m, p_l,amount=0,item_type="sides",sizes=3):
        self._p_s = p_s
        self._p_m = p_m
        self._p_l = p_l
        self._amount = amount
        self._type = item_type
        self.sizes = sizes
    def get(self, num=None):
        if num is None:
            num = self._amount 
        return F_Pc(self._p_s,self._p_m,self._p_l,num, self._type)
    def __str__(self):
        if self._amount == 1:
            return "{}x pc".format(self._amount)
        else:
            return "{}x pcs".format(self._amount)
    def small(self):
        return "{} 4x".format(int(self._amount / 4))
    def med(self):
        return "{} 6x".format(int(self._amount / 6))
    def large(self):
        return "{} 15x".format(int(self._amount / 15))

#Andre ....
    def s(self):
        return int(self._amount/4)
    def m(self):
        return int(self._amount/6)
    def l(self):
        return int(self._amount/15)

    def class_type(self):
        return "Pieces"
    @property       ### These must be defined first before setters
    def p_s(self):  ### can be used....
        return self._p_s
    @property
    def p_m(self):
        return self._p_m
    @property
    def p_l(self):
        return self._p_l

# ANdre........
    def get_price(self, size):
        if size == 'small':
            return self._p_s
        if size == 'medium':
            return self.p_m
        if size == 'large':
            return self.p_l

    @p_s.setter
    def p_s(self, cost):
        if cost <= 0:
            raise ValueError("_price negative or 0!")
            self._p_s = 99999 #prevents accidents
        else:
            self._p_s = cost
    @p_m.setter
    def p_m(self, cost):
        if cost <= 0:
            raise ValueError("_price negative or 0!")
            self._p_m = 99999 #prevents accidents
        else:
            self._p_m = cost
    @p_l.setter
    def p_l(self, cost):
        if cost <= 0:
            raise ValueError("_price negative or 0!")
            self._p_l = 99999 #prevents accidents
        else:
            self._p_l = cost

class F_S(Food):   #Servings
    def __init__(self, price, amount=0, item_type="main", sizes=1):
        super().__init__(price, amount, item_type, sizes)
    def get(self, num=None):
        if num is None:
            num = self._amount 
        return F_S(self._price,num, self._type)
    def class_type(self):
        return "Servings"
    def __str__(self):
        if self._amount == 1:
            return "{}x serving".format(self._amount)
        else:
            return "{}x servings".format(self._amount)
class F_G(Food):     #Grams (small/med/large)
    def __init__(self, p_s,p_m,p_l, amount=0, item_type="sides",sizes=3):
        self._p_s = p_s
        self._p_m = p_m
        self._p_l = p_l
        self._amount = amount
        self._type = item_type
        self.sizes = sizes
    def get(self, num=None):
        if num is None:
            num = self._amount 
        return F_G(self._p_s,self._p_m,self._p_l,num, self._type)
    def class_type(self):
        return "Grams"
    def __str__(self):
        if self._amount == 1:
            return "{}x gram".format(self._amount)
        else:
            return "{}x grams".format(self._amount)
    def small(self):
        return "{}x small".format(int(self._amount / 75))
    def med(self):
        return "{}x medium".format(int(self._amount / 125))
    def large(self):
        return "{}x large".format(int(self._amount / 170))
# Andre
    def s(self):
        return int(self._amount / 75)
    def m(self):
        return int(self._amount / 125)
    def l(self):
        return int(self._amount / 170)


# added this to make coding easier... Andre
    def get_price(self, size):
        if size == 'small':
            return self._p_s
        if size == 'medium':
            return self.p_m
        if size == 'large':
            return self.p_l

    @property       ### These must be defined first before setters
    def p_s(self):  ### can be used....
        return self._p_s
    @property
    def p_m(self):
        return self._p_m
    @property
    def p_l(self):
        return self._p_l

    @p_s.setter
    def p_s(self, cost):
        if cost <= 0:
            raise ValueError("_price negative or 0!")
            self._p_s = 99999 #prevents accidents
        else:
            self._p_s = cost
    @p_m.setter
    def p_m(self, cost):
        if cost <= 0:
            raise ValueError("_price negative or 0!")
            self._p_m = 99999 #prevents accidents
        else:
            self._p_m = cost
    @p_l.setter
    def p_l(self, cost):
        if cost <= 0:
            raise ValueError("_price negative or 0!")
            self._p_l = 99999 #prevents accidents
        else:
            self._p_l = cost

class F_Ml_B(Food):   #Bottled Drinks (600ml)
    def __init__(self, price, amount=0, item_type="drinks", sizes=1):
        super().__init__(price, amount, item_type, sizes)
    def get(self, num=None):
        if num is None:
            num = self._amount 
        return F_Ml_B(self._price,num, self._type)
    def class_type(self):
        return "Milliliters_Bottle"
    def __str__(self):
        if self._amount == 1:
            return "{}x bottle".format(self._amount)
        else:
            return "{}x bottles".format(self._amount)
class F_Ml_C(Food):   #Canned Drinks (375ml)
    def __init__(self, price, amount=0, item_type="drinks", sizes=1):
        super().__init__(price, amount, item_type, sizes)
    def get(self, num=None):
        if num is None:
            num = self._amount 
        return F_Ml_C(self._price, num, self._type)
    def class_type(self):
        return "Milliliters_Can"
    def __str__(self):
        if self._amount == 1:
            return "{}x canned drink".format(self._amount)
        else:
            return "{}x canned drinks".format(self._amount)
class F_Ml(Food):     #Millilitres (Small or Medium)
    def __init__(self, p_s, p_m, amount=0, item_type="drinks", sizes=2):
        self._p_s = p_s
        self._p_m = p_m
        self._amount = amount
        self._type = item_type
        self.sizes = sizes
    def __str__(self):
        if self._amount == 1:
            return "{}x ml".format(self._amount)
        else:
            return "{}x mls".format(self._amount)
    def small(self):
        return "{}x 250ml".format(int(self._amount / 250))
    def med(self):
        return "{}x 450ml".format(int(self._amount / 450))

    def s(self):
        return int(self._amount / 250)
    def m(self):
        return int(self._amount / 450)
    def class_type(self):
        return "Milliliters"
    def get(self, num=None):
        if num is None:
            num = self._amount 
        return F_Ml(self._p_s, self._p_m, num, self._type)

    @property       ### These must be defined first before setters
    def p_s(self):  ### can be used....
        return self._p_s
    @property
    def p_m(self):
        return self._p_m

    def get_price(self, size):
        if size == 'small':
            return self._p_s
        if size == 'medium':
            return self.p_m

    @p_s.setter
    def p_s(self, cost):
        if cost <= 0:
            raise ValueError("_price negative or 0!")
            self._p_s = 99999 #prevents accidents
        else:
            self._p_s = cost
    @p_m.setter
    def p_m(self, cost):
        if cost <= 0:
            raise ValueError("_price negative or 0!")
            self._p_m = 99999 #prevents accidents
        else:
            self._p_m = cost

class F_B(Food):      #Buns
    def __init__(self, price, amount=0, 
                item_type="burger_main", sizes=1):
        super().__init__(price, amount, item_type, sizes)
    def get(self, num=None):
        if num is None:
            num = self._amount 
        return F_B(self._price,num, self._type)
    def class_type(self):
        return "Buns"
    def __str__(self):
        if self._amount == 1:
            return "{}x bun".format(self._amount)
        else:
            return "{}x buns".format(self._amount)
class F_P(Food):      #Paddies
    def __init__(self, price,  amount=0, 
                 item_type="burger_main", sizes=1):
        super().__init__(price, amount, item_type, sizes)
    def __str__(self):
        if self._amount == 1:
            return "{}x patty".format(self._amount)
        else:
            return "{}x patties".format(self._amount)
    def class_type(self):
        return "Paddies"
    def get(self, num=None):
        if num is None:
            num = self._amount 
        return F_P(self._price,num, self._type)

class F_W(Food):      #Wraps
    def __init__(self, price,  amount=0, item_type="wrap_main", sizes=1):
        super().__init__(price, amount, item_type, sizes)
    def __str__(self):
        if self._amount == 1:
            return "{}x wrap".format(self._amount)
        else:
            return "{}x wraps".format(self._amount)
    def class_type(self):
        return "Wraps"
    def get(self, num=None):
        if num is None:
            num = self._amount 
        return F_W(self._price,num, self._type)
