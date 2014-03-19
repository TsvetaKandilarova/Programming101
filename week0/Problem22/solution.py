def calculate_coins(money):
    money *= 100
    COINS = [100, 50, 20, 10, 5, 2, 1]
    outputList = {}

    for coin in COINS:
        coinsNeeded = int(money / coin)
        outputList[coin] = coinsNeeded
        money -= coin * coinsNeeded

    return outputList


# main
def main():
    print(calculate_coins(0.53))
    print(calculate_coins(8.94))

# PROGRAM RUN
if __name__ == '__main__':
    main()
