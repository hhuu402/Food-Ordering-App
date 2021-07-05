
from flask import Flask, render_template, request, redirect, url_for

from data import *

app = Flask(__name__)

# BASE PAGE     (Check data.py to change urls)
@app.context_processor
def nav():
    return dict(nav_start=nav_start, nav_end=nav_end) # from config       

# HOME PAGE
@app.route('/', methods=["GET"])
def home():

    order_func = 'check_meal' # change this later and delete this comment
                        # @andre, this redirects to app.route func 

    burgers = {   # image   sml lrg | prices
        "Tru-Blu": ["b1.png",20, 21],
        "The Leftist": ["b2.png", 14, 15],
        "The Rooster": ["b3.png", 18, 19],
        "custom burger": ["b4.png", -1, -1],
    }
    wraps = {
        "Julius": ["w1.png", 12, 13],
        "The Sheep": ["w2.png", 15, 16],
        "Cow-Ai": ["w3.png", 13, 14],
        "custom wrap": ["w4.png", -1, -1],
    }
    return render_template('home.html', url_next=order_func,
                                        wraps=wraps,
                                        burgers=burgers)

@app.route('/check_meal', methods=["GET","POST"])
def check_meal():
    n =request.args
    new_order= Order()
    temp_orders.append(new_order)
    order = len(temp_orders)
    
    if (len(n)) != 0:
        if n['size'] == 'none':
            new_order= Order()
            temp_orders.append(new_order)
            order = len(temp_orders)
            return render_template('custom.html', main=n['meal_type'], order=order, temp_orders=temp_orders, price=0)
        else:
            if n['meal_type'] == 'burger':
                new_order.set_meal(n['meal_name'])
                new_order.is_meal()
                return finish_meal('burger', n['meal_name'], size=n['size'])
            if n['meal_type'] == 'wrap':
                new_order.set_meal(n['meal_name'])
                new_order.is_meal()
                return finish_meal('burger', n['meal_name'], size=n['size'])
    
    if n['size'] == 'none':
        return redirect(url_for('custom', main=n['main'], order=order))  
    else:
        return redirect(url_for('home'))
        #return redirect(url_for('finish_meal.html', main=main, meal=meal, size=size))

     

@app.route('/custom/<main><order>/', methods=["GET","POST"])
def custom(main, order):
    price = temp_orders[int(order)-1].get_price_total()
    return render_template('custom.html', main=main, order=order, temp_orders=temp_orders,
                                                                              price=price)  
   
 
@app.route('/custom/<main><order>/burger', methods=["GET", "POST"])
def burger(main, order):
    new_order = Order()
    if request.method == "POST":
        if 'burger_type' not in request.form:
            return render_template('burger.html', inventory=inventory, food_list=inventory.get_list(),
                order=order, check_burger_type=False, check_order="check_order", errors={}, main=main)
        if 'bun' not in request.form:
            return render_template('burger.html', inventory=inventory, food_list=inventory.get_list(),
                        order=order, check_bun=False, check_order="check_order", errors={}, main=main)

        for food in request.form:
            if food in inventory.inv and request.form[food] != '':
                new_order.add_item(inventory, food, request.form[food])
        new_order.add_item(inventory, request.form['bun'], str(int(request.form['burger_type'])+1))
        if 'patty' in request.form:
            new_order.add_item(inventory, request.form['patty'], str(int(request.form['burger_type'])))
        if request.form['order']== 'add_items':
            if not new_order.is_valid():
                return render_template('burger.html', inventory=inventory,check_order="add_items",
            order=order, food_list=inventory.get_list(), errors=new_order.pop_errors(), main=main)
            else:
                form = request.form
                errors = add_items_burger(main, order, form)
                if errors:
                    return render_template('burger.html', inventory=inventory, food_list=inventory.get_list(), 
                                               order=order, check_order='add_items', errors=errors, main=main)   
                return redirect(url_for('custom',main=main,order=order))
        
        if request.form['order'] == 'update':         
            if not new_order.is_valid():
                return render_template('burger.html', inventory=inventory,check_order="add_items",
            order=order, food_list=inventory.get_list(), errors=new_order.pop_errors(), main=main)   
            else:
                temp_orders[int(order)-1].remove_mains()
                form = request.form
                errors = add_items_burger(main, order, form)
                if errors:
                    if errors:
                        return render_template('burger.html', inventory=inventory, food_list=inventory.get_list(), 
                                               order=order, check_order='add_items', errors=errors, main=main)   
                return redirect(url_for('custom',main=main,order=order))
            
        if request.form['order'] == 'get_price':
            price= new_order.get_price_total()
            return render_template('burger.html', inventory=inventory, food_list=inventory.get_list(),
                           price=price, order=order, check_order='check_price', errors= {}, main=main)
        
    return render_template('burger.html', inventory=inventory, food_list=inventory.get_list(), 
                                 order=order, errors = {}, check_order='add_items', main=main)
 
