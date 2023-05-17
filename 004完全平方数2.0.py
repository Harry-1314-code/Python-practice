for i in range(1, 100):

    x = int((i + 100) ** 0.5)

    y = int((i + 100 + 168) ** 0.5)

    if x ** 2 == i + 100 and y ** 2 == i + 100 + 168:

        print(i)

