# 1)
a = [1, 5, 50, 3, 8, 90]
a[4] = 80
print(a)


# 2)
a = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
a[2][2].insert(2, 7000)
print(a)


# 3)
a = "1403"

b = ""
c = "۰۱۲۳۴۵۶۷۸۹"

b = b + c[int(a[0])]
b = b + c[int(a[1])]
b = b + c[int(a[2])]
b = b + c[int(a[3])]

print(b)


# 4)
a = int(input("لطفاً یک عدد وارد کنید : "))

if a % 2 == 0 and a % 3 == 0:
    print(f"{a} بر 6 بخش‌پذیر است")
else:
    print(f"{a} بر 6 بخش‌پذیر نیست")


# 5)
a = "admin"
b = "1234"

c = input("please enter your username : ")
d = input("please enter your password : ")

if c == a and d == b:
    print("welcome")
else:
    print("username or password is wrong")


# 6)
a = input("لطفاً گرید خود را وارد کنید (A, B, C, F) : ")

if a == "A":
    print("بازه نمره شما: 17 تا 20")
elif a == "B":
    print("بازه نمره شما: 14 تا 17")
elif a == "C":
    print("بازه نمره شما: 10 تا 14")
elif a == "F":
    print("بازه نمره شما: 0 تا 10")
else:
    print("گرید نامعتبر است! لطفاً A, B, C یا F را وارد کنید.")