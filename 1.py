import random as r


n = int(input())
m = int(input())
a1 = []
for i in range(m):
    a2 = []
    for h in range(n):
        a2.append(r.randint(10,30))
    a1.append(a2)
for g in a1:
    print(*g)


s1 = []
for z in a1:
    s = 0
    for f in z:
        if f > 0 and f % 2 == 0:
            s += f
    s1.append(s)
print()
print(*s1, 's1')
lishnie = s1[:]

new_a = [['0' for j in range(n)] for jj in range(m)]
for i in range(len(s1)):
    minimum = min(lishnie)
    number = s1.index(minimum)
    new_a[i] = a1[number]
    del lishnie[lishnie.index(minimum)]

print()
print(*new_a)