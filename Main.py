from Items import Item
from Items import availableProductsNames
import ShopAssistant
import ShopShelf
import random

selectedProducts = []  # Contains objects of Items


def clear_console(create_a_shelf):
    print('\n'*12)
    if create_a_shelf:
     Shelf.write_shelf()


def select_products():
    # Selects new product object and adds it to selectedProducts. It gives to
    # product number, name from randomised availableProducts and random price

    amountOfPorducts = 10  # Tells how many products we want to Select
    if availableProductsNames.__len__() < amountOfPorducts or amountOfPorducts < 1:
        raise Exception('Wrong amountOfProducts value')
    for i in range(amountOfPorducts):
        r = int(random.uniform(0, availableProductsNames.__len__()))
        product = Item(i + 1, availableProductsNames[r], int(random.uniform(1, 10)) / 2)
        selectedProducts.append(product)
        availableProductsNames.remove(availableProductsNames[r])  # Ensures that the same names aren't chosen again
    for i in selectedProducts:
        availableProductsNames.append(i.name)


select_products()

Shelf = ShopShelf.ShopShelf()
Shelf.generate_shelf(selectedProducts)
Shelf.write_shelf()

ShopAssistant.ask_for_products()
