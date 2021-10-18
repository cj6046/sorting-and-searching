"""This module holds functions for sorting lists of integers in various ways.

This module has functionality for:
selection sort
"""
import random

def print_intro():
    print("""----------------------------------------------------------
----------Welcome to Sorting Algorithm Practice!----------
----------------------------------------------------------""")
    print("""Please choose an option: 
    1: Selection sort
    2: Merge sort
    0: Quit""")


def get_length():
    """Get the length of list from the user."""
    length = int(input("How long is the list? "))
    return length

def get_random_list(length):
    """Return a list of integers between 0 and 100."""
    return random.sample(range(0, 101), length)

def selection_sort(my_list, i):
    """Sort a list of integers in increasing order via selection sort."""
    if i >= len(my_list):
        return my_list
    else:
        swap(my_list, i, get_min_pos(my_list, i))
        return selection_sort(my_list, i + 1)

def swap(my_list, a, b):
    """Swap two elements in a list."""
    temp = my_list[a]
    myList[a] = my_list[b]
    myList[b] = temp

def get_min_pos(my_list, i):
    """Return the position of the smallest integer in a lits."""
    smallest = my_list[i]
    for num in my_list[i:]:
        if num < smallest:
            smallest = num
    return my_list.index(smallest, i, len(my_list))

def merge_sort(my_l):
    """Sort a list of integers in increasing order via merge sort."""
    if(len(my_l) == 1):
        return my_l
    first_half = my_l[:int(len(my_l) / 2)]
    second_half = my_l[int(len(my_l) / 2):]
    # print("The first half of the array is: " + str(first_half))
    # print("The second half of the array is: " + str(second_half))
    merge_sort(first_half)
    merge_sort(second_half)
    merge(my_l, first_half, second_half)
    

def merge(whole_list, first_list, second_list):
    """Merge two sorted lists into one sorted list."""
    first_i = 0
    second_i = 0
    i = 0
    while first_i < len(first_list) and second_i < len(second_list):
        if(first_list[first_i] < second_list[second_i]):
            whole_list[i] = first_list[first_i]
            first_i += 1
        else:
            whole_list[i] = second_list[second_i]
            second_i += 1
        i += 1
    while first_i < len(first_list):
        whole_list[i] = first_list[first_i]
        first_i += 1
        i += 1
    while second_i < len(second_list):
        whole_list[i] = second_list[second_i]
        second_i += 1
        i += 1
    return whole_list
    
print_intro()
while True:
    response = int(input())
    if response == 1:
        print("You chose selection sort")
        my_list = get_random_list(get_length())
        print("The array is: " + str(my_list))
        selection_sort(my_list, 0)
        print("After the array is sorted: " + str(my_list))
    elif response == 2:
        print("You chose merge sort")
        my_list = get_random_list(get_length())
        print("The array is: " + str(my_list))
        merge_sort(my_list)
        print("After the array is sorted: " + str(my_list))
    else:
        print("Goodbye!")
        break