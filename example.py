def readFile():
    f = open("sample.txt")
    data = f.read()
    f.close()
    return len(data.split())

# print (readFile())

def writeFile():
    f = open("sample.txt", "w")
    f.write("this is some new data")
    f.close

# writeFile()

# https://en.wikipedia.org/wiki/Automated_readability_index
import math

def ari():
    f = open("moby-dick.txt")
    data = f.read()
    dataalnum = ''
    for i in data:
        if i.isalnum():
            dataalnum = dataalnum + i
    chara = len(dataalnum)
    words = data.count(" ") + data.count("\n")
    sent = data.count(".") + data.count("?") + data.count("!")
    sc = 4.71*(chara/words) + 0.5*(words/sent) - 21.43
    f.close()
    sc = math.ceil(sc)

    score = {
        1:" 5-6 Kindergarten",
        2:" 6-7 First Grade",
        3:" 7-8 Second Grade",
        4:" 8-9 Third Grade",
        5:" 9-10 Fourth Grade",
        6:" 10-11 Fifth Grade",
        7:" 11-12 Sixth Grade",
        8:" 12-13 Seventh Grade",
        9:" 13-14 Eighth Grade",
        10:" 14-15 Ninth Grade",
        11:" 15-16 Tenth Grade",
        12:" 16-17 Eleventh grade",
        13:" 17-18 Twelfth grade",
        14:" 18-22 College"
    }
    return score[sc] + "\n\nchar: " + str(chara) + "\nwords: " + str(words) + "\nsent: " + str(sent)

# print (ari())

def freq(l):
    d = {}
    for i in l:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    return d

print (freq("dasdasd"))