def binary_search(array, target):
    """ An implementation of iterative binary search.

    Takes in a list of sorted numbers 'array', and a target number 'target'.
    Returns the index of the targe number if it is in 'array', and False otherwise.
    """
    # Invariant: if the target is in array, it is between low (inclusive) and high (exclusive)
    # aka in array[low, high-1]

    low = 0 # first index of array
    high = len(array) # end of array (exclusive)

    while (low < high -1): # when is array[low, high-1] empty (aka when have we looked at all elements or if the list is empty)?
                        # when low = high-1 (because it'd be array[low, low], which is empty)
        mid = (low + high)//2 # mid point of the looked at array
        print("mid", mid)
        if target < array[mid]: # the target is in the lower half
            print("lower")
            high = mid # move high down so we look at the lower half
                        # remember in this case, high is excluded from the active range.
                        # since we know that mid isnt the target, we can directly move high to mid
        if target >= array[mid]: # the target is in the upper half OR
                                    # the target is equal to the mid point
            print("higher")
            low = mid # move low up so we look at the upper half
                        # directly move low to mid since we want to include that element
                        # OR if target is at the midpoint, purposefully fail the while loop
                            # this way, when the loop ends low = high - 1, and there is only element in the active range, which is array[low]
    if array[low] == target: # after the while loop terminates, there is only one element left to look at
        return low
    return False # the target number isn't in the array

print(binary_search([0,1,2,3,4,5,6,7,8], 5))
