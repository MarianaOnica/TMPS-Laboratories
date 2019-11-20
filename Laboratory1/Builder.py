# Director    
class Director(object):
	def __init__(self):
		self.builder = None

	def prepare_burger(self):
		self.builder.new_burger()
		self.builder.choose_bun()
		self.builder.choose_meat()
		self.builder.choose_souce()
		self.builder.choose_cheese()
		return self.builder.burger

##################################

# Abstract Builder  
class Builder(object):
	def __init__(self):
		self.burger = None

	def new_burger(self):
		self.burger = Burger()

################################

# Concrete Builder
class BuilderBeconMonster(Builder):
	def choose_bun(self):
		self.burger.bun = 'Brioche'

	def choose_meat(self):
		self.burger.meat = 'Beef Patty'

	def choose_souce(self):
		self.burger.souce = 'Ketchup'

	def choose_cheese(self):
		self.burger.cheese = 'Cheedar'

class BuilderChickenGrill(Builder):
	def choose_bun(self):
		self.burger.bun = 'Brioche'

	def choose_meat(self):
		self.burger.meat = 'Breade Chicken Fillet'

	def choose_souce(self):
		self.burger.souce = 'Grill'

	def choose_cheese(self):
		self.burger.cheese = 'Gauda'

############################################

# Product
class Burger(object):
	def __init__(self):
		self.bun = None
		self.meat = None
		self.souce = None
		self.cheese = None

	def __repr__(self):
		return 'Bun: %s | Meat: %s | Souce: %s | Cheese: %s' % (self.bun, self.meat, self.souce, self.cheese)

#############################################

#Client
# if __name__ == "__main__":
# 	director = Director()
# 	director.builder = BuilderBeconMonster()
# 	burger = director.prepare_burger()
# 	print burger