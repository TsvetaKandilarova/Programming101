def sum_of_digits(number):
    sum_ = 0
    number = abs(number)

    while number > 0:
        sum_ += number % 10
        number //= 10

    return sum_
