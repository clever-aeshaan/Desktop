import random
import time

def darandomtime(startdate, enddate):
    print("i will print a random date between", startdate, "and", enddate)
    randomgenerate = random.random()
    dateformat = '%m/%d/%Y'
    starttime = time.mktime(time.strptime(startdate, dateformat))
    endtime = time.mktime(time.strptime(enddate, dateformat))
    randomtime = starttime + randomgenerate * (endtime - starttime)
    randomdate = time.strftime(dateformat, time.localtime(randomtime))

    return randomdate

print("the random date is: ", darandomtime("01/01/1999", "12/31/2020"))