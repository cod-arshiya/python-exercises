# 1)
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

print(is_prime(7))
print(is_prime(10))


# 2)
def is_perfect(num):
    total = 0
    for i in range(1, num):
        if num % i == 0:
            total += i
    return total == num

print(is_perfect(6))
print(is_perfect(28))
print(is_perfect(10))


# 3)
def print_persian_number(num):
    persian_digits = {
        "0": "۰", "1": "۱", "2": "۲", "3": "۳", "4": "۴",
        "5": "۵", "6": "۶", "7": "۷", "8": "۸", "9": "۹"
    }
    result = ""
    for digit in str(num):
        result += persian_digits[digit]
    print(result)

number = int(input("یک عدد وارد کنید: "))
print_persian_number(number)


# 4)
def reverse_number(num):
    reverse = 0
    while num != 0:
        remain = num % 10
        reverse = reverse * 10 + remain
        num = num // 10
    return reverse

print(reverse_number(123))
print(reverse_number(4567))