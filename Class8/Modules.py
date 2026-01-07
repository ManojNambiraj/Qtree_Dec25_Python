# Modules

    # def demo(name):
    #     print("Hi, Hello " + name)

# Built-in Modules:

    # import datetime as dt

    # x = dt.datetime(2020, 5, 17)

    # print(x)

        # import math

        # x = min(5, 7, 2, 100, 55)
        # x = max(5, 7, 2, 100, 55)

        # x = math.sqrt(25)
        # x = math.floor(25.6)
        # x = round(25.6)
        # x = math.pi

        # print(x)

# pip (Package)

import camelcase

c = camelcase.CamelCase()

text = "hi, hello john!"

print(c.hump(text))