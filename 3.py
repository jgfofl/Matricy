import random as r

n = 10
m = 10
a = [[r.randint(10, 20) for j in range(n)] for jj in range(m)]

for i in a:
    print(i)
print()

k = 0
for stroka in range(len(a)):
    for stolb in range(len(a[stroka])):

        if stolb == 9 and stroka != 9:
            if a[stroka + 1][stolb] > a[stroka][stolb] and a[stroka][stolb - 1] > a[stroka][stolb]:
                if a[stroka - 1][stolb] > a[stroka][stolb]:
                    print(a[stroka][stolb])
                    k += 1
        elif stolb == 9 and stroka == 9:
            if a[stroka][stolb - 1] > a[stroka][stolb] and a[stroka - 1][stolb] > a[stroka][stolb]:
                print(a[stroka][stolb])
                k += 1


        elif stroka == 0 and stolb == 0:
            if a[stroka + 1][stolb] > a[stroka][stolb] and a[stroka][stolb + 1] > a[stroka][stolb]:
                print(a[stroka][stolb])
                k += 1
        elif stroka == 0 and stolb > 0:
            if a[stroka + 1][stolb] > a[stroka][stolb] and a[stroka][stolb + 1] > a[stroka][stolb]:
                if a[stroka][stolb - 1] > a[stroka][stolb]:
                    print(a[stroka][stolb])
                    k += 1


        elif stroka == 9 and stolb == 0:
            if a[stroka - 1][stolb] > a[stroka][stolb] and a[stroka][stolb + 1] > a[stroka][stolb]:
                print(a[stroka][stolb])
                k += 1
        elif stroka == 9 and stolb > 0:
            if a[stroka - 1][stolb] > a[stroka][stolb] and a[stroka][stolb + 1] > a[stroka][stolb]:
                if a[stroka][stolb - 1] > a[stroka][stolb]:
                    print(a[stroka][stolb])
                    k += 1


        elif stroka > 0 and stolb == 0:
            if a[stroka + 1][stolb] > a[stroka][stolb] and a[stroka][stolb + 1] > a[stroka][stolb]:
                if a[stroka - 1][stolb] > a[stroka][stolb]:
                    print(a[stroka][stolb])
                    k += 1
        elif stroka > 0 and stolb > 0:
            if a[stroka - 1][stolb] > a[stroka][stolb] and a[stroka][stolb + 1] > a[stroka][stolb]:
                if a[stroka][stolb - 1] > a[stroka][stolb] and a[stroka + 1][stolb] > a[stroka][stolb]:
                    print(a[stroka][stolb])
                    k += 1
