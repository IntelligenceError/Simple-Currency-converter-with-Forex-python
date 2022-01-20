#Currency converter ver.1 by Keetaphat
from forex_python.converter import CurrencyRates
from forex_python.converter import CurrencyCodes
import datetime as st
#Use only these currency code
#{EUR,IDR, BGN, ILS, GBP, DKK, CAD, JPY, HUF, RON, MYR, SEK, SGD, HKD, AUD, CHF, KRW, CNY, TRY, HRK, NZD, THB ,USD ,NOK ,RUB, INR, MXN, CZK, BRL, PLN, PHP, ZAR}
a = input("Choose currency to convert: ")
a = a.upper()
b = input("Convert to: ")
b = b.upper()
c = input("Do you want to choose date or not if yes type \"yes\": ")
d = CurrencyCodes()
if c == "yes":
    print("Type number example: \"Year: 2022\"")
    Year = input("Year: ")
    Month = input("Month: ")
    Day = input("Day: ")
    time = st.datetime(int(Year),int(Month),int(Day))
    c = CurrencyRates()
    print(d.get_symbol(b),c.get_rate(a, b, time))
else:
  c = CurrencyRates()
  print(d.get_symbol(b),c.get_rate(a, b))
