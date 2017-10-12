from math import factorial as fc

print(fc(1000))

import sys
from pprint import pprint as pp
pp([sys.float_info, sys.int_info, sys.hash_info, sys.thread_info, sys.version_info, sys.version, sys.api_version])

most_negative_float = -sys.float_info.max
greatest_negative_float = -sys.float_info.min

pp((most_negative_float, greatest_negative_float))
pp(float("10"))
pp(2**53)
pp(float(2**53)) # Correct
pp(float(2**53 + 1)) # Incorrect
pp(float(2**53 + 2)) # Correct
pp(float(2**53 + 3)) # Incorrect
pp(float(2**53 + 4)) # Correct

import decimal
pp(decimal.getcontext())
from decimal import Decimal
pp(Decimal(7))
pp(Decimal(0.8))
pp(Decimal(0.8) - Decimal(0.7))
pp(Decimal("0.8") - Decimal("0.7")) # Works like a charm perfect for usage no floating point issue
import time
time.sleep(0.3)
decimal.getcontext().traps[decimal.FloatOperation] = True
# Decimal(0.4) Not a good process it will fail if FloatOperation is set to true for trapping
# Decimal('0.8') > 0.8 Not a good process it will fail if FloatOperation is set to true for trapping
pp(Decimal('0.9') - Decimal('0.9'))

a = Decimal(3)
b = Decimal('3.0')
c = Decimal('3.00')
print(a, b, c)

decimal.getcontext().prec = 8
d = Decimal('1.12345678')
e = Decimal('1.12345678')
print(d, e)
pp(d + e)
print(Decimal('Infinity'), Decimal('-Infinity'), Decimal('NaN'), # Decimal('Infinity')+Decimal('-Infinity'), This is not allowed
      Decimal('NaN') + Decimal('1982847.8273492843'))

pp(-15 % 4) # 1
pp(Decimal(-15) % Decimal(4)) # -3
pp(15 % 4) # 3
pp(Decimal(15) % Decimal(4)) # 3

