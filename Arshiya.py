# 1)
a = "International"
b = a[0]
c = a[len(a)//2]
d = a[-1]
print(b + c + d)


# 2)
str1 = "python"
str2 = "programing"

e = str2[len(str2)//2]
f = str1 + e
print(f)


# 3)
a = "DjAnGOFraMeWork"

b = ""
c = ""

for i in a:
    if i.isupper():
        c = c + i
    else:
        b = b + i

print(b + c)


# 4)
a = """پایتون یک زبان برنامه‌نویسی سطح بالا، شیءگرا و تفسیری است که توسط خیدو فان روسوم در سال ۱۹۹۱ طراحی شد. این زبان به دلیل سادگی، خوانایی بالا و کتابخانه‌های گسترده، یکی از محبوب‌ترین زبان‌های برنامه‌نویسی در جهان است."""

b = a.split()
print(len(b))