import pytz
# print(dict(pytz.country_timezones)['RU'], end='')
s = dict(pytz.country_timezones)['RU']

for i in s:
    if i.startswith('AsiaS'):
        print(i)