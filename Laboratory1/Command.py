import abc
from Builder import *
from Beverage import *
from Salad import *

class Command(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def execute(self):
        pass

class LunchCommand(Command):
    def __init__(self, lunch):
        self.lunch = lunch

    def execute(self):
        self.lunch.make_lunch()

class Lunch2Command(Command):
    def __init__(self, lunch2):
        self.lunch2 = lunch2
        # self.price = price

    def execute(self):
        self.lunch2.make_lunch2()

class Lunch1:
    def make_lunch(self):
        director = Director()
        director.builder = BuilderBeconMonster()
        burger = director.prepare_burger()
        print (burger)

        salad = Salad.factory_method("CesarSalad")
        salad.get_salad()

        beverage = Beverage.factory_method("Juice")
        beverage.get_beverage()
        print("Lunch is being made")


class Lunch2:
    def make_lunch2(self):
        director = Director()
        director.builder = BuilderChickenGrill()
        burger = director.prepare_burger()
        print("The second type of lunch is being made")
        print (burger)

        salad = Salad.factory_method("TunaSalad")
        salad.get_salad()

        beverage = Beverage.factory_method("Water")
        beverage.get_beverage()
        print("Lunch is being made")

class MealInvoker:
    def __init__(self, command):
        self.command = command
        # self.price = price

    def set_command(self, command):
        self.command = command
        # self.price = price

    def invoke(self):
        self.command.execute()

# if __name__ == '__main__':
#     lunch = Lunch() # receiver
#     command_lunch = LunchCommand(lunch) # concrete command

#     dinner = Dinner() # receiver
#     command_dinner = DinnerCommand(dinner) # concrete command

#     meal_invoker = MealInvoker(command_lunch); # invoker
#     meal_invoker.invoke()

#     meal_invoker.set_command(command_dinner)
#     meal_invoker.invoke()