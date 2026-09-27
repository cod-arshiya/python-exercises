# 1
n = int(input("adad: "))
s = 0
while n != 0:
    r = n % 10
    s += r
    n //= 10
print("jam:", s)


# 2
f = ("mojtaba", "benyamin", "sakineh")
l = ("ghahri", "kachoue", "lopez")
a = (39, 21, 14)

res = tuple(zip(f, l, a))
print(res)


# 3
n = int(input("adad: "))
c = 0
while n != 1:
    print(n, end=" -> ")
    if n % 2 == 0:
        n = n // 2
    else:
        n = n * 3 + 1
    c += 1
print(n)
print("marhale:", c)


# 4
p = ["mojtaba", "mojtaba", "taghi", "naghi", "sakineh", "sara", "mojtaba", "mojtaba", "mojtaba"]
u = []
for i in p:
    if i not in u:
        u.append(i)
print(u)