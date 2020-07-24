def listOfStrings (words):
    listOfStrings = set(words.split())
    secondlist = listOfStrings.sorted()
    strings = "".join(secondlist)

    return strings


