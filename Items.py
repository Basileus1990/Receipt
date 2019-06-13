availableProductsNames = ['ty', 'Chleb', 'Masło', 'Leki', 'Jogurt', 'Wieprzowina',
                          'Woda niegazowana', 'Ser', 'CocaCola', 'Mleczko',
                          'Kurczak', 'Jakieś niedobre to','Woda Polaris',
                          'Cheatos', 'Pepsi', 'Hoop Cola']

class Item:

    def __init__(self, number, name, price):
        self.number = number.__str__()
        self.name = name.__str__()
        self.price = price.__str__()
