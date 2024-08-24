# Домашнее задание по теме "Режимы открытия файлов"
# Основной модуль. Здесь определяется поведение программы.

from Module_7_1_product import Product
from Module_7_1_shop import Shop

shop_1 = Shop()

potato_1 = Product('Potato', 50.5, 'Vegetables')
potato_2 = Product('Potato', 5.5, 'Vegetables')
spaghetti_1 = Product('Spaghetti', 3.4, 'Groceries')

print(spaghetti_1)
shop_1.add(potato_2, potato_1, spaghetti_1)
print(shop_1.get_products())

