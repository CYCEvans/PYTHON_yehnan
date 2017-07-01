import datetime
dateA = [2014, 11, 12]
dateB = [2016, 9, 25]
d1 = datetime.datetime(dateA[0],dateA[1],dateA[2])
d2 = datetime.datetime(dateB[0],dateB[1],dateB[2])
days = (d2 - d1).days
print (days)