@app.route('/custom/<main><order>/wrap', methods=["GET", "POST"])
def wrap(main, order):
    new_order= Order()

    if request.method == "POST":
        if 'wrap' not in request.form:
                return render_template('wrap.html', inventory=inventory, food_list=inventory.get_list(), 
                           order=order, check_wrap=False, check_order='add_items', errors={}, main=main) 

        for food in request.form:  
            if food== 'wrap' and request.form[food] in inventory.inv:
                new_order.add_item(inventory, request.form[food], '1') 
            if food in inventory.inv and request.form[food] != '':
                new_order.add_item(inventory, food, request.form[food])

        if request.form['order'] == 'add_items':
            if not new_order.is_valid():
                #print("find me")
                return render_template('wrap.html', inventory=inventory, food_list=inventory.get_list(), 
                             order=order, check_order='add_items', errors=new_order.pop_errors(), main=main)
            else:
                form = request.form
                errors = add_items(main, order, form)
                if errors:
                    return render_template('wrap.html', inventory=inventory, food_list=inventory.get_list(), 
                                             order=order, check_order='add_items', errors=errors, main=main)    
                return redirect(url_for('custom',main=main,order=order))

        if request.form['order'] == 'update':         
            if not new_order.is_valid():
                return render_template('wrap.html', inventory=inventory, food_list=inventory.get_list(), 
                             order=order, check_order='add_items', errors=new_order.pop_errors(), main=main)    
            else:
                temp_orders[int(order)-1].remove_mains()
                form = request.form
                errors = add_items(main, order, form)
                if errors:
                    if errors:
                        return render_template('wrap.html', inventory=inventory, food_list=inventory.get_list(), 
                                             order=order, check_order='add_items', errors=errors, main=main)    
                return redirect(url_for('custom',main=main,order=order))

        if request.form['order'] == 'get_price':
            price = new_order.get_price_total()
            return render_template('wrap.html', inventory=inventory, food_list=inventory.get_list(),
                         price=price, order=order, check_order='check_price', errors= {}, main=main)
   
                    
    return render_template('wrap.html', inventory=inventory, food_list=inventory.get_list(), 
                               order=order, check_order='add_items', errors = {}, main=main)

