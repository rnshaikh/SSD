from abc import ABC, abstractmethod


class State():

    @abstractmethod
    def insert_coin(self, coin):
        pass

    @abstractmethod
    def press_button(self, isle_no):
        pass

    @abstractmethod
    def dispense(self, product, change):
        pass


class NoCoinInsertedState(State):

    def __init__(self, vending_machine):
        self.vending_machine = vending_machine

    def insert_coin(self, coin):
        self.vending_machine.inserted_amount = coin
        self.vending_machine.set_state(self.vending_machine.get_inserted_coin_state())

    def press_button(self, isle_no):
        raise Exception("First Insert Coin")

    def dispense(self, product, change):
        raise Exception("First Insert Coin")


class CoinInsertedState(State):

    def __init__(self, vending_machine):
        self.vending_machine = vending_machine

    def insert_coin(self, coin):
        raise Exception("Coin already inserted")

    def press_button(self, isle_no):
        product = self.vending_machine.inventory.get_product(isle_no)
        if product.price > self.vending_machine.inserted_amount:
            self.vending_machine.inventory.add_product(product)
            raise Exception("Not sufficent amount")

        else:
            change = 0
            if product.price < self.vending_machine.inserted_amount:
                change = self.vending_machine.inserted_amount - product.price
                if self.vending_machine.amount < change:
                    raise Exception("Insufficient balance.")

                else:
                    self.vending_machine.amount -= change

            self.vending_machine.set_state(self.vending_machine.get_dispense_state())
            return product, change

    def dispense(self, product, change):
        raise Exception("Pleas select product first")


class DispenseState(State):

    def __init__(self, vending_machine):
        self.vending_machine = vending_machine

    def insert_coin(self, coin):
        raise Exception("First Insert Coin")

    def press_button(self, isle_no):
        raise Exception("First Insert Coin")

    def dispense(self, product, change):

        if change:
            print("change: ", change)

        print("product:", product.name, product.price)
        self.vending_machine.set_state(self.vending_machine.get_no_coin_inserted_state())
        self.vending_machine.inserted_amount = 0





