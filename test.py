import datetime
from decimal import Decimal
from fridge import *


import datetime
from decimal import Decimal

print(add_by_note({}, 'Яйца Фабрики №1 4 2023-07-15'))

print({'Яйца Фабрики №1': [{'amount': Decimal('4'),
                      'expiration_date': datetime.date(2023, 7, 15)}]})



print(add({}, 'Макароны', Decimal('1.5')))

print({'Макароны': [{'amount': Decimal('1.5'), 'expiration_date': None}]})



print(add({}, 'Яйца Фабрики №1', Decimal('4'), '2023-07-15'))

print({'Яйца Фабрики №1': [{'amount': Decimal('4'),
                      'expiration_date': datetime.date(2023, 7, 15)}]})

goods = {
    'Яйца': [{'amount': Decimal('1'), 'expiration_date': None}],
    'Морковь': [
        {'amount': Decimal('2'), 'expiration_date': datetime.date(2023, 8, 1)},
        {'amount': Decimal('3'), 'expiration_date': datetime.date(2023, 8, 6)}
    ],
    'Вода': [{'amount': Decimal('2.5'), 'expiration_date': None}]
}


print(amount(goods, 'яйца'))
# Вывод: 1
print(amount(goods, 'морковь'))
# Вывод: 5

import datetime as dt
from decimal import Decimal

goods = {
    'Хлеб': [
        {'amount': Decimal('1'), 'expiration_date': None},
        {'amount': Decimal('1'), 'expiration_date': dt.date(2023, 12, 9)}
    ],
    'Яйца': [
        {'amount': Decimal('2'), 'expiration_date': dt.date(2023, 12, 12)},
        {'amount': Decimal('3'), 'expiration_date': dt.date(2023, 12, 11)}
    ],
    'Вода': [{'amount': Decimal('100'), 'expiration_date': None}]
}



# Вызов функции 10 декабря 2023 года
print(expire(goods))
# Вывод: [('Хлеб', Decimal('1'))]
print(expire(goods, 1))
# Вывод: [('Хлеб', Decimal('1')), ('Яйца', Decimal('3'))]
print(expire(goods, 2))
# Вывод: [('Хлеб', Decimal('1')), ('Яйца', Decimal('5'))]


import datetime
from decimal import Decimal

# Холодильник пуст:
goods = {}


# Добавляем продукт с названием 'Яйца гусиные', количество - 4 шт.
add_by_note(goods, 'Яйца гусиные 4 2023-07-15')

# Словарь goods должен стать таким:

# goods = {
#     'Яйца гусиные': [
#         {'amount': Decimal('4'), 'expiration_date': datetime.date(2023, 7, 15)}
#     ]
# }