@app.route('/custom/<main><order>/sides', methods=["GET", "POST"])
def sides(main, order):
    new_order = Order()
    if request.method == "POST":
        no_input_counter = 0
        for food in request.form:
            if food in inventory.inv and request.form[food] != '':
                no_input_counter = 1
                if food+'_size' not in request.form:
                    new_order.add_item(inventory, food, request.form[food])
                else:
                    new_order.add_item(inventory, food, request.form[food], request.form[food+'_size'])


        if no_input_counter == 0:
            return render_template('sides.html', inventory=inventory, food_list=inventory.get_list(), 
 order=order, check_order='add_items', sides_sizes=sides_sizes, errors=new_order.pop_errors(), main=main)

        if request.form['order'] == 'add_items':

            if not new_order.is_valid():
                return render_template('sides.html', inventory=inventory, food_list=inventory.get_list(), 
 order=order, check_order='add_items', sides_sizes=sides_sizes, errors=new_order.pop_errors(), main=main)
            else:
                form = request.form
                errors = add_items(main, order, form)
                if errors:
                    return render_template('sides.html', inventory=inventory, food_list=inventory.get_list(), 
      order=order, check_order='add_items', sides_sizes=sides_sizes, errors=errors, main=main)    
                return redirect(url_for('custom',main=main,order=order))

        if request.form['order'] == 'get_price':
            price = new_order.get_price_total()
            return render_template('sides.html', inventory=inventory, food_list=inventory.get_list(),
 price=price, order=order, check_order='check_price', sides_sizes=sides_sizes, errors= {}, main=main)

    return render_template('sides.html', inventory=inventory, food_list=inventory.get_list(), errors = {}, 
                                 order=order, check_order='add_items', sides_sizes=sides_sizes, main=main)
 
@app.route('/custom/<main><order>/drinks', methods=["GET", "POST"])
def drinks(main, order):
    new_order = Order()
    if request.method == "POST":
        no_input_counter = 0
        for food in request.form:
            if food in inventory.inv and request.form[food] != '':
                no_input_counter = 1
                if inventory.inv[food].class_type()!="Milliliters":
                    new_order.add_item(inventory, food, request.form[food])
                if inventory.inv[food].class_type()=="Milliliters":

                    if food+'_size' not in request.form:
                        new_order.add_item(inventory, food, request.form[food])
                    else:
                        new_order.add_item(inventory, food, request.form[food], 
                                                request.form[food+'_size'])
        if no_input_counter == 0:
            return render_template('drinks.html', inventory=inventory, food_list=inventory.get_list(), 
  order=order, check_order='add_items', drink_sizes=drink_sizes, errors=new_order.pop_errors(), main=main)

        if request.form['order'] == 'add_items':
            if not new_order.is_valid():
                return render_template('drinks.html', inventory=inventory, food_list=inventory.get_list(), 
  order=order, check_order='add_items', drink_sizes=drink_sizes, errors=new_order.pop_errors(), main=main)
            else:
                form = request.form
                errors = add_items(main, order, form)
                if errors:
                    return render_template('drinks.html', inventory=inventory, food_list=inventory.get_list(), 
      order=order, check_order='add_items', drink_sizes=drink_sizes, errors=errors, main=main)    
                return redirect(url_for('custom',main=main,order=order))

        if request.form['order'] == 'get_price':
            price = new_order.get_price_total()
            return render_template('drinks.html', inventory=inventory, food_list=inventory.get_list(),
  price=price, order=order, check_order='check_price', drink_sizes=drink_sizes, errors= {}, main=main)

    return render_template('drinks.html', inventory=inventory, food_list=inventory.get_list(), errors = {}, 
                                  order=order, check_order='add_items', drink_sizes=drink_sizes, main=main)


def add_items_burger(main, order, form):
    order=int(order)
    if form['burger_type'] == '1':
        if 'patty' in form:
            temp_orders[order-1].add_item(inventory, form['patty'], '1')
        temp_orders[order-1].add_item(inventory, form['bun'], 2)  
    elif form['burger_type'] == '2':
        if 'patty' in form:
            temp_orders[order-1].add_item(inventory, form['patty'], '2')
        temp_orders[order-1].add_item(inventory, form['bun'], '3')  
    for item in form:
        if (item in inventory.inv) and (inventory.inv[item].type != "burger_main") and (form[item] !=''):
            temp_orders[order-1].add_item(inventory, item, form[item]) 

    return temp_orders[order-1].pop_errors()
    #return redirect(url_for('custom',main=main, order=order))

