from datetime import datetime, timedelta
import pytz #type: ignore
m,n = 1,2
print(m,"-",n)

if m == 1:
    print(m)
else:
    print(n)

expected_time = datetime.now().fromordinal(1200)
actual_time = datetime.now() + timedelta(days=2)
print(expected_time,"-",actual_time)
print(pytz.BaseTzInfo)