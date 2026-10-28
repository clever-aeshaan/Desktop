import datetime

months = ("January", "February", "March", "April", "May", "June", 
          "July", "August", "September", "October", "November", "December")

for i in range(1, 13):
    d = datetime.date(2026, i, 1)
    print(months[d.month - 1])
