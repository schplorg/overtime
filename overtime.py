import datetime
import math
from collections import defaultdict
with open('log.txt') as f:
    lines = f.readlines()
    dates = defaultdict(list)
    for line in lines:
        timo = datetime.datetime.strptime(line, '%a %b %d %H:%M:%S %Y\n')
        key = str(timo.day) +"." + str(timo.month)
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
            print(key +". overtime: " + str(dh) + ":" + str(dm))
            total += delta.seconds
    totalh = math.floor(total/3600)
    totalm = math.floor(((total/3600)-totalh)*60)
    print("total: " + str(totalh) + ":" + str(totalm))
