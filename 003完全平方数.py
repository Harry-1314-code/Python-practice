import math

for i in range(1, 100):

    x = int(math.sqrt(i + 100))

    y = int(math.sqrt(i + 100 + 168))

    if x ** 2 == i + 100 and  y ** 2 == i + 100 + 168:

        print(i)

