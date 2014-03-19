def is_number_balanced(number):
    list_ = []
    while number > 10:
        list_.append(number % 10)
        number /= 10

    sum1 = sum(list_[0:len(list_) // 2:])
    sum2 = sum(list_[len(list_) // 2 + 1: len(list_):])
    print (sum1)
    print (sum2)
    return sum1 == sum2


def main():
    print (is_number_balanced(11))

if __name__ == '__main__':
    main()


len = 2
0, 1
