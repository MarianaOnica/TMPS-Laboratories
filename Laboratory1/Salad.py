class Salad(object):
    def factory_method(type):
        if type == "CesarSalad":
            return CaesarSalad()
        if type == "TunaSalad":
            return TunaSalad()
        if type == "FruitSalad":
            return FruitSalad()
    factory_method = staticmethod(factory_method)

class CaesarSalad(Salad):
    def get_salad(self):
        print("The Caesar salad was prepared using letuce, cheese, chicken, eggs, oil...")
        # price += 20
        # return price

class TunaSalad(Salad):
    def get_salad(self):
        print("The Tuna salad was done with the help of: white meat tuna, onion, mayonnaise, lemon juice, black peper.... ")
        # price += 20
        # return price

class FruitSalad(Salad):
    def get_salad(self):
        print("The Fruit salad was prepared with different types of exotic and anexotic fruits mixed with cream")
        # price += 20
        # return price