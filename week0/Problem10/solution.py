def is_number_balanced(number):
    str_number = str(number)
    numDigits = 1
    while number > 10:
        numDigits += 1
        number //= 10

    firstHalf = ""
    secondHalf = ""

    if numDigits % 2 == 0:
        middle = numDigits // 2
        firstHalf = str_number[:middle]
        secondHalf = str_number[middle:]
    else:
        middle = numDigits // 2 + 1
        firstHalf = str_number[:middle]
        secondHalf = str_number[middle-1:]

    firstHalfSum = 0
    secondHalfSum = 0

    for digit in firstHalf:
        firstHalfSum += int(digit)
    for digit in secondHalf:
        secondHalfSum += int(digit)

    if firstHalfSum == secondHalfSum:
        return True

    else:
        return False