def add_items(main, order, form):
# for wrap meal
    #print(items)
    order = int(order)
    for item in form:
        if item in inventory.inv and form[item] != '':
            if item+'_size' in form:
                temp_orders[order-1].add_item(inventory, item, form[item], form[item+'_size'])
            else:   
                temp_orders[order-1].add_item(inventory, item, form[item])
        elif item == 'wrap':
                temp_orders[order-1].add_item(inventory, form[item], '1')

    return temp_orders[order-1].pop_errors()

    #return redirect(url_for('custom',main=main,order=order))

@app.route('/custom<main><order>/edit_order', methods=["GET","POST"])
def edit_order(main, order):
    order_tmp = temp_orders[int(order)-1]
    if request.method == 'POST':
        if request.form['order'] == 'edit_order':
            form = request.form
            return edit_items(main, order, form)
            #return render_template('edit_order.html', errors = {}, order=order, main=main,
                                 #items=order_tmp.get_items(), order_tmp=order_tmp)
        elif request.form['order'] == 'clear_order':
            temp_orders[int(order)-1].remove_all()
            return render_template('custom.html',main=main,order=order,
                                     errors={}, temp_orders=temp_orders, price=0)
            
        elif request.form['order'] == 'get_price':
            price = temp_orders[int(order)-1].get_price_total()
            return render_template('edit_order.html', errors = {}, order=order, main=main,
            price=price, check_order='check_price', items=order_tmp.get_items(), order_tmp=order_tmp)
               
    return render_template('edit_order.html', errors = {}, order=order, main=main,
                                 items=order_tmp.get_items(), order_tmp=order_tmp)

def edit_items(main, order, form):
    temp_order = temp_orders[int(order)-1]
    for item in form:
        dummy_order = Order()
        if item[2:] in temp_order.get_items():
            temp_order.edit_order(inventory, item[2:], form[item], item[0], dummy_order)
    if not temp_order.is_valid():
        return render_template('edit_order.html', errors = temp_order.pop_errors(), order=order,
           main=main, items=temp_order.get_items(), order_tmp=temp_order)
    else:
        return redirect(url_for('custom',main=main,order=order))


@app.route('/custom/<main><order>/confirm', methods=["GET", "POST"])
def confirm_order(main, order):

    if temp_orders[int(order)-1].is_empty():
        return redirect(url_for('custom',main=main,order=order, empty='empty'))
    if not temp_orders[int(order)-1].confirm_order(inventory):
        return render_template('custom.html',main=main,order=order,
                 errors=temp_orders[int(order)-1].pop_errors(), temp_orders=temp_orders)

    else:
        temp_orders[int(order)-1].confirm_order(inventory)
        order_num = q.add_order(temp_orders[int(order)-1])
        return redirect(url_for('confirm_order_page', main=main,order=order_num,
                                                              q=q))


@app.route('/custom/<main><order>/confirm_page', methods =["GET", "POST"])
def confirm_order_page(main, order):
    price=q.get_order(int(order)).get_price_total()
    return render_template('confirm_order.html', order=int(order), q=q, price=price)


@app.route('/finish_meal/<main><meal><size>', methods =["GET", "POST"])
def finish_meal(main, meal, size):
    if request.method == "POST":
        order = Order()
        if 'drink' not in request.form:
            return render_template('finish_meal.html', inventory=inventory,
                                            food_list=inventory.get_list(), 
                                 main=main, meal=meal,size=size, meal_check = 'drink')
        order.add_item(inventory, request.form['drink'], 1)
        order.add_item(inventory, 'fries', 1, size)
        order.set_meal(meal)
        order.make_meal(inventory)
        price = order.get_price_total()
        if request.form['order'] == 'get_price':
            return render_template('finish_meal.html', inventory=inventory, price=price, drink = request.form['drink'],
                                 food_list=inventory.get_list(), main=main, meal=meal,size=size, meal_check = 'price')
        errors = order.get_errors()
        if errors:
            return render_template('finish_meal.html', inventory=inventory,
                                            food_list=inventory.get_list(), 
       main=main, meal=meal,size=size, meal_check = 'stock', errors=errors) 
        order.confirm_order(inventory)
        order_num = q.add_order(order)
        return redirect(url_for('confirm_order_page', main=main,order=order_num, q=q))
    return render_template('finish_meal.html', inventory=inventory,
                        food_list=inventory.get_list(), main=main, 
                                                     meal_check='', meal=meal, size=size)


