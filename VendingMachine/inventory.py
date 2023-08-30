class Inventory:

    def __init__(self, isle_size):

        self.product_count_map = {}
        self.isle_product_map = {}
        self.aisle = [i for i in range(isle_size)]

    def get_product(self, isle_no):

        product = self.isle_product_map[isle_no]
        if not product:
            raise Exception("No Product on given isle")
        return product

    def add_product(self, product):

        if not len(self.aisle):
            raise Exception("No aisle to add product")

        isle_number = self.aisle.pop()

        self.isle_product_map[isle_number] = product
        self.product_count_map[product] = self.product_count_map.get(product, 0) + 1

    def remove_product(self, isle_no):

        if isle_no not in self.isle_product_map:
            raise Exception("No such isle")

        product = self.isle_product_map[isle_no]

        if product not in self.product_count_map or self.product_count_map[product] <= 0:
            raise Exception("given product not available.")

        self.product_count_map[product] -= 1
        del self.isle_product_map[isle_no]
        self.aisle.append(isle_no)










