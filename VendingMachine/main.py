from vending_machine import VendingMachine
from product import Product

if __name__ == "__main__":

    vending_machine = VendingMachine()

    vending_machine.add_inventory_size(10)
    vending_machine.add_amount(1000)

    li = ["coke", "pepsi", "dairymilk", "puff"]
    price = 100
    for i in range(1, 10):
        ind = 3 % i
        product = Product(name=li[ind], price=price)
        vending_machine.add_product(product)
        price += 10

    vending_machine.insert_coin(200)
    vending_machine.press_button(5)
