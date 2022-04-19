import random as r

n = 8
m = 8
a = [[r.randint(10, 20) for j in range(n)] for jj in range(m)]

for i in a:
    print(*i)

f = []
kol = 0
for stroka in range(len(a)):
    for stolb in range(len(a[stroka])):
        if a[stroka][stolb] == a[stolb][stroka]:
            if (stolb, stroka) not in f:
                f.append((stroka, stolb))
print()
print(f)
print(len(f))