@app.route('/login', methods=["GET","POST"])
def staff_login():
    error='passed'
    staff_attempt = Staff()
    if request.method == 'POST':
        form = request.form
        
        try:
            password = request.form["password"]
            if staff_attempt.login(password) == True:
                #success, redirect to /staff
                return redirect(url_for('staff_homepage'))
                #render_template('staff_pages.html',error=error)
            else:
                error = 'error'
                return render_template('staff_login.html',error=error)
        except:
            return render_template('staff_login.html',error=error)

    return render_template('staff_login.html',error=error)


@app.route('/staff', methods=["GET","POST"])
def staff_homepage():
    if request.method == 'POST':
        form = request.form
        
        if 'logout' in request.form:
            return redirect(url_for('home'))
            #render_template('staff_login.html')

        elif 'inventory' in request.form:
            return redirect(url_for('staff_inv'))
            #render_template('staff_inventory.html')

        else:
            return redirect(url_for('staff_powers'))
            #render_template('staff_powers.html')

    else:
        return render_template('staff_pages.html')


@app.route('/staff_powers', methods=["GET","POST"])
def staff_powers():

    
    #orders = q.view_current_orders
    error = 'none'
    status_error = 'none'
    status = ''
    q_tmp = q.view_current_orders()
    if q_tmp == False:
        return render_template('staff_powers.html', orders={}, error='Queue is empty',
                                        status_error=status_error, status=status, q=q)
    if request.method == "POST":
        form = request.form
        if 'confirm' in request.form:
            try:
                order_id = request.form["order_id"]
                try:
                    order = q.get_order(int(order_id))
                    q_tmp = q.view_current_orders()
                    if q_tmp == False:
                        q_tmp = {}
                    q.change_status(order_id)
                    status = order.status
                    error = 'success'
                    return render_template('staff_powers.html', orders=q.view_current_orders(), error=error, status_error=status_error, status=status, q=q)
                except:
                    error = 'error'
                    return render_template('staff_powers.html', orders=q.view_current_orders(), error=error, status_error=status_error, status=status, q=q)
            except:
                return render_template('staff_powers.html', orders=q.view_current_orders(), error=error, status_error=status_error, status=status, q=q)

    else:
        return render_template('staff_powers.html', orders=q.view_current_orders(), error=error, status_error=status_error, status=status, q=q)

