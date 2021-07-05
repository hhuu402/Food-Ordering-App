Style Guide

all classes first letter must be in uppercase (only classes)
all files should be lower case names of the class.
all variable names must be in snakecase e.g. big_num
all functions must be as follows: function() instead of function ()
all use elif instead of else if
all lines must be in 73 line limit
tabs must be in 4 spaces, not tab space // set this in your editor pref
all branches must be named after your class, e.g. c_className in lowercase
all commas must have a space directly after. e.g.
    hello(a, b, c) instead of hello(a,b,c)
all comments must be above function names or statement control (if,elif,else)
or besides variable names

General Rules 

all COMMENT ON YOUR CODE including TODOS
all make sure you test each function under tests/test_fileName.py 
all please have a header comment briefly outlining all your function at top
of the file.

something like this:

#==== Library Header ====================================================
# Constructor << "f_name" >> - Reads & Writes inv from f_name(string)
# add_inventory(str item,int qty) - adds X from inv    | allows negatives  
# sub_inventory(str item,int qty) - removes X from inv | allows negatives
# set_inventory(str item,int qty) - sets value |
# bool delete_item(str item) - removes X from inv | ret (if work) ? 1 : 0
# get_list() - returns list of all food items
# get_type() - returns type of food ("main", "side", "drinks")
# [IMPORTANT] free_inv() - Saves inventory into file and closes file

#==== Function throws =================================================== 
# ValueError    | if item stock falls below zero
#========================================================================

