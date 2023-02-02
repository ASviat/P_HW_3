# 4. *Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре.
# В кортеже должно быть два элемента — номер товара и словарь с параметрами
# (характеристиками товара: название, цена, количество, единица измерения).
# Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.

# Пример готовой структуры:
# [
# (1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
# (2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
# (3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
# ]

# Далее необходимо собрать аналитику о товарах. Реализовать словарь,
# в котором каждый ключ — характеристика товара, например название,
# а значение — список значений-характеристик, например список названий товаров.

# Пример:
# {
# “названия”: [“компьютер”, “принтер”, “сканер”],
# “цены”: [20000, 6000, 2000],
# “количества”: [5, 2, 7],
# “ед”: [“шт.”]
# }

my_counter = int(input('Введите количество товаров: '))

my_list = []


def makeTuple():
    {
    }
    return (tuple(input('Напиши через пробел название товара, цену, количество единиц в шт.: ').split(' ')))


for i in range(0, my_counter):
    my_list.append(makeTuple())

my_dictionary = {}

for i in range(0, my_counter):
    k = 0
    my_dictionary[f'Наименование №{i+1}'] = f'Товар: {my_list[i][k]}, Цена: {my_list[i][k+1]} Шт: {my_list[i][k+2]}'

print(my_dictionary)

my_second_dictionary = {}
my_product = []
my_price = []
my_count = []
for i in range(0, my_counter):
    k = 0
    my_product.append(my_list[i][k])
for i in range(0, my_counter):
    k = 1
    my_price.append(my_list[i][k])
for i in range(0, my_counter):
    k = 2
    my_count.append(my_list[i][k])

my_second_dictionary['Товар'] = my_product
my_second_dictionary['Цена'] = my_price
my_second_dictionary['Кол.-во штук'] = my_count

print(my_second_dictionary)
