class Juice(object):
    def factory_method(type):
        if type == "AppleJuice":
            return AppleJuice()
        if type == "OrangeJuice":
            return OrangeJuice()
    factory_method = staticmethod(factory_method)

class AppleJuice(Juice):
    def getJuice(self, price):
        print("Your Apple Juice is already done. You can take it.")
        price += 20
        return price

class OrangeJuice(Juice):
    def getJuice(self, price):
        print("Your Orange Juice is already done. You can take it.")
        price += 20
        return price

class PeachJuice(Juice):
    def getJuice(self, price):
        print("Your Peach Juice is already done. You can take it.")
        price += 20
        return price

class MultifruitJuice(Juice):
    def getJuice(self, price):
        print("Your Multifruct Juice is already done. You can take it.")
        price += 20
        return price




   
