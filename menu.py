class Menu():
	#print list of food
	def view_menu(self, inventory, menu_choice):
		available_foods = inventory
		#This function prints out the menu!
		print('\n***MAINS:{}***'.format(str.upper(menu_choice)))
		for key in available_foods.get_list():
			if menu_choice == 'wrap':
			#print the wraps menu
				if available_foods.inv[key].type.find('wrap_main') != -1:
					print('{}, ${:.2f}'.format(key,available_foods.inv[key].price))
			else:
			#print the burgers menu
				if available_foods.inv[key].type.find('burger_main') != -1:
					print('{}, ${:.2f}'.format(key,available_foods.inv[key].price))

			#print the mains shared by burgers and wraps
			if available_foods.inv[key].type == 'main':
				print('{}, ${:.2f}'.format(key,available_foods.inv[key].price))

		print('\n***SIDES***')
		for key in available_foods.get_list():
			if available_foods.inv[key].type == 'sides':
				print('{}, ${:.2f} (small)'.format(key,available_foods.inv[key].p_s))
				print('{}, ${:.2f} (medium)'.format(key,available_foods.inv[key].p_m))
				print('{}, ${:.2f} (large)'.format(key,available_foods.inv[key].p_l
					))

		print('\n***DRINKS***')
		if available_foods.inv[key].type == 'drinks':
			for key in available_foods.get_list():
				if available_foods.inv[key].class_type() == "Milliliters_Bottle":
					print('{}, ${:.2f} (per 600ml bottle)'.format(key,available_foods.inv[key].price))

			for key in available_foods.get_list():
				if available_foods.inv[key].class_type() == "Milliliters_Can":
					print('{}, ${:.2f} (per 375ml can)'.format(key,available_foods.inv[key].price))

			for key in available_foods.get_list():
				if available_foods.inv[key].class_type() == "Milliliters":
					print('{}, ${:.2f} (small: per 250ml can)'.format(key,available_foods.inv[key].p_s))
					print('{}, ${:.2f} (medium: per 450ml can)'.format(key,available_foods.inv[key].p_m))

	#this function creates the order
	def order_from_menu(self, inventory, new_order, menu_choice):
		available_foods = inventory

		end_order = 'yes'
		while end_order == 'yes':
			self.view_menu(inventory, menu_choice)
			check = str.lower(input('Would you like to order a main?\n[yes]\n[no]\n'))
			if check == 'yes':
				order = str(input('Order Mains: Select one item from mains to order:\n'))
				#check if food is actually on the menu
				if order in available_foods.get_list():
					if available_foods.inv[order].type.find('main') != -1:
						if menu_choice == 'wrap' and available_foods.inv[order].type == 'burger_main':
							#they have attempted to order a burger only item while having selected to order a wrap

							print('You have attempted to order from the burger menu when you have selected wraps. Please order from the wraps menu.\n')

						elif menu_choice == 'burger' and available_foods.inv[order].type == 'wrap_main':
							#they have attempted to order a wrap only item while having selected to order a burger

							print('You have attempted to order from the wrap menu when you have selected burgers. Please order from the burger menu.\n')
						elif menu_choice == 'wrap' and available_foods.inv[order].type == 'wrap_main':
								quantity = 1
						else:
							if available_foods.inv[order].type == 'wrap_main':
								quantity = 1

							else:
								quantity = int(input('What is the desired quantity of {}?\n'.format(order)))
					
						size = None
						new_order.add_item(available_foods,order,quantity,size)

						print('\nYour current order is:\n\n{}'.format(new_order))
						print('Price: {}$'.format(new_order.get_price_total()))
						end_order = str.lower((input('Is there anything more from mains you would like to order?\n[yes]\n[no]\n')))
							
					else:
						print('That is not on the menu. Please order from the Mains menu.')
				else:		
					print('Please order from the Mains menu.')
			elif check == 'no':
				end_order = 'no'
			else:
				print('Please input a valid response of yes or no')

		end_order = 'yes'
		while end_order == 'yes':
			check = str.lower(input('Would you like to order sides?\n[yes]\n[no]\n'))
			if check == 'yes':
				order = str(input('Order Sides: Select one item from sides to order:\n'))

				#check if food is on the menu
				if order in available_foods.get_list():				
					if available_foods.inv[order].type == 'sides':
						size = str.lower(input('Would you like that in small, medium, or large?\n'))
						quantity = int(input('What is the desired quantity of {}?\n'.format(order)))
						new_order.add_item(available_foods,order,quantity,size)
						print('Your current order is:\n')
						
						print('{}'.format(new_order))
						end_order = str.lower((input('Would you like to order anything else from sides?\n[yes]\n[no]\n')))
					else:
						print('Please order from the Sides menu.')
				else:
					print('That is not on the menu. Please order from the Sides menu.')
			elif check == 'no':
				end_order = 'no'
			else:
				print('Please input a valid response of yes or no')


		end_order = 'yes'
		while end_order == 'yes':
			check = str.lower(input('Would you like to order a drink?\n[yes]\n[no]\n'))
			if check == 'yes':
				order = str(input('Order Sides: Select one item from drinks to order:\n'))

				#check if food is on the menu
				if order in available_foods.get_list():
					if available_foods.inv[order].class_type() == "Milliliters":
						size = str(input('Would you like your {} in small (250ml) or medium (450ml)?\n'.format(order)))
					else:
						size = None

					quantity = int(input('What is the desired quantity of {}?\n'.format(order)))
				
					if available_foods.inv[order].type == 'drinks':
						new_order.add_item(available_foods,order,quantity,size)
						print('Your current order is:\n{}\n'.format(new_order))

						end_order = str.lower(input('Would you like to order anything else from drinks?\n[yes]\n[no]\n'))
					else:
						print('Please order from the Drinks menu.')
				else:
					print('That is not on the menu. Please order from the Drinks menu.')
			elif check == 'no':
				end_order = 'no'
			else:
				print('Please input a valid response of yes or no')
		
		print('Your order is currently:\n{}'.format(new_order))
		return(new_order)
