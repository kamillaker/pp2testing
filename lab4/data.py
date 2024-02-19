# 1 Write a Python program to subtract five days from current date.
from datetime import  *
today = datetime.now()
days_5_from_2day = today - timedelta(days=5)
print(days_5_from_2day)

# 2 Write a Python program to print yesterday, today, tomorrow.

from datetime import  *
today = datetime.now()
yesterday = today - timedelta(days=1)
print(yesterday)
tomorrow = today + timedelta(days=1)
print(tomorrow)

# 3 Write a Python program to drop microseconds from datetime.

from datetime import  *
today = datetime.now()
print(today.strftime("%Y-%m-%d %H:%M:%S"))

# 4 Write a Python program to calculate two date difference in seconds.

from datetime import  *
today = datetime.now()
yesterday = today - timedelta(days = 1)
diff = today - yesterday 
print(diff.total_seconds())