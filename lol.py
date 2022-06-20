import pytz
import random
# print(dict(pytz.country_timezones)['RU'], end='')
s = dict(pytz.country_timezones)['RU']



q = []
for i in range(10):
    k = q.append(str(random.randint(1, 10)))

print("".join(q), end=' ')
    