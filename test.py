import datetime
from decimal import Decimal
from fridge import *


import datetime
from decimal import Decimal


#=========== Expire =============================
print('Expire')
import datetime as dt
from decimal import Decimal
now=dt.date.today()
date1=now + dt.timedelta(-1)
date2=now + dt.timedelta(2)
date3=now + dt.timedelta(1)
goods = {
    'Хлеб': [
        {'amount': Decimal('1'), 'expiration_date': None},
        {'amount': Decimal('1'), 'expiration_date': date1}
    ],
    'Яйца': [
        {'amount': Decimal('2'), 'expiration_date': date2},
        {'amount': Decimal('3'), 'expiration_date': date3}
    ],
    'Вода': [{'amount': Decimal('100'), 'expiration_date': None}]
}

print(expire(goods, in_advance_days=0))
print(expire(goods, in_advance_days=1))
print(expire(goods, in_advance_days=2))
print('Amount')
#=========== Amount =============================
goods = {
    'Яйца': [{'amount': Decimal('1'), 'expiration_date': None}],
    'Морковь': [
        {'amount': Decimal('2'), 'expiration_date': datetime.date(2023, 8, 1)},
        {'amount': Decimal('3'), 'expiration_date': datetime.date(2023, 8, 6)}
    ],
    'вода': [{'amount': Decimal('2.5'), 'expiration_date': None}],
    'Яйца': [{'amount': Decimal('1'), 'expiration_date': datetime.date(2023, 6, 24)}],
    'Яйца Гусиные': [{'amount': Decimal('4'), 'expiration_date': datetime.date(2023, 7, 15)}],
    'Морковь': [{'amount': Decimal('2'), 'expiration_date': datetime.date(2023, 8, 6)}]
}
print(type(amount(goods, 'Мороженное')))
print(amount(goods, 'Мороженное'))
print(0)
print(type(amount(goods, 'яйца')))
print(amount(goods, 'яйца'))
print(1)
print(amount(goods, 'МоРковь'))
print(5)
print(amount(goods, 'ВоДа'))
print(2.5)
print(amount(goods, 'Вода'))
print(2.5)
print('Find')
#=========== Find ===============================
#===1
goods = {
    'Яйца': [{'amount': Decimal('1'), 'expiration_date': datetime.date(2023, 6, 24)}],
    'Яйца Гусиные': [{'amount': Decimal('4'), 'expiration_date': datetime.date(2023, 7, 15)}],
    'Морковь': [{'amount': Decimal('2'), 'expiration_date': datetime.date(2023, 8, 6)}]
}
print(find(goods, 'яйца гусиные'))
print(['Яйца Гусиные'])
#===2
goods = {
    'Яйца': [{'amount': Decimal('1'), 'expiration_date': datetime.date(2023, 6, 24)}],
    'Яйца гусиные': [{'amount': Decimal('4'), 'expiration_date': datetime.date(2023, 7, 15)}],
    'Морковь': [{'amount': Decimal('2'), 'expiration_date': datetime.date(2023, 8, 6)}]
}

# Ищем продукты, в названии которых есть подстрока "йц". 
# Регистр символов не должен влиять на поиск.
print(find(goods, 'яй'))
print(['Яйца', 'Яйца гусиные'])

print('Add by note')
#=========== Add by note ========================


print(add_by_note({}, 'Яйца Фабрики №1 4 2023-07-15'))

print({'Яйца Фабрики №1': [{'amount': Decimal('4'),
                      'expiration_date': datetime.date(2023, 7, 15)}]})

print(add_by_note({}, 'Макароны 1.5'))

print(add({}, 'Макароны', Decimal('1.5')))

print({'Макароны': [{'amount': Decimal('1.5'), 'expiration_date': None}]})