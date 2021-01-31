""" An implementation of a simple sorting algorithm - bubble sort!
(Made for programming bootcamp tutor application - semester 1, 2021)

Why bubble sort works:
-   In each iteration (round) of this algorithm, the largest unsorted number will 'bubble' its way up to
    its correct position. 
-   After enough iterations, every number will be in its correct position and thus the list of numbers will
    be sorted from smallest to largest.

A more detailed explanation on how bubble sort works:
1.  We pick the leftmost number and the number on its right.
2.  Since we are sorting in ascending order, we should check which of the two numbers is bigger.
    - If the one on the left is bigger than the one on the right, we should swap them!
    - In other cases, we should leave them be. 
3.  Repeat steps 1 & 2, but comparing the 2nd leftmost number and the number on its right, the 3rd leftmost
    number and the number on its right, and so on until we can't pick another pair.
    This makes one iteration of this algorithm - meaning that the largest number is now in its correct 
    position.
4.  Repeat steps 1 - 3, until all the numbers are in their correct position.
"""

def bubble_sort(num_list):
    """ An implementation of bubble sort. Takes in a list of numbers 'num_list'. """
    length = len(num_list)  # finds the number of items in the list 'num_list' and stores it in variable length.

    for i in range(length): # code in this loop (lines 27-44) repeats 'length' amount of times.
        # In each iteration of this loop, the largest unsorted number will be in its correct positon.
        # After 'length' iterations (after we exit this loop), every number will be in its correct position
        # since we only have 'length' amount of numbers in the list.

        for j in range(length - 1): # code in this loop (lines 32-44) repeats 'length' - 1 amount of times.
            # In each iteration of this loop, we will pick two numbers and swap them if they are out of place.
            # After 'length' - 1 iterations, this will eventually pick and compare every number excluding the
            # last one (since it will not have a number to its right).

            # picking two numbers
            left_num = num_list[j]  # the first number
            right_num = num_list[j+1]  # the number to the right of 'left_num'

            # comparing the two numbers and swapping if neccessary
            if left_num > right_num: # if the left number is bigger than the right, swap the two numbers 
                                     # (otherwise, the code below (lines 43-44) does not run, and the numbers are not swapped)
                num_list[j] = right_num # assigning the value of right_num to left_num's position
                num_list[j+1] = left_num # assigning the value of left_num to right_num's position.


if __name__ == "__main__":
    # All lines of code below will be run to test whether the algorithm works and will cover some edge cases.
    # If it works, all lists printed out will be in ascending order.

    # test for a list containing positive numbers
    pos_list = [3, 1, 4, 2, 5] # the unsorted list
    bubble_sort(pos_list) # call to the function which will run bubble_sort
    print(pos_list) # printing the list sorted by bubblesort

    # test for a list containing negative numbers
    neg_list = [-3, -2, -5, -4, -1] 
    bubble_sort(neg_list)
    print(neg_list)

    # test for a list containing a mix of positive and negative numbers
    pos_neg_list = [-1, 4, 2, -3, -5] 
    bubble_sort(pos_neg_list)
    print(pos_neg_list)

    # test for a list that has multiple duplicate numbers
    dupli_list = [-2, 3, -2, 3, 1] 
    bubble_sort(dupli_list)
    print(dupli_list)

    # test for a list that has zeros
    zero_list = [4, 0, 1, -5, 0] 
    bubble_sort(zero_list)
    print(zero_list)

    # test for a list that in descending order
    descend_list = [8, 4, 3, 2] 
    bubble_sort(descend_list)
    print(descend_list)

    # test for a list that is already sorted
    sorted_list = [1, 3, 5, 10] 
    bubble_sort(sorted_list)
    print(sorted_list)
