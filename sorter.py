import random

def printIntro():
    print("""----------------------------------------------------------
----------Welcome to Sorting Algorithm Practice!----------
----------------------------------------------------------""")
    print("""Please choose an option: 
    1: Selection sort
    0: Quit""")

def getLength():
    length = int(input("How long is the list? "))
    return length

def getRandomList(length):
    return random.sample(range(0, 100), length)

def selectionSort(l, i):
    if i >= len(l):
        return l
    else:
        swap(l, i, getMinPos(l, i))
        return selectionSort(l, i + 1)

def swap(l, a, b):
    temp = l[a]
    l[a] = l[b]
    l[b] = temp

def getMinPos(l, i):
    smallest = l[i]
    for num in l[i:]:
        if num < smallest:
            smallest = num
    return l.index(smallest, i, len(l))
    
printIntro()
while True:
    response = int(input())
    if response == 1:
        print("You chose selection sort")
        myList = getRandomList(getLength())
        print("The Array is: " + str(myList))
        selectionSort(myList, 0)
        print("After the array is sorted: " + str(myList))
    elif response == 2:
        print("You chose merge sort")
    else:
        print("Goodbye!")
        break