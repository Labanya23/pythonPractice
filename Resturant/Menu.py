class Food:
    def __init__(self, name,price) ->None:
        self.name = name
        self.price = price
        self.cooking_time = 15

class Burger(Food):
    def __init__(selfself, name, price, meat) ->None:
        super().__init__(name, price)
        self.meat = meat
        self.ingredients = ingredeients

class Pizza(Food):
    def __init__(self,name,price,size,ingredients, toppings) -> None:
        super().__init__(name, price)
        self.size = size
        self.toppings = toppings

class Drinks(Food):
    def __init__(self, name, price, isCold = True) -> None:
        super().__init__(name,price)
        self.isCold = isCold

        #composition
class Menu:
    def __init__(self) -> None:
        self.pizzas = []
        self.burgers = []
        self.drinks = []

    def add_meny_item(selfself, item_type,item):
        if item_type == 'pizza':
            self.pizzas.append(item)
        elif item_type =='burger':
            self.burgers.append(item)
        elif item_type == 'drinks':
            self.drinks.append(item)

    def remove_pizza(self, pizza):
        if pizza in self.pizzas:
            self.pizzas.remote(pizza)

    def show_menu(self):
        for pizza in self.pizzas:
            print(f'name: {pizza.name} price: {self.price}')
        for burgers in self.burgers:
            print(f'name: {burger.name} price:{burger.price}')

        for drink in self.drinks:
            print(f'name:{drink.name} price: {drink.price}')



