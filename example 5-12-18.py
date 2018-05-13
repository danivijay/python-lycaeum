def fizzbizz(n):
    for i in range(1, n+1):
        if i % 3 == 0:
            print("fizz")
        elif i % 5 == 0:
            print("bizz")
        elif i % 15 == 0:
            print("fizzbizz")
        else:
            print(n)

def num_digits(n):
    print (len(str(n)))

def num_words(s):
    print (len(s.split(" ")))

def num_sentances(s):
    print (len(s.split(".")) - 1)

def longest_word(s):
    words = s.split(" ")
    longest = words[0]
    for i in words:
        if len(i) > len (longest):
            longest = i
        else:
            pass
    print (longest)

def abbreviate(s):
    words = s.split(" ")
    abbr = ""
    for i in words:
        if i[0] == i[0].capitalize():
            abbr = abbr + i[0]
    print (abbr)

# {:<5} {:^5} {:>5}

def sq_tables(n):
    a = []
    for i in range(1, n+1):
        for j in range(1, n+1):
            a.append(str(i*j).rjust(int(len(str(n*n))) + 2))
        print("".join(a))
        a = []

# sample output

# 1 2 3
# 2 4 6
# 3 6 9

def panagram(s):
    alp = "QWERTYUIOPASDFGHJKLZXCVBNM"
    for i in alp:
        if not i in s.upper():
            return False
        else:
            pass
    return True

# print (panagram("QWERTYUIOPASDFGHKLZXCVBNMj"))


import random
import math
def pie(n):
    cnt_in = 0
    cnt_out = 0
    for i in range(1, n):
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)
        if (math.sqrt(x*x + y*y)) < 1:
            cnt_in = cnt_in + 1
        print(4*cnt_in/n)

pie(100000)