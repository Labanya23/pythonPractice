from Menu import Pizza, Burger, Drinks, Menu
from resturant import resturant
from User import Chef,Customer,Server,Manager
from Order import Order

def main():
    menu =Menu()
    pizza_1 = Pizza('chicken pizza',600,'large',['chiken','onion'])
    menu.add_menu_item('pizza',pizza_1)
    pizza_2 = Pizza('alur vorta pizza' ,400,'large',['pottato','onion'])
    menu.add_menu_item('pizza',pizza_2)
    pizza_3 =Pizza('Dal Pizza', 500, 'large',['dal','oil'])
    menu.add_menu_item('pizza', pizza_3)

    #add burger to the menu
    burger_1 =Burger('naga burger',1000,'chicken',['bread','chilli'])
    menu.add_menu_item('burger',burger_1)
    burger_2 = Burger('CHII Burger',1200,'chii',['chiii','fish'])
    menu.add_menu_item('burger',burger_2)

#add drink to the menu

   coke = Drinks('Coke',50,True)
   menu.add_menu_item('drinks',coke)
   coffee = Drinks('Mocha', 300,Flase)
   menu.add_menu_item('drinks',coffee)

   menu.show_menu()

   Resturant =  resturant('Foodie Resturant',2000,menu)
   manager = Manager('Kala chan manager', 5 ,'kala@chan.com','putre',1500,'january','core')
   Resturant.add_employee('manager',manager)
   chef = Chef('Rustom Baburchi', 6, 'chup@rustom.com','rustomnagar',1500,'february','Chef','everything')
   Resturant.add_employee('chef',chef)
   server = Server('Chotu server',6,'nai@jai.com','resturant',200,'march 1,2024','server')
   Resturant.add_employee('server',server)

   Resturant.show_employes()

   customer_1 = Customer('labanya',6,'labanya@gmail.com','kushtia',)
   order_1 = Order(customer_1,[pizza_3,coffee])
   customer_1.pay_for_order(order_1)
   Resturant.add_order(order_1)

   #customer one paying for order 1
   Resturant.recieve_payments(order_1,200,customer_1)

   print('revenue and balance'Resturant.revenue,resturant.balance)

  customer_2= Customer('labanya', 6, 'labanya@gmail.com', 'kushtia', )
  order_2 = Order(customer_2, [pizza_1,burger_1, coffee])
  customer_2.pay_for_order(order_2)
  Resturant.add_order(order_2)

# customer one paying for order 1
  Resturant.recieve_payments(order_2, 200, customer_2)

print('revenue and balance after second customer'Resturant.revenue,resturant.balance)

#call the main
if __name__ == '__main__':
    main()