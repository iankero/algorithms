#SEARCH!!
import time


sorting = [10, 6, 7, 1, 2, 5, 6, 9, 11, 23, 1293, 2344, 93129, 39, 12839, 888, 8819, 88123,]

def linear():
    pos = None
    search = int(input("what u wanna find mate"))
    for i in range(0, len(sorting)):
        if sorting[i] == search:
            pos = i
            break
    if pos is None:
        print("didnt find it mate.")
    else:
        print("its in position ", pos ," mate.")


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
    search = int(input("what u wanna find mate"))

    left = 0
    right = len(sorting) - 1

    while left <= right:
        mid = (left + right) // 2
        
        if sorting[mid] > search:
            right = mid - 1
        elif sorting[mid] < search:
            left = mid + 1
        else:
            print("its in position ", mid, " mate.")
            return

    print("didnt find it mate.")
    

while True:
    
