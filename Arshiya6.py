# تمرین ۱
def add_infinite(*args):
    total = 0
    for num in args:
        total += num
    return total


# تمرین ۲
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


# تمرین ۳
def divide(a, b):
    if b == 0:
        return "تقسیم بر صفر مجاز نیست!"
    if a < b:
        return 0
    return 1 + divide(a - b, b)


# تمرین ۴
def find_max(lst):
    if len(lst) == 1:
        return lst[0]
    max_rest = find_max(lst[1:])
    return lst[0] if lst[0] > max_rest else max_rest


if __name__ == "__main__":
    print("۱) جمع بی‌نهایت:", add_infinite(1, 2, 3, 4, 5))
    print("۲) فیبوناچی(10):", fibonacci(10))
    print("۳) تقسیم(17, 5):", divide(17, 5))
    print("۴) بزرگترین:", find_max([3, 7, 2, 9, 5]))
