import Main
from ChosenProducts import ChosenProduct


# class meant to check which and how many products you want to buy. then he displays a receipt
def ask_for_products():
    list_of_chosen_products = []
    while True:
        Main.clear_console(True)
        chosenNumber = chose_product()
        if chosenNumber == 0:
            break
        howMany = chose_how_many()
        if howMany == 0:
            continue

        list_of_chosen_products.append(ChosenProduct(Main.selectedProducts[chosenNumber - 1], howMany))
    write_receipt(list_of_chosen_products)


def chose_product():
    while True:
        print('\n' + ('#'*61))
        print('Which product do you want to buy? Chose a number from above. If no more of them write \"0\"')
        try:
            chosenNumber = int(input())
            if chosenNumber < 0 or chosenNumber > Main.selectedProducts.__len__():
                raise Exception
        except(Exception):
            Main.clear_console(False)
            print('You wrote a wrong number!!! Please try again (: Hit enter to continue')
            input()
            Main.clear_console(True)
            continue
        break
    return chosenNumber


def chose_how_many():
    while True:
        print('How much of it you want to buy? Write 0 to go back')
        try:
            howMany = int(input())
            if howMany < 0:
                raise Exception
        except(Exception):
            Main.clear_console(False)
            print('You wrote a wrong number!!! Please try again (: Hit enter to continue')
            input()
            Main.clear_console(True)
            continue
        break
    return howMany


def write_receipt(list_of_chosen_products):
    Main.clear_console(False)
    if list_of_chosen_products.__len__() == 0:
        print('You didn\'t chose any product!')
        return
    print('You bought those products:')
    for i in list_of_chosen_products:
        print(i.product.name + ' in amount of ' + i.amountOfProduct.__str__() +
              '  Total cost equals: ' + (float(i.amountOfProduct) * float(i.product.price)).__str__())

    # calculates sum cost of every product
    total_cost = 0.0
    for  i in list_of_chosen_products:
        total_cost += float(i.amountOfProduct) * float(i.product.price)
    print('In total you will have to pay: ' + total_cost.__str__())
