def sorting(lst,length):
    low = 0
    high = length - 1
    middle = 0
    while middle <= high:
        if(lst[middle] == 0) :
            lst[low] , lst[middle] = lst[middle], lst[low]
            low = low + 1
            middle = middle + 1
        elif(lst[middle] == 1):
            middle = middle + 1
        else:
            lst[middle] , lst[high] = lst[high] , lst[middle]
            high = high - 1
    return lst

def printLst(lst):
    for i in lst:
        print(i)

lst = [0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1]
length = len(lst)
lst = sorting(lst, length)
printLst(lst)