def magic_string(string):

    count_ = 0

    for i in range (int(len(string) / 2)):
        if string[i] == '<':
            count_ += 1
        if string[len(string) - 1 - i] == '>':
            count_ += 1

    return count_

