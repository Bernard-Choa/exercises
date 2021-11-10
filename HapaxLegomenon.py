import re

def HapaxCounter():
    file = open("test", "r")
    myStr = file.read().lower()
    myDict = dict()
    trimmedStr = ""
    myList = []
    for pm in [",", ".", "!", "?", ":", "_", "*", '"', "[", "]", "(", ")", "&", ";", "-", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]:
        myStr = myStr.replace(pm, "")
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


def WriteNewFile():
    file = open("test", "r")
    output = open("numbered-texts", "w")
    oldlines = file.readlines()
    print(oldlines)
    for i in range(len(oldlines)):
        output.write(f"({i+1}) {oldlines[i]}")
    file.close()
    output.close()


def WordLenAvg():
    file = open("test", "r")
    myStr = file.read().lower()
    ttl_l = 0
    for wr in myStr.split():
        ttl_l += len(wr)
    print("{:.2f}".format(ttl_l / len(myStr.split())))
    file.close()


def sent_split():
    file = open("test", "r")
    myStr = file.read().replace("\n", " ")
    output = open("sent-split-output", "w")
    pattern1 = "[a-z]\.[a-z]"
    pattern2 = ".[0-9]"
    for l in myStr.split():
        if "." in l:
            if l[0].isupper():
                print(l[0])
                output.write(f"{l} ")
            elif re.search(pattern1, l):
                output.write(f"{l} ")
            elif re.search(pattern2, l):
                output.write(f"{l} ")
            else:
                output.write(f"{l}\n")
        elif "?" in l or "!" in l:
            output.write(f"{l}\n")
        else:
            output.write(f"{l} ")
    file.close()
    output.close()
