currentNum = 3


def collatzConjecture(a,b):
    permutations = 0
    while a != 1:
        if(a%2 == 0):
            a = a/2
            permutations = permutations + 1
        elif(a%2 != 0):
            a = a*3+1
            permutations = permutations + 1
    if(b == "n"):
        return a
    if(b == "p"):
        return permutations

while(True):
    if(collatzConjecture(currentNum,"n") == 1):
        print(currentNum)
        print(collatzConjecture(currentNum,"p"))
        currentNum = currentNum + 1
        