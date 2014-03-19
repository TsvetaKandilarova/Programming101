def count_numbers (numbers):
    """bonus round 1"""
    numbers.sort()
    numbers.reverse()

    i = 0
    lamp = True

    while i < len (numbers) - 1:
        j = i + 1

        while j < len (numbers) and lamp:
            if not numbers[i] // numbers[j] in numbers:
                numbers.append (numbers[i] // numbers[j])
                numbers.sort()
                numbers.reverse()
                lamp = False
            else:
                j += 1
        if lamp == True:
            i += 1
        else:
            i = 0
        lamp = True

    return len(numbers)

def main ():
    print (count_numbers ([9, 2]))
    print (count_numbers ([8, 2]))
    print (count_numbers ([50]))
    print (count_numbers ([1, 5, 8, 30, 15, 4]))
    print (count_numbers ([1, 2, 4, 8, 16, 32, 64]))
    print (count_numbers ([6, 2, 18]))

if __name__ == '__main__':
    main()
