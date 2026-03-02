#SEARCH!!
import time
import random

sorting = [10, 6, 7, 1, 2, 5, 6, 9, 11, 23, 1293, 2344, 93129, 39, 12839, 888, 8819, 88123,]

def linear():
    pos = None
    print(sorting)
    search = int(input("Linear Search: find what?"'\n'))
    for i in range(0, len(sorting)):
        if sorting[i] == search:
            pos = i
            break
    if pos is None:
        print("Not in the list")
    else:
        print("its in position ", pos ,".")


def bubble():
    for m in range(len(sorting)):
        for i in range(len(sorting) - 1):
            pos = sorting[i]
            if pos > sorting[i+1]:
                temp = sorting[i+1]
                sorting[i+1] = pos
                sorting[i] = temp
            #else:
                #print(sorting[i] , " not bigger than " ,sorting[i+1])
                #print(sorting)
    
            

def binary():
    bubble()
    print(sorting)
    search = int(input("Binary Search: find what?"'\n'))

    left = 0
    right = len(sorting) - 1

    while left <= right:
        mid = (left + right) // 2
        
        if sorting[mid] > search:
            right = mid - 1
        elif sorting[mid] < search:
            left = mid + 1
        else:
            print("its in position ", mid, ".")
            return

    print("Not in the list.")
    

def search():
    while True:
        try:
            choice1 = int(input("which search do you want to do?"'\n'
                                '1: binary''\n''2: linear''\n''3: Exit''\n'))
        except ValueError:
            print("not an option; try again"'\n')
            continue

        if choice1 == 1:
            binary()
        elif choice1 == 2:
            linear()
        else:
            break



    
search()