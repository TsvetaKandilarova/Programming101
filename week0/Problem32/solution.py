def sum_of_divisors(number):
    sum_ = 0
    for i in range(1, number + 1):
        if number % i == 0:
            sum_ += i
    return sum_


def is_prime(number):
    return sum_of_divisors(number) == number + 1


def goldbach(number):
    result = []
    list_ = [i for i in range(2, number + 1) if is_prime(i) == True]

    for item in list_:
        if is_prime(number - item):
            if not (number - item, item) in result:
                result.append((item, number - item))

    return result


def main():
    print (goldbach(4))
    print (goldbach(6))
    print (goldbach(8))
    print (goldbach(10))

if __name__ == '__main__':
    main()
