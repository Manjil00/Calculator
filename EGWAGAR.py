def myFunction(inputList):
    '''

    '''

    for i in range(len(inputList)):
        entry = inputList[i]
        for j in range(i+1, len(inputList)):
            f=inputList[j]
            if inputList[j]==entry:
                return False
    return True
print( myFunction(["a","b","c","a","b","c"]) )

