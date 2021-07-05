from staff import *
from queue_file import *
from order import *
from inventory import *


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
    #initialise inventory
    #inventory = inventory(.db)
    
    q = Queue()
    o = Order()
    #orders = q.view_current_orders
    error = 'none'
    status_error = 'none'
    status = ''

    if request.method == "POST":
        form = request.form

        if 'confirm_status' in request.form:
            try:
            status_id = request.form["status_id"]
                if order == q.get_order(status_id):
                    status = order.status
                    error = 'success'
                    return render_template('staff_powers.html', orders=q.view_current_orders, error=error, status_error=status_error, status=status)
                else:
                    status_error = 'error'
                    #

                    #Having SOME doubts about reusing "order"
                    #
                    #

                    return render_template('staff_powers.html', orders=q.view_current_orders, error=error, status_error=status_error, status=status)
            except:
                return render_template('staff_powers.html', orders=q.view_current_orders, error=error, status_error=status_error, status=status)

        elif 'confirm' in request.form:
            try:
                order_id = request.form["order_id"]
                if q.get_order(order_id):
                    order = q.get_order(order_id)
                    q.change_status(order_id)
                    status = order.status
                    error = 'success'
                    return render_template('staff_powers.html', orders=q.view_current_orders, error=error, status_error=status_error, status=status)
                else:
                    error = 'error'
                    return render_template('staff_powers.html', orders=q.view_current_orders, error=error, status_error=status_error, status=status)
            except:
                return render_template('staff_powers.html', orders=q.view_current_orders, error=error, status_error=status_error, status=status)

    else:
        return render_template('staff_powers.html', orders=q.view_current_orders, error=error, status_error=status_error, status=status)

@app.route('/staff_inventory', methods=["GET","POST"])
def staff_inv():
	staff = Staff()
	inventory = Inventory('.db')
	error = 'none'
	msg = 'none'
	if request.method == 'POST':
		form = request.form
		try:
			item = request.form["item"]
			amount = request.form["amount"]
			try:
				val = int(amount)
			except:
				error = 'Please input a full integer for amount.'
				return render_template('staff_inv.html',inventory=inventory, error=error, msg=msg)

			if staff.update_inventory(inventory, amount, item):
				msg = 'Inventory Updated Successfully.'
				return render_template('staff_inv.html',inventory=inventory, error=error, msg=msg)
			else:
				error = 'Please input a legitimate food item from inventory!'
				return render_template('staff_inv.html',inventory=inventory, error=error, msg=msg)	

		except:
			error = 'Please enter a legitimate input.'
			return render_template('staff_inv.html',inventory=inventory, error=error, msg=msg)

	else:
		return render_template('staff_inv.html',inventory=inventory, error=error, msg=msg)