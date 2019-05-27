import datetime
import math
from collections import defaultdict
with open('log.txt') as f:
    lines = f.readlines()
    dates = defaultdict(list)
    for line in lines:
        if(str(line).startswith("Date:   ")):
            stripped = str(line).replace("Date:   ","")
            timo = datetime.datetime.strptime(stripped, '%a %b %d %H:%M:%S %Y\n')
            key = str(timo.day) +"." + str(timo.month) + "." + str(timo.year)
            dates[key].append(timo)      
    total = 0
    for key,timos in dates.items():
        timo = max(timos)
        eod = datetime.datetime.strptime("18:30:00","%H:%M:%S")
        tim = timo.replace(year=1900,month=1,day=1)
        delta = tim - eod
        if not(delta.days < 0):
            dh = delta.seconds / 3600
            dm = (dh-math.floor(dh))*60
            dh = math.floor(dh)
            dm = math.floor(dm)
            print(key +" overtime: " + str(dh).zfill(2) + ":" + str(dm).zfill(2))
            total += delta.seconds
    totalh = math.floor(total/3600)
    totalm = math.floor(((total/3600)-totalh)*60)
    print("total: " + str(totalh).zfill(2) + ":" + str(totalm).zfill(2))
