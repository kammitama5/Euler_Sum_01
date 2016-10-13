def listsum(numList):
    theSum = 0
    for i in numList:
        if (i % 3 == 0) or (i % 5 == 0) :
            theSum = theSum + i
    return theSum

numList = range(0, 1000)
print(listsum(numList))
#print(listsum([0,1,2,3,4,5,6,7,8,9]))