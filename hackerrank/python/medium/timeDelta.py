import datetime
import math

test_cases = int(input())
date_time_format = "%a %d %b %Y %H:%M:%S %z"
for _ in range(test_cases):
    t1 = datetime.datetime.strptime(input(), date_time_format)
    t2 = datetime.datetime.strptime(input(), date_time_format)

    print(round(math.fabs(t1.timestamp() - t2.timestamp())))
