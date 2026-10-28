
from datetime import datetime

months = ["January", "February", "March", "April", "May", "June", 
          "July", "August", "September", "October", "November", "December"]

for i in range(12):
    date_obj = datetime(2026, i + 1, 1)

    print(months[i])
