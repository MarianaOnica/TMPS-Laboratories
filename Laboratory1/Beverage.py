class Beverage(object):
    def factory_method(type):
        if type == "Juice":
            return Juice()
        if type == "Water":
            return Water()
        if type == "Tea":
            return Tea()
        if type == "Coffee":
            return Coffee()
    factory_method = staticmethod(factory_method)

class Juice(Beverage):
    def get_beverage(self):
        print("Your juice is already done. You can take it.")

class Water(Beverage):
    def get_beverage(self):
        print("Your water is already done. You can take it.")

class Tea(Beverage):
    def get_beverage(self):
        print("Your tea is already done. You can take it.")

class Coffee(Beverage):
    def get_beverage(self):
        print("Your coffee is already done. You can take it.")




   