pp(Decimal(-15) // Decimal(2))
pp(-15 // 2)
pp(Decimal(-15) // Decimal(-2))
pp(-15 // -2)

pp(Decimal('0.16').sqrt())

from fractions import Fraction
two_third = Fraction(2, 3)
four_fifths = Fraction(4, 5)
print(two_third, four_fifths)
pnt_one = Fraction(0.1) # Not correct
pnt_one_1 = Fraction(Decimal('0.1'))
print(pnt_one, pnt_one_1)
print(Fraction('23/234'))

from math import floor
print(Fraction(2,3) + Fraction(4, 5),
      Fraction(2, 3) - Fraction(4, 5),
      Fraction(2, 3) * Fraction(4, 5),
      Fraction(2, 3) / Fraction(4, 5),
      Fraction(2, 3) // Fraction(4, 5),
      Fraction(2, 3) % Fraction(4, 5),
      floor(Fraction(2, 3) + Fraction(4, 5)))

print(2j, 3 + 4j, type(2 -2j), complex(5, -2), complex('(-9+29j)'), complex('-9+29j'))
# not allowed - complex('32 + 23j') white space is not allowed

c = 1 + 234j

print(c.real, c.imag, c.conjugate())

import math
#error when called t = math.sqrt(-1)


import cmath
# no error
t = cmath.sqrt(-123)
pp(t)

t = cmath.sqrt(-1)
pp(t)

print(cmath.phase(complex('1+1j')), abs(complex('1+1j')))
modulus, phase = cmath.polar(complex('1+1j'))
print(modulus, phase)
print(cmath.rect(modulus, phase))


def inductive(ohms):
    return complex(0.0, ohms)


def capacitive(ohms):
    return complex(0.0, -ohms)

def resistive(ohms):
    return complex(ohms)

def impedence(components):
    z = sum(components)
    return z

dt = impedence([inductive(10), resistive(10), capacitive(5)])
pp(dt)

cmath.phase(dt)
print(cmath.phase(dt), abs(dt))
pp(cmath.rect(abs(dt), cmath.phase(dt)))
pp(math.degrees(cmath.phase(dt)))

pp(cmath.rect(abs(dt), cmath.phase(dt)))
'''Testing completed impedence test modulus and phase'''


print(0b101010)
print([0b101010, 0o52, 0x2a, oct(42), hex(42), bin(42), hex(42)[2:],
       int("ABCDEFGH", base=18), int("0b10010101011", base=2),
       int("10010101011", base=2)])

import datetime
pp([datetime.date(year=2017, month=8, day=19), datetime.date.today(),
    datetime.date.fromtimestamp(10000000000),
    datetime.date.fromordinal(736592)])

d = datetime.date.today()
pp([d.year, d.month, d.day, d.weekday(), d.isoweekday(), d.isoformat(), d.strftime("%A %d %B %Y"),
    str("The date is {:%A %d %B %Y}").format(d)])
tt= datetime.time(23, 59, 59, 999999)

pp([tt, datetime.time.min, datetime.time.max, datetime.time.resolution, "{tt.hour}h{tt.minute}m{tt.second}".format(tt=tt)])

# class SGT8(datetime.tzinfo):
#     def utcoffset(self,dt):
#         return datetime.timedelta(hours=8,minutes=0)
#     def tzname(self,dt):
#         return "GMT +08.00"
#     def dst(self,dt):
#         return datetime.timedelta(0)
# sgt8 = SGT8()
# t = datetime.datetime(year=2017, month = 11, day = 3, hour=9, minute=45, second=12, tzinfo=sgt8)
# pp(t)
# newdate = t.astimezone(sgt8)
# pp(newdate.strftime("%d %b %Y %I:%M:%S %p %Z") )
#
# pp(datetime.(newdate, datetime.datetime.today()))

dttm = datetime.datetime.now()
dttm1 = datetime.datetime.today()
dttm2 = datetime.datetime.utcnow()
dt1 = datetime.date.today()
tm1 = datetime.time(6, 2, 12, 239102)

dttm3 = datetime.datetime.combine(dt1, tm1)
pp([dttm, dttm1, dttm2, dt1, tm1, dttm3])

dttm4 = datetime.datetime.strptime("Monday 4 February 2019, 13:12:49",
                                   "%A %d %B %Y, %H:%m:%S")
pp([dttm4, dttm4.date(), dttm.time(), dttm4.day])

sgt = datetime.timezone(datetime.timedelta(hours=8), "SGT")
pp(sgt)
dttm6 = datetime.datetime(2392, 10, 21, 10, 49, 10,tzinfo=sgt)
pp([dttm6, dttm6.utcnow()])
import pytz, datetime
utc = pytz.utc
fmt = '%Y-%m-%d %H:%M:%S'
india = pytz.timezone('Asia/Kolkata')

dt = datetime.datetime.strptime("2017-04-06 1:18:00", fmt)
ind_dt = india.localize(dt)
print(ind_dt.astimezone(utc).strftime(fmt))
# pp(india.localize(dttm6).astimezone(utc).strftime(fmt))

loc_tz = pytz.timezone("Asia/Singapore")
ind_tz = pytz.timezone("Asia/Kolkata")

dttm_without_tz = datetime.datetime.strptime("2017-9-21 14:23:9", fmt)
dttm_with_tz = loc_tz.localize(dttm_without_tz, is_dst=True)
dttm_utc = dttm_with_tz.astimezone(utc)
pp([dttm_without_tz, dttm_with_tz, dttm_utc])

l = [ i* 2 for i in range(120)]
l.append(12321)
pp([type(l), dir(l), l ])

pnt = [(x,y) for x in range(5) for y in range(5)]
pp(pnt)

vals = [   [y * 3 for y in range(x)] for x in range(19)]
pp(vals)

map1 = map(ord, "The quick brown fox jump over the lazy dog")

pp(map1)
for data in map1:
    print(''.join(chr(data)))