#Currency converter ver.1 by Keetaphat
from forex_python.converter import CurrencyRates
import datetime as st

a = input("Choose currency to convert: ")
b = input("Choose another currency: ")
c = input("Do you want to choose date or not if yes type \"yes\": ")
if c == "yes":
    print("Type number example: \"Year: 2022\"")
    Year = input("Year: ")
    Month = input("Month: ")
    Day = input("Day: ")
time = st.datetime(int(Year),int(Month),int(Day))

c = CurrencyRates()
print(c.get_rate(a, b, time))
