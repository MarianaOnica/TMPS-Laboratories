from Command import * 
from Builder import *
from Beverage import *
from Salad import *
import time

class Waiter(object):
	def present_menu(self):
		print("Do you want bussiness Lunch or choose by yourself?")
		print("Press:")
		print("1 for Bussiness Lunch")
		print()
		print("2 for whole menu")
		print()

	def choose_menu(self, digit):
		if digit == 1:
			print("OOo Your are planning a bussiness meeting")
			print("We have some interesting offers for you")
			self.bussiness_menu = BussinessLunchMenu()
			self.bussiness_menu.show_menu()
			self.bussiness_menu.command_to_kitchen()

		else:
			print("We have a very very large variety of dishes  ")
			self.whole_lunch = WholeMenu()
			self.whole_lunch.show_whole_menu()

#################################################

class BussinessLunchMenu(object):
	# def __init__(self):


	def show_menu(self):
		print()
		print("---------------------Lunch 1:-------------------")
		print("1. Becon Monster Burger", "Caezar Salad", "Juice", sep = " + ")
		print("---------------------Lunch 2:-------------------")
		print("2. Chicker Grill Burger", "Tuna Salad", "Water", sep = " + ")
		print()
		print("Do you need time to decide? Press Yes")
		answer = input()
		if answer == "Yes":
			print("I'll come back in some seconds")
			time.sleep(15)
		print("Enter 1 or 2 for which you want")
		self.answer = int(input())

	def command_to_kitchen(self):
		if self.answer == 1:
			lunch = Lunch1() # receiver
			command_lunch = LunchCommand(lunch) # concrete command

			meal_invoker = MealInvoker(command_lunch); # invoker
			meal_invoker.invoke()

		if self.answer == 2:
			lunch2 = Lunch2() # receiver
			command_lunch2 = Lunch2Command(lunch2) # concrete command

			meal_invoker = MealInvoker(command_lunch2); # invoker
			meal_invoker.invoke()

		print("Thank you for choosing our poor VerySlowlyPreparedLaboratoryOfBurgers")
		print("You were served by Mariana & Cristina")

#################################################

class WholeMenu(object):
	def show_whole_menu(self):
		print()
		print("Burgers:")
		print("1. Becon Monster Burger")
		print("2. Chicker Grill Burger")
		print("0. Don't want burger")
		print("-------------------------")
		print("Salads:")
		print("1. Caesar Salad")
		print("2. Tuna Salad")
		print("3. Fruit Salad")
		print("0. Don't want burger")
		print("-------------------------")

		print("Beverages:")
		print("1. Juice")
		print("2. Water")
		print("3. Coffee")
		print("4. Tea")
		print("0. Don't want burger")
		print("-------------------------")
		print()
		print("Do you need time to decide? Press Yes")
		answer = input()
		if answer == "Yes":
			print("I'll come back in some seconds")
			time.sleep(15)
		print("Choose burger")
		self.answer = int(input())
		if self.answer == 1:
			director = Director()
			director.builder = BuilderBeconMonster()
			burger = director.prepare_burger()
			# print (burger)
		if self.answer == 2:
			director = Director()
			director.builder = BuilderChickenGrill()
			burger = director.prepare_burger()

		print("Choose Salad")
		self.answer = int(input())
		if self.answer == 1:
			salad = Salad.factory_method("CesarSalad")
		if self.answer == 2:
			salad = Salad.factory_method("TunaSalad")
		if self.answer == 3:
			salad = Salad.factory_method("FruitSalad")

		print("Choose Beverage")
		self.answer = int(input())
		if self.answer == 1:
			beverage = Beverage.factory_method("Juice")
		if self.answer == 2:
			beverage = Beverage.factory_method("Water")
		if self.answer == 3:
			beverage = Beverage.factory_method("Coffee")
		if self.answer == 4:
			beverage = Beverage.factory_method("Tea")

		print (burger)
		salad.get_salad()
		beverage.get_beverage()
		print("Lunch is being made")
		print("Thank you for choosing our poor VerySlowlyPreparedLaboratoryOfBurgers")
		print("You were served by Mariana & Cristina")
		

##################################################

if __name__ == "__main__":
	waiter = Waiter()
	print("=================Welcome to VerySlowlyPreparedLaboratoryOfBurgers :D====================-")
	print()
	print("You will be served by our only 2 workers: Cristina & Mariana!")
	print()
	print("Here is the menu:")
	waiter.present_menu()
	chosen_menu = int(input())
	waiter.choose_menu(chosen_menu)



