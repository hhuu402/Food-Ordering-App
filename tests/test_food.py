import sys
sys.path.append('../')
from food import *
import pytest

class Test_Foods():
    # NEED TO TEST THAT ALL ABSTRACT CLASSES ARE WORKING
    def setup_method(self):
        fd_1 = F_B(10, 1, "abc")
        fd_2= F_B(10, 5)
        fd_3 = F_B(10)

        fd_4 = F_P(10, 1, "abc")
        fd_5 = F_P(10, 5)
        fd_6 = F_P(10)

        fd_7 = F_G(10,5,3, 1, "abc")
        fd_8 = F_G(10,5,3, 5)
        fd_9 = F_G(10,5,3)

        fd_10 = F_Pc(10,5,3, 1, "abc")
        fd_11 = F_Pc(10,5,3, 5)
        fd_12 = F_Pc(10,5,3)

        fd_13 = F_S(10, 1, "abc")
        fd_14 = F_S(10, 5)
        fd_15 = F_S(10)

        fd_16 = F_Ml(10,5, 1, "abc")
        fd_17 = F_Ml(10,5, 5)
        fd_18 = F_Ml(10,5)

        fd_19 = F_Ml_B(10, 1, "abc")
        fd_20 = F_Ml_B(10, 5)
        fd_21 = F_Ml_B(10)

        fd_22 = F_Ml_C(10, 1, "abc")
        fd_23 = F_Ml_C(10, 5)
        fd_24 = F_Ml_C(10)

        fd_25 = F_W(10, 1, "abc")
        fd_26 = F_W(10, 5)
        fd_27 = F_W(10)

        self.my_foods = [fd_1, fd_2, fd_3, fd_4, fd_5, fd_6, fd_7,   
                         fd_8, fd_9, fd_10, fd_11, fd_12, fd_13, fd_14, 
                         fd_15, fd_16, fd_17, fd_18, fd_19, fd_20, fd_21, 
                         fd_22, fd_23, fd_24, fd_25, fd_26, fd_27]

        # CHECK-LIST #
    # Variable Assignment
    # Function Methods
    # Strings
    # prices

    # Checks if all values are assigned properly for each subclass.
    # Prints i and class type if prone to error.
    def test_values(self):
        for i in range(0,20,3):
            print("i: {} class: {}".format(i, type(self.my_foods[i])))
            assert(self.my_foods[i].amount == 1)
            assert(self.my_foods[i].type == 'abc')
            assert(self.my_foods[i+1].amount == 5)
            assert(self.my_foods[i+2].amount == 0)

    # Checks if all values are assigned the correct type if nothing
    # is inputted
    def test_food_types(self):
        assert(self.my_foods[1].type == "burger_main")
        assert(self.my_foods[2].type == "burger_main")
        assert(self.my_foods[4].type == "burger_main")
        assert(self.my_foods[5].type == "burger_main")
        assert(self.my_foods[7].type == "sides")
        assert(self.my_foods[8].type == "sides")
        assert(self.my_foods[10].type == "sides")
        assert(self.my_foods[11].type == "sides")
        assert(self.my_foods[13].type == "main")
        assert(self.my_foods[14].type == "main")
        assert(self.my_foods[16].type == "drinks")
        assert(self.my_foods[17].type == "drinks")
        assert(self.my_foods[19].type == "drinks")
        assert(self.my_foods[20].type == "drinks")
        assert(self.my_foods[22].type == "drinks")
        assert(self.my_foods[23].type == "drinks")
        assert(self.my_foods[25].type == "wrap_main")
        assert(self.my_foods[26].type == "wrap_main")
    
    # Testing Prices are correct
    def test_price(self):
        for i in range(0,20,3):
            print("i: {} class: {}".format(i, type(self.my_foods[i])))
            if (i in [6,9]): #pcs/grams
                assert(self.my_foods[i].p_s == 10)
                assert(self.my_foods[i].p_m == 5)    
                assert(self.my_foods[i].p_l == 3)
                for j in [0,-1]:
                    try:
                        self.my_foods[i].p_s = j 
                    except ValueError:
                        assert(True)
                    else:
                        assert(False)
                    try:
                        self.my_foods[i].p_m = j 
                    except ValueError:
                        assert(True)
                    else:
                        assert(False)
                    try:
                        self.my_foods[i].p_l = j 
                    except ValueError:
                        assert(True)
                    else:
                        assert(False)
            elif (i is 15): #drinks
                assert(self.my_foods[i].p_s == 10)
                assert(self.my_foods[i].p_m == 5)
                for j in [0,-1]:
                    try:
                        self.my_foods[i].p_s = j 
                    except ValueError:
                        assert(True)
                    else:
                        assert(False)
                    try:
                        self.my_foods[i].p_m = j 
                    except ValueError:
                        assert(True)
                    else:
                        assert(False)
            else:
                assert(self.my_foods[i].price == 10)
                for j in [0,-1]:
                    try:
                        self.my_foods[i].price = j 
                    except ValueError:
                        assert(True)
                    else:
                        assert(False)

    # Testing Setter and Add Function
    def test_types(self):
        self.my_foods[23].set(20) 
        assert(self.my_foods[23].amount == 20)
        self.my_foods[23].add(-500)
        assert(self.my_foods[23].amount == -480)

    # Testing Special Functions
    def test_F_Ml(self):
        #Small Size
        self.my_foods[17].set(0)
        assert(self.my_foods[17].small() == "0x 250ml")
        self.my_foods[17].set(250) 
        assert(self.my_foods[17].small() == "1x 250ml")
        self.my_foods[17].set(260)
        assert(self.my_foods[17].small() == "1x 250ml") 
        self.my_foods[17].set(500)
        assert(self.my_foods[17].small() == "2x 250ml") 

        # Our program in particular should never exceute these
        # But for testing purposes...
        self.my_foods[17].set(-250)
        assert(self.my_foods[17].small() == "-1x 250ml")
        self.my_foods[17].set(-300)
        assert(self.my_foods[17].small() == "-1x 250ml")

        #Medium Size
        self.my_foods[17].set(0)
        assert(self.my_foods[17].med() == "0x 450ml")
        self.my_foods[17].set(450) 
        assert(self.my_foods[17].med() == "1x 450ml")
        self.my_foods[17].set(500)
        assert(self.my_foods[17].med() == "1x 450ml") 
        self.my_foods[17].set(900)
        assert(self.my_foods[17].med() == "2x 450ml") 

        # Our program in particular should never exceute these
        # But for testing purposes...
        self.my_foods[17].set(-450)
        assert(self.my_foods[17].med() == "-1x 450ml")
        self.my_foods[17].set(-500)
        assert(self.my_foods[17].med() == "-1x 450ml")

    def test_F_G(self):

        # Small Size
        self.my_foods[8].set(0)
        assert(self.my_foods[8].small() == "0x small")
        self.my_foods[8].set(75) 
        assert(self.my_foods[8].small() == "1x small")
        self.my_foods[8].set(100)
        assert(self.my_foods[8].small() == "1x small") 
        self.my_foods[8].set(160)
        assert(self.my_foods[8].small() == "2x small") 

        # " "
        self.my_foods[8].set(-75)
        assert(self.my_foods[8].small() == "-1x small")
        self.my_foods[8].set(-80)
        assert(self.my_foods[8].small() == "-1x small")

        # Med Size
        self.my_foods[8].set(0)
        assert(self.my_foods[8].med() == "0x medium")
        self.my_foods[8].set(125) 
        assert(self.my_foods[8].med() == "1x medium")
        self.my_foods[8].set(150)
        assert(self.my_foods[8].med() == "1x medium") 
        self.my_foods[8].set(300)
        assert(self.my_foods[8].med() == "2x medium") 

        # " "
        self.my_foods[8].set(-125)
        assert(self.my_foods[8].med() == "-1x medium")
        self.my_foods[8].set(-130)
        assert(self.my_foods[8].med() == "-1x medium")

        # Med Size
        self.my_foods[8].set(0)
        assert(self.my_foods[8].large() == "0x large")
        self.my_foods[8].set(170) 
        assert(self.my_foods[8].large() == "1x large")
        self.my_foods[8].set(190)
        assert(self.my_foods[8].large() == "1x large") 
        self.my_foods[8].set(400)
        assert(self.my_foods[8].large() == "2x large") 

        # " "
        self.my_foods[8].set(-170)
        assert(self.my_foods[8].large() == "-1x large")
        self.my_foods[8].set(-200)
        assert(self.my_foods[8].large() == "-1x large")

    # Here, we have the gutt of the food test
    # Test get, str, sizes & class
    def test_str(self):
        s = ["x pc", "x pcs", "x serving", "x servings", "x bottle", 
             "x bottles", "x canned drink", "x canned drinks",
             "x ml", "x mls", "x bun", "x buns", "x patty", "x patties",
             "x gram", "x grams", "x wrap", "x wraps"]
        v = [3,1,1,1,2,1,1,3,1]
        c = ["Pieces", "Servings", "Milliliters_Bottle", 
             "Milliliters_Can", "Milliliters", "Buns", 
             "Paddies", "Grams", "Wraps"]
        num = [11, 14, 20, 23, 17, 2, 5, 8, 26]
        j = 0
        k = 0
        for i in num:
            print("i: {} class: {}".format(i, type(self.my_foods[i])))
            self.my_foods[i].set(1)
            # 1 items, (singular item)
            assert(self.my_foods[i].__str__() == "1" + s[j])  
            self.my_foods[i].set(2)
            # 2 items, (plural items)
            assert(self.my_foods[i].__str__()  == "2" + s[j+1])
            # Get without args
            copy = self.my_foods[i].get()
            assert(copy.__str__() == "2" + s[j+1])
            # Get with args
            copy = self.my_foods[i].get(3)
            assert(copy.__str__() == "3" + s[j+1])    
            # Getting Sizes of types without args
            assert(self.my_foods[i].sizes == v[k])
            # Setting sizes of types and asserting
            with pytest.raises(ValueError):
                self.my_foods[i].sizes = 0
            self.my_foods[i].sizes = 5
            assert(self.my_foods[i].sizes == 5)
            # Testing Classes
            assert(self.my_foods[i].class_type() == c[k])
            j += 2;
            k += 1

