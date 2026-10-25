import mymodule as mx
mx.greeting("Zeeyah")

a = mx.person["age"]
print(a)

import platform
x = platform.system()
print(x)

y = dir(platform)
print(y)

import datetime
z = datetime.datetime.now()
print(z)
print(z.year)
print(z.strftime("%A"))
z = datetime.datetime(2020, 5, 17)
print(z)