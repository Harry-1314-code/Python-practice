num = 0

for a in range(1, 5):

    for b in range(1, 5):

        for c in range(1, 5):

            if ((a != b) and (a != c) and (b != c)):

                print(a, b, c)

                num += 1
print('组成无重复三位数数字{}个'.format(num))

