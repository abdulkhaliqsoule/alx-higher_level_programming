#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    myList = []
    if (len(my_list)) > 0:
        for x in my_list:
            if x % 2 is 0:
                myList.append(True)
            else:
                myList.append(False)
    else:
        return (None)
    return(myList)
