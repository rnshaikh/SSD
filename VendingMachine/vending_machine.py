from inventory import Inventory
from product import Product
from state import NoCoinInsertedState, CoinInsertedState, DispenseState


class VendingMachine:

    def __init__(self):

        self.inventory = None
        self.amount = 0
        self.no_coin_inserted_state = NoCoinInsertedState(self)
        self.coin_inserted_state = CoinInsertedState(self)
        self.dispense_state = DispenseState(self)
        self.state = self.no_coin_inserted_state
        self.inserted_amount = 0

    def add_inventory_size(self, size):
        self.inventory = Inventory(size)

    def add_product(self, product):
        self.inventory.add_product(product)

    def add_amount(self, amount):
        self.amount = amount

    def insert_coin(self, amount):
        self.state.insert_coin(amount)

    def press_button(self, isle_no):
        import pdb
        pdb.set_trace()
        product, change = self.state.press_button(isle_no)
        self.state.dispense(product, change)

    def set_state(self, state_obj):
        self.state = state_obj

    def get_no_coin_inserted_state(self):
        return self.no_coin_inserted_state

    def get_inserted_coin_state(self):
        return self.coin_inserted_state

    def get_dispense_state(self):
        return self.dispense_state
