def count_consonants(string):
    consonants = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "z" ]
    numConsonants = 0

    for char in string.lower():
        if char in consonants:
            numConsonants += 1

    return numConsonants