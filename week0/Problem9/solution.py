def contains_digit(number, digit):
    while number > 0:
        if (number % 10 == digit):
            return True
        number //= 10
    return False


def contains_digits(number, digits):
    if len(digits) == 0:
        return False
    for item in digits:
        if not contains_digit(number, item):
            return False
    return True


def main():
    print (contains_digit(1234, 4))

if __name__ == '__main__':
    main()
