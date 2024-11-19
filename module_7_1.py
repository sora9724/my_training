class Product:
    def __init__(self, name, weight, category):
        self.name = str(name)
        self.weight = float(weight)
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'

class Shop:
    __file_name = 'product.txt'

    def get_products(self):
        file = open(self.__file_name, 'r')
        file_read = file.read()
        file.close()
        return file_read

    def add(self, *products):
        file = open(self.__file_name, 'a')
        existing_products = self.get_products()
        for item in products:
            if str(item) in existing_products:
                print(f'Продукт {item} уже есть в магазине.')
            else:
                file.write(f'{item}\n')
        file.close()

s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__

s1.add(p1, p2, p3)

print(s1.get_products())
