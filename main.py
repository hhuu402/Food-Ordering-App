from queue_file import *
from staff import *
from food import *
from order import *
from menu import *
#from customer import *

'''
the beginning of main.py
'''
print('Hello. Welcome to XxxDinerDashxxX.\n')
#initialises inventory
available_foods = Inventory('.db')

m = Menu()
queue = Queue()

confirm_order = False
process = True

while process == True:
	#this is a loop for the correct login
	process = str.lower(input('What would you like to do?\n[login]\n[exit]\n'))

	if process == 'login':
		logged_in = False
		while logged_in == False:
			login = str.lower(input('\nWhat would you like to login as?\n[customer]\n[staff]\n'))
			if login == 'customer':
				#user is a customer
				logged_in = True

			elif login == 'staff':
				#user is a staff
				staff = Staff()
				print('To Testers: The password is 123')
				
				if staff.login():
					logged_in = True

				else:
					print('Program will now exit.')
					exit()

			else:
				print('Please make a valid login choice of customer or staff.')

		#this is the customer page, includes all the customer functions of:
		#1.viewing the menu
		#2.ordering food
		if login == 'customer':

			instruction = str.lower(input('\nHello customer. What would you like to do?\n[new order]\n[view order status]\n[return to login]\n'))

			if instruction == 'new order':
				menu_choice = False
				while menu_choice == False:
					menu_choice = str.lower(input('Which menu would you like to view?\n[burger]\n[wrap]\n'))
					#produce the menu for the corresponding menu of burger or wrap
					if menu_choice != 'wrap' and menu_choice != 'burger':
						print('Please select a menu.\n')
						menu_choice = False
					else:
						#m.view_menu(available_foods, menu_choice)

						#initialise a new order
						new_order = Order()
						
						#the order process called
						new_order = m.order_from_menu(available_foods,new_order,menu_choice)

				end_process = False
				while end_process == False:
					instruction = str.lower(input('\nWhat would you like to do now?\n[confirm order]\n[view order]\n[edit order]\n[exit]\n')) 
					
					if instruction == 'confirm order':
						confirm_order = str.lower(input('\nWould you like to confirm order?\n[yes]\n[no]\n')) 
						if confirm_order == 'yes':
							#confirm order
							#confirm_order removes relevant ordered foods from inventory
							new_order.confirm_order(available_foods)	

							queue.add_order(new_order)

							print('Your order has been confirmed \nYour order is:\n')
							print('Total cost: {}$'.format(new_order.get_price_total()))
							queue.print_order(new_order)
							order_id = queue.get_order_id(new_order)
							print('Your order ID is: {}\nPlease remember it!\n'.format(order_id))
							end_process = True
							process = True

						elif confirm_order == 'no':
							end_process == False

							print('You are now being redirected back to the front page...')

					elif instruction == 'view order':
						print('\n')
						queue.print_order(new_order)
						print('\n')
						
					elif instruction == 'edit order':
						instruction= str.lower(input('What would you like to do with your order?\n[remove item]\n[add item]\n[cancel order]\n[return]\n'))
						if instruction == 'remove item':
							print('Here is your current order:\n\n{}'.format(new_order))
							attempt = False
							while attempt != True:
								item = input('Please enter the name of the food you would like removed? (Please do not specify quantity and size yet.)\n')
								
								#check that the item exists
								if item in available_foods.get_list():
									#check for item's size:
									if available_foods.inv[item].type.find('main') != -1:
										size = None
										#quantity = input('How many of {} would you like to remove?\n'.format(item))
										#new_order.remove_item(item,quantity,size)

									elif available_foods.inv[item].type == 'sides':
										size = str.lower(input('Please specify the size of the {} you would like to remove (small, medium, large)\n'.format(item)))


									elif available_foods.inv[item].type == 'drinks':
										if available_foods.inv[item].class_type() == "Milliliters":
											size = str.lower(input('Please specify the size of the {} you would like to remove (small, medium)\n'.format(item)))
										else:
											size = None


									quantity = input('How many of {} would you like to remove?\n'.format(item))
									new_order.remove_item(item,quantity,size)	

									print('{} of {} has been removed\n'.format(quantity,item))
									print('\nYour current order is:\n\n{}\n'.format(new_order))	

									attempt = True

								else:
									retry = str.lower(input('Your input of "{}" does not exist on the menu. Would you like to try again?\n[yes]\n[no]\n'.format(item)))
									if retry == 'no':
									#exit the loop to ask to confirm order again
										attempt = True

						elif instruction == 'add item':
							
							see_menu = False
							while see_menu == False:
								see_menu = str.lower(input('Would you like to see the menu again?\n[yes]\n[no]\n[return]\n'))
								if see_menu == 'yes':
									#m.view_menu(available_foods, menu_choice)
									new_order = m.order_from_menu(available_foods, new_order, menu_choice)
								elif see_menu == 'no':
									new_order = m.order_from_menu(available_foods, new_order, menu_choice)
								elif see_menu == 'return':
									print('Returning to an earlier page...\n')
								else:
									print('Invlaid input. Please enter yes, no, or to return to an earlier choice, return.')
									see_menu = False

						elif instruction == 'cancel order':
							new_order.cancel_order(available_foods)
							print('Your order has been cancelled.\n')
							end_process = True


						elif instruction == 'return':
							end_process = False

						else:
							print('Please enter valid instructions.')

					elif instruction == 'exit':
						instruction = str.lower(input('Your order is unconfirmed. Exiting now will erase your order. Proceed to exit?\n[yes]\n[no]\n'))
						if instruction == 'yes':
							new_order.cancel_order(available_foods)
							print('Your order has been cancelled.\n')
							end_process = True
						elif instruction == 'no':
							print('You are being redirected back to order page.\n')
						else:
							print('You have not input a valid instruction. Returning to order page.')
					else:
						print('Please input a valid instruction.')

			elif instruction == 'view order status':
				check = 'checking'
				while check != 'exit':
					order_id = input('What is your order ID?\n')
					
					if order_id != 'exit':
						#if queue.get_order(order_id):
						try:
							order_id = int(order_id)
							if queue.get_order(order_id):
								confirm_order = True
								check = 'exit'
							else:
								print('Order ID {} does not exist. Please try again, or enter exit to return to login\n'.format(order_id))
						except:
							print('You have not entered a valid order id. Please try again, or enter exit to return to login\n')

					elif order_id == 'exit':
						print('You are being redirected back to login page...')
						process = True
						check = 'exit'

					else:
						print('You have not entered a valid order id. Please try again, or enter exit to return to login\n')

			elif instruction == 'return to login':
				print('\n')
				process = True

			else:
				print('You have input an invalid instruction.\nYou are being redirected back to the login page...')
				process = True



		if confirm_order == True:			
			check == False
			while check != True:
				instruction = input('Your order is being processed by XxxDinerDashxxX! What would you like to do now?\n[view my order]\n[view order status]\n[return to login]\n')
				if instruction == 'view my order':
					print('\n')
					queue.print_order(new_order)
					print('\n')
				elif instruction == 'view order status':
					print('Your order status is {}'.format(new_order.get_status()))
					print('\n')

				elif instruction == 'return to login':
					print('You will be redirected back to the login page.\n')
					check = True
					process = True
				else:
					print('Invalid input. Please try again.\n')

		if login == 'staff':
			print('\nWelcome XxxDinerDashxxX Staff')
			
			process = staff.staff_interface(available_foods, process, queue)

	elif process == 'exit':
		#free the memories
		del available_foods
		exit()

	else:
		print('Please input valid instruction of login or exit.')
		process = True

#let the memory be free
del available_foods
#free(available_foods)
