def unique_words_count(list):
    uniqueList = []

    for i in range(len(list)):
        if list[i] not in uniqueList:
            uniqueList.append(list[i])

    return len(uniqueList)