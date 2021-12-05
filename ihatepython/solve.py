import random

def do_thing(a, b):
    return ((a << 1) & b) ^ ((a << 1) | b)

def checkFlag(x, prevLen):
    random.seed(997)
    k = [random.randint(0, 256) for _ in range(len(x))]
    a = { b: do_thing(ord(c), d) for (b, c), d in zip(enumerate(x), k) }
    b = list(range(len(x)))
    random.shuffle(b)
    c = [a[i] for i in b[::-1]]
    # print(k)
    # print(c)
    kn = [47, 123, 113, 232, 118, 98, 183, 183, 77, 64, 218, 223, 232, 82, 16, 72, 68, 191, 54, 116, 38, 151, 174, 234, 127]
    valid = len(list(filter(lambda s: kn[s[0]] == s[1], enumerate(c))))
    # print(valid)
    if valid > prevLen:
        return True
    return False

#random.seed(997)

k = [random.randint(0, 256) for _ in range(25)]
# print(k)

#x = "A"*25

# a = {b: do_thing(ord(c), d) for (b, c), d in zip(enumerate(x), k)}

#kn = [47, 123, 113, 232, 118, 98, 183, 183, 77, 64, 218, 223, 232, 82, 16, 72, 68, 191, 54, 116, 38, 151, 174, 234, 127]

# write a loop to go through all the possible ascii 
# values and do_thing it with all values in k

currFlag = 'MetaCTF{'

for i in range(25 - 8):
    for j in range(0, 128):
        nextFlag = currFlag + chr(j) + 'A'*(16-i)
        # print("test")
        print(nextFlag)
        assert(len(nextFlag) == 25)
        if checkFlag(nextFlag, len(currFlag)):
            # print(nextFlag)
            currFlag = currFlag + chr(j)
            break

# print(currFlag)


