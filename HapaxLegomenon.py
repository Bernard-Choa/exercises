def HapaxCounter():
    file = open("test", "r")
    myStr = file.read().lower()
    myDict = dict()
    myList = []
    wr = ""
    for wr in myStr.split():
        if myDict.get(wr) == None:
            myDict[wr] = 1
        else:
            myDict[wr] += 1

    for i in myDict:
        if myDict.get(i) > 1:
            continue
        else:
            myList.append(i)
            print(i)
    print(myList)
    file.close()