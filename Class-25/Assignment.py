"""
-> input() = 12-02-2022
-> pre-define = 12-02-2022
-> if input == pre-define: "HBD" else "Sorry"
"""
import datetime as d
print(d.datetime.now())
print(d.date.today())

temp = d.date(2019, 11, 11)
print(temp)

today =d.date.today()
print(today.year)
print(today.month)
print(today.day)

s1 = d.datetime.now().strftime("%d/%m/%Y %H-%M-%S")
print(s1)

s2 = "2020-03-12  10:14:30"
s2Format = "%Y-%m-%d %H:%M:%S"

parse_date = d.datetime.strptime(s2, s2Format)
print(parse_date)