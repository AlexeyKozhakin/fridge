import datetime
from decimal import Decimal
from fridge import *


import datetime
from decimal import Decimal

print(add_by_note({}, 'Яйца Фабрики №1 4 2023-07-15'))

print({'Яйца Фабрики №1': [{'amount': Decimal('4'),
                      'expiration_date': datetime.date(2023, 7, 15)}]})

print(add_by_note({}, 'Макароны 1.5'))

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
print(1)
print(amount(goods, 'морковь'))
print(5)

