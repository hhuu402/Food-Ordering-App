'''
~~~~Functions~~~~
add_order		:appends a new order to queue
remove_order	:removed a given order from queue
change_status	:changes the status of a given order
print_order		:prints a given order out
view_orders		:view entire list of order
get_order 		:given an order ID (location of order on list), gives order
get_order_history	:returns a list of completed orders
get_size		:gets the length of the list

'''

#from error import *
#from staff import *
#from inventory import *

class Queue():
	def __init__(self):
		self._q = []
		self._ready_orders = []
		
	def add_order(self, order):		
		try:
			self._q.append(order)
		except:
			print('Invalid order')
			return False
		return
		
	def remove_order(self, order):
		try:
			self._q.remove(order)
		except:
			print('invalid order','Order could not be removed.')
			return False
		return
		
	def update_status(self,order_id):
		try: 
			order_id = int(order_id)
			if int(order_id) < len(self._q):
				order = self._q[order_id]
				if str(order.status) == 'Processing':
					order.change_status('Preparing')
					return True
				elif str(order.status) == 'Preparing':
					order.chage_status('Complete')
					ready_orders.append(order)
					remove_order(order)
					return True
				else:
					print('This order does not seem to exist.')
					return False
			else:
				print('Order ID does not exist.')
				return False
		except:
			print('You input an invalid order ID.')
			return False			
		return

	def print_order(self,order):
		print('{}\n'.format(order))
		return

	def get_order_id(self,order):
		index = self._q.index(order)
		return index

	def view_orders(self):
		if len(self._q) == 0:
			print('There are currently no orders!')
			return False
		else:
			return self._q
			#print('List of Orders:\n')
			#for x in self._q:
			#	print('Order ID of {}:\n{}\n'.format(self._q.index(x),x))

	def get_order(self,order_id):
		if order_id <= len(self._q):
			#print('Your order is:\n{}\n'.format(self._q[order_id]))
			return self._q[order_id]
		else:
			return False

	def get_order_history(self):
		print('List of Completed Orders:\n')
		if len(self._ready_orders) > 0:
			for x in self._ready_orders:
				print('{}:\n{}\n'.format(x,self._ready_orders))
		else:
			print('The list of completed orders is empty.')
			return
		return

	def get_size(self):
		if len(self._q) > 0:
			return len(self._q)
		else:
			return '0'
