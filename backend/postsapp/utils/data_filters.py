from django.utils import timezone 


import datetime

def data_filter(filters:dict,data):
    date,to_oldest,string = filters
    date = filters[f'{date=}'.split('=')[0]]
    to_oldest = filters[f'{to_oldest=}'.split('=')[0]]
    string = filters[f'{string=}'.split('=')[0]]

    
    if string != None:
        data = data.filter(name__icontains = string)
    if date != None:
        data = data.filter(created__contains=datetime.date(int(date.split("-")[0]),int(date.split("-")[1]),int(date.split("-")[2])))
    if to_oldest != None:
        if to_oldest:    
            data = data.filter(created__lte = datetime.datetime.now(tz=timezone.utc))
        else:    
            data = data.filter(created__gte = datetime.datetime.now(tz=timezone.utc))