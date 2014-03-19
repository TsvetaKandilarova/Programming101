#[i**2 for i in range (1,20) if i %2==0] - filtrira mapva i prawi magiq
def is_an_bn(word):
    if len(word) == 0:
        return True
    word = [i for i in word]
    if max(word) != 'b':
        return False
    i = 0
    count_ = 0
    while word[i] == 'a' and i < len(word):
        count_ += 1
        i += 1
    while word[i] == 'b' and i < len(word) - 1:
        count_ -= 1
        i += 1
    return count_ == 1


def main():
    print (is_an_bn("aaabb"))

if __name__ == '__main__':
    main()