@app.route('/staff_inventory', methods=["GET", "POST"])
def staff_inv():
    error = 'none'
    msg = 'none'
    l0 = [] #master
    l1 = [] #main
    l1_b = [] #main_burger
    l1_w = [] #main_wrap
    l2 = [] #sides
    l3 = [] #drinks
    #print(inventory)
    for i in inventory.inv:
        if inventory.inv[i].type == "main":
            l1.append([i, inventory.inv[i].__str__(), inventory.inv[i].type])
        elif inventory.inv[i].type == "burger_main":
            l1_b.append([i, inventory.inv[i].__str__(), inventory.inv[i].type])
        elif inventory.inv[i].type == "wrap_main":
            l1_w.append([i, inventory.inv[i].__str__(), inventory.inv[i].type])
        elif inventory.inv[i].type == "sides":
            l2.append([i, inventory.inv[i].__str__(), inventory.inv[i].type])
        elif inventory.inv[i].type == "drinks":
            l3.append([i, inventory.inv[i].__str__(), inventory.inv[i].type])
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
        if inventory.inv[l0[i][0]].amount == 0:
            l0[i][1] = l0[i][1] + " [EMPTY]"  

        elif inventory.inv[l0[i][0]].amount <= 20:
            l0[i][1] = l0[i][1] + " [LOW]"
            l0[i][0] = "!! " +l0[i][0] + " !!"  
        elif inventory.inv[l0[i][0]].class_type() == 'Milliliters' and inventory.inv[l0[i][0]].amount <= 500:
            l0[i][1] = l0[i][1] + " [LOW]" 
            l0[i][0] = "!! " +l0[i][0] + " !!"   
        elif inventory.inv[l0[i][0]].class_type() == 'Grams' and inventory.inv[l0[i][0]].amount <= 500:
            l0[i][1] = l0[i][1] + " [LOW]"
            l0[i][0] = "!! " +l0[i][0] + " !!"

    for i in range(len(l0)):
        l1.append(l0[i][0])
        l2.append(l0[i][1])
        l3.append(l0[i][2])

    if request.method == 'POST':
        form = request.form
        item = request.form["item"]
        amount = request.form["amount"]
        if "item" not in form:
            error = 'Please input a legitimate food item from inventory!'
            return render_template('staff_inv.html',inventory=inventory, error=error, msg=msg,a1=l1,b1=l2,c1=l3)
        elif 'amount' not in form:
            error = 'Please enter a legitimate input.'
            return render_template('staff_inv.html',inventory=inventory, error=error, msg=msg,a1=l1,b1=l2,c1=l3)
        elif not request.form['amount'].isdigit():
            error = 'Please input a valid quantity.'
            return render_template('staff_inv.html',inventory=inventory, error=error, msg=msg,a1=l1,b1=l2,c1=l3)
        
        if item in inventory.inv:
            if staff.update_inventory(inventory, amount, item):
                return edit_inv(item, amount, msg, l1, l2, l3)
        else:
            return render_template('staff_inv.html',inventory=inventory, error='Invalid item given', msg=msg,a1=l1,b1=l2,c1=l3)

        #return render_template('staff_inv.html',inventory=inventory, error=error, msg=msg,a1=l1,b1=l2,c1=l3)    


    else:
        return render_template('staff_inv.html',inventory=inventory, error=error, msg=msg,a1=l1,b1=l2,c1=l3)


def edit_inv(item, amount, msg, l1, l2, l3):
   error = 'Inventory Update Successful!'
   return redirect(url_for('staff_inv')  ) 
   error = 'Inventory Update Unsuccessful :('
   return render_template('staff_inv.html',inventory=inventory, error=error, msg=msg,a1=l1,b1=l2,c1=l3)  

@app.route("/id/", methods=["GET","POST"])
def check_id():
    if request.method == "POST":
        if request.form['id'] == '':
            return render_template('get_id.html', id = '', error = 'Please input an ID', order='')
        if not (request.form['id'].isdigit()):
            return render_template('get_id.html', id = '', error = 'Please input a valid ID',
                                                                                    order='')
        if not q.view_current_orders():
            return render_template('get_id.html', id = '', error = 'Queue is Empty', order='')
        ID = int(request.form['id'])
        if ID <= 0 or ID > len(q.view_current_orders()):
            return render_template('get_id.html', id = '', error = 'Please input a valid ID',
                                                                                 order = '')

        return render_template('get_id.html', id = '', error = '', order= q.get_order(ID))

    return render_template('get_id.html', id = '', error = '', order= '')

'''
# CHECK ID
@app.route("/id/", methods=["GET","POST"])
def check_id():
    if request.method == "POST":
        id = request.form['id']
        return redirect(url_for('get_id', order_id=id))
    return render_template('get_id.html', id = -1)
@app.route("/id/<order_id>/", methods=["GET","POST"])
def get_id(order_id):
    if request.method == "POST":
        id = request.form['id']
        return redirect(url_for('get_id', order_id=id))
    return render_template('get_id.html', id=order_id)



#Use if cant be bothered to fix above
# CHECK ID
'''


