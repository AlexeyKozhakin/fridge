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
    for item in items.keys():
        lower_item=item.lower()
        if needle.lower() in lower_item:
            names.append(item)
    return names


def amount(items, needle):
    keys=list(items.keys())
    keys_low=[]
    for i in keys:
        keys_low.append(i.lower())
    keys_ok=[]
    for key in keys_low:
        if needle.lower() in key:
            keys_ok.append(key)

    if len(key)!=0:
        count=Decimal(0)
        for key_ok in keys_ok:
            id=keys_low.index(key_ok)
            for item in items[keys[id]]:
                count+=item['amount']
        return count 
    else:
        return Decimal(0)

def expire(items, in_advance_days=0):
    product=[]
    crutch={}
    for item in items.keys():
        for it in items[item]:
            if str(it['expiration_date']) != 'None':
                delta= it['expiration_date'] - datetime.datetime.now().date()
                if delta.days<=in_advance_days:
                    if item in crutch.keys():
                        crutch[item]+= it['amount']
                    else: 
                        crutch[item]=it['amount']
    for item in crutch.keys():
        good_list=[]
        good_list.append(item)
        good_list.append(crutch[item])
        good=tuple(good_list)
        product.append(good)
    return product

