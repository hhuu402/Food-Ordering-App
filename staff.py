class Staff():
	def __init__(self):
		self._pw = '123'
		self._history = []
		
	def login(self,password):
		if password == self._pw:
			return True
		else:
			return False
		'''
		count = 3
		while count > 0:
			if password == self._pw:
				return True
			else:
				self._history.append(password)
				count = count - 1
		return False
		'''
	
	#Split interface up into view order, update order, view order history

	def view_order(self, queue):
		return queue.view_orders

	def view_size(self, queue):
		return queue.get_size()

	def view_order_history(self, queue):
		return queue.get_order_history()

	def update_order(self, order_id, queue):
		if queue.update_status(order_id):
			#returned a legitimate order ID
			return True
		else:
			#ID incorrect
			return False

	def view_inventory(self,inventory):
		return inventory

	def update_inventory(self,inventory, amount, inv_item):
		if inv_item in inventory.inv:
			try:
				val = int(amount)
			except ValueError:
				return False
			else:
				try:
					inventory.add(inv_item,val)
				except ValueError:
					return False
			return True
		else:
			return False
	'''
	def staff_interface(self, inventory, process, queue):
		end_task = False
		while end_task == False:
			instruction = str.lower(input('What would you like to do?\n[view orders]\n[view inventory]\n[exit]\n'))

			if instruction == 'view orders':
				queue.view_orders()
				print('\nThere are a total of {} orders\n'.format(queue.get_size()))
				print('What would you like to do?\n')
				instruction2 = input('[view completed orders]\n[update an order status]\n[return]\n')
				
				if instruction2 == 'update an order status':
					order_id = input('Which order would you like to update? Please enter the order ID\n')
					if queue.update_status(order_id):
						#returned a legitimate order ID
						print('Order has been updated.\n')
					else:
						print('Please input a legitimate ID.\n')
				
				elif instruction2 == 'return':
					end_task == False

				elif instruction2 == 'view completed orders':
					queue.get_order_history()
				
				else:
					print('Instruction invalid: returning to staff page.\n')

			elif instruction == 'view inventory':
				print('{}\n'.format(inventory))

			elif instruction == 'exit':
				print('Logging out for XxxDinerDashxxX staff...\n')
				process = True
				return process

			else:
				print('Please input valid instructions.')
	'''
