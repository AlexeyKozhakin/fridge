from decimal import Decimal
from datetime import datetime

DATE_FORMAT = '%Y-%m-%d'

def add(items, title, amount, expiration_date=None):
    date_obj = datetime.datetime.strptime(expiration_date, '%Y-%m-%d')
    if title in items.keys():
        items[title].append({'amount': Decimal(amount), 'expiration_date': date_obj})


def add_by_note(items, note):
    info=note.split(' ')
    date=info[-1]
    amount=info[-2]
    name=info[:-2]
    str_name=''
    for i in name:
        str_name+=f'{i} '
    am_ad={}
    am_ad['amount']= Decimal(f'{amount}')
    am_ad['expiration_date']=datetime.strptime(date,'%Y-%m-%d')

    if str_name[:-1] in items.keys():
        items[str_name[:-1]].append(am_ad)

    else:
        food=[]
        food.append(am_ad)
        items[str_name[:-1]]=food
    return items


def find(items,needle):
    names=[]
    for item in items.keys():
        if needle in item:
            names.append(item)
    return names


def amount(items, needle):
    count=0
    for item in items[needle.capitalize()]:
        count+=item['amount']
    return count

def expire(items, in_advance_days=0):
    pass
