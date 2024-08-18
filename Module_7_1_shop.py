# класс Shop
from Module_7_1_product import Product


class Shop:
    __file_name = 'products.txt'

    def __init__(self):
        self.__products_list = []
        self.get_products()
        pass

    def get_products(self):
        file = open(self.__file_name, 'r')
        products_list = file.read()
        file.close()
        items_list = products_list.strip('\n').split('\n')
        for product_item in items_list:
            if len(product_item):
                product_item = product_item.replace(' ', '').split(',')
                product_item[1] = float(product_item[1])
                self.__products_list.append(Product(*product_item))
        return products_list

    def add(self, *products_list):
        for new_product in products_list:
            if not self.is_product_in_list(new_product):
                self.__products_list.append(new_product)
                # print(f'Added new product {new_product.name}')
            else:
                print(f'Продукт {new_product} уже есть в магазине')
        self.save_product_list()

    def save_product_list(self):
        file = open(self.__file_name, 'w')
        for product in self.__products_list:
            file.write(product.__str__() + '\n')
        file.close()

    def is_product_in_list(self, product: Product):
        for present_product in self.__products_list:
            if product == present_product:
                return True
        return False
