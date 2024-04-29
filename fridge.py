from decimal import Decimal
import datetime

DATE_FORMAT = '%Y-%m-%d'

def add(items, title, amount, expiration_date=None):
    if expiration_date==None:
        date_obj=None
    else:
        date_obj = datetime.datetime.strptime(expiration_date, '%Y-%m-%d').date()        
    if title in items.keys():
        items[title].append({'amount': Decimal(amount), 'expiration_date': date_obj})
    else:
        items[title]=[{'amount': Decimal(amount), 'expiration_date': date_obj}]
    return items

def add_by_note(items, note):
    info=note.split(' ')
    
    
    if '-' in info[-1]:
        date=info[-1]
        amount=info[-2]
        name=info[:-2]
        str_name=''
        for i in name:
            str_name+=f'{i} '
        return add(items, str_name.strip(), amount, date)
    else:
        amount=info[-1]
        name=info[:-1]
        str_name=''
        for i in name:
            str_name+=f'{i} '
        return add(items, str_name.strip(), amount)


def find(items,needle):
    names=[]
    ittems_key_list=list(items.keys())
    lower_keys=list(map(lambda num: num.lower(),ittems_key_list))
    for item in lower_keys:
        if needle.lower() in item:
            names.append(item.capitalize())
    return names


def amount(items, needle):
    count=0
    for item in items[needle.capitalize()]:
        count+=item['amount']
    return count

def expire(items, in_advance_days=0):
    product=[]
    crutch={}
    for item in items.keys():
        for it in items[item]:
            if str(it['expiration_date']) != 'None':

                delta= it['expiration_date'] - datetime.datetime.now().date()
                if delta.days<in_advance_days:
                    if item in crutch.keys():
                        crutch[item]+= it['amount']
                    else: 
                        crutch[item]=it['amount']
    for item in crutch.keys():
        good_list=[]
        good_list.append(item)
        good_list.append(crutch[item])
        good=set(good_list)
        product.append(good)
    return product

