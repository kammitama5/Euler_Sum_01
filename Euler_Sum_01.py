#Find sum of all numbers that are multiples of 3 or 5 from 1 through 1000.

def listsum(numList):
    theSum = 0
    for i in numList:
        if (i % 3 == 0) or (i % 5 == 0) :
            theSum = theSum + i
    return theSum

numList = range(0, 1000)
print(listsum(numList))
#print(listsum([0,1,2,3,4,5,6,7,8,9]))
#checked solution with numbers 0 through 9 to ensure algorithm worked (base case)
