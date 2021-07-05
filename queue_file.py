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

from call_error import *
from staff import *
from inventory import *
from order import *

class Queue():
	def __init__(self):
		self._q = []
		self._completed_orders  = []
		self._ID = int(1)
		
	def add_order(self, order):
	
		self._q.append(order)
		order.set_ID(self._ID)
		self._ID += 1
		return self._ID -1
		
	def remove_order(self, order):
		try:
			self._q.remove(order)
		except:
			raise CallError('invalid order','Order could not be removed.')
			return False
		return True
		
	def change_status(self,order_id):
		if int(order_id) <= 0 or int(order_id) > self._ID:
			raise CallError('Invalid ID', 'Must input a valid ID')
		else:
			counter = 0
			for x in self._q:
				if x.get_ID() == int(order_id):
					order = x
					counter = 1
					break
			if counter == 0:
				("Order no longer in queue")
				return True
			if order.status == 'Processing':
				order.change_status('Preparing')
			elif order.status == 'Preparing':
				order.change_status('Complete')
				self._completed_orders.append(order)
		#print("Order status has been updated to \"{}\"".format(order.status))
		return True

	def print_order(self,order):
		#print('{}\n'.format(order))
		return order

	def get_order_id(self,order):	
		return order.get_ID()

	def view_current_orders(self):
		if len(self._q) == 0:
			print('There are currently no orders!')
			return False
		else:
            #print('List of Orders:\n')
			#for x in self._q:
				#print('Order ID of {}:\nStatus = {}\n\n{}'.format(x.get_ID(),x.status,str(x)))

			#return True
			return self._q

			print('List of Orders:\n')
			for x in self._q:
				print('Order ID of {}:\nStatus = {}\n\n{}'.format(x.get_ID(),x.status,str(x)))
			return True

	def view_completed_orders(self):
		if len(self._completed_orders) == 0:
			#print("There are currently no completed orders")
			return False
		else:
			#print("List of completed Orders:\n")
			#for x in self._completed_orders:
			#	print("Order ID of {}:\n{}\n",format(x.get_ID(),str()))
			return self._completed_orders
				
	def get_order(self,order_id):
		if int(order_id) <= int(len(self._q)):
			#print('Your order is:\n{}\n'.format(self._q[order_id-1]))
			return self._q[int(order_id)-1]

		else:
			return False

	def get_order_history(self):
		print('List of Completed Orders:\n')
		if len(self._completed_orders ) > 0:
			#for x in self._completed_orders :
			#	print('{}:\n{}\n'.format(x,self._completed_orders ))
			return self._completed_orders
		else:
			#print('The list of completed orders is empty.')
			return False
		return

	def get_status(self, ID):
		if ID <= 0 or ID > self._ID:
			raise CallError('Invalid ID','ID of {} is not in queue'.format(ID))
		else:
			for order in self._q:
				if order.get_ID() == ID:
					return order.status
			for order in self._completed_orders:
				if order.get_ID() == ID:
					return order.status
                    
	def get_size(self):
		return len(self._q)
