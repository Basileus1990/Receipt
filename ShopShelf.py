class ShopShelf:
    def __init__(self):
        self.width = 61
        if not (self.width - 1) % 4 == 0:
            raise Exception('Wrong width of Shelf')
        self.height = 9
        if not (self.height - 1) % 4 == 0:
            raise Exception('Wrong height of Shelf')
        self.shelf = [[' '] * self.height for i in range(self.width)]

    def generate_shelf(self, products):
        productsCount = 0
        productsCountInCurrentLine = 0
        for i in range(self.height):
            for j in range(self.width):
                if (i == 0 or i % 4 == 0):
                    for k in range(self.width):
                        self.shelf[k][i] = '_'
                    break
                if (i == 1 or i % 5 == 0) and j % 5 == 0 and productsCount < products.__len__():
                    if self.check_length_of_line(i + 1, 0, j - 1) + products[productsCount].name.__len__() > self.width:
                        productsCountInCurrentLine = 0
                        break
                    self.shelf[j][i + 1] = products[productsCount].name

                    width = self.check_length_of_line(i + 1, 0, j - 1) + (products[productsCount].name.__len__() - 1) / 2
                    self.shelf[int(width)][i] = products[productsCount].number

                    if products[productsCount].name.__len__() < 3 and products[productsCount].number == '1':
                        width = 0
                    else:
                        width -= (1 + productsCountInCurrentLine * 2)
                    if round(width) > width:
                            pass
                    self.shelf[round(width)][i + 2] = products[productsCount].price
                    productsCount += 1
                    productsCountInCurrentLine += 1

    def write_shelf(self):
        for i in range(self.height):
            for j in range(self.width):
                print(self.shelf[j][i], end='', sep='')
            print()

    # returns current length of line in shelf
    def check_length_of_line(self, line, start, stop):
        sumOfCharacters = 0
        for i in range(start, stop + 1):
            sumOfCharacters += self.shelf[i][line].__len__()
        return sumOfCharacters
